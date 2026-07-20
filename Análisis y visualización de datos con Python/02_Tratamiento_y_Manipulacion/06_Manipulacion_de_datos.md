
# Manipulación de Datos con Pandas

## Introducción

La manipulación de datos es una de las habilidades más importantes en análisis de datos, ciencia de datos e ingeniería de datos.

La biblioteca **Pandas** proporciona herramientas potentes para:

- Limpiar datos.
- Transformar información.
- Analizar tendencias.
- Preparar datos para Machine Learning.
- Generar reportes y métricas.

---

# ¿Por qué Pandas es tan importante?

Pandas permite trabajar con datos de forma similar a una hoja de cálculo avanzada, pero con toda la potencia de Python.

Sus principales ventajas son:

- ✅ Manipulación eficiente de grandes volúmenes de datos.
- ✅ Transformaciones complejas con pocas líneas de código.
- ✅ Integración con bibliotecas de Machine Learning y visualización.
- ✅ Soporte para múltiples formatos de datos.

---

# Cargar Datos

Antes de comenzar cualquier análisis es necesario importar Pandas.

```python
import pandas as pd
```

---

## Leer un archivo CSV

```python
df = pd.read_csv("ventas.csv")
```

El resultado es un **DataFrame**, la estructura principal de Pandas.

---

## Visualizar las primeras filas

```python
df.head()
```

Permite:

- Conocer la estructura del dataset.
- Detectar errores rápidamente.
- Verificar que la carga fue correcta.

---

# Transformaciones Fundamentales

## 1. Ordenación (Sorting)

Ordenar ayuda a identificar rápidamente patrones y tendencias.

---

### Orden ascendente

```python
df.sort_values("Ventas")
```

---

### Orden descendente

```python
df.sort_values(
    "Ventas",
    ascending=False
)
```

---

## Caso práctico

Identificar los productos más vendidos:

```python
df.sort_values(
    "Ventas",
    ascending=False
)
```

Beneficios:

- Detectar productos estrella.
- Priorizar recursos.
- Identificar oportunidades de negocio.

---

# 2. Agrupación (GroupBy)

Permite dividir los datos en grupos basados en una o más columnas.

---

## Ejemplo

| Región | Ventas |
|---------|---------|
| Norte | 100 |
| Norte | 200 |
| Sur | 150 |

Agrupar:

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

## Caso práctico

Analizar ventas por región:

```python
df.groupby("Region")["Ventas"].sum()
```

Resultado:

| Región | Ventas Totales |
|---------|---------------|
| Norte | 300 |
| Sur | 150 |

---

# 3. Agregación (Aggregation)

Permite resumir información mediante cálculos estadísticos.

---

## Funciones comunes

| Función | Descripción |
|----------|------------|
| sum() | Suma |
| mean() | Promedio |
| count() | Cantidad |
| min() | Mínimo |
| max() | Máximo |

---

## Ejemplo

```python
df["Ventas"].mean()
```

Resultado:

```text
Promedio general de ventas
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

# 4. Filtrado

Permite centrarse únicamente en los datos relevantes.

---

## Ejemplo

Ventas superiores a 1000:

```python
df[df["Ventas"] > 1000]
```

Resultado:

```text
Solo transacciones de alto valor
```

---

## Beneficios

- Reducir ruido.
- Analizar segmentos específicos.
- Detectar casos especiales.

---

# 5. Aplicar Funciones Personalizadas

Pandas permite crear transformaciones adaptadas a necesidades específicas.

---

## Crear función

```python
def descuento(valor):
    return valor * 0.90
```

---

## Aplicar función

```python
df["Ventas_Descuento"] = (
    df["Ventas"]
    .apply(descuento)
)
```

Resultado:

| Ventas | Ventas_Descuento |
|---------|------------------|
| 1000 | 900 |
| 500 | 450 |

---

## Casos de uso

- Cálculo de impuestos.
- Descuentos.
- Clasificaciones.
- Conversión de unidades.

---

# 6. Tablas Dinámicas (Pivot)

Pivot reorganiza los datos para facilitar comparaciones.

---

## Ejemplo

```python
tabla = df.pivot_table(
    index="Region",
    columns="Producto",
    values="Ventas"
)
```

Resultado conceptual:

| Región | Laptop | Mouse |
|---------|---------|---------|
| Norte | 1000 | 500 |
| Sur | 800 | 300 |

---

## Beneficios

- Comparaciones rápidas.
- Análisis multidimensional.
- Visualización más clara.

---

# Manejo de Valores Faltantes

Los datos reales suelen contener información incompleta.

---

# 7. Rellenar valores faltantes

## Con cero

```python
df.fillna(0)
```

---

## Con promedio

```python
df.fillna(
    df["Ventas"].mean()
)
```

---

### Ventajas

- Conserva registros.
- Facilita cálculos posteriores.

---

# 8. Eliminar valores faltantes

```python
df.dropna()
```

---

### Ventajas

- Mantiene la calidad de los datos.

### Desventajas

- Puede perder información valiosa.

---

# Combinar DataFrames

Muchas veces los datos provienen de múltiples fuentes.

---

# 9. Concatenación

Une DataFrames por filas o columnas.

---

## Filas

```python
pd.concat([df1, df2])
```

Visualmente:

```text
df1
↓
df2
```

---

## Columnas

```python
pd.concat(
    [df1, df2],
    axis=1
)
```

---

## Casos de uso

- Archivos mensuales.
- Datos históricos.
- Consolidación de reportes.

---

# 10. Fusión (Merge)

Relaciona DataFrames mediante columnas comunes.

---

## Ejemplo

Clientes:

| id | Nombre |
|----|---------|
| 1 | Ana |

Compras:

| id | Producto |
|----|----------|
| 1 | Laptop |

---

Resultado:

| id | Nombre | Producto |
|----|---------|----------|
| 1 | Ana | Laptop |

---

## Código

```python
pd.merge(
    clientes,
    compras,
    on="id"
)
```

---

## Similar a SQL

```sql
SELECT *
FROM clientes
JOIN compras
ON clientes.id = compras.id
```

---

# Flujo Típico de Manipulación

```python
import pandas as pd

df = pd.read_csv("ventas.csv")

# Explorar
df.head()

# Ordenar
df.sort_values("Ventas")

# Filtrar
df[df["Ventas"] > 1000]

# Agrupar
df.groupby("Region")

# Agregar
df.groupby("Region")["Ventas"].sum()

# Transformar
df["Ventas"] = (
    df["Ventas"] * 0.90
)
```

---

# Pandas vs Polars

## Ordenación

### Pandas

```python
df.sort_values("Ventas")
```

### Polars

```python
df.sort("Ventas")
```

---

## Agrupación

### Pandas

```python
df.groupby("Region").sum()
```

### Polars

```python
df.group_by("Region").sum()
```

# Resumen Final

✅ Pandas es una herramienta esencial para la manipulación de datos en Python.

✅ Las transformaciones más importantes son:

1. Ordenación (`sort_values`)
2. Agrupación (`groupby`)
3. Agregación (`mean`, `sum`, `count`)
4. Filtrado
5. Aplicación de funciones (`apply`)
6. Pivotado (`pivot_table`)
7. Manejo de nulos (`fillna`, `dropna`)
8. Concatenación (`concat`)
9. Fusión (`merge`)

✅ Estas operaciones permiten convertir datos crudos en información útil para la toma de decisiones.

### Flujo recomendado

```text
Cargar datos
      ↓
Explorar
      ↓
Limpiar
      ↓
Filtrar
      ↓
Ordenar
      ↓
Agrupar
      ↓
Agregar
      ↓
Visualizar
      ↓
Tomar decisiones
```

> Pandas no solo permite analizar datos; permite transformarlos en conocimiento útil para resolver problemas reales.




## Escenario: Usted tiene un DataFrame de pandas llamado datos_ventas [SAY: Sales Data] que contiene columnas para "Producto," "Región," y "Ventas." Quiere identificar el producto más vendido en cada región.

### Pregunta Stem: ¿Qué operaciones de Pandas utilizaría para conseguirlo? Seleccione la mejor respuesta.

Filtra el DataFrame para incluir sólo las filas con el valor más alto de "Ventas".
Ordena el DataFrame por "Ventas" en orden descendente.
- **Agrupe el DataFrame por "Región" y luego ordene cada grupo por "Ventas" en orden descendente.**
Agrupe el DataFrame por "Producto" y calcule la suma de "Ventas" de cada producto.

Correcto

> Correcto Esta es la forma más eficaz de identificar el producto más vendido en cada región. La agrupación permite analizar las ventas dentro de cada región, y la clasificación ayuda a identificar el producto más vendido. 