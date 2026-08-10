# Regresión Logística

## 1. ¿Qué es la clasificación?

La **clasificación** es una tarea de Machine Learning cuyo objetivo es determinar a qué **grupo o categoría** pertenece un dato nuevo a partir de sus características.

Ejemplos:

```text
Correo electrónico
       ↓
¿Spam o no spam?

Transacción
       ↓
¿Fraudulenta o legítima?

Paciente
       ↓
¿Tiene riesgo de desarrollar una enfermedad?
```

La regresión logística es especialmente utilizada para **clasificación binaria**.

---

# 2. ¿Qué significa clasificación binaria?

Una clasificación es **binaria** cuando solamente existen dos resultados posibles.

Por ejemplo:

```text
SPAM
NO SPAM
```

Otros ejemplos:

```text
Fraude / No fraude

Enfermo / No enfermo

Aprueba / No aprueba

Sí / No
```

La regresión logística es un algoritmo muy utilizado para este tipo de problemas.

---

# 3. La función sigmoidea

La base de la regresión logística es la **función sigmoidea**.

La función sigmoidea transforma una combinación de las características de entrada en un valor de **probabilidad entre 0 y 1**.

Conceptualmente:

```text
Características
      ↓
Combinación de las características
      ↓
Función sigmoidea
      ↓
Probabilidad entre 0 y 1
```

La función tiene una forma característica de **S**:

```text
Probabilidad
1.0 |                    ______
    |                 __/
    |              __/
0.5 |------------_/
    |          _/
    |       __/
0.0 |______/
    +--------------------------> Entrada
```

---

# 4. ¿Cómo se interpreta la probabilidad?

La salida de la función sigmoidea representa una probabilidad.

Por ejemplo:

```text
0.10 → probabilidad baja
0.30 → probabilidad baja
0.50 → zona de decisión
0.70 → probabilidad alta
0.95 → probabilidad muy alta
```

Para convertir esa probabilidad en una clase se utiliza un **punto de corte (threshold)**.

El curso utiliza como ejemplo un punto de corte de:

```text
0.5
```

Entonces:

```text
Probabilidad > 0.5
        ↓
      Clase 1

Probabilidad ≤ 0.5
        ↓
      Clase 0
```

Por ejemplo:

```text
P(spam) = 0.80
       ↓
0.80 > 0.50
       ↓
SPAM
```

Mientras que:

```text
P(spam) = 0.20
       ↓
0.20 ≤ 0.50
       ↓
NO SPAM
```

> **Importante:** la sigmoidea produce una probabilidad y el punto de corte permite convertir esa probabilidad en una clasificación.

---

# 5. Proceso para construir un modelo

El curso presenta un proceso paso a paso.

```text
1. Recopilar y limpiar los datos
              ↓
2. Transformar datos no numéricos
              ↓
3. Separar entrenamiento y prueba
              ↓
4. Seleccionar características
              ↓
5. Entrenar el modelo
              ↓
6. Evaluar el modelo
              ↓
7. Realizar nuevas predicciones
```

---

# 6. Preparación de los datos

Antes de entrenar el modelo es necesario preparar los datos.

Esto incluye:

- limpiar los datos;
- gestionar información faltante;
- transformar datos no numéricos;
- preparar las características para el algoritmo.

Por ejemplo, si tenemos:

```text
color = rojo
color = azul
color = verde
```

el algoritmo necesita que estas categorías sean representadas de una manera numérica que pueda procesar.

---

# 7. Separar datos de entrenamiento y prueba

Al igual que vimos en regresión lineal, los datos se dividen en dos conjuntos.

```text
Dataset
   │
   ├──────────────► Training set
   │                    ↓
   │                 Entrenar
   │
   └──────────────► Test set
                        ↓
                     Evaluar
```

### Training set

Se utiliza para que el modelo aprenda.

### Test set

Se utiliza posteriormente para comprobar cómo funciona el modelo con datos que no utilizó durante el entrenamiento.

---

# 8. Selección e ingeniería de características

Las **características (features)** son las variables que utiliza el modelo para realizar sus predicciones.

El curso destaca la importancia de seleccionar las características más relevantes.

Esto puede ayudar a:

- mejorar el rendimiento;
- concentrar el aprendizaje en la información más importante;
- reducir el riesgo de sobreajuste;
- reducir el riesgo de subajuste.

---

# 9. Sobreajuste (Overfitting)

El **sobreajuste** ocurre cuando el modelo se vuelve demasiado especializado en los datos de entrenamiento.

Puede funcionar muy bien con los datos utilizados para entrenarlo, pero funcionar mal con datos nuevos.

```text
Training
   ↓
Modelo demasiado especializado
   ↓
Muy buen resultado en entrenamiento
   ↓
Mal resultado con datos nuevos
```

---

# 10. Subajuste (Underfitting)

El **subajuste** ocurre cuando el modelo es demasiado simple para capturar los patrones presentes en los datos.

```text
Modelo demasiado simple
        ↓
No captura los patrones importantes
        ↓
Mal rendimiento
```

Por eso es importante encontrar un modelo que pueda aprender los patrones relevantes sin memorizar excesivamente los datos de entrenamiento.

---

# 11. Pesos de las características

Durante el entrenamiento, a cada característica se le asigna un **peso**.

El peso representa la importancia o influencia de esa característica en la predicción.

Conceptualmente:

```text
Característica 1 ──► Peso 1 ──┐
Característica 2 ──► Peso 2 ──┼──► Predicción
Característica 3 ──► Peso 3 ──┘
```

Un peso mayor significa que esa característica tiene una mayor influencia en la predicción.

El algoritmo aprende los pesos durante el entrenamiento.

---

# 12. Entrenamiento del modelo

Durante el entrenamiento:

```text
Datos de entrenamiento
          ↓
Regresión logística
          ↓
Aprende pesos
          ↓
Calcula probabilidades
          ↓
Realiza predicciones
```

El objetivo es aprender qué combinación de características permite realizar buenas predicciones.

---

# 13. Evaluación

Una vez entrenado el modelo, se utilizan los datos de prueba para evaluar su rendimiento.

```text
Modelo entrenado
       ↓
Datos de prueba
       ↓
Predicciones
       ↓
Evaluación
```

Si el rendimiento es satisfactorio, el modelo puede utilizarse para clasificar nuevos datos.

---

# 14. Clasificación multiclase

Aunque la regresión logística se utiliza principalmente para clasificación binaria, el curso explica que también puede utilizarse cuando existen **más de dos clases**.

Una estrategia mencionada es:

## One-vs-Rest (Uno contra el resto)

La idea consiste en entrenar varios modelos de regresión logística binaria.

Cada modelo aprende a distinguir:

```text
Una clase
   VS
Todas las demás clases
```

Por ejemplo, si tenemos tres clases:

```text
Clase A
Clase B
Clase C
```

se pueden crear modelos:

```text
Modelo 1 → A vs. B + C

Modelo 2 → B vs. A + C

Modelo 3 → C vs. A + B
```

Cuando aparece un dato nuevo, cada modelo genera una probabilidad.

La clase cuyo modelo produzca la mayor probabilidad será la clasificación final.

```text
Nuevo dato
    ↓
┌─────────────┐
│ Modelo A    │ → Probabilidad A
├─────────────┤
│ Modelo B    │ → Probabilidad B
├─────────────┤
│ Modelo C    │ → Probabilidad C
└─────────────┘
       ↓
Mayor probabilidad
       ↓
Clase predicha
```

---

# 15. Aplicaciones reales

El curso presenta diferentes aplicaciones de la regresión logística.

## 🏥 Salud

Puede utilizarse para:

- predecir la probabilidad de que un paciente desarrolle una enfermedad;
- analizar la eficacia de tratamientos.

---

## 🏦 Finanzas

Los bancos e instituciones financieras pueden utilizarla para:

- evaluar riesgo crediticio;
- decidir sobre solicitudes de préstamos;
- detectar transacciones fraudulentas.

---

## 🌳 Ciencias ambientales

Puede utilizarse para modelar relaciones entre factores ambientales y determinados eventos.

Ejemplos mencionados:

- probabilidad de extinción de especies;
- propagación de incendios forestales.

---

# 16. Ejemplo conceptual: detección de spam

Supongamos que queremos determinar si un correo es spam.

Tenemos características como:

```text
cantidad de enlaces
cantidad de palabras sospechosas
remitente
frecuencia de determinadas palabras
```

El modelo analiza estas características:

```text
Características
      ↓
Regresión logística
      ↓
Función sigmoidea
      ↓
P(spam)
```

Supongamos que obtenemos:

```text
P(spam) = 0.87
```

Con un threshold de `0.5`:

```text
0.87 > 0.5
   ↓
SPAM
```

En cambio:

```text
P(spam) = 0.15

0.15 ≤ 0.5
   ↓
NO SPAM
```

---

# 17. Ejemplo de código con Scikit-learn

El material se centra en el proceso de construcción del modelo. Un ejemplo básico en Python puede representarse así:

```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# X = características
# y = clases

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

# Crear el modelo
modelo = LogisticRegression()

# Entrenar
modelo.fit(X_train, y_train)

# Realizar predicciones
y_pred = modelo.predict(X_test)

# Obtener probabilidades
probabilidades = modelo.predict_proba(X_test)

print(y_pred)
print(probabilidades)
```

La diferencia conceptual es importante:

```python
modelo.predict(X_test)
```

devuelve la **clase predicha**.

Mientras que:

```python
modelo.predict_proba(X_test)
```

devuelve las **probabilidades** asociadas a las clases.

---

# 18. Flujo completo

El proceso completo puede resumirse así:

```text
DATOS
  ↓
Limpieza
  ↓
Transformación de categorías
  ↓
Selección de características
  ↓
Training / Test
  ↓
Regresión logística
  ↓
Aprendizaje de pesos
  ↓
Función sigmoidea
  ↓
Probabilidad
  ↓
Threshold
  ↓
Clase
  ↓
Evaluación
```

---

# 19. Regresión lineal vs. regresión logística

Es importante no confundirlas.

| Regresión lineal | Regresión logística |
|---|---|
| Predice valores continuos | Predice clases |
| Ej.: precio de una vivienda | Ej.: spam / no spam |
| Salida numérica | Probabilidad → clase |
| Regresión | Clasificación |
| MSE y R² son métricas utilizadas en el curso | Se evalúa como modelo de clasificación |

Ejemplo:

```text
Regresión lineal:

Características → Precio
                  350000


Regresión logística:

Características → Probabilidad → Clase
                  0.87            SPAM
```

---

# 20. Ideas fundamentales para recordar

### 1. La regresión logística es un algoritmo de clasificación

Aunque su nombre contiene la palabra "regresión", en este contexto se utiliza para **clasificar datos**.

### 2. Es especialmente útil para clasificación binaria

```text
Clase 0 / Clase 1
```

### 3. La sigmoidea produce una probabilidad

```text
Entrada
  ↓
Sigmoidea
  ↓
Probabilidad entre 0 y 1
```

### 4. El threshold convierte probabilidad en clase

Con `0.5` como ejemplo:

```text
> 0.5 → una clase

≤ 0.5 → otra clase
```

### 5. Los pesos se aprenden durante el entrenamiento

Cada característica recibe un peso que representa su influencia en la predicción.

### 6. Hay que evaluar el modelo con datos nuevos

Por eso se separan los datos en:

```text
Training
Test
```

### 7. También puede utilizarse para varias clases

Una estrategia presentada en el curso es **One-vs-Rest**.

---

# 21. Conceptos clave

```text
Clasificación
→ determinar a qué categoría pertenece un dato

Clasificación binaria
→ solamente existen dos clases

Regresión logística
→ algoritmo utilizado para clasificación

Sigmoidea
→ transforma la combinación de características en una probabilidad

Probabilidad
→ valor entre 0 y 1

Threshold
→ punto de corte utilizado para transformar probabilidad en clase

Feature
→ característica utilizada por el modelo

Peso
→ influencia de una característica en la predicción

Overfitting
→ modelo demasiado especializado en los datos de entrenamiento

Underfitting
→ modelo demasiado simple para capturar los patrones

One-vs-Rest
→ estrategia para utilizar modelos binarios en problemas multiclase
```

---

# 22. Idea principal

> **La regresión logística utiliza las características de los datos para calcular una probabilidad mediante una función sigmoidea y, a partir de un punto de corte, convertir esa probabilidad en una clasificación.**

El concepto central es:

```text
CARACTERÍSTICAS
      ↓
REGRESIÓN LOGÍSTICA
      ↓
SIGMOIDEA
      ↓
PROBABILIDAD
      ↓
THRESHOLD
      ↓
CLASIFICACIÓN
```

## Pregunta


### ¿Cuál de las siguientes opciones describe mejor el papel de la función sigmoidea en la regresión logística? Seleccione la mejor respuesta.

- Divide los datos en conjuntos de entrenamiento y prueba para la evaluación del modelo.
- **Transforma la combinación lineal de las características de entrada en un valor de probabilidad entre 0 y 1.**
- Asigna pesos a cada característica de entrada en función de su importancia.
- Predice directamente la clase o categoría de los nuevos datos no vistos.

> Correcto La función sigmoidea es esencial en la Regresión logística para convertir el resultado del modelo en una probabilidad, lo que permite la clasificación.