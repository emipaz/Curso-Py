# Bibliotecas Esenciales de Python para el Análisis de Datos

## Introducción

Python se ha convertido en uno de los lenguajes más utilizados para el análisis de datos y la computación científica gracias a su amplio ecosistema de bibliotecas especializadas. Entre las más importantes se encuentran:

- **NumPy** → Computación numérica y manipulación eficiente de matrices.
- **Pandas** → Limpieza, transformación y análisis de datos.
- **Matplotlib** → Visualización de datos.
- **Apache Superset** → Visualizaciones estadísticas avanzadas y atractivas.

Estas herramientas permiten transformar datos sin procesar en información útil para la toma de decisiones.

---

# NumPy (Numerical Python)

## ¿Qué es?

NumPy proporciona la estructura de datos **ndarray (N-dimensional Array)**, diseñada para almacenar y procesar grandes cantidades de datos numéricos de manera eficiente.

### Capacidades principales

- Operaciones matemáticas de alto rendimiento.
- Álgebra lineal.
- Transformadas de Fourier.
- Estadística y cálculo científico.
- Manipulación de matrices multidimensionales.

---

## Casos de uso

### Computación científica e ingeniería

Permite modelar y simular sistemas complejos:

- Predicción meteorológica.
- Simulación física.
- Análisis estructural.
- Modelado matemático.

### Procesamiento de imágenes

Las imágenes son matrices de píxeles, por lo que NumPy facilita:

- Eliminación de ruido.
- Detección de bordes.
- Reconocimiento de objetos.
- Aplicación de filtros y efectos.

---

## Vectorización

La vectorización permite reemplazar bucles tradicionales por operaciones sobre matrices completas.

### Ejemplo

```python
import numpy as np

prices = np.array([100, 105, 112, 98])

percentage_change = (
    (prices[1:] - prices[:-1])
    / prices[:-1]
    * 100
)

print(percentage_change)
```

### Ventajas

- Código más corto.
- Mayor legibilidad.
- Mucho mejor rendimiento.

---

## Broadcasting (Difusión)

Permite realizar operaciones entre matrices de diferentes dimensiones sin necesidad de bucles.

### Ejemplo incorrecto

```python
import numpy as np

arr1 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

arr2 = np.array([10, 20])

result = arr1 + arr2
```

**Error**

```text
ValueError: operands could not be broadcast together
```

---

### Solución con reshape()

```python
arr2_reshaped = arr2.reshape(2, 1)

result = arr1 + arr2_reshaped

print(result)
```

Resultado:

```text
[[11 12 13]
 [24 25 26]]
```

---

### Solución con np.newaxis

```python
arr2_newaxis = arr2[:, np.newaxis]

result = arr1 + arr2_newaxis
```

---

## Buenas prácticas con Broadcasting

- Verificar siempre las dimensiones con `.shape`.
- Utilizar `reshape()` cuando sea necesario.
- Utilizar `np.newaxis` para agregar dimensiones.
- Visualizar mentalmente cómo NumPy expandirá las matrices.

---

## Problemas de precisión numérica

Los números de punto flotante pueden producir errores pequeños pero acumulativos.

### Ejemplo

```python
import numpy as np

small_values = np.full(1000000, 0.1)

sum_value = np.sum(small_values)

print(sum_value)
```

Resultado:

```text
99999.9999999998
```

Resultado esperado:

```text
100000
```

### Recomendaciones

- Tener cuidado con cálculos críticos.
- Verificar resultados importantes.
- Investigar técnicas como:
  - Suma de Kahan.
  - Aritmética de punto fijo.
  - Bibliotecas de alta precisión.

---

# Pandas

## ¿Qué es?

Pandas proporciona estructuras de datos de alto nivel para trabajar con datos tabulares.

### Estructuras principales

#### Series

Vector unidimensional etiquetado.

#### DataFrame

Tabla bidimensional similar a:

- Excel
- SQL
- CSV

---

## Casos de uso

### Limpieza de datos

Permite:

- Completar valores faltantes.
- Convertir tipos de datos.
- Eliminar duplicados.
- Filtrar registros.

### Integración de datos

- Merge.
- Join.
- Concatenación.

### Análisis de datos

- Estadísticas descriptivas.
- Agrupaciones.
- Agregaciones.
- Series temporales.
- Pronósticos.

---

## Aspectos importantes

### 1. Indexación

Pandas dispone de dos mecanismos principales:

#### loc → etiquetas

```python
df.loc[0]
```

#### iloc → posiciones

```python
df.iloc[0]
```

### Riesgo

Confundir etiquetas con posiciones puede generar resultados incorrectos.

---

### 2. Alineación automática

Pandas alinea datos según:

- Índices.
- Nombres de columnas.

### Problema frecuente

```python
df1 + df2
```

Si las etiquetas no coinciden:

- Se generan valores NaN.
- Los cálculos pueden ser incorrectos.

---

### 3. Valores faltantes

Las técnicas de imputación pueden introducir sesgos.

Ejemplo:

Completar ingresos faltantes con la media podría ocultar diferencias entre grupos.

### Recomendación

Elegir cuidadosamente el método de imputación según el contexto.

---

### 4. Modificaciones inesperadas

Algunas operaciones pueden modificar datos originales.

### Recomendación

Crear copias cuando sea necesario:

```python
df_copy = df.copy()
```

---

# Matplotlib

## ¿Qué es?

Matplotlib es la biblioteca estándar para visualización de datos en Python.

Permite crear:

- Histogramas.
- Gráficos de barras.
- Gráficos de líneas.
- Diagramas de dispersión.
- Gráficos personalizados.

---

## Principal caso de uso: EDA

EDA = Exploratory Data Analysis (Análisis Exploratorio de Datos)

Permite:

- Identificar patrones.
- Detectar valores atípicos.
- Descubrir correlaciones.
- Comprender distribuciones.

---

## Visualizaciones profesionales

Matplotlib permite controlar:

- Colores.
- Etiquetas.
- Leyendas.
- Marcadores.
- Anotaciones.
- Diseño general.

Esto lo hace ideal para:

- Artículos científicos.
- Informes.
- Presentaciones ejecutivas.

---

## Desafíos

### Curva de aprendizaje

Su enfoque orientado a objetos puede resultar complejo para principiantes.

---

### Exceso de información

Error común:

- Incluir demasiados elementos visuales.
- Saturar el gráfico.

### Recomendación

Aplicar la regla:

> Menos es más.

---

### Compatibilidad

Pueden surgir conflictos entre versiones de bibliotecas.

### Solución

Utilizar entornos virtuales:

```bash
python -m venv venv
```

---

# Apache Superset

## ¿Qué es?

Apache Superset proporciona una capa superior para crear visualizaciones estadísticas avanzadas con menos esfuerzo.

---

## Casos de uso

### Mapas de calor (Heatmaps)

Permiten visualizar:

- Correlaciones.
- Intensidades.
- Tendencias.

---

### Gráficos de violín

Permiten comparar distribuciones entre grupos.

---

### Pair Plots

Permiten analizar relaciones entre múltiples variables simultáneamente.

---

## Ventajas

- Visualizaciones atractivas por defecto.
- Paletas de colores bien diseñadas.
- Menos configuración manual.
- Excelente para comunicar resultados a públicos técnicos y no técnicos.

---

# Comparación rápida

| Biblioteca | Función principal | Uso típico |
|------------|------------------|-------------|
| NumPy | Computación numérica | Álgebra lineal, simulaciones, procesamiento de imágenes |
| Pandas | Manipulación de datos | Limpieza, transformación y análisis |
| Matplotlib | Visualización | Gráficos personalizados y EDA |
| Apache Superset | Visualización estadística avanzada | Heatmaps, violin plots, pair plots |

---

# Conclusiones

- **NumPy** es la base de la computación numérica en Python.
- **Pandas** simplifica la limpieza y el análisis de datos.
- **Matplotlib** transforma datos en visualizaciones detalladas.
- **Apache Superset** facilita la creación de gráficos estadísticos avanzados y visualmente atractivos.
- Dominar estas bibliotecas proporciona una base sólida para cualquier proyecto de análisis de datos, ciencia de datos o computación científica.

## Idea clave

> NumPy procesa los datos, Pandas los organiza, Matplotlib los visualiza y Apache Superset los presenta de forma estadística y atractiva.