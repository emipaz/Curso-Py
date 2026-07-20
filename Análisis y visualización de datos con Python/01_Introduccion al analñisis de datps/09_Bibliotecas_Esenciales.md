# Bibliotecas Esenciales de Python para el Análisis de Datos

## Introducción

En el análisis de datos con Python, tres bibliotecas son fundamentales:

1. **NumPy** → Computación numérica eficiente.
2. **Pandas** → Manipulación y preparación de datos.
3. **Matplotlib** → Visualización de datos.

Cada una ofrece herramientas poderosas, pero también presenta desafíos y buenas prácticas que conviene conocer.

---

# NumPy

NumPy proporciona la estructura de datos **ndarray** (arreglo multidimensional), optimizada para trabajar con grandes cantidades de datos numéricos.

## Principales ventajas

- Alto rendimiento.
- Operaciones vectorizadas.
- Soporte para álgebra lineal.
- Funciones matemáticas avanzadas.
- Uso eficiente de memoria.

---

## Vectorización

La vectorización permite reemplazar bucles explícitos por operaciones sobre arreglos completos.

### Ejemplo

```python
import numpy as np

prices = np.array([100, 105, 112, 98])

percentage_change = (
    (prices[1:] - prices[:-1]) /
    prices[:-1]
) * 100

print(percentage_change)
```

### Beneficios

- Código más limpio.
- Mayor velocidad.
- Menor consumo de recursos.

---

## Broadcasting (Difusión)

Permite realizar operaciones entre arreglos con formas diferentes.

### Ejemplo simple

```python
import numpy as np

arr = np.array([1, 2, 3])

resultado = arr + 10

print(resultado)
```

Salida:

```python
[11 12 13]
```

NumPy expande automáticamente el escalar para cada elemento.

---

## Problemas comunes de Broadcasting

### 1. Formas incompatibles

```python
import numpy as np

arr1 = np.array([[1, 2, 3],
                 [4, 5, 6]])

arr2 = np.array([10, 20])

resultado = arr1 + arr2
```

Error:

```python
ValueError:
operands could not be broadcast together
```

---

### Solución con reshape()

```python
arr2 = arr2.reshape(2, 1)

resultado = arr1 + arr2
```

Resultado:

```python
[[11 12 13]
 [24 25 26]]
```

---

### Solución con np.newaxis

```python
arr2 = np.array([10, 20])

arr2_newaxis = arr2[:, np.newaxis]

resultado = arr1 + arr2_newaxis
```

---

## Buenas prácticas con Broadcasting

### Verificar dimensiones

```python
print(arr1.shape)
print(arr2.shape)
```

### Utilizar

- `reshape()`
- `np.newaxis`

para alinear correctamente los arreglos.

---

## Problemas de Precisión Numérica

Los números de punto flotante pueden generar errores pequeños pero importantes.

### Ejemplo

```python
import numpy as np

small_values = np.full(1000000, 0.1)

suma = np.sum(small_values)

print(suma)
```

Resultado:

```python
99999.9999999998
```

En lugar de:

```python
100000
```

---

### Causa

Limitaciones de representación de números flotantes en memoria.

### Recomendación

Cuando la precisión sea crítica:

- Verificar resultados.
- Usar técnicas especializadas.
- Considerar algoritmos de suma más precisos.

---

# Pandas

Pandas es la biblioteca principal para manipulación y limpieza de datos.

Sus estructuras fundamentales son:

## Series

Datos unidimensionales.

```python
import pandas as pd

s = pd.Series([10, 20, 30])
```

---

## DataFrame

Datos tabulares.

```python
import pandas as pd

df = pd.DataFrame({
    "nombre": ["Ana", "Juan"],
    "edad": [25, 30]
})
```

---

# Riesgos y Errores Comunes en Pandas

## 1. Confusión entre loc e iloc

### loc

Acceso por etiqueta.

```python
df.loc[0]
```

### iloc

Acceso por posición.

```python
df.iloc[0]
```

---

## Problema frecuente

Confundir:

```python
df[0]
```

con:

```python
df.loc[0]
```

Puede devolver resultados inesperados.

---

## 2. Alineación Automática de Datos

Pandas alinea automáticamente índices y columnas.

### Ejemplo

```python
df1 + df2
```

Si los índices no coinciden:

- Aparecen valores NaN.
- Los cálculos pueden ser incorrectos.

### Recomendación

Verificar:

```python
df1.index
df2.index
```

antes de combinar datos.

---

## 3. Valores Faltantes (Missing Values)

### Problema

Imputar valores incorrectamente puede introducir sesgos.

Ejemplo:

```python
df["income"].fillna(df["income"].mean())
```

Puede ocultar diferencias importantes entre grupos.

---

### Buenas prácticas

- Analizar por qué faltan datos.
- Elegir cuidadosamente la estrategia de imputación.
- Documentar las decisiones tomadas.

---

## 4. Modificaciones Inesperadas

Algunas operaciones modifican objetos existentes.

### Recomendación

Trabajar sobre copias.

```python
df_copy = df.copy()
```

Esto evita efectos secundarios indeseados.

---

# Matplotlib

Biblioteca estándar para visualización de datos en Python.

---

## Ventajas

- Muy flexible.
- Altamente configurable.
- Integración con NumPy y Pandas.
- Amplia variedad de gráficos.

---

## Ejemplo básico

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [5, 7, 4, 8]

plt.plot(x, y)

plt.show()
```

---

# Desafíos de Matplotlib

## Curva de Aprendizaje

Su modelo orientado a objetos puede resultar complejo al principio.

### Problemas comunes

- Demasiados elementos en un mismo gráfico.
- Visualizaciones difíciles de interpretar.

### Recomendación

Dividir información compleja en varios gráficos.

---

## Exceso de Personalización

Matplotlib permite modificar casi todo:

- Colores
- Fuentes
- Líneas
- Leyendas
- Ejes

Sin embargo:

> Más personalización no siempre significa mejor visualización.

---

### Regla importante

**Menos es más.**

Evitar:

- Demasiados colores.
- Decoraciones innecesarias.
- Saturación visual.

---

## Compatibilidad entre Bibliotecas

Pueden surgir conflictos de versiones entre:

- Pandas
- Matplotlib
- NumPy
- Otras dependencias

### Solución recomendada

Utilizar entornos virtuales:

```bash
python -m venv venv
```

o

```bash
conda create -n analisis python=3.12
```

---

# Comparación de Bibliotecas

| Biblioteca | Función Principal | Fortalezas | Riesgos Comunes |
|------------|------------------|-------------|-----------------|
| NumPy | Computación numérica | Velocidad y vectorización | Broadcasting y precisión flotante |
| Pandas | Manipulación de datos | DataFrames y limpieza de datos | Indexación, alineación e imputación |
| Matplotlib | Visualización | Gran flexibilidad | Curva de aprendizaje y exceso de personalización |

---

# Buenas Prácticas Generales

## NumPy

✅ Utilizar vectorización.

✅ Verificar dimensiones con `.shape`.

✅ Revisar resultados numéricos críticos.

---

## Pandas

✅ Diferenciar `loc` e `iloc`.

✅ Verificar alineación de índices.

✅ Trabajar con copias cuando sea necesario.

✅ Analizar cuidadosamente los valores faltantes.

---

## Matplotlib

✅ Priorizar claridad visual.

✅ Evitar gráficos sobrecargados.

✅ Mantener estilos consistentes.

---

# Conclusión

Las tres bibliotecas forman el núcleo del ecosistema de análisis de datos en Python:

- **NumPy** proporciona la base matemática y numérica.
- **Pandas** permite limpiar, transformar y analizar datos.
- **Matplotlib** convierte los datos en visualizaciones comprensibles.

Dominar estas herramientas implica no solo conocer sus funciones, sino también entender sus limitaciones, errores comunes y mejores prácticas. Con experiencia y práctica, se convierten en un conjunto de herramientas indispensable para cualquier analista o desarrollador de datos.