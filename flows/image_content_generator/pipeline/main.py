import argparse
from enum import Enum
from pathlib import Path

from flows.image_content_generator.pipeline.pipeline import Pipeline
from flows.image_content_generator.pipeline.schemas import VideoOrientation
from tools.common.messenger import Messenger

RESOURCE_BASE = Path("flows/image_content_generator/resource")
LONG_OUT_BASE = Path("flows/image_content_generator/out_long")
SHORT_OUT_BASE = Path("flows/image_content_generator/out_short")


class PipelineStep(str, Enum):
    ALL = "all"
    STEP1 = "step1"
    STEP2 = "step2"
    STEP3 = "step3"
    STEP4 = "step4"
    STEP5 = "step5"
    STEP6 = "step6"
    STEP7 = "step7"
    FIXED = "fixed"


from tools.common.terminal import disable_quick_edit

def main():
    # Disable Windows console QuickEdit mode to prevent freezes when running in background
    disable_quick_edit()

    parser = argparse.ArgumentParser()
    parser.add_argument("orientation", type=VideoOrientation, choices=list(VideoOrientation))
    parser.add_argument("step", type=PipelineStep, choices=list(PipelineStep))
    args = parser.parse_args()

    # Determine output base based on orientation
    out_base = SHORT_OUT_BASE if args.orientation == VideoOrientation.SHORT else LONG_OUT_BASE

    pipeline = Pipeline(
        out_base=out_base,
        resource_base=RESOURCE_BASE,
        orientation=args.orientation
    )

    # Map Enum members to their corresponding pipeline methods
    step_methods = {
        PipelineStep.STEP1: pipeline.step1_generate_story,
        PipelineStep.STEP2: pipeline.step2_generate_images,
        PipelineStep.STEP3: pipeline.step3_generate_audios,
        PipelineStep.STEP4: pipeline.step4_generate_videos,
        PipelineStep.STEP5: pipeline.step5_generate_subtitles,
        PipelineStep.STEP6: pipeline.step6_add_background_music,
        PipelineStep.STEP7: pipeline.step7_rename_final_video,
    }

    # Define steps to execute (excluding 'all' and 'fixed')
    steps = [s for s in PipelineStep if s not in (PipelineStep.ALL, PipelineStep.FIXED)]

    if args.step == PipelineStep.ALL:
        Messenger.info("--- Starting Infinite Generation Loop ---")
        while True:
            for step in steps:
                if step == PipelineStep.STEP1:
                    step_methods[step](force_new=False)
                else:
                    step_methods[step]()
            Messenger.success("Cycle completed. Starting next cycle...")
    elif args.step == PipelineStep.FIXED:
        Messenger.info("--- Starting Fixed Generation Loop (Finishing existing only) ---")
        from flows.image_content_generator.pipeline.schemas import State
        
        state_to_step = {
            State.SCRIPT_GENERATED: PipelineStep.STEP2,
            State.IMAGES_GENERATED: PipelineStep.STEP3,
            State.AUDIO_GENERATED: PipelineStep.STEP4,
            State.VIDEO_GENERATED: PipelineStep.STEP5,
            State.VIDEO_SUBTITLED: PipelineStep.STEP6,
            State.VIDEO_MUSIC_GENERATED: PipelineStep.STEP7,
            State.NEW: PipelineStep.STEP1
        }
        
        while True:
            incomplete = pipeline.store.get_incomplete_idea()
            if not incomplete:
                Messenger.success("All ideas are finished! Exiting fixed loop.")
                break
                
            Messenger.info(f"\n--- Procesando idea {incomplete.id} (Estado: {incomplete.state.value}) ---")
            
            step_to_run = state_to_step.get(incomplete.state)
            if not step_to_run:
                Messenger.error(f"Estado desconocido: {incomplete.state}")
                break
                
            if step_to_run == PipelineStep.STEP1:
                step_methods[step_to_run](force_new=False)
            else:
                step_methods[step_to_run]()
                
            Messenger.success(f"Paso {step_to_run.value} completado para idea {incomplete.id}. Verificando siguiente paso...")
    else:
        # Run specific step
        if args.step == PipelineStep.STEP1:
            step_methods[args.step](force_new=True)
        else:
            step_methods[args.step]()


if __name__ == "__main__":
    main()
