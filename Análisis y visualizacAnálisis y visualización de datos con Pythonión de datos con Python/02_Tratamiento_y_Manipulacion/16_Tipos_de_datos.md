# Tipos de Datos en NumPy y Pandas

## Introducción

Cuando trabajamos con **Pandas**, en realidad estamos trabajando sobre la infraestructura de **NumPy**, ya que las columnas (`Series`) de un `DataFrame` utilizan internamente tipos de datos optimizados para almacenar y procesar información eficientemente.

Elegir correctamente el tipo de dato permite:

- Reducir el consumo de memoria.
- Mejorar el rendimiento.
- Facilitar el análisis.
- Evitar errores de conversión.
- Optimizar modelos de Machine Learning.

---

# Relación entre Python, NumPy y Pandas

```text
Python
   ↓
NumPy (arrays y tipos de datos)
   ↓
Pandas (Series y DataFrames)
```

Ejemplo:

```python
import pandas as pd
import numpy as np
```

```python
df = pd.DataFrame({
    "edad": [20, 25, 30],
    "nombre":["juan","mateo","maria"],
    "sexo":["Masculino","Masculino","Femenino"]
})
display(df)
print(df["edad"].dtype)
```

```python
df.info()
```

---

# Inspeccionar tipos de datos

## Tipo de una columna

```python
df["edad"].dtype
```

---

## Tipos de todas las columnas

```python
df.dtypes
```

Ejemplo:


edad           int64
salario      float64
nombre        object
activo          bool
dtype: object


---

# Tipos Numéricos Enteros (NumPy)

## Enteros con signo

| Tipo | Bytes | Rango |
|--------|--------|--------|
| int8 | 1 | -128 a 127 |
| int16 | 2 | -32.768 a 32.767 |
| int32 | 4 | ±2.147 millones |
| int64 | 8 | ±9.22e18 |

---

## Ejemplo

```python
import numpy as np

edad = np.array([20, 25, 30], dtype=np.int8)

edad.dtype
```

---

## Comparación de memoria

```python
import numpy as np

a = np.array([1,2,3], dtype=np.int8)
b = np.array([1,2,3], dtype=np.int64)

print(a.nbytes)
print(b.nbytes)
```

---

# Enteros sin signo (Unsigned)

Sólo admiten valores positivos.

| Tipo | Rango |
|--------|--------|
| uint8 | 0 a 255 |
| uint16 | 0 a 65.535 |
| uint32 | 0 a 4.294 millones |
| uint64 | Muy grande |

---

## Ejemplo

```python
pixel_normal = np.array([0,100,255])
pixel_8bits = np.array([0,100,255], dtype=np.uint8)

```

```python
pixel_normal
```

```python
pixel_normal.nbytes
```

```python
pixel_8bits
```

```python
pixel_8bits.nbytes
```

---

## Casos de uso

- Imágenes.
- Cantidades positivas.
- Códigos numéricos.

---

# Tipos de Punto Flotante

| Tipo | Bytes |
|--------|--------|
| float16 | 2 |
| float32 | 4 |
| float64 | 8 |

---

## Ejemplo

```python
precio = np.array(
    [10.5, 20.3, 30.7],
    dtype=np.float64
)
```

```python
precio.nbytes
```

```python
import pandas as pd
```

```python
df_1 = pd.DataFrame ({
    "precio":precio
})
display(df_1)
df_1.info()
```

---

## Comparación

```python
df_1["precio"] = df_1["precio"].astype("float16")
display(df_1)
df_1.info()
```

Reduce memoria respecto a:


---

# Booleanos

Representan:

```python
True
False
```

---

## Ejemplo

```python
activo = np.array(
    [True, False, True],
    dtype=np.bool_
)
print(activo)
activo.nbytes
```

---

## En Pandas

```python
df["activo"] = activo
display(df)
display(df.info())


df["activo"] = df["activo"].astype("int8")
display(df)
df.info()
```

---

# Cadenas de Texto

## Tipo object

Históricamente Pandas almacenaba texto usando:


Ejemplo:

```python
df["nombre"].dtype
```

Resultado:


---

# Nuevo tipo string

Recomendado actualmente.

```python
df["nombre"] = df["nombre"].astype("string")
df.info()
```

Resultado:

```python
df["nombre"].dtype
```

En pandas, la diferencia entre dtype str y dtype string radica en cómo se manejan internamente los datos de texto y qué funcionalidades ofrecen:

1. dtype=str
  - Cuando se usa dtype=str en pandas, los datos se almacenan como objetos de tipo object en pandas, que en realidad son cadenas de texto de Python estándar (str de Python).
  - Esto significa que internamente es una columna de tipo object que contiene cadenas de texto nativas de Python.
  - No tiene funcionalidades específicas de pandas para cadenas, solo se comporta como una colección de objetos Python.
  - Es el comportamiento tradicional y más antiguo en pandas para manejar texto.

2. dtype="string" (con comillas)
  - Introducido en versiones recientes de pandas (a partir de pandas 1.0), es un tipo de dato específico para cadenas de texto llamado StringDtype.
  - Es un tipo de dato nativo de pandas para texto, que ofrece mejor integración y funcionalidades específicas para trabajar con datos de texto.
  - Permite manejar valores faltantes (NA) de forma más consistente, usando pd.NA en lugar de np.nan o None.
  - Ofrece métodos vectorizados y optimizados para operaciones con texto, mejor rendimiento y menor uso de memoria en algunos casos.
  - Facilita la interoperabilidad con otras funciones de pandas que esperan tipos de datos nativos.

<!-- #region -->
Resumen en tabla

|Característica|dtype=str (object)|dtype="string" (StringDtype)|
|:---------|:-|:---------------------------|
|Tipo interno|object (Python str)|Tipo nativo pandas StringDtype|
|Manejo de valores faltantes|None o np.nan|pd.NA (más consistente)|
|Funcionalidades pandas|Limitadas|Mejor integración y métodos optimizados|
|Rendimiento|Menor optimización|Mejor optimización en operaciones vectorizadas|
|Compatibilidad|Tradicional, compatible con todo|Requiere pandas >= 1.0|


Conclusión
> Si buscas aprovechar las funcionalidades modernas de pandas para trabajar con texto, usar dtype="string" es la mejor opción.

> Si solo necesitas almacenar texto sin funcionalidades adicionales, dtype=str funciona pero es menos eficiente y menos integrado.
<!-- #endregion -->

# Datos Categóricos

Uno de los tipos más importantes para análisis de datos.

---

## ¿Qué es un dato categórico?

Variables con un conjunto limitado de valores.

Ejemplos:

- Sexo
- Provincia
- Estado civil
- Nivel educativo

---

## Ejemplo

```python
df["sexo_categoria"] = df["sexo"].astype("category")

df.info()
```

## Verificar

```python
df["sexo_categoria"].dtype
```

Resultado:


---

# Beneficios de category

## Menor consumo de memoria

```python
df["sexo"].memory_usage(deep=True)
```

Comparar con:

```python
df.sexo_categoria.memory_usage(deep=True)
```

---

## Categorías únicas

```python
df["sexo_categoria"].cat.categories
```

---

## Códigos internos

```python
df["sexo_categoria"].cat.codes
```

---

## Categorías ordenadas

```python
# Crear un DataFrame con una columna de tamaños
data = {'Tamaño': ['Pequeño', 'Mediano', 'Grande', 'Mediano', 'Pequeño', 'Grande']}
df_categoria = pd.DataFrame(data)
df_categoria
```

```python
# Definir la columna 'Tamaño' como categoría ordenada con un orden específico
orden = ['Pequeño', 'Mediano', 'Grande']
df_categoria['Tamaño'] = pd.Categorical(df_categoria['Tamaño'], categories=orden, ordered=True)
print(df_categoria)
print('\nTipo de dato de la columna Tamaño:')
print(df_categoria['Tamaño'].dtype)
```

```python
df_categoria['Tamaño'].dtype
```

```python
# Ejemplo de comparación entre categorías ordenadas
print('\nComparación entre categorías ordenadas:')
print(df_categoria['Tamaño'][0] < df_categoria['Tamaño'][2])  # Pequeño < Grande → True
print(df_categoria['Tamaño'][1] > df_categoria['Tamaño'][0])  # Mediano > Pequeño → True
```

```python
# Ordenar el DataFrame según la columna categórica ordenada
df_sorted = df_categoria.sort_values('Tamaño')
print('\nDataFrame ordenado por Tamaño:')
print(df_sorted)
```

---

# Fechas y Horas

Uno de los tipos más utilizados en análisis.

---

## datetime64[ns]

Representa fecha y hora.

```python
data = {
    'id': [1,2,3,4,5],
    'fecha_str': ['2023-01-05', '05/02/2023', '2023-03-10 14:30', '2023-04-01T09:15:00', "2025-12-31"]
}
df_fechas = pd.DataFrame(data)

# Conversión robusta: detecta formatos; errores -> NaT
df_fechas['fecha'] = pd.to_datetime(df_fechas['fecha_str'], errors='coerce', dayfirst=False)
display(df_fechas)
print(df_fechas['fecha'].dtype)  # datetime64[ns]
```

```python
data = {
    'id': [1,2,3,4],
    'fecha_str': ['2023-01-05', '05/02/2023', '2023-03-10 14:30', '2023-04-01T09:15:00']
}
def parsear_fecha(fecha_str):
    formatos = [
        '%Y-%m-%d',           # 2023-01-05
        '%d/%m/%Y',           # 05/02/2023 (día/mes/año)
        '%Y-%m-%d %H:%M',     # 2023-03-10 14:30
        '%Y-%m-%dT%H:%M:%S',  # 2023-04-01T09:15:00
    ]
    for fmt in formatos:
        try:
            return pd.to_datetime(fecha_str, format=fmt)
        except (ValueError, TypeError):
            continue
    return pd.NaT  # si ninguno matchea

df_fechas['fecha'] = df_fechas['fecha_str'].apply(parsear_fecha)
display(df_fechas)
print(df_fechas['fecha'].dtype)
```

---

# Componentes de fecha

```python
df_fechas["fecha"].dt.year
```

```python
df_fechas["fecha"].dt.month
```

```python
df_fechas["fecha"].dt.day
```

```python
df_fechas["fecha"].dt.day_name()
```

---

# Diferencia entre fechas

```python
df_fechas.loc[1,"fecha"]- df_fechas.loc[0,"fecha"]
```

Resultado:


---

# Timedelta

Representa duración.

```python
pd.Timedelta(days=5)
```

---

## Ejemplo

```python

```

---

# Tipos Nullable de Pandas

Desde Pandas moderno se introdujeron tipos que admiten nulos.

---

## Int64 (nullable)

```python
df
```

```python
df["edad"] = df["edad"].astype("Int64")
```

Observe la diferencia:


---

## Permite


`<NA>`



---

## Ejemplo

```python
pd.Series(
    [10,20,None],
    dtype="Int64"
)
```

---

# Float64 Nullable


`dtype="Float64"`

```python
pd.Series([1.23,0.25,None,"3.1416"], 
          dtype="Float64")
```

---

# Boolean Nullable


`dtype="boolean"`


Ejemplo:

```python
pd.Series(
    [True, False, None],
    dtype="boolean"
)
```

---

# Tipos Especiales de NumPy

---

## Complex

```python
np.complex64
np.complex128
```

Ejemplo:

```python
z = np.array(
    [1+2j, 3+4j],
    dtype=np.complex128
)
```

```python
z
```

---

# Conversión de Tipos

## astype()

```python
df["edad"] = (
    df["edad"]
    .astype("int32")
)
```

---

## Múltiples columnas

```python
df = df.astype({
    "edad":"int16",
    "salario":"float32"
})
```

---

# Optimización de Memoria

## Antes

```python
df.info(memory_usage="deep")
```

---

## Optimización

```python
df
```

```python
df["edad"] = df["edad"].astype("int8")

df["sexo"] = df["sexo"].astype("category")
```

---

## Después

```python
df.info(memory_usage="deep")
```

<!-- #region -->
---

# Tabla Resumen

| Tipo Pandas | Base NumPy | Uso |
|-------------|------------|------|
| int8 | np.int8 | Enteros pequeños |
| int16 | np.int16 | Enteros medianos |
| int32 | np.int32 | Enteros estándar |
| int64 | np.int64 | Enteros grandes |
| uint8 | np.uint8 | Enteros positivos |
| float32 | np.float32 | Decimales |
| float64 | np.float64 | Mayor precisión |
| bool | np.bool_ | Verdadero/Falso |
| string | object/string | Texto |
| category | category | Variables categóricas |
| datetime64[ns] | datetime64 | Fechas |
| timedelta64[ns] | timedelta64 | Duraciones |
| Int64 | Nullable | Enteros con NA |
| Float64 | Nullable | Decimales con NA |
| boolean | Nullable | Booleanos con NA |

---

# Buenas Prácticas

✅ Usar `category` para variables con pocos valores únicos.

✅ Convertir fechas con `pd.to_datetime()`.

✅ Utilizar `float32` cuando no se requiera alta precisión.

✅ Utilizar `int8`, `int16` o `int32` según el rango de valores.

✅ Utilizar tipos nullable (`Int64`, `boolean`) cuando existan nulos.

✅ Revisar periódicamente:

```python
df.info(memory_usage="deep")
```
<!-- #endregion -->

---

# Conclusiones

- Pandas se basa en los tipos de datos de NumPy.
- Elegir correctamente los tipos mejora rendimiento y memoria.
- Los tipos más importantes en análisis de datos son:
  - Numéricos (`int`, `float`)
  - Categóricos (`category`)
  - Temporales (`datetime64`, `timedelta64`)
  - Booleanos (`bool`)
  - Texto (`string`)
- Los tipos nullable modernos de Pandas facilitan el manejo de valores faltantes.
- La optimización de tipos es una de las primeras tareas de cualquier proceso de limpieza y preparación de datos.


