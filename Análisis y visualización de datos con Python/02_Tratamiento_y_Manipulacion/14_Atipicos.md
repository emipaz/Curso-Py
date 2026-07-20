# Detección y Tratamiento de Valores Atípicos (Outliers) en Python

## Objetivos de aprendizaje

Al finalizar esta sección serás capaz de:

- Definir qué son los valores atípicos (*outliers*).
- Comprender cómo afectan el análisis de datos.
- Detectar valores atípicos mediante métodos estadísticos.
- Utilizar técnicas como Z-Score e IQR.
- Visualizar outliers con gráficos.
- Aplicar estrategias de tratamiento como recorte, winsorización e imputación.
- Seleccionar la mejor estrategia según el contexto del análisis.

---

# ¿Qué son los valores atípicos?

Los **valores atípicos** (*outliers*) son observaciones que se alejan significativamente del comportamiento general de los datos.

Representan valores extremadamente altos o bajos respecto al resto del conjunto de datos.

## Ejemplo

| Cliente | Salario |
|----------|----------|
| 1 | 50.000 |
| 2 | 55.000 |
| 3 | 60.000 |
| 4 | 58.000 |
| 5 | 5.000.000 |

El salario de **5.000.000** es un valor atípico.

---

# ¿Por qué aparecen los outliers?

## 1. Errores de medición

Problemas durante la captura de datos.

### Ejemplo

```text
Temperatura real: 25°C
Temperatura registrada: 250°C
```

---

## 2. Errores de carga

Errores humanos al ingresar información.

### Ejemplo

```text
Edad correcta: 35
Edad ingresada: 350
```

---

## 3. Eventos reales

Algunos outliers representan situaciones legítimas.

### Ejemplo

```text
Ingresos de una celebridad
```

o

```text
Ganancias extraordinarias de una empresa
```

---

# ¿Por qué son importantes?

Los outliers pueden:

- Distorsionar promedios.
- Alterar desviaciones estándar.
- Sesgar análisis estadísticos.
- Impactar modelos de Machine Learning.
- Dificultar la visualización de datos.

---

## Ejemplo

### Datos originales

```text
10, 12, 11, 13, 14
```

Media:

\[
12
\]

### Con un outlier

```text
10, 12, 11, 13, 100
```

Media:

\[
29.2
\]

La media deja de representar adecuadamente los datos.

---

# Dataset de ejemplo

```python
import pandas as pd

df = pd.DataFrame({
    "salario": [
        50000,
        52000,
        54000,
        56000,
        58000,
        60000,
        5000000
    ]
})

df
```

---

# Detección visual de outliers

## Histograma

```python
df["salario"].hist()
```

---

## Boxplot

```python
import matplotlib.pyplot as plt

df.boxplot(column="salario")
plt.show()
```

### Interpretación

Un boxplot muestra:

- Mínimo
- Primer cuartil (Q1)
- Mediana
- Tercer cuartil (Q3)
- Máximo
- Valores atípicos

Los outliers aparecen como puntos fuera de los "bigotes".

---

# Método 1: Z-Score

## Concepto

El Z-Score mide cuántas desviaciones estándar se encuentra un dato respecto de la media.

### Fórmula

\[
Z = \frac{x - \mu}{\sigma}
\]

Donde:

- \(x\) = valor observado
- \(\mu\) = media
- \(\sigma\) = desviación estándar

---

## Regla general

Un dato suele considerarse outlier cuando:

```text
|Z| > 3
```

---

## Ejemplo en Python

```python
from scipy.stats import zscore

df["z_score"] = zscore(df["salario"])

df
```

---

## Filtrar outliers

```python
outliers = df[abs(df["z_score"]) > 3]

outliers
```

---

## Ventajas

✅ Fácil de calcular.

✅ Funciona bien con distribuciones normales.

## Desventajas

❌ Sensible a los propios outliers.

❌ Menos efectivo en distribuciones asimétricas.

---

# Método 2: IQR (Rango Intercuartílico)

## Concepto

El IQR mide la dispersión del 50% central de los datos.

### Fórmula

\[
IQR = Q3 - Q1
\]

Donde:

- Q1 = Primer cuartil
- Q3 = Tercer cuartil

---

## Límites para detectar outliers

### Límite inferior

\[
Q1 - 1.5 \times IQR
\]

### Límite superior

\[
Q3 + 1.5 \times IQR
\]

Todo valor fuera de esos límites se considera atípico.

---

## Ejemplo en Python

```python
Q1 = df["salario"].quantile(0.25)
Q3 = df["salario"].quantile(0.75)

IQR = Q3 - Q1

limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR
```

---

## Detectar outliers

```python
outliers = df[
    (df["salario"] < limite_inferior) |
    (df["salario"] > limite_superior)
]

outliers
```

---

## Ventajas

✅ Robusto frente a valores extremos.

✅ Funciona bien en datos no normales.

## Desventajas

❌ Puede detectar demasiados outliers en distribuciones muy sesgadas.

---

# Comparación Z-Score vs IQR

| Característica | Z-Score | IQR |
|---------------|---------|---------|
| Basado en media | Sí | No |
| Basado en cuartiles | No | Sí |
| Sensible a outliers | Sí | No |
| Datos normales | Excelente | Bueno |
| Datos asimétricos | Regular | Excelente |

---

# Tratamiento de valores atípicos

Detectar outliers es sencillo.

La decisión difícil es qué hacer con ellos.

---

# Estrategia 1: Eliminación (Trimming)

Consiste en eliminar los registros atípicos.

## Ejemplo

```python
df_sin_outliers = df[
    (df["salario"] >= limite_inferior) &
    (df["salario"] <= limite_superior)
]
```

### Ventajas

✅ Fácil.

✅ Elimina ruido.

### Desventajas

❌ Puede eliminar información valiosa.

---

# Estrategia 2: Winsorización

Sustituye los valores extremos por límites definidos.

## Ejemplo

```python
from scipy.stats.mstats import winsorize

df["salario_w"] = winsorize(
    df["salario"],
    limits=[0.05, 0.05]
)
```

### Antes

```text
5000000
```

### Después

```text
60000
```

(aproximadamente)

### Ventajas

✅ Conserva registros.

✅ Reduce impacto de outliers.

### Desventajas

❌ Modifica los datos originales.

---

# Estrategia 3: Imputación

Reemplazar el outlier por:

- Media.
- Mediana.
- Valor calculado.

## Ejemplo

```python
mediana = df["salario"].median()

df.loc[
    df["salario"] > limite_superior,
    "salario"
] = mediana
```

### Ventajas

✅ Mantiene tamaño del dataset.

### Desventajas

❌ Puede introducir sesgo.

---

# Estrategia 4: Mantener el valor

En algunos casos el outlier es información válida.

### Ejemplo

```text
Salario de un CEO
```

o

```text
Ganancias excepcionales
```

Eliminarlo podría ser incorrecto.

---

# Análisis de sensibilidad

Una buena práctica consiste en ejecutar el análisis:

1. Con outliers.
2. Sin outliers.

Comparar resultados.

## Ejemplo

```python
media_original = df["salario"].mean()

media_limpia = df_sin_outliers["salario"].mean()

print(media_original)
print(media_limpia)
```

---

# Flujo recomendado

```text
Datos originales
        ↓
Visualización
        ↓
Detección de outliers
(Z-Score o IQR)
        ↓
Análisis de contexto
        ↓
Evaluar impacto
        ↓
Seleccionar estrategia
        ↓
Validar resultados
        ↓
Continuar análisis
```

---

# Buenas prácticas

✅ Investigar la causa del outlier antes de eliminarlo.

✅ Consultar expertos del negocio.

✅ Comparar resultados con y sin outliers.

✅ Documentar las decisiones tomadas.

✅ Utilizar IQR cuando los datos no sean normales.

✅ Utilizar Z-Score cuando la distribución sea aproximadamente normal.

❌ No eliminar automáticamente todos los valores extremos.

---

# Ejercicio práctico

Utilizando el dataset de salarios:

1. Calcular media y mediana.
2. Crear un boxplot.
3. Detectar outliers usando IQR.
4. Detectar outliers usando Z-Score.
5. Eliminar outliers.
6. Comparar estadísticas antes y después.
7. Aplicar winsorización.
8. Comparar resultados.

---

# Conclusiones

- Los outliers son observaciones que se alejan significativamente del resto de los datos.
- Pueden deberse a errores o representar fenómenos reales.
- Los métodos más utilizados para detectarlos son **Z-Score** e **IQR**.
- No siempre deben eliminarse.
- La decisión correcta depende del contexto del negocio y del objetivo del análisis.
- Un tratamiento adecuado de los outliers mejora la calidad y confiabilidad del análisis de datos.

## ¿Cuál de las siguientes opciones describe mejor el impacto de los valores atípicos en el Análisis de datos? Seleccione la mejor respuesta.

- Los valores atípicos siempre representan errores en la recogida de datos y deben eliminarse.
- Los valores atípicos no influyen en el análisis de datos y pueden ignorarse sin problemas.
- Los valores atípicos siempre son beneficiosos y deben incluirse en todos los análisis.
- **Los valores atípicos pueden sesgar las mediciones estadísticas y llevar a conclusiones erróneas.**

Correcto
> Correcto. Los valores atípicos pueden influir significativamente en medidas como la media y la desviación típica, distorsionando potencialmente los resultados de su análisis.