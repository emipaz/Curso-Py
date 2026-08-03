# 📘 Resumen: La Matriz de Confusión y las Métricas de Evaluación en Machine Learning

## 🎯 Objetivos de aprendizaje

Al finalizar este tema podrás:

- Comprender qué es una **Matriz de Confusión (Confusion Matrix)**.
- Interpretar los cuatro resultados posibles de un modelo de clasificación.
- Conocer las principales métricas derivadas de la matriz de confusión.
- Elegir la métrica adecuada según el problema de negocio.
- Comprender las limitaciones de la matriz de confusión.

---

# ¿Qué es una Matriz de Confusión?

La **Matriz de Confusión** es una herramienta utilizada para evaluar el rendimiento de un **modelo de clasificación**.

Compara:

- las **clases reales** (la verdad);
- las **clases predichas** por el modelo.

Su objetivo es mostrar **qué tipos de errores comete el modelo**, no solo cuántos aciertos obtiene.

> **Idea clave:** La matriz de confusión proporciona una visión mucho más completa que una simple medida de Accuracy.

---

# ¿Cómo está formada?

Para un problema de clasificación binaria, la matriz tiene **4 cuadrantes**.

| | Predicción Positiva | Predicción Negativa |
|----------------|------------------|------------------|
| **Real Positivo** | ✅ Verdadero Positivo (TP) | ❌ Falso Negativo (FN) |
| **Real Negativo** | ❌ Falso Positivo (FP) | ✅ Verdadero Negativo (TN) |

---

# Los cuatro resultados posibles

## ✅ Verdadero Positivo (True Positive - TP)

El modelo predice correctamente un caso positivo.

### Ejemplo

Un cliente iba a realizar una compra.

El modelo predijo que compraría.

✅ La predicción fue correcta.

---

## ✅ Verdadero Negativo (True Negative - TN)

El modelo predice correctamente un caso negativo.

### Ejemplo

El cliente no iba a comprar.

El modelo también predijo que no compraría.

✅ Predicción correcta.

---

## ❌ Falso Positivo (False Positive - FP)

También llamado:

**Error de Tipo I**

El modelo predice un caso positivo cuando en realidad era negativo.

### Ejemplo

El modelo cree que un cliente comprará.

Finalmente:

❌ El cliente no compra.

### Consecuencia

La empresa puede gastar recursos innecesarios.

---

## ❌ Falso Negativo (False Negative - FN)

También llamado:

**Error de Tipo II**

El modelo predice un caso negativo cuando en realidad era positivo.

### Ejemplo

El modelo predice que un cliente no comprará.

Finalmente:

❌ El cliente sí compra.

### Consecuencia

La empresa pierde una oportunidad de venta.

---

# Resumen visual

```text
                 Predicción

               Sí         No
            ---------------------
Real Sí |    TP      |    FN    |
            ---------------------
Real No |    FP      |    TN    |
            ---------------------
```

---

# Métricas derivadas de la Matriz de Confusión

A partir de estos cuatro valores se calculan distintas métricas.

---

# 1. Accuracy (Exactitud)

Mide el porcentaje total de predicciones correctas.

## Fórmula

```text
Accuracy =
(TP + TN)
──────────────
Total
```

### Ventajas

- Fácil de entender.
- Útil cuando las clases están equilibradas.

### Limitaciones

Puede resultar engañosa cuando existen clases desbalanceadas.

---

# Ejemplo

Supongamos:

- 990 clientes NO compran.
- 10 clientes SÍ compran.

Un modelo responde:

> "Nadie comprará"

Obtiene:

```text
Accuracy = 99%
```

Pero:

❌ Nunca detectó compradores reales.

---

# 2. Precision (Precisión)

Responde:

> **Cuando el modelo predice un resultado positivo, ¿con qué frecuencia tiene razón?**

## Fórmula

```text
Precision =
TP
──────────
TP + FP
```

Busca minimizar los:

- Falsos Positivos.

---

## Ejemplo

Marketing.

Si una campaña cuesta mucho dinero, interesa contactar únicamente a clientes con alta probabilidad de compra.

Una alta Precision evita gastar recursos innecesarios.

---

# 3. Recall (Sensibilidad)

También llamado:

- Recall
- Sensibilidad
- Tasa de verdaderos positivos

Responde:

> **¿Cuántos casos positivos reales logró detectar el modelo?**

## Fórmula

```text
Recall =
TP
──────────
TP + FN
```

Busca minimizar los:

- Falsos Negativos.

---

## Ejemplo

Diagnóstico médico.

Es preferible detectar todos los pacientes enfermos aunque aparezcan algunos falsos positivos.

---

# 4. F1-Score

El **F1-Score** combina Precision y Recall en una única métrica.

Su principal característica es que:

- penaliza valores bajos;
- requiere equilibrio entre ambas métricas.

Es especialmente útil cuando:

- existen clases desbalanceadas;
- tanto FP como FN son importantes.

---

# ¿Qué mide cada métrica?

| Métrica | Prioridad |
|----------|-----------|
| Accuracy | Cantidad total de aciertos |
| Precision | Reducir Falsos Positivos |
| Recall | Reducir Falsos Negativos |
| F1-Score | Equilibrio entre Precision y Recall |

---

# ¿Qué métrica utilizar?

## 📧 Detección de Spam

Objetivo:

No enviar correos importantes a la carpeta Spam.

### Métrica prioritaria

✅ **Precision**

Es preferible recibir algunos correos basura antes que perder un correo importante.

---

## 🏥 Diagnóstico Médico

Objetivo:

Detectar la mayor cantidad posible de pacientes enfermos.

### Métrica prioritaria

✅ **Recall**

Es mucho más grave no detectar una enfermedad que realizar pruebas adicionales.

---

## 💳 Detección de Fraude

Objetivo:

- detectar fraudes;
- evitar bloquear operaciones legítimas.

Aquí se necesita equilibrio entre:

- Precision;
- Recall.

La métrica recomendada suele ser:

✅ **F1-Score**

---

## 📈 Predicción de abandono de clientes (Churn)

Las empresas utilizan la matriz de confusión para identificar clientes con riesgo de abandonar.

Una buena evaluación permite:

- focalizar campañas de retención;
- reducir pérdidas;
- optimizar recursos.

---

## 👁️ Visión por Computadora

La matriz de confusión ayuda a descubrir qué clases confunde el modelo.

Ejemplo:

- perro ↔ gato

Si aparecen muchas confusiones, puede ser necesario:

- más datos;
- nuevas características;
- otro modelo.

---

## 😊 Análisis de Sentimientos

Permite detectar errores de clasificación.

Ejemplo:

El modelo interpreta un comentario sarcástico como positivo.

La matriz ayuda a identificar estos patrones de error.

---

## 🏦 Evaluación de préstamos

Las entidades financieras utilizan modelos para estimar el riesgo de impago.

Aquí suele ser importante un **Recall elevado**, ya que es preferible identificar a la mayoría de los posibles morosos para reducir el riesgo financiero.

---

# Limitaciones de la Matriz de Confusión

Aunque es una herramienta muy poderosa, presenta algunas limitaciones.

## 1. Problemas multiclase

Cuando existen muchas categorías:

- la matriz crece;
- resulta más difícil interpretarla.

En estos casos suele representarse como un **mapa de calor (Heatmap)**.

---

## 2. No considera el costo de los errores

Todos los errores aparecen con el mismo peso.

Pero en muchos problemas:

- un FN puede ser mucho más grave que un FP;
- o viceversa.

Por ello, además de la matriz de confusión, deben analizarse métricas acordes al contexto del negocio.

---

# Comparación de métricas según el problema

| Aplicación | Métrica más importante | Motivo |
|------------|------------------------|--------|
| 📧 Spam | Precision | Evitar bloquear correos legítimos |
| 🏥 Diagnóstico médico | Recall | Detectar la mayor cantidad posible de enfermos |
| 💳 Fraude financiero | F1-Score | Equilibrar FP y FN |
| 📈 Churn | Precision + Recall | Optimizar campañas de retención |
| 👁️ Visión Artificial | Matriz de Confusión | Detectar clases que el modelo confunde |

---

# Ideas clave

- La **Matriz de Confusión** es la principal herramienta para evaluar modelos de clasificación.
- Está formada por cuatro resultados: **TP, TN, FP y FN**.
- A partir de ella se calculan métricas como **Accuracy**, **Precision**, **Recall** y **F1-Score**.
- No existe una métrica universal; la elección depende del problema y del costo asociado a los distintos tipos de errores.
- La matriz permite identificar fortalezas y debilidades del modelo y orientar su mejora.

---

# Esquema general

```text
                Datos reales
                      │
                      ▼
             Modelo de clasificación
                      │
                      ▼
           Predicciones del modelo
                      │
                      ▼
             Matriz de Confusión
                      │
        ┌─────────────┼──────────────┐
        ▼             ▼              ▼
    Accuracy      Precision      Recall
                       │
                       ▼
                   F1-Score
                      │
                      ▼
          Evaluación y mejora del modelo
```

---

# Conclusión

La **Matriz de Confusión** es una herramienta esencial para comprender el comportamiento de un modelo de clasificación más allá de un simple porcentaje de aciertos. Permite identificar los distintos tipos de errores (**TP, TN, FP y FN**) y calcular métricas como **Accuracy**, **Precision**, **Recall** y **F1-Score**, cada una útil según el contexto. Elegir la métrica adecuada depende del problema que se desea resolver y del impacto que tienen los errores en la aplicación real, ya sea en medicina, finanzas, comercio electrónico o visión por computadora.