# PRESENTACIÓN: APRENDIZAJE SUPERVISADO, MODELOS Y SCIKIT-LEARN

---

## DIAPOSITIVA 1 — PORTADA

- **Título:** Construye tus primeros modelos de Machine Learning
- **Subtítulo:** Regresión Lineal, Regresión Logística, Redes Neuronales y Scikit-Learn
- **Tagline:** De los datos a las predicciones

---

## DIAPOSITIVA 2 — AGENDA

1) ¿Qué es Machine Learning y cómo aprende un modelo?
2) Regresión Lineal: predecir valores continuos
3) Regresión Logística: clasificar con probabilidades
4) Redes Neuronales: neuronas, capas y entrenamiento
5) Documentación de Scikit-Learn y flujo práctico con Iris
6) Preguntas y respuestas clave del módulo
7) Ideas clave para recordar

---

## DIAPOSITIVA 3 — IDEA CENTRAL DEL MÓDULO

- **Machine Learning =** descubrir patrones ocultos en los datos para predecir sobre información nueva
- No se programan todas las reglas; el algoritmo las aprende a partir de ejemplos
- Analogía del curso: **mapa del tesoro**
  - Datos = pistas
  - Algoritmo = descubre el patrón
  - Modelo = resultado del aprendizaje
  - Predicciones = "tesoro"

---

## DIAPOSITIVA 4 — ¿CÓMO APRENDE UN MODELO?

1. Recopilar datos
2. Analizar datos
3. Encontrar patrones y relaciones
4. Construir un modelo
5. Realizar predicciones sobre datos nuevos

- **No memoriza respuestas**
- Aprende relaciones entre variables

---

## DIAPOSITIVA 5 — EJEMPLO PRÁCTICO: PREDECIR PREFERENCIAS

- Caso del curso: ¿comprará el cliente una nueva mezcla de café?
- Entradas usadas por el modelo:
  - Compras anteriores
  - Preferencias
  - Historial de pedidos
- Salida: probabilidad o predicción de compra
- **Importante:** cuantos más datos, mejor suele ser la predicción (rompecabezas: muchas piezas = imagen más clara)

---

## DIAPOSITIVA 6 — HERRAMIENTAS: PYTHON + SCIKIT-LEARN

- **Python** permite:
  - Cargar datos
  - Entrenar modelos
  - Realizar predicciones
  - Evaluar resultados
- **Scikit-learn = "navaja suiza" del ML**
  - Regresión Lineal
  - Redes Neuronales
  - Árboles de decisión
  - Métricas, división de datos, preprocesamiento

---

## DIAPOSITIVA 7 — REGRESIÓN LINEAL: ¿PARA QUÉ SIRVE?

- Tarea: predecir **valores continuos**
- Caso típico del curso: **precio de viviendas**
- Variables de entrada (X):
  - Dormitorios
  - Superficie
  - Ubicación
  - Otras características
- Variable objetivo (y):
  - Precio de la vivienda

---

## DIAPOSITIVA 8 — PASO 0: PREPARACIÓN DE DATOS

Antes de modelar:

- **Pandas para:**
  - Cargar datos
  - Limpiar datos
  - Transformar datos
  - Exploración y estadísticas
- Gestionar **valores faltantes** para no romper el modelo
- Crear o transformar características (conocimiento del dominio)
- **Regla del curso:** primero preparar datos, después modelar

---

## DIAPOSITIVA 9 — DIVISIÓN TRAIN / TEST

- **Training set:** entrenar el modelo
- **Test set:** evaluar con datos NUNCA vistos durante el entrenamiento
- División típica usada en el curso: **70% train / 30% test**
- Herramienta: `train_test_split()`
- `random_state=42` para experimentos reproducibles

---

## DIAPOSITIVA 10 — FLUJO DE REGRESIÓN LINEAL

- Crear modelo: `LinearRegression()`
- Entrenar: `.fit(X_train, y_train)`
- Predecir: `.predict(X_test)` → `y_pred`
- Comparar: `y_test` (valores reales) vs `y_pred` (predicciones)
- Visualizar con matplotlib: `scatter(y_test, y_pred)`

---

## DIAPOSITIVA 11 — MÉTRICAS EN REGRESIÓN LINEAL

- **MSE (Mean Squared Error)**
  - Error promedio al cuadrado
  - Cuanto **más bajo**, mejor
- **R² (R-squared)**
  - Qué tan bien se ajusta el modelo
  - Cuanto **más alto y cercano a 1**, mejor
- **No confundir:**
  - MSE ↓ = mejor
  - R² ↑ = mejor

---

## DIAPOSITIVA 12 — BIBLIOTECAS USADAS EN REGRESIÓN LINEAL

- `pandas` → carga, limpieza, transformación
- `numpy` → operaciones numéricas
- `sklearn.linear_model.LinearRegression`
- `sklearn.model_selection.train_test_split`
- `sklearn.metrics.mean_squared_error`, `r2_score`
- `matplotlib.pyplot` → gráficos

---

## DIAPOSITIVA 13 — ESTRUCTURA BÁSICA DE CÓDIGO (REGRESIÓN)

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv("housing.csv")

X = df[["bedrooms", "sqft", "location"]]
y = df["price"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

modelo = LinearRegression()
modelo.fit(X_train, y_train)

y_pred = modelo.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
```

---

## DIAPOSITIVA 14 — ¿QUÉ ES CLASIFICACIÓN?

- Asignar un dato a una **categoría o grupo**
- Ejemplos del curso:
  - Spam / No spam
  - Fraude / No fraude
  - Enfermo / No enfermo
  - Aprueba / No aprueba
- **Clasificación binaria =** solo dos clases posibles

---

## DIAPOSITIVA 15 — REGRESIÓN LOGÍSTICA: CLASIFICA CON PROBABILIDADES

- A pesar del nombre, se usa para **clasificación**, especialmente binaria
- **Función sigmoidea:**
  - Transforma entradas en **probabilidad entre 0 y 1**
  - Forma de "S"
- Con un **threshold / punto de corte** (ej. 0.5) convertimos probabilidad en clase:
  - P > 0.5 → Clase 1
  - P ≤ 0.5 → Clase 0

---

## DIAPOSITIVA 16 — EJEMPLO: DETECCIÓN DE SPAM

- Características:
  - Cantidad de enlaces
  - Palabras sospechosas
  - Remitente
  - Frecuencia de términos
- Salida esperada:
  - P(spam) = 0.87 → **SPAM**
  - P(spam) = 0.15 → **NO SPAM**

---

## DIAPOSITIVA 17 — ENTRENAMIENTO EN REGRESIÓN LOGÍSTICA

- Aprende **pesos** para cada característica
- Peso mayor = característica más influyente en la predicción
- Pesos no se definen a mano; los aprende el algoritmo
- Proceso:
  1. Datos de entrenamiento
  2. Aprende pesos
  3. Calcula probabilidades
  4. Realiza predicciones

---

## DIAPOSITIVA 18 — OVERFITTING Y UNDERFITTING

- **Overfitting (sobreajuste)**
  - Modelo demasiado especializado en entrenamiento
  - Bueno en train, malo en datos nuevos
  - Riesgo al memorizar en vez de aprender
- **Underfitting (subajuste)**
  - Modelo demasiado simple
  - No captura patrones importantes
  - Malo en train y en test
- Objetivo: punto medio entre ambos

---

## DIAPOSITIVA 19 — REGRESIÓN LOGÍSTICA PARA MÚLTIPLES CLASES

- Estrategia presentada: **One-vs-Rest (Uno contra el resto)**
- Para 3 clases A, B, C se entrenan 3 modelos binarios:
  - A vs B+C
  - B vs A+C
  - C vs A+B
- Clasificación final: **clase con mayor probabilidad**

---

## DIAPOSITIVA 20 — CÓDIGO BÁSICO EN SCIKIT-LEARN (LOGÍSTICA)

```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

modelo = LogisticRegression()
modelo.fit(X_train, y_train)

y_pred = modelo.predict(X_test)
probabilidades = modelo.predict_proba(X_test)
```

- `predict()` → **clase predicha**
- `predict_proba()` → **probabilidades por clase**

---

## DIAPOSITIVA 21 — REGRESIÓN LINEAL VS REGRESIÓN LOGÍSTICA

| Lineal | Logística |
|--------|-----------|
| Predice valores continuos | Predice categorías |
| Ej.: precio de vivienda | Ej.: spam / no spam |
| Salida: número | Salida: probabilidad → clase |
| Tarea: regresión | Tarea: clasificación |
| MSE + R² | Métricas de clasificación (Accuracy, Precision, Recall, F1) |

---

## DIAPOSITIVA 22 — REDES NEURONALES: ¿QUÉ SON?

- Modelo computacional **inspirado en el cerebro humano**
- Objetivos del curso:
  - Aprender de los datos
  - Identificar patrones
  - Realizar predicciones
  - Tomar decisiones
- A diferencia de reglas fijas, la red aprende patrones a partir de ejemplos

---

## DIAPOSITIVA 23 — LA NEURONA COMO UNIDAD BÁSICA

Componentes de una neurona:

- **Entradas (Inputs):** información que recibe
- **Pesos (Weights):** importancia de cada entrada
- **Bias (Sesgo):** ajusta la suma independientemente de entradas
- **Suma ponderada + bias**
- **Función de activación →** introduce no linealidad (permite relaciones complejas)
- **Salida**

---

## DIAPOSITIVA 24 — FÓRMULA CONCEPTUAL DE UNA NEURONA

```text
z = x1·w1 + x2·w2 + ... + xn·wn + b

salida = función_de_activación(z)
```

- `x` → entradas
- `w` → pesos
- `b` → bias
- `z` → combinación lineal
- Importante: **pesos y bias se aprenden durante el entrenamiento**

---

## DIAPOSITIVA 25 — ¿POR QUÉ FUNCIÓN DE ACTIVACIÓN?

- Introduce **no linealidad**
- Sin ella la red sería solo una combinación lineal simple
- Permite modelar **relaciones complejas** de los datos
- Conceptual pero clave para el curso

---

## DIAPOSITIVA 26 — ENTRENAMIENTO: FUNCIÓN DE PÉRDIDA

- **Loss Function** = qué tan equivocada está la red
- Compara **predicción vs valor real**
- Objetivo del entrenamiento: **minimizar la pérdida**
- Para ello se ajustan iterativamente:
  - pesos
  - bias
- Ciclo:
  - Predecir
  - Medir error
  - Ajustar parámetros
  - Repetir

---

## DIAPOSITIVA 27 — ESTRUCTURA DE UNA RED: CAPAS

- **Capa de entrada** → recibe los datos brutos
- **Capas ocultas** → procesan y extraen características cada vez más complejas
- **Capa de salida** → resultado final (predicción, clasificación, etc.)
- La potencia viene de combinar MUCHAS neuronas en capas

---

## DIAPOSITIVA 28 — ¿QUÉ ES LA PROFUNDIDAD?

- Número de **capas ocultas**
- Más profunda → puede aprender patrones más complejos
- Pero también:
  - Más recursos computacionales
  - Suele necesitar más datos
  - Más riesgo de sobreajuste
- Por eso es una decisión de diseño (depende de tarea y datos)

---

## DIAPOSITIVA 29 — APLICACIONES DE REDES NEURONALES

- **Reconocimiento de imágenes**
  - Reconocimiento facial
  - Detección de objetos
  - Imágenes médicas (CNN)
- **NLP (Procesamiento Lenguaje Natural)**
  - Traducción automática
  - Análisis de sentimientos
  - Generación de texto
  - (RNN y Transformers son arquitecturas mencionadas)
- **Vehículos autónomos**
  - Percepción del entorno
  - Predicciones de tráfico
  - Control del vehículo
- **Sistemas de recomendación**
  - Video, compras, música

---

## DIAPOSITIVA 30 — DESAFÍOS DE LAS REDES NEURONALES

- Requieren **muchos recursos computacionales**
- Dependen de **grandes cantidades de datos etiquetados**
- Riesgo de **sobreajuste (overfitting)**
- Estrategias útiles del curso:
  - **Regularización** → restricciones para evitar especialización excesiva
  - **Transfer Learning (aprendizaje por transferencia)** → reutilizar conocimientos aprendidos en otra tarea

---

## DIAPOSITIVA 31 — BIBLIOTECAS DE PYTHON PARA REDES Y ML

Mencionadas en el material:

- **Scikit-learn** → ML clásico y modelos de clasificación/regresión
- **PyTorch** → redes neuronales modernas
- **Microsoft Cognitive Toolkit** → herramienta MS para ML

---

## DIAPOSITIVA 32 — DOCUMENTACIÓN DE SCIKIT-LEARN

Es el puente entre teoría y práctica. Sirve para:

- Comprender algoritmos
- Conocer parámetros
- Ver ejemplos y tutoriales
- Evaluar y ajustar modelos
- Elegir algoritmos apropiados por tipo de tarea

---

## DIAPOSITIVA 33 — CUATRO SECCIONES CLAVE DE LA DOCU

- **📚 User Guide**
  - Conceptos fundamentales, buenas prácticas, errores comunes, preprocesamiento, evaluación
- **📖 API Reference**
  - Diccionario técnico: clases, funciones, métodos, parámetros, retornos
- **💻 Examples**
  - Ejemplos de código y problemas reales
- **🧑‍💻 Tutorials**
  - Flujos paso a paso, prácticos

---

## DIAPOSITIVA 34 — FLUJO RECOMENDADO PARA USAR LA DOCU

1) Identificar el problema
2) Elegir tarea de ML: clasificación / regresión / clustering
3) Explorar algoritmos
4) Comprender parámetros
5) Experimentar
6) Evaluar modelo
7) Ajustar modelo

---

## DIAPOSITIVA 35 — PARÁMETROS DE UN MODELO: EJEMPLO CON DECISION TREE

Usado en el ejemplo práctico del curso: `DecisionTreeClassifier`

- **criterion** → cómo medir calidad de una división
- **max_depth** → profundidad máxima del árbol (controla complejidad)
- **min_samples_split** → muestras mínimas para dividir un nodo
- Modificar estos parámetros cambia el comportamiento del modelo

---

## DIAPOSITIVA 36 — BUSCAR MEJOR CONFIGURACIÓN

- No probar parámetros al azar
- Técnicas mencionadas:
  - **Grid Search**
  - **Random Search**
- Objetivo: explorar configuraciones sistemáticamente
- Después: **evaluar y comparar** métricas

---

## DIAPOSITIVA 37 — MÉTRICAS SEGÚN TIPO DE TAREA

- **Clasificación:**
  - Accuracy
  - Precision
  - Recall
  - F1 Score
- **Regresión:**
  - MSE
  - R²
- Regla importante: la evaluación es **continua**, no solo al final
  - Entrenar → Evaluar → Ajustar → Nuevos datos → Volver a evaluar

---

## DIAPOSITIVA 38 — EJEMPLO PRÁCTICO CON IRIS (SCIKIT-LEARN)

- Dataset Iris: clasificación de flores por medidas de sépalo/pétalo
- Flujo del curso:
  1. `load_iris()`
  2. `train_test_split()`
  3. `DecisionTreeClassifier`
  4. `.fit()`
  5. `.predict()`
  6. `accuracy_score()`

---

## DIAPOSITIVA 39 — CÓDIGO COMPLETO IRIS

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

modelo = DecisionTreeClassifier(criterion="gini", max_depth=5, min_samples_split=10)
modelo.fit(X_train, y_train)

y_pred = modelo.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
```

- También se puede **visualizar el árbol** para interpretar decisiones

---

## DIAPOSITIVA 40 — ¿QUÉ APRENDEMOS DE LA DOCUMENTACIÓN?

No hay que memorizarlo todo. La docu ayuda a saber:

- **QUÉ** algoritmo usar
- **CÓMO** funciona
- **QUÉ** parámetros tiene
- **CÓMO** configurarlo
- **CÓMO** evaluarlo

---

## DIAPOSITIVA 41 — RESPUESTAS CLAVE (19_Preguntas_1.md)

1) **ML = encontrar patrones ocultos:** analogía correcta es **mapa del tesoro** (pistas para encontrar un tesoro escondido)
2) **Red neuronal en laberinto (robot):** funciona como un **cerebro**, aprende de errores y mejora navegación
3) **Paso crucial antes de Regresión Lineal (precio coches):** limpiar y preparar datos (valores faltantes, incoherencias)
4) **Predecir clic en recomendación (Sí/No):** **Regresión logística** (clasificación binaria)
5) **Docu de Scikit-learn ayuda en inicio:** explica algoritmos, casos de uso y ajuste de parámetros
6) **Predicción de compra próximo mes con histórico etiquetado:** **Aprendizaje supervisado** (porque hay datos etiquetados para entrenar)

---

## DIAPOSITIVA 42 — OTRAS PREGUNTAS INCORPORADAS EN LOS MATERIALES

- **Función de la sigmoidea en Regresión Logística:**
  - Transforma la combinación lineal en **probabilidad entre 0 y 1**
- **Función principal red neuronal en ML:**
  - Imitar estructura/funcionamiento del cerebro humano para **aprender de los datos y hacer predicciones**

---

## DIAPOSITIVA 43 — IDEAS CLAVE FINALES (POR MODELO)

- **Regresión Lineal**
  - Predice valores continuos
  - Calidad con MSE ↓ y R² ↑
- **Regresión Logística**
  - Predice probabilidades → clases
  - Sigmoidea + threshold
- **Redes Neuronales**
  - Neuronas → capas → entrenamiento por pérdida
  - Potentes pero costosas
- **Scikit-learn + documentación**
  - No memorices todo: aprende a buscar, probar y evaluar

---

## DIAPOSITIVA 44 — FRASE PARA CERRAR

> "En Machine Learning no se trata solo de entrenar modelos: se trata de preparar bien los datos, elegir el modelo adecuado, medir con las métricas correctas y ajustar usando documentación y experimentación."

---


