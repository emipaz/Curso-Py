# formatear_txt.py — Versión básica con argparse
# Ejecutar desde terminal:
#   python formatear_txt.py intro.txt -w 80
#   python formatear_txt.py  (procesa todos los .txt del directorio)

import argparse
import sys
from pathlib import Path
from textwrap import TextWrapper


def formatear_archivo(ruta: Path, ancho: int) -> Path:
    """Lee un archivo .txt y crea una versión formateada con el ancho indicado."""
    wrapper = TextWrapper(
        width=ancho,
        break_long_words=False,
        break_on_hyphens=False,
        replace_whitespace=True,
    )

    lineas_salida = []
    for linea in ruta.read_text(encoding="utf-8").splitlines():
        if not linea.strip():
            lineas_salida.append("")
        else:
            lineas_salida.extend(wrapper.wrap(linea))

    ruta_salida = ruta.with_name(f"{ruta.stem}_{ancho}.txt")
    ruta_salida.write_text("\n".join(lineas_salida) + "\n", encoding="utf-8")
    return ruta_salida


def main():
    parser = argparse.ArgumentParser(
        description="Reformatea archivos TXT envolviendo el texto con textwrap."
    )
    parser.add_argument(
        "archivos", nargs="*",
        help="Archivos .txt a procesar (por defecto, todos los del directorio actual)"
    )
    parser.add_argument(
        "-w", "--ancho", type=int, default=100,
        help="Ancho máximo de columna (default: 100)"
    )
    args = parser.parse_args()

    if args.archivos:
        rutas = [Path(a) for a in args.archivos]
    else:
        rutas = sorted(Path(".").glob("*.txt"))

    if not rutas:
        print("No se encontraron archivos .txt para procesar.")
        sys.exit(1)

    for ruta in rutas:
        if not ruta.is_file():
            print(f"AVISO: {ruta} no existe, se omite.")
            continue
        salida = formatear_archivo(ruta, args.ancho)
        print(f"OK: {ruta} -> {salida}")


if __name__ == "__main__":
    main()
