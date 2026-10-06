# El combo que SI funciona bien: un parser (BS4 o Scrapy) navega el arbol y
# aisla el pedacito de texto/atributo correcto; regex limpia o extrae datos
# de ESE pedacito ya aislado (no del HTML completo).
#
# Corre con internet (pide books.toscrape.com):
#   uv run python 02_regex_combinado_con_scraping.py
import re

# Solo necesario en esta maquina (certificado TLS corporativo que requests
# no reconoce por default). Si en el aula no hace falta, se puede borrar
# sin problema.
import truststore

truststore.inject_into_ssl()

import requests
from bs4 import BeautifulSoup

html = requests.get("https://books.toscrape.com", timeout=10).text
soup = BeautifulSoup(html, "html.parser")

patron_precio = re.compile(r"(?P<entero>\d+)\.(?P<decimales>\d+)")
patron_id_url = re.compile(r"_(?P<id>\d+)/")

libros = []
for articulo in soup.select("article.product_pod"):
    # 1) BS4 ya hizo el trabajo duro: encontrar el <p class="price_color">
    #    exacto DENTRO de este <article>, sin importarle el resto de la
    #    pagina ni el orden de los atributos.
    texto_precio = articulo.select_one("p.price_color").get_text()  # "£51.77"

    # 2) Regex entra para lo que regex hace bien: separar el numero del
    #    simbolo de moneda, sin tener que andar haciendo
    #    .replace("£", "").replace(",", "") a mano por cada moneda rara.
    coincidencia = patron_precio.search(texto_precio)
    precio = float(f"{coincidencia['entero']}.{coincidencia['decimales']}")

    # 3) El rating viene como class="star-rating Three" -- es texto libre,
    #    no un numero. BS4 te da la lista de clases; regex (o un dict, las
    #    dos sirven) lo convierte a algo usable.
    clases_rating = articulo.select_one("p.star-rating")["class"]  # ["star-rating", "Three"]
    rating_texto = " ".join(clases_rating)
    rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
    rating = next((v for k, v in rating_map.items() if re.search(rf"\b{k}\b", rating_texto)), None)

    # 4) El id del libro esta "escondido" en la URL del link de detalle.
    #    BS4 saca el atributo href completo; regex extrae solo el numero.
    href = articulo.select_one("h3 a")["href"]
    id_match = patron_id_url.search(href)
    id_libro = id_match["id"] if id_match else None

    libros.append(
        {
            "titulo": articulo.select_one("h3 a")["title"],
            "precio": precio,
            "rating": rating,
            "id": id_libro,
        }
    )

for libro in libros[:5]:
    print(libro)

print(f"\nTotal: {len(libros)} libros, precio promedio: {sum(l['precio'] for l in libros) / len(libros):.2f}")
