#!/usr/bin/env python
import argparse
import subprocess
import sys
from pathlib import Path

def run_command(cmd_args):
    print(f"🚀 Ejecutando: {' '.join(cmd_args)}")
    try:
        subprocess.run(cmd_args, check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ El comando falló con código de salida {e.returncode}", file=sys.stderr)
        sys.exit(e.returncode)
    except KeyboardInterrupt:
        print("\n🛑 Proceso interrumpido por el usuario.")
        sys.exit(130)

def main():
    parser = argparse.ArgumentParser(
        description="CLI para administrar el proyecto de Automatización de Videos (Video Automation)",
        epilog="Ejemplo: python cli.py run short step1"
    )

    subparsers = parser.add_subparsers(dest="command", help="Comandos disponibles", required=True)

    # Comando 'run'
    run_parser = subparsers.add_parser("run", help="Ejecutar un paso del pipeline (flows.pipeline.main)")
    run_parser.add_argument(
        "format",
        choices=["short", "long"],
        help="Formato del video (short o long)"
    )
    run_parser.add_argument(
        "step",
        choices=["step1", "step2", "step3", "step4", "step5", "step6", "step7", "all", "fixed"],
        help="Paso a ejecutar"
    )

    # Comandos adicionales (utilidades)
    subparsers.add_parser("import-images", help="Importar imágenes (import_images.py)")
    subparsers.add_parser("extract-scripts", help="Extraer scripts (extract_scripts.py)")

    args = parser.parse_args()

    if args.command == "run":
        cmd = ["poetry", "run", "python", "-m", "flows.pipeline.main", args.format, args.step]
        run_command(cmd)

    elif args.command == "import-images":
        cmd = ["poetry", "run", "python", "scripts/import_images.py"]
        run_command(cmd)

    elif args.command == "extract-scripts":
        cmd = ["poetry", "run", "python", "scripts/extract_scripts.py"]
        run_command(cmd)

if __name__ == "__main__":
    main()
