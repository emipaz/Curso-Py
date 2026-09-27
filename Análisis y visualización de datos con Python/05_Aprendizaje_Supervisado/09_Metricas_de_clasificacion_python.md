# 📘 Resumen: Métricas de Clasificación en Machine Learning con Python

## 🎯 Objetivos de aprendizaje

Al finalizar este tema podrás:

- Comprender las principales **métricas de evaluación** para modelos de clasificación.
- Aprender cómo aplicarlas en Python utilizando **Scikit-Learn**.
- Interpretar los resultados para seleccionar el modelo más adecuado.
- Entender cuándo utilizar cada métrica según el problema.

---

# ¿Por qué son importantes las métricas?

Una vez entrenado un modelo de clasificación, es necesario responder una pregunta fundamental:

> **¿Qué tan bueno es el modelo?**

Las métricas permiten medir objetivamente el rendimiento del modelo y compararlo con otros.

Se utilizan en aplicaciones como:

- 📧 Detección de spam.
- 💳 Detección de fraude.
- 🏥 Diagnóstico médico.
- 🛒 Clasificación de productos.
- 🌸 Clasificación de especies de flores.

---

# Bibliotecas utilizadas

Para este ejemplo se utilizan varias bibliotecas de Python.

| Biblioteca | Función |
|------------|---------|
| **pandas** | Manipulación y organización de datos. |
| **scikit-learn (sklearn)** | Entrenamiento y evaluación de modelos de Machine Learning. |
| **matplotlib** | Visualización de datos mediante gráficos. |

---

# Modelos utilizados

Se comparan dos algoritmos de clasificación.

## 1. Regresión Logística (Logistic Regression)

Busca una **frontera de decisión lineal** para separar las clases.

### Características

- rápida;
- sencilla;
- muy utilizada como modelo base;
- funciona bien cuando las clases pueden separarse aproximadamente mediante una línea o plano.

---

## 2. Árbol de Decisión (Decision Tree)

Construye una estructura en forma de árbol mediante preguntas sucesivas.

Ejemplo:

```text
¿Longitud del pétalo > 2 cm?

        Sí
       /   \
     Clase A  ¿Ancho > 1 cm?
                /       \
           Clase B    Clase C
```

### Características

- fácil de interpretar;
- maneja relaciones no lineales;
- puede sobreajustarse si no se controla su profundidad.

---

# Conjunto de datos utilizado

Se utiliza el famoso **Iris Dataset**, incluido en Scikit-Learn.

## ¿Qué contiene?

150 flores de iris clasificadas en tres especies:

- 🌸 Iris Setosa
- 🌸 Iris Versicolor
- 🌸 Iris Virginica

Cada flor posee cuatro características:

- longitud del sépalo;
- ancho del sépalo;
- longitud del pétalo;
- ancho del pétalo.

El objetivo es predecir la especie a partir de estas mediciones.

---

# Preparación de los datos

Los datos se dividen en:

## Variables predictoras (**X**)

Contienen las características de cada flor.

## Variable objetivo (**Y**)

Contiene la especie correspondiente.

---

# División entre entrenamiento y prueba

Se utiliza:

```python
train_test_split()
```

En este ejemplo:

- **70 %** → entrenamiento.
- **30 %** → prueba.

```python
test_size = 0.30
```

Además:

```python
random_state = 42
```

permite obtener siempre la misma división, haciendo los experimentos **reproducibles**.

---

# Entrenamiento del modelo

Cada algoritmo aprende utilizando únicamente los datos de entrenamiento.

Posteriormente realiza predicciones sobre datos que **nunca había visto**, permitiendo evaluar su capacidad de generalización.

---

# Accuracy (Precisión Global)

## ¿Qué mide?

La proporción de predicciones correctas sobre el total.

### Fórmula

```text
Accuracy =
Predicciones correctas
────────────────────────
Total de predicciones
```

### Ejemplo

Si un modelo acierta:

- 95 de 100 casos

Entonces:

```text
Accuracy = 95%
```

### Ventajas

- sencilla de entender;
- útil cuando las clases están balanceadas.

### Desventajas

Puede resultar engañosa cuando existe un gran desbalance entre clases.

---

# ¿Por qué Accuracy puede ser engañosa?

Supongamos un conjunto de datos donde:

- 99 % → correos normales.
- 1 % → spam.

Un modelo que clasifique **todos** los correos como normales tendría:

```text
Accuracy = 99 %
```

Pero sería completamente inútil porque **nunca detecta el spam**.

Por eso se necesitan otras métricas.

---

# Precision (Precisión)

## ¿Qué responde?

> De todas las predicciones positivas realizadas por el modelo, ¿cuántas fueron realmente correctas?

### Fórmula

```text
Precision =
Verdaderos Positivos
────────────────────────────────────
Verdaderos Positivos + Falsos Positivos
```

### Es importante cuando...

Los falsos positivos tienen un costo elevado.

### Ejemplo

- detección de fraude;
- filtros automáticos;
- bloqueo de cuentas.

---

# Recall (Sensibilidad o Exhaustividad)

## ¿Qué responde?

> De todos los casos positivos reales, ¿cuántos logró detectar el modelo?

### Fórmula

```text
Recall =
Verdaderos Positivos
────────────────────────────────────
Verdaderos Positivos + Falsos Negativos
```

### Es importante cuando...

No detectar un caso positivo puede ser muy grave.

### Ejemplos

- diagnóstico de cáncer;
- detección de enfermedades;
- incendios;
- sistemas de alarma.

---

# El equilibrio entre Precision y Recall

En muchos problemas existe un compromiso (**trade-off**).

Si aumentamos la precisión:

- suele disminuir el recall.

Si aumentamos el recall:

- puede disminuir la precisión.

El objetivo suele ser encontrar un equilibrio.

---

# F1-Score

Para equilibrar ambas métricas se utiliza el **F1 Score**.

Es la **media armónica** entre Precision y Recall.

### Fórmula

```text
            2 × Precision × Recall
F1 = ─────────────────────────────────────
        Precision + Recall
```

### ¿Cuándo utilizarla?

Cuando:

- Precision y Recall son igualmente importantes;
- existen clases desbalanceadas;
- se desea una medida única del rendimiento.

---

# Matriz de Confusión (Confusion Matrix)

La matriz de confusión muestra todas las predicciones realizadas por el modelo.

| | Predijo Positivo | Predijo Negativo |
|---|---:|---:|
| **Real Positivo** | Verdadero Positivo (TP) | Falso Negativo (FN) |
| **Real Negativo** | Falso Positivo (FP) | Verdadero Negativo (TN) |

Permite identificar exactamente qué tipos de errores está cometiendo el modelo.

---

# ROC-AUC

Otra métrica muy utilizada es **ROC-AUC**.

## ¿Qué evalúa?

La capacidad del modelo para distinguir correctamente entre clases utilizando distintos umbrales de decisión.

### Ventajas

- independiente del umbral de clasificación;
- muy útil para comparar modelos.

Cuanto más cercano a **1**, mejor será el modelo.

---

# Ejemplo práctico en Python con Iris y Scikit-Learn

El siguiente ejemplo carga el dataset `Iris`, divide los datos, entrena dos modelos y calcula las métricas principales.

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
    roc_auc_score
)

# 1. Cargar dataset
iris = load_iris()
X = iris.data
y = iris.target

# 2. Dividir datos
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42, stratify=y
)

# 3. Crear modelos
log_reg = LogisticRegression(max_iter=200)
tree = DecisionTreeClassifier(max_depth=3, random_state=42)

# 4. Entrenar modelos
log_reg.fit(X_train, y_train)
tree.fit(X_train, y_train)

# 5. Predecir
y_pred_log = log_reg.predict(X_test)
y_pred_tree = tree.predict(X_test)
```

---

# Ejemplo de Accuracy, Precision, Recall y F1-Score

Como `Iris` es un problema multiclase, en `sklearn` suele utilizarse `average="macro"` para promediar el resultado entre las tres especies.

```python
print("Regresión Logística")
print("Accuracy :", accuracy_score(y_test, y_pred_log))
print("Precision:", precision_score(y_test, y_pred_log, average="macro"))
print("Recall   :", recall_score(y_test, y_pred_log, average="macro"))
print("F1-Score :", f1_score(y_test, y_pred_log, average="macro"))

print("\nÁrbol de Decisión")
print("Accuracy :", accuracy_score(y_test, y_pred_tree))
print("Precision:", precision_score(y_test, y_pred_tree, average="macro"))
print("Recall   :", recall_score(y_test, y_pred_tree, average="macro"))
print("F1-Score :", f1_score(y_test, y_pred_tree, average="macro"))
```

También es muy útil obtener un reporte completo por clase:

```python
print(classification_report(y_test, y_pred_log, target_names=iris.target_names))
```

Este reporte muestra:

- precision por clase;
- recall por clase;
- f1-score por clase;
- soporte (cantidad de ejemplos reales por clase).

---

# Ejemplo de Matriz de Confusión

La matriz de confusión permite ver exactamente en qué especies se equivoca el modelo.

```python
cm = confusion_matrix(y_test, y_pred_log)
print(cm)
```

Una posible salida sería:

```text
[[15  0  0]
 [ 0 14  1]
 [ 0  1 14]]
```

Interpretación:

- la diagonal principal contiene los aciertos;
- los valores fuera de la diagonal representan errores;
- por ejemplo, una flor `Versicolor` confundida con `Virginica`.

---

# Ejemplo de ROC-AUC en un problema multiclase

Para calcular `ROC-AUC` en `Iris`, usamos las probabilidades predichas por el modelo y un enfoque multiclase como `ovr` (*one-vs-rest*).

```python
y_prob_log = log_reg.predict_proba(X_test)

roc_auc = roc_auc_score(
    y_test,
    y_prob_log,
    multi_class="ovr",
    average="macro"
)

print("ROC-AUC:", roc_auc)
```

Si el valor se acerca a `1.0`, significa que el modelo separa muy bien las clases.

---

# Comparación rápida entre modelos

Podemos construir un pequeño resumen para comparar ambos algoritmos en el mismo dataset.

```python
metricas = {
    "Modelo": ["Regresión Logística", "Árbol de Decisión"],
    "Accuracy": [
        accuracy_score(y_test, y_pred_log),
        accuracy_score(y_test, y_pred_tree)
    ],
    "Precision_macro": [
        precision_score(y_test, y_pred_log, average="macro"),
        precision_score(y_test, y_pred_tree, average="macro")
    ],
    "Recall_macro": [
        recall_score(y_test, y_pred_log, average="macro"),
        recall_score(y_test, y_pred_tree, average="macro")
    ],
    "F1_macro": [
        f1_score(y_test, y_pred_log, average="macro"),
        f1_score(y_test, y_pred_tree, average="macro")
    ]
}

import pandas as pd
df_metricas = pd.DataFrame(metricas)
print(df_metricas)
```

Esto facilita decidir cuál modelo se comporta mejor según la métrica que más nos interese.

---

# ¿Qué métrica elegir?

Depende completamente del problema.

| Problema | Métrica recomendada | Motivo |
|----------|---------------------|--------|
| 🏥 Diagnóstico médico | **Recall** | Es fundamental detectar la mayor cantidad posible de casos positivos. |
| 💳 Detección de fraude | **Precision** | Se busca minimizar las falsas alarmas. |
| ⚖️ Cuando Precision y Recall son importantes | **F1 Score** | Equilibra ambas métricas. |
| 📊 Comparación general de modelos | **Accuracy** | Adecuada cuando las clases están balanceadas. |
| 📈 Comparación con distintos umbrales | **ROC-AUC** | Evalúa la capacidad discriminatoria del modelo. |

---

# Flujo completo del proceso

```text
Conjunto de datos
        │
        ▼
División entrenamiento / prueba
        │
        ▼
Entrenamiento del modelo
        │
        ▼
Predicciones
        │
        ▼
Evaluación mediante métricas
        │
        ├── Accuracy
        ├── Precision
        ├── Recall
        ├── F1 Score
        ├── Matriz de Confusión
        └── ROC-AUC
        │
        ▼
Selección del mejor modelo
```

---

# Ideas clave

- Las métricas permiten evaluar objetivamente un modelo de clasificación.
- **Accuracy** mide el porcentaje total de aciertos, pero puede ser engañosa con datos desbalanceados.
- **Precision** indica qué proporción de las predicciones positivas fueron correctas.
- **Recall** mide cuántos casos positivos reales logró detectar el modelo.
- **F1 Score** combina Precision y Recall en una única métrica.
- La **Matriz de Confusión** ayuda a comprender los errores cometidos por el modelo.
- **ROC-AUC** compara el rendimiento del clasificador considerando distintos umbrales.
- En problemas multiclase como `Iris`, suele utilizarse `average="macro"` para resumir las métricas.
- No existe una métrica universalmente mejor: la elección depende del problema y de los objetivos del proyecto.

---

# Conclusión

Las métricas son herramientas esenciales para evaluar modelos de clasificación en Machine Learning. Más allá de entrenar un algoritmo, es fundamental interpretar correctamente su rendimiento utilizando métricas adecuadas. Elegir la métrica correcta permite seleccionar el modelo más confiable y adaptado a cada caso de uso, ya sea detectar fraudes, diagnosticar enfermedades o clasificar cualquier otro tipo de información.
