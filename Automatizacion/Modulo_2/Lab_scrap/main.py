# Step 3.1: Fetch HTML Content
# Please be careful to follow instructions on how to run the program;
# the Run menu or right-click > Run options do not work in the simulated environment.
# Ensure you have run the terminal command to install the correct libraries using pip.
# You must use the terminal window as directed in Step 3.

### YOUR CODE HERE ###
# Solo necesario en esta maquina (certificado TLS corporativo que requests
# no reconoce por default). Si en el aula no hace falta, se puede borrar.

import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

URL = "https://emipaz.com.ar/baseball_stats.html"

respuesta = requests.get(URL, timeout=10)
respuesta.raise_for_status()

soup = BeautifulSoup(respuesta.text, "html.parser")

# Step 3.2: Extract the Required Data
### YOUR CODE HERE ###

patron_numero = re.compile(r"^-?\d+(\.\d+)?$")


def convertir(valor):
    """Convierte a int/float si el texto es numerico; si no, lo deja como str."""
    valor = valor.strip()
    if patron_numero.match(valor):
        return float(valor) if "." in valor else int(valor)
    return valor


encabezados = [th.get_text(strip=True) for th in soup.select("table thead th")]

partidos = []
for fila in soup.select("table tbody tr"):
    celdas = [td.get_text(strip=True) for td in fila.find_all("td")]
    partidos.append({encabezado: convertir(valor) for encabezado, valor in zip(encabezados, celdas)})


# Step 4.1: Convert to a DataFrame
# Import pandas
### YOUR CODE HERE ###
# (ya importado arriba como pd)

# Convert the game data into a pandas DataFrame
### YOUR CODE HERE ###
df = pd.DataFrame(partidos)

# Inspect the DataFrame
### YOUR CODE HERE ###
print(df.info())
print(df.head())

# Save and print the shaped data
### YOUR CODE HERE ###
print(df)

# Step 5.1: Save to a CSV File
# Save the DataFrame to a CSV file named sports_statistics.csv
### YOUR CODE HERE ###
df.to_csv("sports_statistics.csv", index=False)
