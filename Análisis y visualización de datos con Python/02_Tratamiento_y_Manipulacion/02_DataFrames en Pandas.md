# DataFrames en Pandas: Estructura y Operaciones Fundamentales

## ¿Qué es un DataFrame?

Un **DataFrame** es la estructura de datos principal de Pandas.

Puede imaginarse como una hoja de cálculo de Excel o una tabla de base de datos, donde los datos se organizan en:

- Filas (registros u observaciones)
- Columnas (variables o características)

Es una estructura bidimensional capaz de almacenar distintos tipos de datos simultáneamente:

- Números
- Texto
- Fechas
- Valores booleanos
- Objetos complejos

---

# ¿Por qué son tan importantes?

Los DataFrames son la herramienta más utilizada en:

- Ciencia de Datos
- Machine Learning
- Ingeniería de Datos
- Análisis Estadístico
- Inteligencia de Negocios (BI)

Permiten:

- ✅ Organizar datos.
- ✅ Limpiar información.
- ✅ Analizar patrones.
- ✅ Transformar datos.
- ✅ Crear reportes y visualizaciones.

---

# Estructura de un DataFrame

Un DataFrame está compuesto por tres elementos fundamentales:

## 1. Datos (Data)

Es la información almacenada.

Ejemplo:

| Nombre | Edad | Ciudad |
|----------|------|---------|
| Ana | 25 | Madrid |
| Luis | 30 | Buenos Aires |

---

## 2. Índice (Index)

Identifica de forma única cada fila.

Por defecto:

```text
0
1
2
3
...
```

Ejemplo:

| Índice | Nombre | Edad |
|---------|---------|------|
| 0 | Ana | 25 |
| 1 | Luis | 30 |

También puede personalizarse:

```python
df.index = ["A", "B"]
```

Resultado:

| Índice | Nombre |
|---------|---------|
| A | Ana |
| B | Luis |

---

## 3. Columnas (Columns)

Representan las variables del conjunto de datos.

```python
df.columns
```

Resultado:

```python
Index(['Nombre', 'Edad', 'Ciudad'])
```

Cada columna tiene:

- Un nombre
- Un tipo de dato

Ejemplo:

```python
df.dtypes
```

Resultado:

```text
Nombre    object
Edad       int64
Ciudad    object
```

---

# Creación de un DataFrame

```python
import pandas as pd

df = pd.DataFrame({
    "Nombre": ["Ana", "Luis", "Pedro"],
    "Edad": [25, 30, 40],
    "Ciudad": ["Madrid", "Buenos Aires", "Bogotá"]
})
```

Resultado:

| Nombre | Edad | Ciudad |
|----------|------|---------|
| Ana | 25 | Madrid |
| Luis | 30 | Buenos Aires |
| Pedro | 40 | Bogotá |

---

# Operaciones Básicas

## 1. Indexación

Permite acceder a elementos específicos.

### Acceso por etiqueta: loc

```python
df.loc[0]
```

Resultado:

```text
Nombre      Ana
Edad          25
Ciudad    Madrid
```

### Acceso por índice numérico: iloc

```python
df.iloc[0]
```

---

## Acceso a una celda específica

```python
df.loc[0, "Nombre"]
```

Resultado:

```text
Ana
```

---

# Diferencia entre loc e iloc

| Método | Tipo de acceso |
|----------|---------------|
| loc | Etiquetas |
| iloc | Posiciones numéricas |

Ejemplo:

```python
df.loc[0]
```

```python
df.iloc[0]
```

Ambos devuelven la primera fila cuando el índice es numérico.

---

# Caso práctico: Comercio Electrónico

Supongamos:

| Pedido | Cliente | Producto |
|----------|----------|-----------|
| 1001 | Ana | Laptop |
| 1002 | Luis | Mouse |

Obtener pedido 1001:

```python
df.loc[df["Pedido"] == 1001]
```

---

# 2. Segmentación (Slicing)

Permite seleccionar rangos de filas o columnas.

## Filas

```python
df.iloc[0:3]
```

Obtiene:

```text
Filas 0, 1 y 2
```

---

## Columnas

```python
df[["Nombre", "Edad"]]
```

Resultado:

| Nombre | Edad |
|---------|------|
| Ana | 25 |
| Luis | 30 |

---

## Filas y columnas simultáneamente

```python
df.iloc[0:3, 0:2]
```

Resultado:

```text
Primeras 3 filas
Primeras 2 columnas
```

---

# Caso práctico: Mercado bursátil

Extraer datos del año 2023:

```python
df_2023 = df[
    df["fecha"].dt.year == 2023
]
```

---

# 3. Filtrado

Permite seleccionar registros que cumplen una condición.

---

## Filtrar por valor

```python
df[df["Edad"] > 30]
```

Resultado:

| Nombre | Edad |
|---------|------|
| Pedro | 40 |

---

## Varias condiciones

```python
df[
    (df["Edad"] > 25)
    & (df["Ciudad"] == "Buenos Aires")
]
```

---

## Operador OR

```python
df[
    (df["Edad"] > 40)
    | (df["Ciudad"] == "Madrid")
]
```

---

# Caso práctico: Encuesta de satisfacción

Seleccionar clientes insatisfechos:

```python
clientes_insatisfechos = df[
    df["satisfaccion"] < 3
]
```

Esto permite:

- Detectar problemas.
- Analizar causas.
- Mejorar servicios.

---

# Operaciones muy utilizadas

## Mostrar primeras filas

```python
df.head()
```

---

## Mostrar últimas filas

```python
df.tail()
```

---

## Información general

```python
df.info()
```

---

## Estadísticas descriptivas

```python
df.describe()
```

Obtiene:

- Promedio
- Máximo
- Mínimo
- Cuartiles
- Desviación estándar

---

## Ordenar datos

```python
df.sort_values("Edad")
```

---

## Renombrar columnas

```python
df.rename(
    columns={"Edad": "Anios"}
)
```

---

## Eliminar columnas

```python
df.drop(
    columns=["Ciudad"]
)
```

---

# Relación con SQL

Muchos comandos de Pandas tienen equivalentes en SQL.

| SQL | Pandas |
|-------|---------|
| SELECT | df[["col"]] |
| WHERE | df[df["edad"] > 30] |
| ORDER BY | sort_values() |
| GROUP BY | groupby() |
| JOIN | merge() |

Ejemplo:

```sql
SELECT *
FROM clientes
WHERE edad > 30
```

Equivalente:

```python
df[df["edad"] > 30]
```


## En el contexto de Pandas DataFrames, ¿cuál de las siguientes opciones describe mejor el concepto de 'slicing'? Elija la mejor respuesta.

- Conversión de DataFrame a array unidimensional.
- **Acceder a un rango de filas o a un subconjunto del DataFrame.**
- Extracción de una columna específica del DataFrame.
- Filtrado de filas basado en condiciones específicas.

Correcto

> Correcto Slicing permite extraer una parte del DataFrame, ya sea un rango continuo de filas o una selección basada en criterios específicos.



---

# DataFrames en Pandas vs Polars

## Pandas

```python
df = pd.read_csv("ventas.csv")
```

Ventajas:

- Más popular.
- Más documentación.
- Excelente integración con Scikit-Learn.

---

## Polars

```python
df = pl.read_csv("ventas.csv")
```

Ventajas:

- Más rápido.
- Menos consumo de memoria.
- Paralelismo automático.

---

## Regla práctica

### Usar Pandas cuando:

- Estás aprendiendo.
- Trabajas en Jupyter.
- Harás Machine Learning.
- Los datos caben cómodamente en memoria.

### Usar Polars cuando:

- Tienes millones de filas.
- Procesas archivos muy grandes.
- Construyes ETLs.
- Necesitas máximo rendimiento.

---

# Resumen Final

✅ Un DataFrame es una tabla bidimensional formada por datos, índices y columnas.

✅ Es la estructura central de Pandas para manipular información.

✅ Las operaciones fundamentales son:

1. Indexación (`loc`, `iloc`)
2. Segmentación (Slicing)
3. Filtrado (Filtering)

✅ Estas operaciones permiten extraer, transformar y analizar datos con precisión.

✅ Dominar DataFrames es el primer paso para avanzar en:
- Ciencia de Datos
- Machine Learning
- Ingeniería de Datos
- Análisis Empresarial

> Un DataFrame es para los datos lo que una hoja de cálculo es para un analista: el lugar donde ocurre todo el trabajo importante.