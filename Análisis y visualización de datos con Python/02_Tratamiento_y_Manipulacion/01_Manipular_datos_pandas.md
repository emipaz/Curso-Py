# Introducción a Pandas: El Superhéroe del Manejo de Datos en Python

## Idea principal
Pandas es una biblioteca de Python especializada en la manipulación, limpieza, análisis y transformación de datos. Se la presenta como una "navaja suiza" para trabajar con grandes cantidades de información.

---

# ¿Qué es Pandas?

- Es una de las bibliotecas más populares de Python para análisis de datos.
- Permite cargar datos desde:
  - Excel
  - CSV
  - Bases de datos
  - JSON
  - APIs
- Facilita la limpieza y transformación de datos.
- Ayuda a descubrir patrones e información útil.

### Analogía

> Si eres un detective de datos, Pandas es tu lupa.

---

# Problema que resuelve

Los datos reales suelen venir en hojas de cálculo enormes y desordenadas:

- Datos faltantes.
- Valores incorrectos.
- Formatos inconsistentes.
- Información dispersa.

Pandas permite convertir esos datos en información útil para la toma de decisiones.

---

# Ejemplo: Tienda Online

Imagina que tienes una tienda de comercio electrónico con datos de:

- Clientes.
- Ventas.
- Productos.
- Fechas de compra.

Con Pandas puedes:

### Filtrar información

Mostrar únicamente las ventas de diciembre:

```python
ventas_diciembre = df[df["mes"] == "Diciembre"]
```

### Calcular estadísticas

Importe promedio de compra por cliente:

```python
promedio = df["importe_compra"].mean()
```

### Agrupar datos

Ventas por producto:

```python
ventas_por_producto = df.groupby(
    "producto"
)["ventas"].sum()
```

---

# ¿Es difícil aprender Pandas?

No.

Según el diálogo:

> Aprender Pandas es como aprender un nuevo baile: al principio requiere práctica, pero está diseñado para ser fácil de usar.

### Ventajas para principiantes

- Sintaxis intuitiva.
- Excelente documentación.
- Gran comunidad.
- Integración con otras herramientas de Python.

---

# ¿Qué se puede hacer con Pandas?

## 1. Limpiar datos

Eliminar valores nulos:

```python
df = df.dropna()
```

Rellenar valores faltantes:

```python
df["edad"] = df["edad"].fillna(
    df["edad"].mean()
)
```

---

## 2. Filtrar información

```python
clientes_vip = df[
    df["gasto_total"] > 1000
]
```

---

## 3. Analizar tendencias

```python
ventas_mensuales = df.groupby(
    "mes"
)["ventas"].sum()
```

Permite identificar:

- Estacionalidad.
- Crecimiento.
- Caídas en ventas.
- Comportamiento de clientes.

---

## 4. Realizar cálculos estadísticos

```python
df.describe()
```

Obtiene:

- Promedio.
- Mediana.
- Máximo.
- Mínimo.
- Desviación estándar.

---

## 5. Preparar datos para Machine Learning

```python
X = df.drop("objetivo", axis=1)
y = df["objetivo"]
```

Pandas suele ser el primer paso antes de utilizar Scikit-Learn.

---

## 6. Crear visualizaciones

Combinado con Matplotlib:

```python
import matplotlib.pyplot as plt

df["ventas"].plot()
plt.show()
```

Permite visualizar:

- Tendencias.
- Comparaciones.
- Distribuciones.
- Evolución temporal.

---

# Conceptos fundamentales de Pandas

## Series

Estructura unidimensional.

```python
import pandas as pd

s = pd.Series([10, 20, 30])
```

Resultado:

```text
0    10
1    20
2    30
```

---

## DataFrame

Tabla bidimensional similar a Excel.

```python
df = pd.DataFrame({
    "Nombre": ["Ana", "Luis"],
    "Edad": [25, 30]
})
```

Resultado:

| Nombre | Edad |
|----------|------|
| Ana | 25 |
| Luis | 30 |

---

# Flujo típico de trabajo con Pandas

```text
1. Cargar datos
        ↓
2. Explorar datos
        ↓
3. Limpiar datos
        ↓
4. Transformar datos
        ↓
5. Analizar datos
        ↓
6. Visualizar resultados
        ↓
7. Tomar decisiones
```

---

# Instalación

```bash
pip install pandas
```

Verificar instalación:

```python
import pandas as pd

print(pd.__version__)
```

---

# Resumen Final

✅ Pandas es la biblioteca más utilizada para manipulación y análisis de datos en Python.

✅ Permite cargar, limpiar, transformar y analizar información de forma sencilla.

✅ Es especialmente útil para trabajar con archivos Excel, CSV y bases de datos.

✅ Facilita la detección de tendencias, generación de estadísticas y preparación de datos para Machine Learning.

✅ Sus estructuras principales son:
- Series
- DataFrame

✅ Puede combinarse con:
- NumPy
- Matplotlib
- Scikit-Learn
- Seaborn

> "Piensa en los datos como un bloque de arcilla. Pandas es la herramienta que te permite moldearlo hasta convertirlo en información valiosa."

___

# Anexo: Pandas vs Polars

## Introducción

Durante muchos años, **Pandas** ha sido la biblioteca estándar para análisis y manipulación de datos en Python. Sin embargo, en los últimos años ha ganado popularidad **Polars**, una biblioteca moderna diseñada para trabajar con grandes volúmenes de datos de forma más rápida y eficiente.

Ambas herramientas tienen el mismo objetivo: permitir cargar, transformar, limpiar y analizar datos. La diferencia principal está en su arquitectura y rendimiento.

---

# ¿Qué es Pandas?

Pandas es una biblioteca basada principalmente en:

- NumPy
- DataFrames
- Ejecución inmediata (eager execution)

Características:

- Fácil de aprender.
- Amplia documentación.
- Gran ecosistema.
- Compatible con casi todas las bibliotecas de ciencia de datos.

```python
import pandas as pd

df = pd.read_csv("ventas.csv")
```

---

# ¿Qué es Polars?

Polars es una biblioteca moderna escrita en Rust que ofrece:

- Mayor velocidad.
- Menor consumo de memoria.
- Procesamiento paralelo.
- Optimización automática de consultas.

```python
import polars as pl

df = pl.read_csv("ventas.csv")
```

---

# Comparación rápida

| Característica | Pandas | Polars |
|---------------|---------|---------|
| Facilidad de aprendizaje | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| Ecosistema | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| Velocidad | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Uso de memoria | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Paralelismo | ❌ Limitado | ✅ Nativo |
| Big Data local | ⭐⭐ | ⭐⭐⭐⭐⭐ |
| Integración con ML | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| Madurez | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |

---

# Ventajas de Polars sobre Pandas

## 1. Mucho más rápido

En datasets grandes, Polars suele ser:

- 2x a 10x más rápido.
- En algunos casos hasta 50x más rápido.

Ejemplo:

```python
# Pandas
df.groupby("producto")["ventas"].sum()

# Polars
df.group_by("producto").agg(
    pl.col("ventas").sum()
)
```

---

## 2. Menor consumo de memoria

Polars utiliza:

- Apache Arrow.
- Estructuras de memoria más eficientes.

Esto permite trabajar con datasets más grandes sin agotar la RAM.

---

## 3. Paralelismo automático

Pandas normalmente usa un solo núcleo.

Polars aprovecha múltiples núcleos automáticamente.

```text
CPU de 8 núcleos

Pandas → usa principalmente 1
Polars → usa los 8
```

---

## 4. Lazy Evaluation

Una de las mayores ventajas.

Polars puede construir un plan de ejecución antes de procesar los datos.

```python
df = (
    pl.scan_csv("ventas.csv")
    .filter(pl.col("ventas") > 100)
    .group_by("producto")
    .agg(pl.col("ventas").sum())
)
```

Nada se ejecuta hasta:

```python
df.collect()
```

Esto permite optimizaciones automáticas.

---

## 5. Excelente integración con Apache Arrow

Polars trabaja de forma nativa con:

- Arrow
- Parquet
- Feather

Formatos muy utilizados en ingeniería de datos moderna.

---

# Ventajas de Pandas sobre Polars

## 1. Ecosistema gigantesco

Prácticamente todas las bibliotecas de Python esperan un DataFrame de Pandas.

Ejemplos:

- Scikit-Learn
- StatsModels
- XGBoost
- LightGBM
- Seaborn
- Matplotlib

---

## 2. Mayor cantidad de tutoriales

Es mucho más sencillo encontrar:

- Cursos.
- Ejemplos.
- Soluciones en Stack Overflow.
- Libros.

---

## 3. Más conocido en empresas

Actualmente Pandas sigue siendo el estándar de facto.

---

## 4. Más flexible para análisis exploratorio

Muchos analistas trabajan directamente con:

```python
df.head()
df.info()
df.describe()
```

Pandas resulta muy cómodo para este tipo de trabajo.

---

# ¿Cuándo usar Pandas?

### Ideal para:

- Aprender análisis de datos.
- Ciencia de datos tradicional.
- Machine Learning.
- Jupyter Notebooks.
- Dashboards pequeños y medianos.
- Datos menores a algunos millones de registros.

Ejemplos:

- Análisis de ventas.
- Reportes empresariales.
- Estudios estadísticos.
- Exploración de datasets.

---

# ¿Cuándo usar Polars?

### Ideal para:

- Grandes volúmenes de datos.
- ETL.
- Ingeniería de datos.
- Procesamiento masivo de CSV.
- Archivos Parquet.
- Pipelines de transformación.

Ejemplos:

- 20 millones de registros.
- Logs de aplicaciones.
- Datos de sensores.
- Procesamiento financiero.
- Data Warehouses.

---

# Estrategia recomendada: usar ambos

No es necesario elegir uno u otro.

Muchos proyectos modernos utilizan ambos.

```text
Polars
   ↓
Transformación rápida
   ↓
Pandas
   ↓
Machine Learning
   ↓
Scikit-Learn
```

---

# Ejemplo práctico

## Carga masiva con Polars

```python
import polars as pl

df = pl.read_csv("ventas_grandes.csv")
```

## Limpieza rápida

```python
df = df.filter(
    pl.col("ventas") > 0
)
```

## Conversión a Pandas

```python
df_pandas = df.to_pandas()
```

## Entrenamiento de modelo

```python
from sklearn.ensemble import RandomForestClassifier

modelo = RandomForestClassifier()
modelo.fit(X, y)
```

---

# Tabla de decisión rápida

| Situación | Recomendación |
|------------|---------------|
| Estoy aprendiendo análisis de datos | Pandas |
| Uso Jupyter Notebook | Pandas |
| Machine Learning | Pandas |
| ETL masivo | Polars |
| Más de 10 millones de filas | Polars |
| Trabajo con Parquet | Polars |
| Necesito máxima velocidad | Polars |
| Proyecto empresarial tradicional | Pandas |
| Ingeniería de datos moderna | Polars |
| Necesito compatibilidad con muchas librerías | Pandas |

---

# Recomendación para 2026

Para un desarrollador Python orientado a datos:

### Nivel inicial

Aprender primero:

```text
Pandas
↓
NumPy
↓
Matplotlib
↓
Scikit-Learn
```

### Nivel intermedio

Incorporar:

```text
Polars
↓
PyArrow
↓
DuckDB
↓
DBT
```

### Nivel avanzado

Combinar:

```text
Polars + DuckDB + Parquet + DBT
```

para construir pipelines modernos de análisis e ingeniería de datos.

---

# Conclusión

- **Pandas** sigue siendo la herramienta más importante para análisis de datos y Machine Learning.
- **Polars** es una alternativa moderna, más rápida y eficiente para grandes volúmenes de información.
- No son competidores directos: muchas veces son complementarios.
- La mejor estrategia actual es dominar Pandas primero y luego incorporar Polars para tareas de alto rendimiento y procesamiento masivo de datos.