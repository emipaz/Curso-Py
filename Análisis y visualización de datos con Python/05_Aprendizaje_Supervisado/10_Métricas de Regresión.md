# 📘 Resumen: Métricas de Regresión en Machine Learning (MSE, MAE y R²)

## 🎯 Objetivos de aprendizaje

Al finalizar este tema podrás:

- Comprender qué son las **métricas de regresión**.
- Calcular e interpretar las métricas **MSE**, **MAE** y **R² (R-Squared)**.
- Conocer las ventajas y limitaciones de cada una.
- Elegir la métrica más adecuada según el problema y los datos.

---

# ¿Qué es un problema de regresión?

En **Machine Learning**, la **regresión** se utiliza para **predecir valores numéricos continuos**, a diferencia de la clasificación, que predice categorías.

## Ejemplos de regresión

- 🏠 Precio de una vivienda.
- 🌡️ Temperatura de mañana.
- 🚗 Precio de un automóvil usado.
- 📈 Ventas del próximo mes.
- 🌳 Edad de un árbol.

En estos problemas necesitamos medir **qué tan cerca están las predicciones del valor real**, para lo cual utilizamos **métricas de regresión**.

---

# ¿Por qué necesitamos métricas?

Supongamos que un modelo predice el precio de una casa.

| Casa | Precio real | Predicción |
|------|------------:|-----------:|
| A | \$200.000 | \$198.000 |
| B | \$350.000 | \$360.000 |
| C | \$500.000 | \$450.000 |

Aunque el modelo realiza predicciones, necesitamos una forma objetiva de responder preguntas como:

- ¿Qué tan preciso es?
- ¿Comete errores grandes?
- ¿Es mejor que otro modelo?

Las métricas permiten responder estas preguntas.

---

# Error Cuadrático Medio (MSE)

## ¿Qué es?

El **Mean Squared Error (MSE)** mide el **promedio de los errores al cuadrado** entre los valores predichos y los reales.

### Fórmula

```text
          Σ (Valor real − Predicción)²
MSE = ─────────────────────────────────────
          Número de observaciones
```

---

## ¿Por qué se elevan los errores al cuadrado?

Elevar los errores al cuadrado tiene dos objetivos:

- Todos los errores se vuelven positivos.
- Los errores grandes reciben una penalización mucho mayor que los pequeños.

---

## Ejemplo

Supongamos:

| Valor real | Predicción | Error | Error² |
|------------:|-----------:|------:|--------:|
| 12 | 10 | 2 | 4 |
| 20 | 18 | 2 | 4 |
| 15 | 16 | -1 | 1 |

```text
MSE = (4 + 4 + 1) / 3 = 3
```

---

## Ventajas

- Muy utilizado en regresión.
- Penaliza fuertemente los errores grandes.
- Ideal cuando los grandes errores son costosos.

---

## Desventajas

Es muy sensible a los **valores atípicos (Outliers)**.

Un único error muy grande puede aumentar considerablemente el MSE.

---

# Valores Atípicos (Outliers)

Un **valor atípico** es un dato que se aleja significativamente del resto.

Ejemplo:

Edad de árboles:

```text
10
12
11
13
150   ← valor atípico
```

Si el modelo falla al predecir ese árbol de 150 años, el MSE crecerá mucho debido al error elevado al cuadrado.

---

# Error Absoluto Medio (MAE)

## ¿Qué es?

El **Mean Absolute Error (MAE)** calcula el promedio de los errores absolutos.

No eleva los errores al cuadrado.

### Fórmula

```text
          Σ |Valor real − Predicción|
MAE = ───────────────────────────────────
          Número de observaciones
```

---

## Ejemplo

| Valor real | Predicción | Error absoluto |
|------------:|-----------:|---------------:|
| 12 | 10 | 2 |
| 20 | 18 | 2 |
| 15 | 16 | 1 |

```text
MAE = (2 + 2 + 1) / 3 = 1,67
```

---

## Ventajas

- Fácil de interpretar.
- Menos sensible a valores atípicos.
- Todos los errores tienen el mismo peso.

---

## Desventajas

No penaliza especialmente los errores grandes.

Por ello, un error muy importante puede pasar relativamente desapercibido.

---

# MSE vs MAE

| Característica | MSE | MAE |
|---------------|-----|-----|
| Eleva errores al cuadrado | ✅ Sí | ❌ No |
| Penaliza errores grandes | ✅ Mucho | ⚠️ Poco |
| Sensible a valores atípicos | ✅ Sí | ❌ Mucho menos |
| Fácil de interpretar | ⚠️ Menos | ✅ Sí |

---

# ¿Cuándo usar MSE?

Conviene utilizar **MSE** cuando:

- los errores grandes son especialmente costosos;
- se desea que el modelo evite predicciones muy alejadas del valor real;
- no existen muchos valores atípicos.

### Ejemplos

- Predicción del consumo eléctrico.
- Estimación de demanda.
- Control industrial.

---

# ¿Cuándo usar MAE?

Es recomendable cuando:

- existen muchos valores atípicos;
- todos los errores tienen una importancia similar;
- se busca una interpretación sencilla del error promedio.

### Ejemplos

- Precio de viviendas con propiedades extremadamente caras.
- Datos financieros con valores extremos.
- Datos experimentales con mediciones atípicas.

---

# Coeficiente de Determinación (R²)

## ¿Qué es?

El **R² (R-Squared o Coeficiente de Determinación)** mide qué proporción de la variabilidad de los datos puede explicar el modelo.

No mide directamente el error, sino la **calidad del ajuste**.

---

## Interpretación

| Valor de R² | Interpretación |
|-------------|----------------|
| **1** | Ajuste perfecto. |
| **0,8** | El modelo explica el 80 % de la variación de los datos. |
| **0** | El modelo no explica la variabilidad de los datos. |

Cuanto más cercano a **1**, mejor se ajusta el modelo.

---

## Analogía

Imagina una nube de puntos y una línea de regresión.

- Si todos los puntos caen exactamente sobre la línea → **R² = 1**.
- Si la línea apenas representa la tendencia de los datos → **R² cercano a 0**.

---

# Limitaciones de R²

Aunque es una métrica muy útil, tiene algunas limitaciones.

Un modelo con más variables suele obtener un **R² mayor**, aunque esas variables no aporten información relevante.

Esto puede conducir al **sobreajuste (Overfitting)**.

---

# Sobreajuste (Overfitting)

El **Overfitting** ocurre cuando un modelo aprende demasiado los datos de entrenamiento, incluyendo el ruido.

Como consecuencia:

- obtiene excelentes resultados con los datos conocidos;
- falla al predecir datos nuevos.

Por ello, un R² muy alto no siempre implica que el modelo sea mejor.

---

# ¿Qué métrica elegir?

Depende del objetivo del proyecto.

| Situación | Métrica recomendada | Motivo |
|-----------|---------------------|--------|
| Penalizar fuertemente errores grandes | **MSE** | Los errores grandes reciben mayor castigo. |
| Datos con muchos valores atípicos | **MAE** | Es más robusto frente a outliers. |
| Medir la calidad general del ajuste | **R²** | Indica cuánta variabilidad explica el modelo. |

---

# Comparación de las métricas

| Métrica | ¿Qué mide? | Valor ideal | Sensible a outliers |
|----------|------------|-------------|---------------------|
| **MSE** | Error cuadrático promedio | Lo más cercano posible a **0** | ✅ Sí |
| **MAE** | Error absoluto promedio | Lo más cercano posible a **0** | ⚠️ Mucho menos |
| **R²** | Calidad del ajuste | Lo más cercano posible a **1** | ❌ No directamente |

---

# Flujo de evaluación de un modelo de regresión

```text
Datos
   │
   ▼
Entrenamiento del modelo
   │
   ▼
Predicciones
   │
   ▼
Comparación con valores reales
   │
   ▼
Cálculo de métricas
   │
   ├── MSE
   ├── MAE
   └── R²
   │
   ▼
Evaluación del modelo
   │
   ▼
Selección del mejor modelo
```

---

# Ideas clave

- La **regresión** predice valores numéricos continuos.
- **MSE** calcula el promedio de los errores al cuadrado y penaliza fuertemente los errores grandes.
- **MAE** calcula el promedio de los errores absolutos y es más robusto frente a valores atípicos.
- **R²** indica qué proporción de la variabilidad de los datos explica el modelo.
- Ninguna métrica es universalmente mejor: la elección depende del problema y de las características de los datos.
- Es recomendable evaluar un modelo utilizando **más de una métrica**, ya que cada una ofrece una perspectiva diferente de su rendimiento.

---

# Conclusión

Las métricas de regresión son fundamentales para evaluar modelos predictivos. El **MSE** ayuda a identificar modelos que minimizan los errores grandes, el **MAE** proporciona una medida más robusta frente a valores extremos y el **R²** permite conocer qué tan bien se ajusta el modelo a los datos. Utilizar estas métricas de forma conjunta facilita comparar modelos, detectar problemas como el sobreajuste y seleccionar la mejor solución para cada tarea de predicción.