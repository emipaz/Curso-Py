# A veces una pagina "parece" dinamica (hay un <script> armando cosas con
# JS) pero los DATOS ya estan ahi, en texto plano, adentro del HTML crudo --
# el JS solo los toma de una variable y los pinta en el DOM. En ese caso NO
# hace falta Selenium/Playwright: alcanza con regex para sacar ese bloque de
# texto y json.loads() para convertirlo a datos de Python.
#
# Esto es muy comun en sitios reales: buscan "window.__DATOS__" o
# "application/ld+json" en el codigo fuente antes de prender un navegador.
#
# Corre solo, sin internet:
#   uv run python 03_regex_json_embebido.py
import json
import re

# HTML de ejemplo: simula una pagina donde el listado de productos se
# "pinta" con JS, pero el JSON con los datos reales ya viene en el <script>.
html = """
<html>
<body>
  <div id="catalogo">Cargando...</div>
  <script>
    window.__CATALOGO__ = {"productos": [
        {"nombre": "Mouse", "precio": 1999.90},
        {"nombre": "Teclado", "precio": 4500.00}
    ]};
    document.getElementById("catalogo").innerText = "Listo";
  </script>
</body>
</html>
"""

print("=== Si esto se pide con requests/Scrapy (sin ejecutar el JS) ===")
print("El <div id='catalogo'> en el HTML crudo dice 'Cargando...', nunca 'Listo'.")
print("Pero el JSON de productos YA esta en el texto del <script>.\n")

# re.DOTALL para que "." tambien matchee saltos de linea, por si el JSON
# viene formateado en varias lineas (como en este ejemplo).
patron = re.compile(r"window\.__CATALOGO__\s*=\s*(?P<json>\{.*?\});", re.DOTALL)
coincidencia = patron.search(html)

datos = json.loads(coincidencia["json"])
print("Productos extraidos sin navegador:")
for producto in datos["productos"]:
    print(f"  - {producto['nombre']}: ${producto['precio']}")

print()
print("=== Cuando esto NO alcanza ===")
print(
    "Si el JSON no esta en el HTML crudo (por ejemplo, el navegador hace un\n"
    "fetch() a una API aparte DESPUES de cargar, y la respuesta nunca queda\n"
    "escrita en el <script>), ahi si hace falta un navegador real\n"
    "(Selenium/Playwright) o, mejor, buscar esa misma llamada a la API con\n"
    "la pestaña Network de F12 y pedirla directo con requests (suele ser\n"
    "mas rapido y mas estable que simular un navegador)."
)
