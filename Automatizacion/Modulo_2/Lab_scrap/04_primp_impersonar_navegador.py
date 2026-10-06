# Tercer motivo (ademas de "hace falta JS" y "el dato ya esta en un <script>")
# por el que un scraper puede fallar: el SERVIDOR bloquea requests porque
# detecta que no es un navegador real. No por el contenido (no hace falta
# JS), sino por como se ve la conexion:
#   - El header User-Agent dice literalmente "python-requests/x.y.z".
#   - El "fingerprint" TLS (como arma el handshake HTTPS) no coincide con
#     el de un navegador real -- esto se llama JA3/JA3n/JA4 y varios
#     servicios anti-bot (Cloudflare, etc.) lo chequean ANTES de mirar
#     siquiera el header User-Agent.
#
# `primp` es un cliente HTTP (Rust por debajo) que imita el fingerprint TLS
# y los headers de un navegador real. No ejecuta JavaScript -- sigue siendo
# "solo HTTP", liviano y rapido como requests -- pero el servidor lo ve
# como si fuera Chrome/Firefox real.
#
# Instalacion: uv add --system-certs primp
#
# Corre con internet (usa tls.peet.ws, un servicio PUBLICO hecho justamente
# para que cualquiera pueda chequear su propio fingerprint TLS/HTTP -- no
# estamos esquivando la proteccion de nadie, es una herramienta de
# diagnostico):
#   uv run python 04_primp_impersonar_navegador.py
import truststore

truststore.inject_into_ssl()

import primp
import requests

URL_DIAGNOSTICO = "https://tls.peet.ws/api/all"

print("=== requests (TLS/headers 'de Python', se nota a la legua) ===")
r = requests.get(URL_DIAGNOSTICO, timeout=10)
datos = r.json()
print("JA3 hash  :", datos["tls"]["ja3_hash"])
print("Protocolo :", datos["http_version"])
print("User-Agent:", datos["user_agent"])

print()
print("=== primp con impersonate='chrome_146' ===")
cliente = primp.Client(impersonate="chrome_146")
r2 = cliente.get(URL_DIAGNOSTICO)
datos2 = r2.json()
print("JA3 hash  :", datos2["tls"]["ja3_hash"])
print("Protocolo :", datos2["http_version"])
print("User-Agent:", datos2["user_agent"])

print()
print("=== primp tambien sirve como reemplazo directo de requests ===")
# response.status_code, response.text, etc. funcionan igual -- se puede
# pasar directo a BeautifulSoup como si fuera requests.
from bs4 import BeautifulSoup

r3 = cliente.get("https://books.toscrape.com")
soup = BeautifulSoup(r3.text, "html.parser")
primer_titulo = soup.select_one("h3 a")["title"]
print(f"status={r3.status_code}, primer libro: {primer_titulo!r}")

print()
print("=== Cuando usar cada cosa ===")
print(
    "- Si el dato esta en el HTML crudo y el sitio no te bloquea: requests/\n"
    "  Scrapy normal, lo mas simple y rapido.\n"
    "- Si te bloquean por fingerprint/headers pero el dato sigue siendo HTML\n"
    "  estatico (no depende de JS): primp (o curl_cffi, la libreria en la que\n"
    "  primp se inspira). Mucho mas liviano que levantar un navegador.\n"
    "- Si el dato se arma recien cuando corre JavaScript en el navegador:\n"
    "  ahi si hace falta Selenium/Playwright (o scrapy-playwright)."
)
