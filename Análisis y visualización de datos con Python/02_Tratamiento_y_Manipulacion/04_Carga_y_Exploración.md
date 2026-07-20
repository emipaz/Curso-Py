# Carga y Exploración Inicial de Datos con Pandas

## Introducción

**Pandas** es una de las bibliotecas más importantes de Python para el análisis y manipulación de datos.

Puede considerarse una **navaja suiza para los datos**, ya que permite:

- Cargar datos desde múltiples fuentes.
- Limpiar información.
- Transformar datasets.
- Analizar patrones.
- Preparar datos para Machine Learning.
- Generar estadísticas descriptivas.

---

# ¿Por qué Pandas es tan importante?

En el mundo real los datos suelen ser:

- Incompletos.
- Desordenados.
- Inconsistentes.
- Difíciles de interpretar.

Pandas ayuda a transformar esos datos en información útil para la toma de decisiones.

---

# Conceptos básicos

## Filas y Columnas

Un conjunto de datos suele representarse como una tabla:

| Marca | Modelo | Año |
|---------|---------|------|
| Ford | Focus | 2020 |
| Toyota | Corolla | 2022 |

### Filas

Representan observaciones o registros.

```text
Fila 1 → Ford Focus
Fila 2 → Toyota Corolla
```

### Columnas

Representan atributos o características.

```text
Marca
Modelo
Año
```

---

# Dimensionalidad

La dimensionalidad representa el número de ejes en una estructura de datos.

## 1D

Una lista:

```python
[10, 20, 30]
```

---

## 2D

Una tabla:

```python
[
 [10, 20],
 [30, 40]
]
```

Filas y columnas.

---

## 3D

Capas + filas + columnas.

```text
Capa
 └── Filas
      └── Columnas
```

---

# ¿Qué es un DataFrame?

Un DataFrame es la estructura principal de Pandas.

Es una tabla bidimensional con:

- Filas
- Columnas
- Índices
- Tipos de datos

Ejemplo:

| Marca | Modelo | Precio |
|---------|---------|---------|
| Ford | Focus | 25000 |
| Toyota | Corolla | 30000 |

---

# Paso 1: Importar Pandas

Antes de trabajar con datos debemos importar la biblioteca.

```python
import pandas as pd
```

### ¿Por qué se usa `pd`?

Es simplemente un alias.

En lugar de escribir:

```python
pandas.read_csv()
```

escribimos:

```python
pd.read_csv()
```

---

# Paso 2: Cargar un archivo CSV

Supongamos que tenemos:

```text
cars.csv
```

Cargamos los datos con:

```python
import pandas as pd

df = pd.read_csv("cars.csv")
```

---

## ¿Qué hace `read_csv()`?

- Lee el archivo CSV.
- Interpreta filas y columnas.
- Crea automáticamente un DataFrame.

Visualmente:

```text
cars.csv
      ↓
pd.read_csv()
      ↓
DataFrame
```

---

# Variable `df`

Por convención se suele utilizar:

```python
df
```

que significa:

```text
DataFrame
```

Ejemplo:

```python
df = pd.read_csv("cars.csv")
```

---

# Exploración Inicial de Datos (EDA)

Una vez cargado el dataset, lo primero es explorarlo.

Las tres funciones más utilizadas son:

```python
head()
info()
describe()
```

---

# 1. head()

Muestra las primeras filas.

```python
df.head()
```

Resultado:

| Marca | Modelo | Año |
|---------|---------|------|
| Ford | Focus | 2020 |
| Toyota | Corolla | 2022 |
| Honda | Civic | 2021 |

---

## Mostrar más filas

```python
df.head(10)
```

Muestra las primeras 10 filas.

---

## ¿Para qué sirve?

Permite:

- Verificar que la carga fue correcta.
- Conocer la estructura.
- Detectar errores rápidamente.
- Entender el contenido del dataset.

---

# 2. info()

Muestra información técnica del DataFrame.

```python
df.info()
```

Ejemplo:

```text
RangeIndex: 1000 entries
Data columns (total 5 columns)

Marca      object
Modelo     object
Precio     float64
Año         int64
Stock       int64
```

---

## Información que proporciona

### Número de filas

```text
1000 entries
```

### Número de columnas

```text
5 columns
```

### Tipos de datos

```text
int64
float64
object
```

### Valores nulos

```text
Non-Null Count
```

---

## ¿Para qué sirve?

Permite detectar:

- Datos faltantes.
- Tipos incorrectos.
- Problemas de calidad.

---

# 3. describe()

Genera estadísticas descriptivas.

```python
df.describe()
```

Ejemplo:

| Estadística | Precio |
|------------|---------|
| count | 1000 |
| mean | 25000 |
| std | 5000 |
| min | 10000 |
| max | 50000 |

---

## Estadísticas generadas

### count

Cantidad de registros.

### mean

Promedio.

### std

Desviación estándar.

### min

Valor mínimo.

### max

Valor máximo.

### quartiles

- 25%
- 50% (mediana)
- 75%

---

# Flujo típico de exploración

```python
import pandas as pd

df = pd.read_csv("cars.csv")

df.head()

df.info()

df.describe()
```

---

# Ejemplo completo

```python
import pandas as pd

df = pd.read_csv("cars.csv")

print(df.head())

print(df.info())

print(df.describe())
```

---

# Tipos de datos comunes en Pandas

| Tipo | Descripción |
|--------|-------------|
| int64 | Enteros |
| float64 | Decimales |
| object | Texto |
| bool | Verdadero/Falso |
| datetime64 | Fechas |

---

# Relación con Polars

Las mismas tareas pueden realizarse en Polars.

## Pandas

```python
import pandas as pd

df = pd.read_csv("cars.csv")
```

---

## Polars

```python
import polars as pl

df = pl.read_csv("cars.csv")
```

---

## Exploración inicial

### Pandas

```python
df.head()
df.info()
df.describe()
```

### Polars

```python
df.head()
df.describe()
df.schema
```

---

# Buenas prácticas al cargar datos

## 1. Revisar las primeras filas

```python
df.head()
```

---

## 2. Verificar tipos de datos

```python
df.info()
```

---

## 3. Analizar estadísticas

```python
df.describe()
```

---

## 4. Buscar valores nulos

```python
df.isnull().sum()
```

---

## 5. Validar tamaño del dataset

```python
df.shape
```

Resultado:

```python
(1000, 5)
```

```text
1000 filas
5 columnas
```

---

# Resumen Final

✅ Pandas es la biblioteca estándar para manipulación y análisis de datos en Python.

✅ Los datos se organizan en estructuras llamadas **DataFrames**.

✅ El primer paso en cualquier análisis es cargar el dataset mediante:

```python
pd.read_csv()
```

✅ Las funciones más importantes para la exploración inicial son:

| Función | Propósito |
|----------|------------|
| `head()` | Ver primeras filas |
| `info()` | Revisar estructura y tipos |
| `describe()` | Obtener estadísticas descriptivas |

✅ Estas funciones permiten comprender rápidamente la calidad, estructura y distribución de los datos antes de comenzar cualquier limpieza o análisis.

### Flujo recomendado

```text
Cargar datos
      ↓
head()
      ↓
info()
      ↓
describe()
      ↓
Analizar calidad
      ↓
Limpiar datos
      ↓
Analizar y visualizar
```

> La primera regla del análisis de datos es simple: antes de intentar responder preguntas, asegúrate de entender los datos que tienes delante.