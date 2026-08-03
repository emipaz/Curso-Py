# 📘 Resumen: Evaluación de Modelos en Machine Learning

## 🎯 Objetivos de aprendizaje

Al finalizar este tema podrás:

- Comprender qué es la **evaluación de modelos**.
- Entender por qué es una etapa fundamental en cualquier proyecto de Machine Learning.
- Conocer las principales **métricas de evaluación**.
- Seleccionar la métrica adecuada según el problema.
- Comprender la importancia de la evaluación continua de un modelo.

---

# ¿Qué es la evaluación de modelos?

La **evaluación de modelos (Model Evaluation)** es el proceso de medir qué tan bien un modelo de Machine Learning cumple la tarea para la que fue diseñado.

Su objetivo es responder preguntas como:

- ¿El modelo realiza predicciones correctas?
- ¿Es confiable?
- ¿Puede utilizarse en situaciones reales?
- ¿Generaliza correctamente con datos nuevos?

> **Idea clave:** Un modelo no es útil solo por haber sido entrenado; debe demostrar que funciona correctamente mediante una evaluación rigurosa.

---

# ¿Por qué es importante evaluar un modelo?

Entrenar un modelo es solo una parte del proceso.

Sin una evaluación adecuada no es posible saber si:

- las predicciones son confiables;
- el modelo comete muchos errores;
- el modelo funcionará correctamente con nuevos datos.

La evaluación permite tomar decisiones basadas en evidencia y no en suposiciones.

---

# Ejemplos del mundo real

## 💰 Detección de fraude

Los bancos utilizan modelos para detectar operaciones fraudulentas.

Un modelo mal evaluado puede provocar:

- pérdidas económicas;
- fraudes no detectados;
- bloqueo de operaciones legítimas.

Una evaluación continua permite adaptar el modelo a nuevas estrategias de fraude.

---

## 🏥 Diagnóstico médico

En medicina, la precisión del modelo puede afectar directamente la vida de los pacientes.

Un modelo poco confiable puede generar:

- diagnósticos incorrectos;
- tratamientos equivocados;
- retrasos en la atención médica.

Por ello, la evaluación rigurosa es indispensable antes de utilizar modelos de IA en entornos clínicos.

---

# Beneficios de evaluar un modelo

Una evaluación adecuada permite:

- detectar errores del modelo;
- identificar debilidades;
- mejorar los algoritmos;
- ajustar hiperparámetros;
- comparar distintos modelos;
- elegir la mejor solución;
- aumentar la confianza en las predicciones.

---

# Evaluación y Overfitting

Uno de los objetivos principales de la evaluación es detectar el **Overfitting (Sobreajuste)**.

## ¿Qué es el Overfitting?

Ocurre cuando un modelo aprende demasiado bien los datos de entrenamiento.

Como consecuencia:

- obtiene excelentes resultados durante el entrenamiento;
- falla cuando aparecen datos nuevos.

---

## ¿Cómo detectarlo?

Se evalúa el modelo utilizando datos que **no fueron utilizados durante el entrenamiento**, como:

- conjunto de validación (*Validation Set*);
- conjunto de prueba (*Test Set*).

Si el rendimiento disminuye mucho sobre estos datos, probablemente exista sobreajuste.

---

# Comparación entre modelos

Cuando existen varias alternativas, la evaluación permite compararlas objetivamente.

Por ejemplo:

- Regresión logística
- Árbol de decisión
- Random Forest
- Redes neuronales

La elección debe basarse en métricas objetivas y no en preferencias personales.

---

# Principales métricas de evaluación

La métrica adecuada depende del tipo de problema.

---

# 1. Accuracy (Precisión global o Exactitud)

Mide el porcentaje de predicciones correctas.

## Fórmula

```text
Accuracy =
Predicciones correctas
────────────────────────
Total de predicciones
```

### Ventajas

- Muy fácil de interpretar.
- Adecuada cuando las clases están equilibradas.

### Desventajas

Puede resultar engañosa cuando las clases están desbalanceadas.

### Ejemplo

Supongamos un conjunto con:

- 99 clientes honestos
- 1 cliente fraudulento

Si el modelo responde siempre:

> "No es fraude"

obtendrá:

```text
Accuracy = 99%
```

Pero:

❌ Nunca detectó el fraude.

Por eso, **Accuracy no siempre es una buena métrica**.

---

# 2. Precision (Precisión)

Responde a la pregunta:

> **De todas las predicciones positivas realizadas por el modelo, ¿cuántas eran realmente correctas?**

Su objetivo es minimizar los **Falsos Positivos (False Positives)**.

### Ejemplo

Diagnóstico médico.

Si el modelo dice que una persona está enferma, queremos que esa afirmación sea correcta la mayor cantidad de veces posible.

Una alta precisión evita:

- diagnósticos innecesarios;
- tratamientos incorrectos;
- alarmas falsas.

---

# 3. Recall (Sensibilidad o Exhaustividad)

Responde a la pregunta:

> **¿Cuántos casos positivos reales logró detectar el modelo?**

Busca minimizar los **Falsos Negativos (False Negatives)**.

### Ejemplo

En medicina:

Es preferible detectar todos los pacientes enfermos, incluso si aparecen algunos falsos positivos.

Un **Recall** alto significa que el modelo deja escapar muy pocos casos positivos.

---

# 4. F1-Score

El **F1-Score** combina:

- Precision
- Recall

en una única métrica.

Se utiliza cuando ambas son igualmente importantes.

### Características

- penaliza valores muy bajos;
- exige equilibrio entre Precision y Recall;
- es muy útil cuando las clases están desbalanceadas.

---

# 5. Matriz de Confusión (Confusion Matrix)

Es una tabla que resume todos los resultados de clasificación.

Incluye:

- ✅ Verdaderos Positivos (TP)
- ✅ Verdaderos Negativos (TN)
- ❌ Falsos Positivos (FP)
- ❌ Falsos Negativos (FN)

---

## Interpretación

| Resultado | Significado |
|-----------|-------------|
| **Verdadero Positivo (TP)** | El modelo predijo positivo y era correcto. |
| **Verdadero Negativo (TN)** | El modelo predijo negativo y era correcto. |
| **Falso Positivo (FP)** | El modelo indicó positivo cuando era negativo. |
| **Falso Negativo (FN)** | El modelo indicó negativo cuando en realidad era positivo. |

La matriz de confusión permite comprender exactamente en qué tipos de errores falla el modelo.

---

# Comparación de métricas

| Métrica | ¿Qué mide? | ¿Cuándo utilizarla? |
|----------|------------|---------------------|
| **Accuracy** | Porcentaje de aciertos | Clases equilibradas |
| **Precision** | Calidad de las predicciones positivas | Cuando los falsos positivos son costosos |
| **Recall** | Capacidad para detectar casos positivos | Cuando los falsos negativos son críticos |
| **F1-Score** | Equilibrio entre Precision y Recall | Clases desbalanceadas |
| **Confusion Matrix** | Distribución completa de errores | Para analizar detalladamente el rendimiento |

---

# ¿Qué métrica elegir?

| Problema | Métrica recomendada |
|----------|---------------------|
| Spam | Precision |
| Diagnóstico médico | Recall |
| Detección de fraude | F1-Score + Matriz de Confusión |
| Clasificación con clases equilibradas | Accuracy |
| Comparación detallada de modelos | Matriz de Confusión |

---

# La evaluación es un proceso continuo

La evaluación no termina cuando el modelo entra en producción.

Debe repetirse continuamente porque:

- aparecen nuevos datos;
- cambian los patrones;
- evolucionan los problemas;
- el modelo puede degradar su rendimiento con el tiempo.

Este proceso permite mantener modelos precisos, confiables y actualizados.

---

# Ideas clave

- La evaluación de modelos es una etapa esencial del Machine Learning.
- Permite verificar si un modelo realmente resuelve el problema para el que fue creado.
- Ayuda a detectar errores y mejorar el rendimiento.
- También permite identificar y prevenir el **Overfitting**.
- Accuracy no siempre es suficiente, especialmente con clases desbalanceadas.
- Precision y Recall analizan distintos tipos de errores.
- El **F1-Score** equilibra Precision y Recall.
- La **Matriz de Confusión** ofrece una visión completa del desempeño del modelo.
- La evaluación debe realizarse de forma continua durante todo el ciclo de vida del modelo.

---

# Esquema del proceso de evaluación

```text
Entrenar modelo
       │
       ▼
Evaluar con datos nuevos
       │
       ▼
Calcular métricas
       │
       ├── Accuracy
       ├── Precision
       ├── Recall
       ├── F1-Score
       └── Matriz de Confusión
       │
       ▼
Analizar errores
       │
       ▼
Mejorar el modelo
       │
       ▼
Volver a evaluar
```

---

# Conclusión

La **evaluación de modelos** es una etapa indispensable en cualquier proyecto de Machine Learning, ya que permite medir objetivamente el desempeño de un modelo antes de utilizarlo en aplicaciones reales. Gracias a métricas como **Accuracy**, **Precision**, **Recall**, **F1-Score** y la **Matriz de Confusión**, es posible detectar errores, comparar modelos y garantizar que las predicciones sean confiables. Una evaluación continua asegura que el modelo siga siendo útil y preciso a medida que evolucionan los datos y las necesidades del negocio.

## Pregunta

### ¿Cuál de las siguientes métricas es especialmente útil cuando se necesita equilibrar las preocupaciones tanto de falsos positivos como de falsos negativos en el rendimiento de un modelo de Aprendizaje automático? Seleccione la mejor respuesta.

- Recall
- Accuracy
- Precisión
- **Puntuación F1**

> ¡Correcto! La puntuación F1 es la media armónica de la precisión y la exhaustividad (recall), lo que la convierte en una métrica equilibrada que tiene en cuenta tanto los falsos positivos como los falsos negativos. Es una excelente opción cuando necesitas un único valor para representar el rendimiento general de tu modelo.