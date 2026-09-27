# Ejemplo con sys.argv
# Ejecutar desde terminal: python script.py hola mundo

import sys

print(f"Nombre del script: {sys.argv[0]}")
print(f"Argumentos: {sys.argv[1:]}")
print(f"Cantidad de argumentos: {len(sys.argv) - 1}")

# Ejemplo práctico: sumar números pasados por CLI
# Ejecutar: python script.py 10 20 30
if len(sys.argv) > 1:
    numeros = [int(x) for x in sys.argv[1:]]
    print(f"Suma de {numeros} = {sum(numeros)}")
else:
    print("no pasaste nada")
