# Redes Neuronales
## Resumen basado exclusivamente en el contenido del curso

> **Objetivo del módulo**
>
> Al finalizar este tema se espera que puedas:
>
> - Describir qué es una red neuronal en Machine Learning.
> - Explicar los componentes principales de una neurona simple.
> - Reconocer algunas bibliotecas de Python utilizadas para trabajar con Machine Learning y redes neuronales.

---

# 1. ¿Qué es una red neuronal?

Una **red neuronal** es un modelo computacional inspirado en la estructura y funcionamiento del cerebro humano.

Está diseñada para:

- aprender de los datos;
- identificar patrones;
- realizar predicciones;
- tomar decisiones.

A diferencia de la programación tradicional, el modelo aprende los patrones a partir de los datos en lugar de recibir explícitamente todas las reglas necesarias para resolver el problema.

---

# 2. ¿Cómo está formada una red neuronal?

Una red neuronal está formada por:

- **neuronas**;
- **conexiones** entre las neuronas;
- **capas** de neuronas.

Cada neurona realiza cálculos sencillos.

La capacidad de la red neuronal surge de la combinación de muchas neuronas conectadas y del aprendizaje de sus parámetros durante el entrenamiento.

```text
Entradas
   │
   ▼
┌───────────────┐
│   Neuronas    │
│   Capa        │
└───────────────┘
   │
   ▼
┌───────────────┐
│   Neuronas    │
│   Capa        │
└───────────────┘
   │
   ▼
Salida
```

---

# 3. ¿Qué hace una neurona?

Una neurona puede verse como una pequeña calculadora.

Recibe:

- entradas;
- pesos;
- un sesgo (**bias**).

Luego realiza una serie de cálculos y produce una salida.

```text
Entrada 1 ──► Peso 1 ──┐
                        │
Entrada 2 ──► Peso 2 ──┼──► Suma + Bias
                        │
Entrada 3 ──► Peso 3 ──┘
                              │
                              ▼
                    Función de activación
                              │
                              ▼
                           Salida
```

---

# 4. Entradas (Inputs)

Las **entradas** son los datos que recibe la red neuronal para realizar una predicción.

El curso las compara con:

> "pistas o evidencias" que ayudan al modelo a aprender.

Por ejemplo, conceptualmente:

```text
Entrada 1
Entrada 2
Entrada 3
   ↓
Red neuronal
   ↓
Predicción
```

Las entradas proporcionan la información que la neurona necesita para realizar sus cálculos.

---

# 5. Pesos (Weights)

Cada entrada está asociada a un **peso**.

El peso representa la importancia o fuerza de esa entrada para la neurona.

Un peso grande significa que esa entrada tiene una mayor influencia sobre la salida de la neurona.

```text
Entrada ─────► Peso ─────► Neurona
```

Los pesos **no se establecen necesariamente de forma manual**.

El curso explica que:

> Los pesos se aprenden durante el entrenamiento.

---

# 6. Sesgo (Bias)

Además de las entradas y los pesos, la neurona utiliza un **sesgo o bias**.

El bias es un valor adicional que se suma a la combinación ponderada de las entradas.

Su función es permitir que la neurona ajuste su salida independientemente de las entradas.

Al igual que los pesos:

> **El bias también se aprende durante el entrenamiento.**

---

# 7. Cálculo de una neurona

El proceso explicado en el curso puede representarse conceptualmente así:

```text
Entradas
   ↓
Multiplicar cada entrada por su peso
   ↓
Sumar los resultados
   ↓
Agregar el bias
   ↓
Aplicar función de activación
   ↓
Obtener salida
```

De forma matemática:

```text
z = (x₁ × w₁) + (x₂ × w₂) + ... + (xₙ × wₙ) + b

salida = función_de_activación(z)
```

Donde:

- `x` = entrada
- `w` = peso
- `b` = bias
- `z` = suma ponderada más bias

---

# 8. Función de activación

Después de calcular la suma ponderada de las entradas más el bias, la neurona aplica una **función de activación**.

El curso destaca una característica fundamental:

> La función de activación introduce no linealidad en la salida de la neurona.

Esto permite que la red pueda modelar **relaciones complejas en los datos**.

```text
Entradas
   ↓
Pesos
   ↓
Suma + Bias
   ↓
Función de activación
   ↓
Salida
```

> **Importante:** en este módulo el curso explica la función de activación conceptualmente, pero no profundiza en funciones concretas como ReLU, sigmoid o tanh.

---

# 9. Función de pérdida (Loss Function)

La **función de pérdida** es fundamental durante el entrenamiento de una red neuronal.

Aunque técnicamente no forma parte de una única neurona, permite medir qué tan equivocada está la red.

Compara:

```text
Predicción del modelo
        │
        │
        ▼
Función de pérdida
        ▲
        │
        │
Valor real / etiqueta
```

La función de pérdida cuantifica la diferencia entre:

- la salida que predijo la red;
- la salida real o etiqueta.

---

# 10. Objetivo del entrenamiento

El objetivo del entrenamiento es:

> **Minimizar la pérdida.**

Para lograrlo, la red ajusta sus parámetros internos:

- pesos;
- bias.

El proceso se repite de manera iterativa.

```text
Datos
  ↓
Predicción
  ↓
Comparar con valor real
  ↓
Calcular pérdida
  ↓
Ajustar pesos y bias
  ↓
Volver a predecir
  ↓
Reducir pérdida
```

Con el entrenamiento, la red busca mejorar progresivamente sus predicciones.

---

# 11. Aprendizaje de la red neuronal

Durante el aprendizaje:

1. La red recibe los datos.
2. Realiza cálculos utilizando pesos y bias.
3. Produce una predicción.
4. La función de pérdida mide el error.
5. Los parámetros se ajustan.
6. El proceso se repite.

El objetivo es que la red se vuelva cada vez más competente para:

- realizar predicciones;
- reconocer patrones.

---

# 12. ¿Por qué son importantes las redes neuronales?

El curso destaca que las redes neuronales permiten abordar problemas complejos que pueden resultar difíciles de resolver mediante programación tradicional.

Su capacidad para aprender patrones complejos permite utilizarlas en aplicaciones como:

- reconocimiento de imágenes;
- procesamiento del lenguaje natural;
- vehículos autónomos.

---

# 13. Reconocimiento de imágenes

Las redes neuronales se utilizan para reconocer patrones en imágenes.

Ejemplo mencionado por el curso:

```text
Imagen
   ↓
Red neuronal
   ↓
Identificación de patrones
   ↓
Resultado
```

El curso menciona el reconocimiento de imágenes como una de las aplicaciones importantes de las redes neuronales.

---

# 14. Procesamiento del lenguaje natural

Otra aplicación mencionada es el **procesamiento del lenguaje natural (NLP)**.

Las redes neuronales pueden utilizarse para trabajar con información relacionada con el lenguaje humano.

El curso lo presenta como una de las áreas en las que las redes neuronales tienen aplicaciones importantes.

---

# 15. Vehículos autónomos

Los vehículos autónomos también aparecen como ejemplo de aplicación.

Las redes neuronales forman parte de sistemas capaces de aprender patrones y ayudar a interpretar información para tomar decisiones.

---

# 16. Bibliotecas de Python

El curso presenta diferentes bibliotecas que pueden utilizarse para desarrollar aplicaciones de Machine Learning y redes neuronales.

Entre ellas menciona:

- **Scikit-learn**
- **Microsoft Cognitive Toolkit**
- **PyTorch**

Estas bibliotecas proporcionan herramientas para:

- crear modelos;
- entrenarlos;
- evaluarlos.

---

# 17. Scikit-learn

El curso ya había presentado anteriormente **Scikit-learn** como una biblioteca de Machine Learning.

En este módulo vuelve a mencionarla como una herramienta que permite trabajar con diferentes tipos de modelos, incluyendo redes neuronales.

---

# 18. PyTorch

El curso menciona **PyTorch** como otra biblioteca de Python utilizada para trabajar con modelos de Machine Learning y redes neuronales.

En este módulo no se explica su sintaxis ni se desarrolla un ejemplo práctico con PyTorch.

---

# 19. Microsoft Cognitive Toolkit

También se menciona **Microsoft Cognitive Toolkit** como una biblioteca relacionada con Machine Learning.

El curso la presenta únicamente como una de las herramientas disponibles.

No se desarrolla código con esta biblioteca en este módulo.

---

# 20. Ejemplo conceptual completo

Podemos representar una neurona de la siguiente manera:

```text
                 Peso 1
Entrada 1 ───────────────┐
                         │
                 Peso 2  │
Entrada 2 ───────────────┼──► Suma + Bias
                         │
                 Peso 3  │
Entrada 3 ───────────────┘
                              │
                              ▼
                     Función de activación
                              │
                              ▼
                           Salida
```

Durante el entrenamiento:

```text
                 ┌─────────────────┐
                 │     Neurona     │
                 └────────┬────────┘
                          │
                          ▼
                     Predicción
                          │
                          ▼
                  Función de pérdida
                          │
                          ▼
                Ajustar pesos y bias
                          │
                          └──────► repetir
```

---

# 21. Ejemplo sencillo

Supongamos que queremos que una red realice una predicción utilizando tres entradas.

```text
Entrada 1 ──► x₁
Entrada 2 ──► x₂
Entrada 3 ──► x₃
```

Cada entrada tiene un peso:

```text
x₁ → w₁
x₂ → w₂
x₃ → w₃
```

La neurona calcula:

```text
z = x₁w₁ + x₂w₂ + x₃w₃ + b
```

Después:

```text
salida = función_de_activación(z)
```

Durante el entrenamiento, los valores de:

```text
w₁
w₂
w₃
b
```

se van ajustando para reducir la pérdida.

---

# 22. Conceptos fundamentales

| Concepto | Significado |
|----------|-------------|
| Neurona | Unidad básica que recibe entradas, realiza cálculos y produce una salida. |
| Entrada | Datos que recibe la neurona. |
| Peso | Representa la fuerza o importancia de una entrada. |
| Bias | Valor adicional que se suma a la suma ponderada. |
| Función de activación | Introduce no linealidad y permite modelar relaciones complejas. |
| Salida | Resultado producido por la neurona. |
| Función de pérdida | Mide la diferencia entre la predicción y el valor real. |
| Entrenamiento | Proceso mediante el cual se ajustan pesos y bias. |

---

# 23. El concepto más importante

La idea fundamental del módulo puede resumirse en:

```text
ENTRADAS
   ↓
Pesos + Bias
   ↓
Cálculo
   ↓
Función de activación
   ↓
SALIDA
   ↓
Comparar con valor real
   ↓
Función de pérdida
   ↓
Ajustar pesos y bias
   ↓
REPETIR
```

---

# 24. Relación con Machine Learning

Las redes neuronales son un tipo de modelo de Machine Learning.

Al igual que otros modelos:

```text
Datos
   ↓
Entrenamiento
   ↓
Modelo
   ↓
Predicción
```

La diferencia está en la estructura interna del modelo:

```text
Machine Learning
       │
       └── Redes neuronales
              │
              ├── Neuronas
              ├── Pesos
              ├── Bias
              ├── Activación
              └── Función de pérdida
```

---

# 25. Resumen final

- Una red neuronal es un modelo computacional inspirado en el cerebro humano.
- Está formada por neuronas interconectadas organizadas en capas.
- Cada neurona recibe entradas y realiza cálculos.
- Las entradas tienen pesos que representan su influencia.
- La neurona también utiliza un bias.
- Los pesos y el bias se aprenden durante el entrenamiento.
- La función de activación introduce no linealidad.
- La no linealidad permite modelar relaciones complejas.
- La función de pérdida mide el error entre la predicción y el valor real.
- El objetivo del entrenamiento es minimizar la pérdida.
- Para ello se ajustan iterativamente los pesos y los bias.
- Las redes neuronales tienen aplicaciones en reconocimiento de imágenes, procesamiento del lenguaje natural y vehículos autónomos.
- El curso menciona Scikit-learn, Microsoft Cognitive Toolkit y PyTorch como bibliotecas de Python relacionadas con Machine Learning y redes neuronales.

---

# Lo que NO se desarrolla en este módulo

Para mantener la presentación fiel al curso, no agregar como contenido explicado:

- ReLU
- Sigmoid
- Tanh
- Backpropagation
- Gradient Descent
- Perceptrón
- CNN
- RNN
- LSTM
- Transformers
- Deep Learning
- TensorFlow

Estos conceptos pueden estar relacionados con redes neuronales, pero **no son desarrollados en el video proporcionado**.

## Preginta

### ¿Cuál es la función principal de una red neuronal en el Aprendizaje automático? Seleccione la mejor respuesta.

- **Imitar la estructura y el funcionamiento del cerebro humano para aprender de los datos y hacer predicciones.**
- Para realizar cálculos matemáticos complejos sin ninguna capacidad de aprendizaje.
- Para ocuparse exclusivamente de tareas de Reconocimiento de imágenes.
- Programar explícitamente reglas específicas para la toma de decisiones.

> Correcto Las redes neuronales son modelos computacionales inspirados en el cerebro humano, diseñados para aprender de los datos y hacer predicciones o tomar decisiones.