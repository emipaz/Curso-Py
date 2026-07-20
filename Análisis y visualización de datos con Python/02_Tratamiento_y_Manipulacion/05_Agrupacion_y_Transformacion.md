
# Transformación de Datos con Pandas

## Introducción

La **transformación de datos** es una etapa fundamental del análisis de datos. Una vez que los datos han sido cargados y limpiados, es necesario organizarlos, combinarlos y resumirlos para extraer información útil.

Pandas proporciona herramientas muy potentes para realizar estas tareas mediante operaciones como:

- Fusión (Merge)
- Concatenación (Concat)
- Ordenación (Sort)
- Agrupación (GroupBy)
- Agregación (Aggregation)

Estas técnicas permiten convertir datos dispersos en información valiosa para la toma de decisiones.

---

# ¿Qué son las transformaciones de datos?

Las transformaciones consisten en modificar la estructura o el contenido de los datos para:

- ✅ Combinar información de distintas fuentes.
- ✅ Organizar datos de forma lógica.
- ✅ Detectar patrones y tendencias.
- ✅ Resumir grandes volúmenes de información.
- ✅ Preparar datos para análisis o Machine Learning.

---

# 1. Fusión de DataFrames (Merge)

La fusión permite combinar dos DataFrames utilizando columnas o índices comunes.

Puede imaginarse como unir dos piezas de un rompecabezas.

## Ejemplo

### Clientes

| id_cliente | nombre |
|------------|---------|
| 1 | Ana |
| 2 | Luis |

### Compras

| id_cliente | compra |
|------------|---------|
| 1 | Laptop |
| 2 | Mouse |

Resultado:

| id_cliente | nombre | compra |
|------------|---------|---------|
| 1 | Ana | Laptop |
| 2 | Luis | Mouse |

---

## Sintaxis

```python
pd.merge(
    df_clientes,
    df_compras,
    on="id_cliente"
)
```

---

## Tipos de Merge

| Tipo | Descripción |
|--------|------------|
| inner | Solo coincidencias |
| left | Todas las filas de la izquierda |
| right | Todas las filas de la derecha |
| outer | Todas las filas de ambos DataFrames |

---

## Ejemplo

```python
pd.merge(
    df1,
    df2,
    on="id",
    how="inner"
)
```

---

# 2. Concatenación (Concat)

La concatenación permite unir DataFrames sin necesidad de una columna común.

Puede imaginarse como apilar tablas.

---

## Concatenar filas

```python
pd.concat([df1, df2])
```

Resultado:

```text
df1
↓
df2
```

---

## Concatenar columnas

```python
pd.concat(
    [df1, df2],
    axis=1
)
```

Resultado:

```text
df1 | df2
```

---

## Casos de uso

- Archivos CSV mensuales.
- Datos provenientes de múltiples fuentes.
- División de datasets grandes.

---

# Diferencia entre Merge y Concat

| Merge | Concat |
|---------|---------|
| Une mediante una clave común | Une por posición |
| Similar a JOIN en SQL | Similar a apilar tablas |
| Relaciona datos | Combina estructuras |

---

# 3. Ordenación (Sorting)

Ordenar permite organizar los datos para facilitar el análisis.

---

## Orden ascendente

```python
df.sort_values("ventas")
```

---

## Orden descendente

```python
df.sort_values(
    "ventas",
    ascending=False
)
```

---

## Varias columnas

```python
df.sort_values(
    ["region", "ventas"]
)
```

---

## Casos prácticos

### Ventas

```python
df.sort_values(
    "ventas",
    ascending=False
)
```

Identifica los productos más vendidos.

---

### Comentarios de usuarios

```python
df.sort_values("fecha")
```

Permite analizar la evolución temporal.

---

# 4. Agrupación (GroupBy)

La agrupación divide los datos en grupos según una o varias columnas.

Es una de las herramientas más poderosas de Pandas.

---

## Ejemplo

| Región | Ventas |
|---------|---------|
| Norte | 100 |
| Norte | 200 |
| Sur | 150 |

Agrupar por región:

```python
df.groupby("Region")
```

Resultado conceptual:

```text
Norte
 ├─100
 └─200

Sur
 └─150
```

---

# 5. Agregación (Aggregation)

Después de agrupar, normalmente se realizan cálculos.

Esto se llama agregación.

---

## Funciones comunes

| Función | Descripción |
|----------|------------|
| mean() | Promedio |
| sum() | Suma |
| count() | Cantidad |
| min() | Mínimo |
| max() | Máximo |

---

## Ejemplo

```python
df.groupby("Region")["Ventas"].mean()
```

Resultado:

| Región | Promedio |
|---------|----------|
| Norte | 150 |
| Sur | 150 |

---

# Método agg()

Permite aplicar múltiples funciones simultáneamente.

---

## Ejemplo

```python
df.groupby("Region").agg({
    "Ventas": [
        "sum",
        "mean",
        "max"
    ]
})
```

Resultado:

| Región | Suma | Promedio | Máximo |
|---------|------|-----------|---------|
| Norte | 300 | 150 | 200 |
| Sur | 150 | 150 | 150 |

---

# Caso Práctico: Engagement por Edad

Supongamos:

| Edad | TiempoUso |
|--------|-----------|
| 18 | 20 |
| 18 | 30 |
| 25 | 40 |

Agrupar:

```python
df.groupby("Edad")["TiempoUso"].mean()
```

Resultado:

| Edad | Tiempo Promedio |
|--------|----------------|
| 18 | 25 |
| 25 | 40 |

Esto permite entender cómo interactúan distintos grupos demográficos con una aplicación.

---

# Funciones Principales de Transformación

| Función | Propósito |
|----------|------------|
| `pd.merge()` | Fusionar DataFrames |
| `pd.concat()` | Concatenar DataFrames |
| `sort_values()` | Ordenar datos |
| `groupby()` | Crear grupos |
| `agg()` | Agregar estadísticas |

---

# Flujo Típico de Transformación

```python
import pandas as pd

df = pd.read_csv("datos.csv")

# Fusionar
df = pd.merge(df1, df2)

# Ordenar
df = df.sort_values("ventas")

# Agrupar
grupo = df.groupby("region")

# Agregar
resultado = grupo["ventas"].sum()
```

---

# Buenas Prácticas

## 1. Definir un objetivo

Antes de transformar datos, pregúntese:

```text
¿Qué quiero descubrir?
```

Ejemplos:

- Ventas por región.
- Usuarios más activos.
- Productos más vendidos.

---

## 2. Documentar las transformaciones

Registrar:

- Qué se modificó.
- Por qué se modificó.
- Qué resultado se esperaba.

Esto mejora:

- Reproducibilidad.
- Mantenimiento.
- Auditoría.

---

## 3. Validar resultados

Después de cada transformación:

```python
df.head()
```

```python
df.shape
```

```python
df.info()
```

Verificar que los resultados sean correctos.

---

## 4. Experimentar

No existe una única forma correcta.

Pandas permite:

- Probar distintos enfoques.
- Comparar resultados.
- Refinar análisis.

---

# Equivalencias con SQL

| SQL | Pandas |
|--------|---------|
| JOIN | merge() |
| UNION ALL | concat() |
| ORDER BY | sort_values() |
| GROUP BY | groupby() |
| SUM | agg("sum") |
| AVG | agg("mean") |

---

# Pandas vs Polars en Transformaciones

## Pandas

```python
df.groupby("region")["ventas"].sum()
```

Ventajas:

- Sintaxis muy conocida.
- Gran comunidad.
- Excelente documentación.

---

## Polars

```python
df.group_by("region").agg(
    pl.col("ventas").sum()
)
```

Ventajas:

- Más rápido en datasets grandes.
- Menor consumo de memoria.
- Paralelismo automático.

---

## ¿Cuál elegir?

### Pandas

Ideal para:

- Aprendizaje.
- Análisis exploratorio.
- Machine Learning clásico.
- Jupyter Notebooks.

### Polars

Ideal para:

- ETLs.
- Big Data local.
- Millones de filas.
- Procesamiento de alto rendimiento.

---

# Resumen Final

✅ Las transformaciones permiten convertir datos en información útil.

✅ Las principales operaciones son:

1. Merge → Fusionar datos.
2. Concat → Unir estructuras.
3. Sort → Ordenar registros.
4. GroupBy → Crear grupos.
5. Aggregation → Calcular estadísticas.

✅ Estas herramientas permiten descubrir patrones, tendencias y relaciones ocultas.

✅ Documentar y validar cada transformación es una práctica esencial.

### Flujo recomendado

```text
Cargar datos
      ↓
Limpiar datos
      ↓
Fusionar (Merge)
      ↓
Ordenar (Sort)
      ↓
Agrupar (GroupBy)
      ↓
Agregar (Agg)
      ↓
Analizar resultados
```

> Los datos por sí solos rara vez cuentan una historia. Las transformaciones son el proceso que convierte datos dispersos en conocimiento accionable.



## ¿Cuál describe mejor el concepto de agrupación en el contexto de las transformaciones de datos utilizando pandas? Seleccione la mejor respuesta.

- Disposición de los datos en un orden específico para identificar patrones y valores atípicos.
- **Dividir los datos en grupos basados en columnas específicas y luego realizar cálculos en estos grupos.**
- Combinación de dos o más marcos de datos basados en columnas o índices comunes.
- Apilar varios marcos de datos uno encima de otro, ya sea por filas o por columnas.

Correcto

> Correcto La agrupación consiste en dividir los datos en subconjuntos basados en características compartidas, lo que permite realizar análisis y cálculos posteriores dentro de cada grupo.