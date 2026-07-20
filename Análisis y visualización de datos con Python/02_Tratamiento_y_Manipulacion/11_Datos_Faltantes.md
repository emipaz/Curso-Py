# Manejo de Valores Faltantes (Missing Data) en Python

## Introducción

En el mundo real, los conjuntos de datos rara vez están completos. Es frecuente encontrar **valores faltantes** (*missing values*), que pueden surgir por diversas razones:

- Encuestas con preguntas sin responder.
- Fallos en sensores o dispositivos.
- Errores durante la captura de datos.
- Problemas en procesos de integración o almacenamiento.

Si no se gestionan adecuadamente, estos valores pueden afectar significativamente los análisis, los modelos predictivos y la toma de decisiones.

---

## ¿Por qué son un problema los valores faltantes?

Los datos faltantes pueden provocar:

- Errores inesperados en el código.
- Cálculos incorrectos de promedios, sumas y estadísticas.
- Resultados sesgados.
- Pérdida de precisión en modelos de Machine Learning.
- Predicciones poco confiables.

### Ejemplo

Si un conjunto de datos contiene edades faltantes y estas se representan con el valor `999`, los cálculos estadísticos pueden quedar completamente distorsionados si no se detecta este problema.

---

## Cómo identificar valores faltantes

### Valores faltantes evidentes

Son fáciles de detectar:

- Celdas vacías en hojas de cálculo.
- Valores `NULL`.
- Valores `NaN` en Pandas.

### Valores faltantes ocultos

Son más difíciles de identificar y pueden aparecer como:

| Valor | Posible significado |
|---------|---------|
| 999 | Dato desconocido |
| -1 | Valor no registrado |
| Otro | Categoría utilizada para ocultar faltantes |
| Desconocido | Información ausente |

### Recomendaciones

- Revisar la documentación del conjunto de datos.
- Consultar el diccionario de datos.
- Analizar valores atípicos o inconsistentes.
- Buscar patrones sospechosos.

---

## Factores a considerar antes de tratar valores faltantes

### 1. Cantidad de datos faltantes

- Pocos valores faltantes → eliminación puede ser adecuada.
- Muchos valores faltantes → eliminación puede causar pérdida importante de información.

### 2. Tipo de dato faltante

- Numérico.
- Categórico.
- Fechas.
- Texto.

### 3. Motivo de la ausencia

Es importante determinar si los datos faltan:

#### Al azar (MCAR)

Missing Completely At Random.

La ausencia no depende de ninguna variable.

#### Dependientes de otras variables (MAR)

Missing At Random.

La ausencia está relacionada con otros datos.

#### No aleatorios (MNAR)

Missing Not At Random.

Existe una razón específica por la que faltan.

### Ejemplo de sesgo

Si las personas con menores ingresos omiten responder preguntas sobre salario, eliminar esas filas puede hacer que el ingreso promedio parezca artificialmente más alto.

---

# Técnicas para tratar valores faltantes

## 1. Eliminación (Deletion)

Consiste en eliminar filas o columnas con valores faltantes.

### Ventajas

- Fácil de implementar.
- No introduce valores artificiales.

### Desventajas

- Puede perderse información valiosa.
- Puede generar sesgos.

### Ejemplo en Pandas

```python
import pandas as pd

# Eliminar filas con valores faltantes
df = df.dropna()

# Eliminar columnas con valores faltantes
df = df.dropna(axis=1)
```

---

## 2. Imputación (Imputation)

Consiste en reemplazar los valores faltantes por valores estimados.

### Ventajas

- Conserva más información.
- Reduce la pérdida de registros.

### Desventajas

- Puede introducir errores si se utiliza incorrectamente.

---

## Imputación por Media

Sustituye los valores faltantes por la media de la variable.

### Fórmula

\[
Media = \frac{\sum x_i}{n}
\]

### Ejemplo

```python
df["edad"] = df["edad"].fillna(df["edad"].mean())
```

### Uso recomendado

Cuando los datos tienen distribución aproximadamente normal.

---

## Imputación por Mediana

Sustituye los valores faltantes por la mediana.

### Ejemplo

```python
df["salario"] = df["salario"].fillna(df["salario"].median())
```

### Uso recomendado

Cuando existen valores extremos (*outliers*).

---

## Imputación por Moda

Sustituye los valores faltantes por el valor más frecuente.

### Ejemplo

```python
df["ciudad"] = df["ciudad"].fillna(df["ciudad"].mode()[0])
```

### Uso recomendado

Para variables categóricas.

---

## 3. Imputación por Regresión

Utiliza otras variables para predecir los valores faltantes.

### Idea

Si existe una relación entre variables, puede entrenarse un modelo para estimar los valores ausentes.

### Ventajas

- Mayor precisión.

### Desventajas

- Más compleja de implementar.
- Requiere mayor capacidad computacional.

---

## 4. Imputación Múltiple

Genera varios conjuntos de datos imputados con distintos valores plausibles.

### Características

- Reduce incertidumbre.
- Muy utilizada en investigación estadística.

### Ventajas

- Resultados más robustos.

### Desventajas

- Implementación compleja.

---

## 5. Crear una categoría específica

Para variables categóricas puede agregarse una categoría adicional.

### Ejemplo

```python
df["estado_civil"] = df["estado_civil"].fillna("Desconocido")
```

### Ventajas

- Mantiene toda la información.
- Fácil de interpretar.

---

## 6. Algoritmos que manejan datos faltantes

Algunos algoritmos de Machine Learning pueden trabajar directamente con valores faltantes.

### Ejemplos

- XGBoost
- LightGBM
- CatBoost

### Ventajas

- Menor necesidad de preprocesamiento.

---

## 7. Recopilar más datos

La mejor solución, cuando es posible.

### Ventajas

- Elimina incertidumbre.

### Desventajas

- Costoso.
- No siempre viable.

---

# Comparación de métodos

| Método | Ventajas | Desventajas |
|----------|----------|----------|
| Eliminación | Simple | Pérdida de información |
| Media | Fácil y rápida | Sensible a outliers |
| Mediana | Robusta frente a outliers | Puede ocultar variabilidad |
| Moda | Ideal para categorías | Puede introducir sesgo |
| Regresión | Más precisa | Más compleja |
| Imputación múltiple | Muy robusta | Costosa computacionalmente |
| Nueva categoría | Conserva información | Puede agregar ruido |
| Recopilar datos | Solución ideal | Costosa y lenta |

---

# Detección de valores faltantes con Pandas

## Contar valores faltantes por columna

```python
df.isnull().sum()
```

## Mostrar porcentaje de faltantes

```python
(df.isnull().sum() / len(df)) * 100
```

## Visualizar registros incompletos

```python
df[df.isnull().any(axis=1)]
```

---

# Flujo de trabajo recomendado

```text
Datos originales
        ↓
Identificar valores faltantes
        ↓
Analizar causa y cantidad
        ↓
Evaluar impacto
        ↓
Seleccionar técnica adecuada
        ↓
Aplicar corrección
        ↓
Validar resultados
        ↓
Datos listos para análisis
```

---

# Conclusiones

- Los valores faltantes son uno de los problemas más comunes en los datos reales.
- No existe una única solución válida para todos los casos.
- La estrategia adecuada depende de la cantidad de datos faltantes, el tipo de variable y el objetivo del análisis.
- Una mala gestión de los valores faltantes puede introducir sesgos y afectar seriamente los resultados.
- La detección y tratamiento correcto de los valores faltantes es una etapa fundamental del proceso de limpieza de datos y de cualquier proyecto de análisis o Machine Learning.


## ¿Cuál de los siguientes es un ejemplo de una forma sutil de representar los datos que faltan en un conjunto de datos? Elija la mejor respuesta.

- Aparece un mensaje de error al acceder a los datos
- Un valor nulo en una base de datos
- **Un valor como "999" para la edad**
- Una celda en blanco en una hoja de cálculo

Correcto
> Correcto Es una forma sutil de representar los datos que faltan, ya que a primera vista pueden parecer datos válidos.