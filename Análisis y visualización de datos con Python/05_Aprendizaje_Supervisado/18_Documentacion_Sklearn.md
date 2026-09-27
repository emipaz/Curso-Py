# Documentación de Scikit-Learn

## 1. ¿Qué es Scikit-Learn?

El aprendizaje automático incluye muchos algoritmos y aplicaciones diferentes. Esto puede resultar complejo, especialmente cuando comenzamos a trabajar con distintos algoritmos y parámetros.

La **documentación de Scikit-Learn** sirve como una guía para comprender e implementar algoritmos de Machine Learning.

Permite:

- Comprender cómo funcionan los algoritmos.
- Conocer sus fundamentos.
- Identificar sus puntos fuertes y débiles.
- Conocer sus parámetros.
- Encontrar ejemplos prácticos.
- Elegir algoritmos adecuados para cada problema.
- Evaluar y ajustar modelos.

La documentación funciona como un puente entre la **teoría y la práctica**.

---

# 2. Secciones principales de la documentación

El curso presenta cuatro recursos principales.

## 📚 User Guide

La **Guía del Usuario** es el punto de partida para comprender Machine Learning con Scikit-Learn.

Incluye:

- Conceptos fundamentales.
- Buenas prácticas.
- Errores comunes.
- Preprocesamiento de datos.
- Evaluación de modelos.
- Tutoriales.
- Ejemplos.

Es recomendable comenzar por esta sección cuando todavía estamos aprendiendo los conceptos.

---

## 📖 API Reference

La **Referencia de API** funciona como un diccionario técnico.

Contiene información detallada sobre:

- Clases.
- Funciones.
- Métodos.
- Parámetros.
- Valores de retorno.
- Ejemplos de utilización.

Es especialmente útil cuando ya comprendemos los fundamentos y necesitamos conocer los detalles de una determinada clase o algoritmo.

---

## 💻 Examples

La sección **Examples** contiene ejemplos de código que muestran cómo aplicar diferentes algoritmos y técnicas.

Los ejemplos permiten:

- Ver cómo se implementa un algoritmo.
- Comprender la lógica utilizada.
- Analizar problemas reales.
- Adaptar el código a nuestros propios proyectos.

---

## 🧑‍💻 Tutorials

Los **Tutoriales** proporcionan una experiencia más práctica y paso a paso.

Pueden incluir:

- Preparación de datos.
- Implementación de modelos.
- Código.
- Visualizaciones.
- Explicaciones detalladas.

Son útiles para reforzar los conceptos mediante la práctica.

---

# 3. ¿Cómo utilizar la documentación?

El curso propone un proceso para explorar algoritmos y sus parámetros.

```text
Identificar el problema
        ↓
Elegir la tarea de Machine Learning
        ↓
Explorar los algoritmos
        ↓
Comprender sus parámetros
        ↓
Experimentar
        ↓
Evaluar el modelo
        ↓
Ajustar el modelo
```

# 4. Paso 1 — Identificar la tarea

Primero debemos determinar qué problema queremos resolver.

Por ejemplo:

- ¿Quiero clasificar?
- ¿Quiero predecir un valor?
- ¿Quiero agrupar datos?

Algunas tareas mencionadas por el curso son:

- Clasificación
- Regresión
- Clustering / agrupación

La Guía del Usuario y los ejemplos pueden ayudarnos a encontrar algoritmos apropiados para cada tarea.

# 5. Paso 2 — Explorar los algoritmos

Una vez identificada la tarea, podemos consultar la API Reference.

Los algoritmos están organizados por categorías.

Es importante revisar:

Cómo funciona el algoritmo.

- Sus características.
- Sus puntos fuertes.
- Sus puntos débiles.
- Para qué problemas resulta apropiado.

No se trata simplemente de elegir un algoritmo al azar.

# 6. Paso 3 — Comprender los parámetros

Cada algoritmo posee diferentes parámetros.

La documentación explica:

- Qué hace cada parámetro.
- Qué valores puede tomar.
- Cuáles son sus valores predeterminados.
- Cómo afectan al comportamiento del algoritmo.

Estos parámetros permiten personalizar el modelo.

# 7. Ejemplo: DecisionTreeClassifier

El curso utiliza como ejemplo un árbol de decisión.

Algunos de sus parámetros son:

- criterion:

Indica cómo se mide la calidad de una división del árbol.

- max_depth:

Define la profundidad máxima que puede alcanzar el árbol.

min_samples_split:

Indica el número mínimo de muestras necesarias para dividir un nodo interno.

Conceptualmente:

```text
DecisionTreeClassifier
        │
        ├── criterion
        ├── max_depth
        └── min_samples_split
```

# 8. Paso 4 — Experimentar con parámetros

Modificar estos parámetros puede cambiar significativamente el comportamiento y rendimiento del modelo.

# 8. Paso 4 — Experimentar con parámetros

Una vez comprendidos los parámetros, podemos experimentar con diferentes valores.

Por ejemplo:

- max_depth = 2
- max_depth_depth = 5
- depth = 10

Podemos comparar cómo cambia el rendimiento del modelo.

La documentación proporciona ejemplos que pueden utilizarse como punto de partida.

También se mencionan técnicas como:

- Grid Search
- Random Search

Estas permiten explorar sistemáticamente diferentes configuraciones de parámetros.

9. Paso 5 — Evaluar el modelo

Después de entrenar un modelo debemos evaluar su rendimiento.

Las métricas dependen del tipo de problema.

Clasificación

El curso menciona:

- Accuracy
- Precision
- Recall
- F1 Score

Regresión

Menciona:

- MSE
- R²

La evaluación permite comparar diferentes algoritmos y configuraciones.

10. La evaluación es un proceso continuo

Evaluar un modelo no significa hacerlo solamente una vez.

El curso destaca la importancia de continuar supervisando el rendimiento del modelo cuando recibe nuevos datos.

```text
Entrenar
   ↓
Evaluar
   ↓
Ajustar
   ↓
Nuevos datos
   ↓
Volver a evaluar
```

# 11. Ejemplo práctico del curso: Iris
11. Ejemplo práctico del curso: Iris

El curso utiliza el conocido conjunto de datos Iris para demostrar cómo consultar y utilizar la documentación de Scikit-Learn.

Iris es un conjunto de datos utilizado para problemas de clasificación.

El flujo general del ejemplo es:

```text
Dataset Iris
     ↓
Dividir datos
     ↓
Training / Test
     ↓
DecisionTreeClassifier
     ↓
Entrenar
     ↓
Predecir
     ↓
Evaluar Accuracy
```


12. Código del ejemplo

El curso muestra el uso de DecisionTreeClassifier junto con el dataset Iris.

Un ejemplo representativo del flujo utilizado es:
```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Cargar el dataset Iris
iris = load_iris()

X = iris.data
y = iris.target

# Separar los datos
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

# Crear el modelo
modelo = DecisionTreeClassifier()

# Entrenar
modelo.fit(X_train, y_train)

# Realizar predicciones
y_pred = modelo.predict(X_test)

# Evaluar
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)
13. ¿Qué está haciendo este código?
1. Cargar los datos
iris = load_iris()
```	

Se carga el conjunto de datos Iris.

2. Separar características y etiquetas
```python
X = iris.data
y = iris.target
X → características
y → etiquetas / clases
```

3. Separar entrenamiento y prueba

```python
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)
```

Los datos se dividen en:

Training → entrenar el modelo

Test → evaluar el modelo

4. Crear el árbol de decisión
modelo = DecisionTreeClassifier()

Creamos una instancia del algoritmo.

5. Entrenar

```python
modelo.fit(X_train, y_train)
```

El modelo aprende utilizando los datos de entrenamiento.

6. Realizar predicciones

```python
y_pred = modelo.predict(X_test)
```

El modelo utiliza los datos de prueba para realizar predicciones.

7. Evaluar
accuracy = accuracy_score(y_test, y_pred)

Se compara:

```text
Predicciones
     ↓
Valores reales
     ↓
Accuracy
```

14. Parámetros del árbol de decisión

Una de las ventajas de consultar la documentación es poder conocer los parámetros disponibles.

Por ejemplo:

```python
modelo = DecisionTreeClassifier(
    criterion="gini",
    max_depth=5,
    min_samples_split=10
)
```

El curso destaca especialmente:

- criterion
→ calidad de la división

- max_depth
→ profundidad máxima del árbol

- min_samples_split
→ mínimo de muestras necesarias para dividir un nodo

Experimentar con estos valores permite observar cómo afectan al rendimiento.

15. Visualización del árbol

La documentación también proporciona orientación para visualizar el árbol de decisión.

Esto puede ayudar a:

comprender cómo toma decisiones el modelo;
observar las divisiones;
interpretar el proceso;
detectar posibles áreas de mejora.

16. La documentación como herramienta de aprendizaje

La idea principal del módulo es que no necesitamos memorizar todos los algoritmos y parámetros de Scikit-Learn.

Podemos utilizar la documentación para investigar.

```text
Tengo un problema
       ↓
Identifico el tipo de Machine Learning
       ↓
Busco algoritmos apropiados
       ↓
Leo la documentación
       ↓
Reviso parámetros
       ↓
Busco ejemplos
       ↓
Pruebo el código
       ↓
Evalúo el resultado
```



17. Ideas fundamentales

Scikit-Learn

→ Biblioteca con herramientas para Machine Learning.

User Guide

→ Explica conceptos, tareas y buenas prácticas.

API Reference

→ Detalla clases, funciones, métodos y parámetros.

Examples

→ Muestra implementaciones prácticas.

Tutorials

→ Enseñan mediante procesos paso a paso.

Training

→ Datos utilizados para entrenar el modelo.

Test

→ Datos utilizados para evaluar el modelo.

Parámetros

→ Permiten configurar el comportamiento del algoritmo.

Grid Search / Random Search

→ Técnicas para explorar configuraciones de parámetros.

Evaluación

→ Permite medir y comparar el rendimiento de los modelos.

18. Idea principal del curso

La documentación de Scikit-Learn es una herramienta fundamental para aprender, implementar y ajustar modelos de Machine Learning.

No solamente sirve para copiar código.

Permite entender:

```text
QUÉ algoritmo utilizar
        ↓
CÓMO funciona
        ↓
QUÉ parámetros tiene
        ↓
CÓMO configurarlo
        ↓
CÓMO evaluarlo
``` 

Y el ejemplo del curso resume todo el proceso:

```text
Iris
 ↓
train_test_split()
 ↓
DecisionTreeClassifier
 ↓
fit()
 ↓
predict()
 ↓
accuracy_score()
```	   