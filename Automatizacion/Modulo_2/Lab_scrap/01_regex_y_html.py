# Por que "no conviene" parsear HTML completo con regex (pero a veces SI sirve
# para un pedacito puntual). Corre solo, sin internet:
#
#   uv run python 01_regex_y_html.py
import re

html = """
<article class="product_pod">
  <h3><a href="libro1.html" title="A Light in the Attic">A Light...</a></h3>
  <p class="price_color">£51.77</p>
</article>
<article class="product_pod">
  <h3><a href="libro2.html" title="Tipping the Velvet">Tipping...</a></h3>
  <p class="price_color">£53.74</p>
</article>
"""

print("=== Intento 1: sacar los titulos con un regex 'obvio' (greedy) ===")

patron_ingenuo = r'<a.*title="(.*)".*>'

print("sobre el HTML de ejemplo (un <a> por linea):", re.findall(patron_ingenuo, html))

# Con un <a> por linea "funciona", pero es casualidad: ".*" no cruza saltos
# de linea por default, asi que cada busqueda queda contenida en su propia
# linea. El problema real aparece con dos <a> en la MISMA linea:

html_misma_linea = '<a title="Primero">x</a> <a title="Segundo">y</a>'

print("sobre dos <a> en la misma linea:", re.findall(patron_ingenuo, html_misma_linea))

# -> da ['Segundo'], perdimos el primero. El ".*" codicioso se come todo lo
# que puede y recien retrocede (backtracking) hasta la ULTIMA comilla que le
# permite seguir matcheando, por eso "salta" al segundo <a>.

print()

print("=== Intento 2: 'arreglarlo' con perezoso (.*?) ===")

patron_perezoso = r'<a.*?title="(.*?)".*?>'

print("sobre dos <a> en la misma linea:", re.findall(patron_perezoso, html_misma_linea))

# Ahora SI aparecen los dos. Pero sigue siendo fragil: si cambia el orden de
# los atributos (href antes de title), o el valor tiene un caracter " escapado
# como &quot;, el patron deja de matchear y hay que retocarlo a mano. Un
# selector CSS (".product_pod h3 a::attr(title)") no le importa el orden de
# los atributos ni los saltos de linea, porque interpreta el HTML como
# arbol, no como texto plano con backtracking.

print()

print("=== Caso donde el regex se rompe de verdad: atributos en otro orden ===")

html_orden_distinto = '<a title="Otro libro" href="libro3.html">Otro...</a>'

print("con el patron perezoso de arriba:", re.findall(patron_perezoso, html_orden_distinto))

# Sigue funcionando ESTE caso particular porque title viene primero, pero si
# agregamos un atributo ANTES de title ya se complica:

html_con_id_antes = '<a id="x1" title="Otro libro" href="libro3.html">Otro...</a>'

print("con un atributo id antes:", re.findall(r'<a title="(.*?)".*?>', html_con_id_antes))

# -> esto da [] (vacio): el patron esperaba que "<a " fuera seguido
# directamente de title=, y ahora no lo es. Un parser de HTML (BS4/Scrapy)
# ni se entera de este cambio.

print()
print("=== Conclusion ===")
print(
    "Regex no entiende 'arbol' ni 'atributos en cualquier orden': solo ve\n"
    "texto. Para NAVEGAR la estructura (entrar a tal tag, que tenga tal\n"
    "clase, sacar tal atributo) conviene un parser real (BS4/Scrapy).\n"
    "Regex brilla DESPUES de eso, limpiando o extrayendo de un pedacito de\n"
    "texto ya aislado (ver 02_regex_combinado_con_scraping.py)."
)
