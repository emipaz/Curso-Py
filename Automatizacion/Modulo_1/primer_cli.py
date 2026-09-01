# Ejemplo con argparse
# Guardá este código como mi_cli.py y ejecutá: python mi_cli.py --nombre Juan --edad 25

import argparse

parser = argparse.ArgumentParser(description="Mi primera CLI con argparse")

# Argumento obligatorio
parser.add_argument("nombre", help="Tu nombre")

parser.add_argument("apellido", help="tu apellido")

# Argumento opcional con valor por defecto
parser.add_argument("--edad", type=int, default=18, help="Tu edad (default: 18)")

# Argumento con opciones predefinidas
parser.add_argument("--color", choices=["rojo", "azul", "verde"], help="Color favorito")

args = parser.parse_args()

print(f"Hola {args.nombre} {args.apellido}, tenés {args.edad} años.")
if args.color:
    print(f"Tu color favorito es {args.color}.")
