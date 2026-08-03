# 📘 Resumen: Matriz de Confusión y Métricas de Evaluación en Machine Learning

## 🎯 Objetivos de aprendizaje

Al finalizar este tema podrás:

- Comprender qué es una **Matriz de Confusión (Confusion Matrix)**.
- Interpretar los distintos tipos de aciertos y errores de un modelo de clasificación.
- Conocer las métricas más utilizadas para evaluar modelos de Machine Learning.
- Saber cuándo utilizar cada métrica según el problema.
- Entender las limitaciones de la matriz de confusión.

---

# ¿Por qué es importante evaluar un modelo?

Cuando entrenamos un modelo de Machine Learning no basta con obtener predicciones; debemos comprobar **qué tan bien está funcionando**.

Una buena evaluación permite:

- detectar errores;
- comparar distintos modelos;
- mejorar el algoritmo;
- evitar el sobreajuste (*Overfitting*);
- generar confianza antes de utilizar el modelo en producción.

> **Idea clave:** Un modelo con un Accuracy del 99% no siempre es un buen modelo.

---

# ¿Qué es una Matriz de Confusión?

La **Matriz de Confusión** es una tabla que compara:

- ✅ La respuesta real.
- 🤖 La respuesta predicha por el modelo.

Gracias a esta comparación podemos conocer exactamente en qué casos el modelo acierta y en cuáles se equivoca.

---

# Estructura de la Matriz de Confusión

Para un problema de clasificación binaria, la matriz tiene cuatro resultados posibles.

|                      | Predicción Positiva | Predicción Negativa |
|----------------------|--------------------|--------------------|
| **Clase Real Positiva** | ✅ Verdadero Positivo (TP) | ❌ Falso Negativo (FN) |
| **Clase Real Negativa** | ❌ Falso Positivo (FP) | ✅ Verdadero Negativo (TN) |

---

# Los cuatro resultados posibles

## ✅ Verdadero Positivo (True Positive - TP)

El modelo predijo correctamente un resultado positivo.

### Ejemplo

El cliente realmente compró un producto y el modelo también predijo que compraría.

---

## ✅ Verdadero Negativo (True Negative - TN)

El modelo predijo correctamente un resultado negativo.

### Ejemplo

El cliente no realizó ninguna compra y el modelo acertó.

---

## ❌ Falso Positivo (False Positive - FP)

También llamado **Error de Tipo I**.

El modelo predice un resultado positivo cuando en realidad era negativo.

### Ejemplo

El banco bloquea una tarjeta creyendo que existe fraude.

Después descubre que la compra era completamente legítima.

---

## ❌ Falso Negativo (False Negative - FN)

También llamado **Error de Tipo II**.

El modelo predice un resultado negativo cuando realmente era positivo.

### Ejemplo

El sistema considera que una transacción fraudulenta es normal.

El fraude pasa desapercibido.

---

# Representación visual

```text
                     Predicción

                 Positivo   Negativo
              -------------------------
Real Positivo |     TP     |    FN    |
              -------------------------
Real Negativo |     FP     |    TN    |
              -------------------------
```

---

# Ejemplo sencillo

Supongamos un modelo que detecta spam.

De 100 correos:

- 40 eran Spam.
- 60 eran normales.

El modelo obtiene:

| Resultado | Cantidad |
|-----------|----------|
| TP | 35 |
| TN | 55 |
| FP | 5 |
| FN | 5 |

La matriz sería:

|               | Predijo Spam | Predijo No Spam |
|---------------|-------------|----------------|
| **Spam** | 35 | 5 |
| **No Spam** | 5 | 55 |

---

# Métricas derivadas de la Matriz de Confusión

---

# 1. Accuracy (Exactitud)

Indica el porcentaje de predicciones correctas.

## Fórmula

```text
Accuracy = (TP + TN) / Total
```

### Ventajas

- Muy fácil de interpretar.
- Funciona bien cuando las clases tienen tamaños similares.

### Desventajas

Puede ser engañosa cuando existe un gran desbalance entre clases.

### Ejemplo

Supongamos:

- 990 pacientes sanos.
- 10 pacientes enfermos.

Si el modelo responde siempre:

> "Está sano"

Obtendrá:

```text
Accuracy = 99%
```

Pero:

❌ No detectó ningún paciente enfermo.

---

## Ejemplo en Scikit-Learn

```python
from sklearn.metrics import accuracy_score

y_real = [1, 1, 0, 0, 1]
y_pred = [1, 0, 0, 0, 1]

accuracy = accuracy_score(y_real, y_pred)

print(accuracy)
```

Salida:

```python
0.8
```

El modelo acertó el **80%** de las predicciones.

---

# 2. Precision (Precisión)

Responde:

> **Cuando el modelo dice "Sí", ¿cuántas veces tiene razón?**

## Fórmula

```text
Precision = TP / (TP + FP)
```

Su objetivo es minimizar los **Falsos Positivos**.

### ¿Cuándo usarla?

Cuando el costo de un falso positivo es alto.

Ejemplos:

- Detección de Spam.
- Publicidad.
- Marketing.
- Sistemas de recomendación.

---

## Ejemplo en Scikit-Learn

```python
from sklearn.metrics import precision_score

precision = precision_score(y_real, y_pred)

print(precision)
```

---

# 3. Recall (Sensibilidad)

También conocido como:

- Sensibilidad
- Tasa de Verdaderos Positivos

Responde:

> **¿Cuántos positivos reales logró detectar el modelo?**

## Fórmula

```text
Recall = TP / (TP + FN)
```

Busca minimizar los **Falsos Negativos**.

### ¿Cuándo usarlo?

Cuando perder un caso positivo puede tener consecuencias graves.

Ejemplos:

- Diagnóstico médico.
- Detección de fraude.
- Detección de incendios.
- Sistemas de seguridad.

---

## Ejemplo en Scikit-Learn

```python
from sklearn.metrics import recall_score

recall = recall_score(y_real, y_pred)

print(recall)
```

---

# 4. F1-Score

El **F1-Score** combina Precision y Recall.

Es útil cuando ambas métricas son importantes.

## Fórmula

```text
F1 = 2 × (Precision × Recall)
     -------------------------
      Precision + Recall
```

Características:

- penaliza valores bajos;
- busca equilibrio;
- muy útil con clases desbalanceadas.

---

## Ejemplo en Scikit-Learn

```python
from sklearn.metrics import f1_score

f1 = f1_score(y_real, y_pred)

print(f1)
```

---

# 5. Matriz de Confusión en Scikit-Learn

La biblioteca Scikit-Learn permite obtener la matriz de forma muy sencilla.

```python
from sklearn.metrics import confusion_matrix

y_real = [1, 1, 0, 0, 1]
y_pred = [1, 0, 0, 0, 1]

matriz = confusion_matrix(y_real, y_pred)

print(matriz)
```

Salida:

```python
[[2 0]
 [1 2]]
```

Interpretación:

```text
TN = 2
FP = 0
FN = 1
TP = 2
```

---

# Informe completo

Scikit-Learn también genera automáticamente todas las métricas.

```python
from sklearn.metrics import classification_report

print(classification_report(y_real, y_pred))
```

Obtendremos:

- Precision
- Recall
- F1-Score
- Accuracy
- Support (cantidad de ejemplos)

---

# ¿Qué métrica utilizar?

| Problema | Métrica recomendada | Motivo |
|----------|---------------------|--------|
| 📧 Detección de Spam | Precision | Evitar marcar correos importantes como spam. |
| 🏥 Diagnóstico Médico | Recall | No dejar pacientes enfermos sin detectar. |
| 💳 Detección de Fraude | F1-Score | Equilibrar FP y FN. |
| 🛒 Predicción de Compras | Accuracy + F1 | Evaluar el rendimiento general y el equilibrio entre errores. |
| 📈 Predicción de Churn | Recall + Precision | Detectar clientes con riesgo de abandono sin generar demasiadas falsas alarmas. |

---

# Casos de uso reales

## 💳 Finanzas

Detectar:

- fraude;
- lavado de dinero;
- riesgo crediticio.

---

## 🏥 Medicina

Evaluar modelos de:

- diagnóstico;
- análisis de imágenes;
- detección de enfermedades.

---

## 📧 Correo electrónico

Clasificar mensajes en:

- Spam
- No Spam

---

## 👁️ Visión Artificial

Detectar errores de clasificación entre objetos.

Ejemplo:

- gato ↔ perro
- automóvil ↔ camión

---

## 😊 Análisis de Sentimientos

Clasificar opiniones como:

- positivas;
- negativas;
- neutras.

---

# Limitaciones de la Matriz de Confusión

Aunque es una herramienta muy útil, presenta algunas limitaciones.

## 1. Problemas multiclase

Cuando existen muchas categorías:

- la matriz crece;
- resulta más difícil de interpretar.

En estos casos suele visualizarse mediante un **Heatmap**.

---

## 2. No considera el costo de los errores

Todos los errores parecen iguales.

Sin embargo:

Un falso negativo en medicina puede ser muchísimo más grave que un falso positivo.

Por ello siempre debe analizarse el contexto del problema.

---

# Ideas clave

- La Matriz de Confusión permite comprender exactamente cómo se comporta un modelo de clasificación.
- Está formada por cuatro resultados: **TP**, **TN**, **FP** y **FN**.
- Accuracy mide el porcentaje de aciertos, pero no siempre refleja la calidad real del modelo.
- Precision minimiza los falsos positivos.
- Recall minimiza los falsos negativos.
- El F1-Score busca un equilibrio entre Precision y Recall.
- Scikit-Learn facilita el cálculo de todas estas métricas mediante funciones ya implementadas.
- La mejor métrica depende del problema que se desea resolver y del costo asociado a cada tipo de error.

---

# Resumen visual

```text
                Datos reales
                     │
                     ▼
            Modelo de Clasificación
                     │
                     ▼
              Predicciones
                     │
                     ▼
           Matriz de Confusión
      ┌────────┬────────┬────────┐
      ▼        ▼        ▼        ▼
     TP       TN       FP       FN
      │
      ▼
 ┌───────────────┬────────────────────────┐
 │ Accuracy      │ % de aciertos          │
 │ Precision     │ Reduce FP              │
 │ Recall        │ Reduce FN              │
 │ F1-Score      │ Balance entre ambos    │
 └───────────────┴────────────────────────┘
```

---

# Conclusión

La **Matriz de Confusión** es una de las herramientas más importantes para evaluar modelos de clasificación. Más allá de indicar cuántas predicciones fueron correctas, permite analizar **qué tipo de errores comete el modelo** y calcular métricas como **Accuracy, Precision, Recall y F1-Score**. Comprender estas métricas es fundamental para elegir el modelo adecuado según el problema, ya sea detectar fraudes, diagnosticar enfermedades, clasificar correos electrónicos o analizar sentimientos. Además, bibliotecas como **Scikit-Learn** simplifican enormemente su cálculo y análisis, convirtiéndolas en herramientas indispensables para cualquier científico de datos.