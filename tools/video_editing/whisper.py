import json
import shlex
import subprocess
from pathlib import Path
from typing import ClassVar, List

from tools.common.base_model import BaseModelTool
from tools.video_editing.whisper_schemas import (
    WhisperTranscription,
    WhisperTranscriptionSegment,
    WhisperWord,
)


class WhisperTool(BaseModelTool):
    """
    Tool for transcribing audio using whisper-cpp and generating SRT files.
    """
    DEFAULT_MODEL: ClassVar[str] = "models/whisper/ggml-small.bin"

    def _run(self, cmd_args: List[str]) -> None:
        p = subprocess.run(cmd_args, shell=False)
        if p.returncode != 0:
            raise RuntimeError(f"Whisper Error: {' '.join(cmd_args)}")

    def _get_transcription_json(
        self,
        audio_path: Path,
    ) -> WhisperTranscription:
        """
        Runs whisper-cli (if needed) and returns the parsed JSON content.
        """
        json_path = audio_path.with_name(audio_path.name + ".json")
        if not json_path.exists():
            # Construir ruta absoluta al binario
            whisper_bin = Path("bin/whisper/whisper-cli.exe").absolute()
            # -ojf: output json full (tokens with timestamps)
            cmd_args = [
                str(whisper_bin),
                "-m", self.DEFAULT_MODEL,
                "-l", "es",
                "-ojf",
                "-f", str(audio_path)
            ]
            self._run(cmd_args)

        try:
            with open(json_path, 'r', encoding='utf-8', errors='replace') as f:
                content = f.read()
            return WhisperTranscription.model_validate(json.loads(content))
        except json.JSONDecodeError as e:
            raise RuntimeError(
                f"Este paso falló porque el archivo de transcripción está corrupto (JSONDecodeError).\n"
                f"Sugerencia: Borrar este archivo corrupto '{json_path}' y reiniciar el paso IMAGES_GENERATED en el CSV."
            )

    def get_transcription_segments(
        self,
        audio_path: Path
    ) -> List[WhisperTranscriptionSegment]:
        """
        Transcribes audio and returns a list of segments with text and timestamps.
        Each segment: {"text": str, "start": float, "end": float} (times in seconds)
        """
        data = self._get_transcription_json(audio_path)
        segments: List[WhisperTranscriptionSegment] = []
        for s in data.transcription:
            segments.append(WhisperTranscriptionSegment(
                text=s.text.strip(),
                start=s.offsets.from_ms / 1000.0,
                end=s.offsets.to_ms / 1000.0
            ))

        return segments

    def generate_srt(
        self,
        audio_path: Path,
        output_srt: Path,
    ) -> None:
        """
        Generates SRT file from audio file.
        """
        data = self._get_transcription_json(audio_path)

        # 1. Extract and merge tokens into words
        tokens = [
            t
            for s in data.transcription
            for t in s.tokens
            if not t.text.startswith("[_") and t.text.strip()
        ]

        words: List[WhisperWord] = []
        for t in tokens:
            text, t_from, t_to = t.text, t.offsets.from_ms, t.offsets.to_ms
            if text.startswith(" ") or not words:
                words.append(WhisperWord(text=text.strip(), start=t_from, end=t_to))
            else:
                words[-1].text += text
                words[-1].end = t_to

        # 2. Group words into blocks (max 3 words or pause > 0.4s)
        blocks: List[List[WhisperWord]] = []
        current: List[WhisperWord] = []
        for w in words:
            pause = (float(w.start) - float(current[-1].end)) / 1000.0 if current else 0.0
            if len(current) >= 3 or pause > 0.4:
                blocks.append(current)
                current = []
            current.append(w)
        if current:
            blocks.append(current)

        def fmt(ms: int) -> str:
            s, ms = divmod(ms, 1000)
            m, s = divmod(s, 60)
            h, m = divmod(m, 60)
            return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

        # 3. Write SRT
        with open(output_srt, 'w', encoding='utf-8') as f:
            for i, block in enumerate(blocks):
                f.write(f"{i+1}\n{fmt(block[0].start)} --> {fmt(block[-1].end)}\n")
                f.write(" ".join(w.text.upper() for w in block) + "\n\n")
