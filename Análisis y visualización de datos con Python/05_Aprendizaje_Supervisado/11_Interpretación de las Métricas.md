# 📘 Resumen: Interpretación de las Métricas de Evaluación en Machine Learning

## 🎯 Objetivos de aprendizaje

Al finalizar este tema podrás:

- Comprender la importancia de las métricas de evaluación en Machine Learning.
- Elegir la métrica adecuada según el problema y los objetivos del negocio.
- Interpretar correctamente las métricas de clasificación y regresión.
- Entender el impacto de los falsos positivos y falsos negativos.
- Relacionar las métricas con casos de uso reales.

---

# ¿Por qué son importantes las métricas?

Las métricas de evaluación permiten responder una pregunta fundamental:

> **¿Qué tan bueno es mi modelo?**

No solo indican el rendimiento del modelo, sino que también ayudan a:

- comparar diferentes modelos;
- detectar fortalezas y debilidades;
- tomar decisiones de negocio;
- mejorar continuamente el modelo.

Las métricas son el puente entre el **desempeño técnico** del modelo y el **valor que aporta al negocio**.

---

# Elegir la métrica correcta

No existe una métrica universalmente mejor.

La elección depende de varios factores.

## 1. Comprender el problema

Primero debemos responder:

- ¿Qué queremos predecir?
- ¿Qué problema estamos resolviendo?

Ejemplos:

- pérdida de clientes (Churn)
- detección de fraude
- recomendación de productos
- diagnóstico médico
- predicción de ventas

---

## 2. Definir los objetivos del negocio

Cada proyecto tiene indicadores clave (**KPI**) diferentes.

Ejemplos:

- retención de clientes;
- ingresos;
- reducción del fraude;
- precisión de diagnósticos;
- satisfacción del cliente.

Las métricas elegidas deben alinearse con estos objetivos.

---

## 3. Analizar los datos

Antes de elegir una métrica debemos conocer el conjunto de datos.

Preguntas importantes:

- ¿Los datos están etiquetados?
- ¿Las clases están balanceadas?
- ¿Existen valores atípicos (Outliers)?
- ¿Cuál es la variable objetivo?

Conocer los datos ayuda a seleccionar métricas más apropiadas.

---

## 4. Identificar el tipo de modelo

Las métricas dependen del algoritmo utilizado.

### Modelos de Clasificación

Utilizan métricas como:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC

---

### Modelos de Regresión

Utilizan métricas como:

- MSE
- RMSE
- MAE
- R²

---

## 5. Evaluar el costo de los errores

No todos los errores tienen el mismo impacto.

Hay que analizar:

- costo de un falso positivo;
- costo de un falso negativo.

Esta decisión determina qué métrica debe priorizarse.

---

# Métricas de Clasificación

## Accuracy (Exactitud)

### ¿Qué mide?

El porcentaje total de predicciones correctas.

### Fórmula

```text
Accuracy =
Predicciones correctas
────────────────────────
Total de predicciones
```

### Ventajas

- sencilla;
- fácil de interpretar.

### Limitación

Puede resultar engañosa en conjuntos de datos desbalanceados.

### Ejemplo

Si el 95 % de los correos son normales y el modelo clasifica todos como normales:

```text
Accuracy = 95 %
```

Aunque parece excelente, nunca detecta spam.

---

# Precision (Precisión)

## ¿Qué responde?

> De todas las predicciones positivas, ¿cuántas eran realmente correctas?

### Fórmula

```text
Precision =
TP
──────────────
TP + FP
```

### Es importante cuando...

Los falsos positivos son costosos.

### Ejemplo

Sistema de reconocimiento facial.

Un falso positivo permitiría el acceso a una persona no autorizada.

---

# Recall (Sensibilidad)

## ¿Qué responde?

> De todos los casos positivos reales, ¿cuántos detectó el modelo?

### Fórmula

```text
Recall =
TP
──────────────
TP + FN
```

### Es importante cuando...

No detectar un caso positivo es muy grave.

### Ejemplo

Detección de fraude.

No identificar una operación fraudulenta puede provocar pérdidas económicas importantes.

---

# F1 Score

Combina Precision y Recall mediante la media armónica.

### Fórmula

```text
           2 × Precision × Recall
F1 = ──────────────────────────────────
        Precision + Recall
```

### ¿Cuándo utilizarla?

Cuando:

- Precision y Recall son igualmente importantes.
- Existen clases desbalanceadas.

---

# ROC-AUC

## ¿Qué mide?

La capacidad del modelo para distinguir correctamente entre clases utilizando distintos umbrales de decisión.

### Características

- independiente del umbral;
- ideal para comparar clasificadores;
- cuanto más cercano a **1**, mejor.

---

# Métricas de Regresión

## MSE (Mean Squared Error)

Calcula el promedio de los errores al cuadrado.

### Características

- penaliza mucho los errores grandes;
- sensible a valores atípicos.

### Ideal cuando

Los errores grandes son especialmente costosos.

---

## RMSE (Root Mean Squared Error)

Es la raíz cuadrada del MSE.

### Ventajas

- mantiene las unidades originales de la variable;
- más fácil de interpretar.

### Ejemplo

Si se predicen ventas en dólares:

- MSE → dólares² (difícil de interpretar).
- RMSE → dólares (interpretación directa).

---

## MAE (Mean Absolute Error)

Calcula el promedio de los errores absolutos.

### Ventajas

- fácil de interpretar;
- robusto frente a valores atípicos.

### Desventajas

No penaliza especialmente los errores grandes.

---

# Comparación MSE vs RMSE vs MAE

| Métrica | ¿Qué mide? | Sensible a outliers | Unidades originales |
|----------|------------|--------------------|---------------------|
| **MSE** | Error cuadrático medio | ✅ Sí | ❌ No |
| **RMSE** | Raíz del MSE | ✅ Sí | ✅ Sí |
| **MAE** | Error absoluto medio | ⚠️ Poco | ✅ Sí |

---

# Interpretar las métricas según el contexto

Las métricas nunca deben analizarse de forma aislada.

Siempre deben interpretarse considerando:

- el problema;
- los datos;
- el impacto de los errores;
- los objetivos del negocio.

---

# Caso práctico 1: Predicción de abandono de clientes (Churn)

## Objetivo

Detectar clientes con riesgo de cancelar un servicio.

### Métricas prioritarias

- **Recall**, para no dejar escapar clientes en riesgo.
- **Precision**, para no gastar recursos en clientes que realmente no abandonarán.

---

# Caso práctico 2: Detección de fraude

## Objetivo

Detectar operaciones fraudulentas minimizando molestias a clientes legítimos.

### Debe buscarse

- baja tasa de falsos negativos (no dejar pasar fraudes);
- baja tasa de falsos positivos (no bloquear operaciones legítimas).

El equilibrio entre ambas es fundamental.

---

# La mejora continua del modelo

La evaluación no termina después del entrenamiento.

El proceso debe repetirse continuamente.

```text
Entrenar
      │
      ▼
Evaluar
      │
      ▼
Analizar métricas
      │
      ▼
Modificar modelo
      │
      ▼
Volver a entrenar
      │
      ▼
Mejorar resultados
```

---

# Resumen de métricas

## Clasificación

| Métrica | ¿Qué mide? | Cuándo utilizarla |
|----------|------------|------------------|
| Accuracy | Porcentaje total de aciertos | Clases balanceadas |
| Precision | Exactitud de los positivos | Falsos positivos costosos |
| Recall | Detección de positivos reales | Falsos negativos costosos |
| F1 Score | Equilibrio entre Precision y Recall | Ambas métricas son importantes |
| ROC-AUC | Capacidad de discriminación | Comparar modelos |

---

## Regresión

| Métrica | ¿Qué mide? | Cuándo utilizarla |
|----------|------------|------------------|
| MSE | Error cuadrático promedio | Penalizar errores grandes |
| RMSE | Error promedio en unidades originales | Interpretación sencilla |
| MAE | Error absoluto promedio | Datos con valores atípicos |
| R² | Calidad del ajuste del modelo | Evaluación general |

---

# Ideas clave

- Las métricas permiten medir objetivamente el rendimiento de un modelo.
- La elección de la métrica depende del problema, los datos y los objetivos del negocio.
- Accuracy no siempre es suficiente, especialmente con clases desbalanceadas.
- Precision y Recall permiten analizar distintos tipos de errores.
- F1 Score equilibra Precision y Recall.
- ROC-AUC evalúa el rendimiento del clasificador considerando distintos umbrales.
- En regresión, MSE, RMSE y MAE cuantifican el error desde diferentes perspectivas.
- Ninguna métrica es universalmente mejor; deben interpretarse siempre en contexto.
- La evaluación del modelo es un proceso continuo que permite mejorar su rendimiento con el tiempo.

---

# Conclusión

Las métricas de evaluación son mucho más que simples números: son herramientas esenciales para comprender el rendimiento real de un modelo de Machine Learning. Elegir la métrica adecuada implica considerar el tipo de problema, la naturaleza de los datos, el impacto de los errores y los objetivos del negocio. Una evaluación correcta permite desarrollar modelos más confiables, optimizar recursos y generar soluciones con verdadero valor para las organizaciones.