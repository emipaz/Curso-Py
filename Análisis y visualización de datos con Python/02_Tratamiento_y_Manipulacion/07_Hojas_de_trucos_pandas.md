# Hoja de Trucos de Pandas

## Introducción

**Pandas** es una de las bibliotecas más importantes del ecosistema Python para:

- Manipulación de datos
- Limpieza de datos
- Transformación de datos
- Análisis exploratorio
- Preparación para Machine Learning

Su estructura principal es el **DataFrame**, una tabla bidimensional compuesta por filas y columnas.

---

# 1. Creación de DataFrames

## Desde un diccionario

```python
import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 28]
}

df = pd.DataFrame(data)
```

### Ventajas

- Ideal para datos estructurados.
- Muy utilizado al trabajar con JSON o APIs.

---

## Desde una lista de listas

```python
data = [
    ["Alice", 25],
    ["Bob", 30],
    ["Charlie", 28]
]

df = pd.DataFrame(
    data,
    columns=["Name", "Age"]
)
```

### Ventajas

- Útil para datos tabulares simples.
- Fácil de generar dinámicamente.

---

## Desde un archivo CSV

```python
df = pd.read_csv("data.csv")
```

### Otras fuentes de datos

```python
pd.read_excel("archivo.xlsx")
```

```python
pd.read_json("archivo.json")
```

```python
pd.read_sql(query, conexion)
```

---

# 2. Inspección Inicial del DataFrame

## Ver primeras filas

```python
df.head()
```

Por defecto muestra:

```text
Primeras 5 filas
```

---

## Ver últimas filas

```python
df.tail()
```

Por defecto muestra:

```text
Últimas 5 filas
```

---

## Dimensiones del DataFrame

```python
df.shape
```

Resultado:

```python
(filas, columnas)
```

Ejemplo:

```python
(1000, 12)
```

---

## Información general

```python
df.info()
```

Muestra:

- Nombres de columnas
- Tipos de datos
- Valores nulos
- Uso de memoria

---

## Estadísticas descriptivas

```python
df.describe()
```

Incluye:

- count
- mean
- std
- min
- max
- cuartiles

---

# 3. Selección de Datos

## Una columna

```python
df["Age"]
```

Retorna una:

```python
Series
```

---

## Varias columnas

```python
df[["Name", "Age"]]
```

Retorna un:

```python
DataFrame
```

---

# 4. Selección de Filas

## loc() → por etiqueta

```python
df.loc[0]
```

Selecciona:

```text
Fila cuyo índice es 0
```

---

## iloc() → por posición

```python
df.iloc[0]
```

Selecciona:

```text
Primera fila
```

---

## Rangos

```python
df.iloc[0:5]
```

Primeras 5 filas.

---

# 5. Filtrado de Datos

## Filtrado simple

```python
df[df["Age"] > 25]
```

Resultado:

```text
Filas donde Age > 25
```

---

## Múltiples condiciones

```python
df[
    (df["Age"] > 25)
    &
    (df["Name"] == "Bob")
]
```

---

## Método query()

Más legible para filtros complejos.

```python
df.query(
    'Age > 25 and Name == "Bob"'
)
```

---

# 6. Manejo de Valores Nulos

Los valores faltantes aparecen como:

```python
NaN
```

---

## Detectar nulos

```python
df.isnull()
```

Devuelve:

```python
True / False
```

para cada celda.

---

## Nulos por columna

```python
df["Age"].isnull()
```

---

## Contar nulos

```python
df.isnull().sum()
```

---

# 7. Eliminar Valores Nulos

## Eliminar filas con NaN

```python
df.dropna()
```

### Ventajas

- Datos más limpios.

### Desventajas

- Puede perder información importante.

---

# 8. Completar Valores Nulos

## Con cero

```python
df.fillna(0)
```

---

## Con promedio

```python
df["Age"].fillna(
    df["Age"].mean(),
    inplace=True
)
```

---

## Con mediana

```python
df["Age"].fillna(
    df["Age"].median(),
    inplace=True
)
```

---

# Estrategias de Imputación

| Método | Uso recomendado |
|----------|----------------|
| 0 | Valores opcionales |
| Mean | Datos numéricos simétricos |
| Median | Datos con outliers |
| Mode | Variables categóricas |

---

# 9. Operaciones Más Utilizadas

## Ordenar

```python
df.sort_values("Age")
```

---

## Orden descendente

```python
df.sort_values(
    "Age",
    ascending=False
)
```

---

## Agrupar

```python
df.groupby("Region")
```

---

## Sumar por grupo

```python
df.groupby(
    "Region"
)["Ventas"].sum()
```

---

## Promedio por grupo

```python
df.groupby(
    "Region"
)["Ventas"].mean()
```

---

## Agregaciones múltiples

```python
df.groupby("Region").agg({
    "Ventas": [
        "sum",
        "mean",
        "max"
    ]
})
```

---

# 10. Crear Nuevas Columnas

## Operación simple

```python
df["IVA"] = df["Precio"] * 0.21
```

---

## Función personalizada

```python
def descuento(valor):
    return valor * 0.9

df["Precio_Final"] = (
    df["Precio"]
    .apply(descuento)
)
```

---

# 11. Combinar DataFrames

## Concatenar

```python
pd.concat([df1, df2])
```

Apila filas.

---

## Concatenar columnas

```python
pd.concat(
    [df1, df2],
    axis=1
)
```

---

## Merge

```python
pd.merge(
    df1,
    df2,
    on="id"
)
```

Equivalente a:

```sql
JOIN
```

en SQL.

---

# 12. Tabla Dinámica (Pivot)

```python
df.pivot_table(
    index="Region",
    columns="Producto",
    values="Ventas"
)
```

Permite:

- Comparar categorías.
- Crear reportes.
- Analizar tendencias.

---

# Funciones Más Importantes

| Función | Uso |
|----------|------|
| read_csv() | Cargar CSV |
| head() | Primeras filas |
| tail() | Últimas filas |
| shape | Dimensiones |
| info() | Información general |
| describe() | Estadísticas |
| loc[] | Selección por etiqueta |
| iloc[] | Selección por posición |
| query() | Filtrado |
| isnull() | Detectar nulos |
| fillna() | Completar nulos |
| dropna() | Eliminar nulos |
| sort_values() | Ordenar |
| groupby() | Agrupar |
| agg() | Agregar |
| concat() | Concatenar |
| merge() | Fusionar |
| pivot_table() | Tabla dinámica |

---

# Pandas vs Polars

## Pandas

### Ventajas

- Más documentación.
- Más ejemplos.
- Integración total con Scikit-Learn.
- Ideal para aprendizaje.

```python
df.groupby("Region").sum()
```

---

## Polars

```python
df.group_by("Region").sum()
```

### Usa Polars cuando:

- Procesas millones de registros.
- Necesitas máxima velocidad.
- Construyes pipelines ETL.
- El consumo de memoria es crítico.

### Estrategia recomendada

```text
Análisis exploratorio
        ↓
      Pandas
        ↓
Producción / ETL grande
        ↓
      Polars
```

---

# Resumen Final

✅ El DataFrame es la estructura principal de Pandas.

✅ Las tareas fundamentales son:

- Cargar datos.
- Inspeccionar datos.
- Seleccionar columnas y filas.
- Filtrar información.
- Manejar valores nulos.
- Agrupar y agregar.
- Combinar DataFrames.
- Crear transformaciones personalizadas.

✅ Pandas es la herramienta estándar para análisis de datos en Python.

✅ Polars es una alternativa moderna y mucho más rápida para datasets grandes.

> Dominar `head()`, `info()`, `query()`, `groupby()`, `merge()` y `fillna()` cubre aproximadamente el 80% de las tareas diarias de análisis de datos con Pandas.