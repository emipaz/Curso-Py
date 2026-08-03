# 📘 Resumen: Métricas de Evaluación para Modelos de Regresión

## 🎯 Objetivos de aprendizaje

Al finalizar este tema podrás:

- Comprender qué son las **métricas de regresión**.
- Diferenciar las principales métricas utilizadas para evaluar modelos de regresión.
- Saber cuándo utilizar **MSE**, **MAE** y **R²**.
- Comprender cómo afectan los valores atípicos (*outliers*) a cada métrica.
- Evaluar correctamente un modelo de regresión utilizando Scikit-Learn.

---

# ¿Qué es un modelo de regresión?

Los **modelos de regresión** son algoritmos de Machine Learning que permiten **predecir valores numéricos continuos**.

A diferencia de los modelos de clasificación (que predicen categorías), un modelo de regresión responde preguntas como:

- ¿Cuál será el precio de una casa?
- ¿Cuántas ventas habrá el próximo mes?
- ¿Cuál será la temperatura mañana?
- ¿Cuánto consumirá un cliente?

En otras palabras:

```text
Entrada (X) ─────────► Modelo ─────────► Valor numérico (y)
```

---

# ¿Por qué necesitamos métricas de regresión?

Una vez entrenado un modelo debemos responder una pregunta muy importante:

> **¿Qué tan buenas son sus predicciones?**

Para ello utilizamos **métricas de evaluación**, que comparan:

- el valor real;
- el valor predicho.

Mientras menor sea la diferencia entre ambos, mejor será el modelo.

---

# Principales métricas de regresión

Las tres métricas más utilizadas son:

- 📏 MSE (Mean Squared Error)
- 📏 MAE (Mean Absolute Error)
- 📊 R² (Coeficiente de Determinación)

Cada una mide el error desde una perspectiva diferente.

---

# 1. Mean Squared Error (MSE)

## ¿Qué es?

El **Error Cuadrático Medio (MSE)** calcula el promedio de los errores elevados al cuadrado.

## Fórmula

```text
               Σ (yreal − ypred)^2
MSE =  ------------------------------
                Número de datos
```

---

## ¿Por qué se elevan al cuadrado?

Elevar los errores al cuadrado tiene dos efectos:

- elimina los signos negativos;
- penaliza mucho más los errores grandes.

Por ejemplo:

| Error | Error² |
|--------|--------|
| 1 | 1 |
| 2 | 4 |
| 5 | 25 |
| 10 | 100 |

Un error de **10** pesa **100 veces** más que uno de **1**.

---

## Ventajas

- Muy utilizado en Machine Learning.
- Penaliza fuertemente errores grandes.
- Ideal cuando los errores grandes son muy costosos.

---

## Desventajas

Es muy sensible a los **valores atípicos (Outliers)**.

Un único dato muy alejado puede aumentar considerablemente el MSE.

---

## Ejemplo

Supongamos que queremos predecir el precio de viviendas.

Valores reales:

```text
100
120
130
500
```

Predicciones:

```text
98
121
129
350
```

El último error es enorme.

Como el MSE eleva al cuadrado los errores, ese único caso influirá mucho más que los demás.

---

## ¿Cuándo utilizar MSE?

Es recomendable cuando:

- los errores grandes son muy graves;
- queremos penalizarlos fuertemente.

Ejemplos:

- Predicción financiera.
- Riesgo bancario.
- Predicción de demanda energética.

---

## Ejemplo en Scikit-Learn

```python
from sklearn.metrics import mean_squared_error

y_real = [10, 20, 30, 40]
y_pred = [12, 18, 29, 43]

mse = mean_squared_error(y_real, y_pred)

print(mse)
```

---

# 2. Mean Absolute Error (MAE)

## ¿Qué es?

El **Error Absoluto Medio (MAE)** calcula el promedio del valor absoluto de los errores.

## Fórmula

```text
              Σ |yreal − ypred|
MAE = ----------------------------
             Número de datos
```

---

## ¿Qué significa?

Cada error tiene exactamente el mismo peso.

No importa si el error fue:

- 2
- 5
- 10

Todos se consideran de forma proporcional.

---

## Ventajas

- Muy fácil de interpretar.
- Robusto frente a valores atípicos.
- No exagera los errores grandes.

---

## Desventajas

No penaliza especialmente los errores muy grandes.

---

## Ejemplo

Predicción de ventas de café.

Habitualmente se venden:

```text
100 cafés
```

Durante un recital se venden:

```text
300 cafés
```

Ese día es completamente excepcional.

Con MAE ese error no afectará exageradamente la evaluación del modelo.

---

## ¿Cuándo utilizar MAE?

Cuando existen:

- valores atípicos;
- datos muy variables;
- eventos excepcionales.

Ejemplos:

- Ventas.
- Consumo.
- Demanda.
- Tráfico.

---

## Ejemplo en Scikit-Learn

```python
from sklearn.metrics import mean_absolute_error

mae = mean_absolute_error(y_real, y_pred)

print(mae)
```

---

# Comparación entre MSE y MAE

Supongamos estos errores.

| Error | MAE | MSE |
|--------|----|----|
| 2 | 2 | 4 |
| 5 | 5 | 25 |
| 10 | 10 | 100 |

Podemos observar que:

- **MAE** mantiene la escala original.
- **MSE** castiga mucho más los errores grandes.

---

# 3. Coeficiente de Determinación (R²)

También conocido como:

- R-Squared
- R²
- Coeficiente de Determinación

---

## ¿Qué mide?

No mide el error.

Mide **qué porcentaje de la variabilidad de los datos es explicado por el modelo**.

Su valor normalmente está entre:

```text
0 y 1
```

---

## Interpretación

| R² | Interpretación |
|----|----------------|
| 1.0 | Modelo perfecto |
| 0.9 | Excelente |
| 0.8 | Muy bueno |
| 0.6 | Aceptable |
| 0 | No explica la variabilidad |

---

## Ejemplo

Queremos predecir el precio de viviendas usando únicamente su superficie.

Si obtenemos:

```text
R² = 0.80
```

Significa que:

> El **80 %** de la variación del precio puede explicarse mediante el tamaño de la vivienda.

El 20 % restante depende de otras variables, por ejemplo:

- ubicación;
- antigüedad;
- cantidad de habitaciones;
- estado de conservación.

---

## Ventajas

- Muy fácil de interpretar.
- Permite comparar distintos modelos.
- Resume el rendimiento general.

---

## Limitaciones

Un **R² alto no garantiza un buen modelo**.

Puede existir:

- sobreajuste (*Overfitting*);
- mala generalización.

Por eso siempre debe analizarse junto con otras métricas.

---

## Ejemplo en Scikit-Learn

```python
from sklearn.metrics import r2_score

r2 = r2_score(y_real, y_pred)

print(r2)
```

---

# Overfitting y Underfitting

## Overfitting (Sobreajuste)

El modelo aprende demasiado bien los datos de entrenamiento.

```text
Entrenamiento  → Excelente

Datos nuevos   → Malo
```

Puede presentar un **R² muy alto**, pero fallar con datos nunca vistos.

---

## Underfitting (Subajuste)

El modelo es demasiado simple.

No logra capturar los patrones de los datos.

Generalmente produce:

- errores altos;
- R² bajo.

---

# ¿Qué métrica elegir?

| Situación | Métrica recomendada |
|-----------|--------------------|
| Penalizar errores grandes | MSE |
| Existen muchos Outliers | MAE |
| Comparar modelos rápidamente | R² |
| Evaluación completa | MSE + MAE + R² |

---

# Comparación general

| Métrica | ¿Qué mide? | Sensible a Outliers | Valor ideal |
|----------|------------|---------------------|-------------|
| **MSE** | Error cuadrático medio | ✅ Sí | Bajo |
| **MAE** | Error absoluto medio | ❌ Poco | Bajo |
| **R²** | Variabilidad explicada | No aplica | Cercano a 1 |

---

# Ejemplo completo con Scikit-Learn

```python
from sklearn.metrics import (
    mean_squared_error,
    mean_absolute_error,
    r2_score
)

y_real = [100, 120, 130, 150]
y_pred = [98, 118, 135, 148]

print("MSE :", mean_squared_error(y_real, y_pred))
print("MAE :", mean_absolute_error(y_real, y_pred))
print("R²  :", r2_score(y_real, y_pred))
```

Salida aproximada:

```text
MSE : 4.25
MAE : 1.75
R²  : 0.98
```

Interpretación:

- **MSE = 4.25** → Los errores cuadráticos son muy bajos.
- **MAE = 1.75** → En promedio, el modelo se equivoca solo 1.75 unidades.
- **R² = 0.98** → El modelo explica el 98 % de la variabilidad de los datos.

---

# Casos de uso

## 🏠 Precio de viviendas

Predecir el valor de una casa según:

- superficie;
- barrio;
- antigüedad;
- habitaciones.

---

## 📈 Predicción bursátil

Estimar:

- precios de acciones;
- índices financieros;
- criptomonedas.

En este contexto suele utilizarse **MSE**, ya que los errores grandes pueden implicar pérdidas importantes.

---

## ☕ Predicción de demanda

Una cafetería desea estimar cuántos cafés venderá cada día.

Aquí suele preferirse **MAE**, porque eventos excepcionales (feriados, recitales, tormentas) no deberían distorsionar excesivamente la evaluación.

---

## ⚡ Consumo energético

Predecir el consumo eléctrico de una ciudad para optimizar la generación de energía.

Se utilizan conjuntamente **MSE**, **MAE** y **R²**.

---

# Ideas clave

- Los modelos de regresión predicen **valores numéricos continuos**.
- Las métricas de regresión permiten medir la calidad de esas predicciones.
- **MSE** penaliza fuertemente los errores grandes.
- **MAE** trata todos los errores por igual y es más robusto frente a valores atípicos.
- **R²** indica qué proporción de la variabilidad de los datos explica el modelo.
- Ninguna métrica es suficiente por sí sola; es recomendable analizarlas en conjunto.
- La elección de la métrica depende del problema de negocio y del impacto que tienen los errores.

---

# Resumen visual

```text
                  Modelo de Regresión
                          │
                          ▼
                 Predicciones Numéricas
                          │
        ┌─────────────────┼─────────────────┐
        ▼                 ▼                 ▼
      MSE               MAE                R²
 Penaliza           Error medio       Variabilidad
 grandes errores     absoluto          explicada
        │                 │                 │
        ▼                 ▼                 ▼
  Sensible a         Robusto frente    Cercano a 1
   Outliers            a Outliers      es mejor
```

---

# Conclusión

Las **métricas de regresión** son fundamentales para evaluar la calidad de un modelo que predice valores numéricos. El **MSE** es ideal cuando los errores grandes deben penalizarse con fuerza, el **MAE** ofrece una medida más robusta frente a valores atípicos y el **R²** proporciona una visión global de qué tan bien el modelo explica la variabilidad de los datos. En la práctica, lo más recomendable es utilizar **las tres métricas de forma complementaria**, obteniendo así una evaluación más completa y confiable del rendimiento del modelo.