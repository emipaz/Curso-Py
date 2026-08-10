# Redes Neuronales Artificiales
## Resumen del material del curso

> **Objetivo:** comprender los componentes fundamentales de una red neuronal, cómo se organizan sus neuronas en capas, cómo aprenden y cuáles son algunas de sus aplicaciones en el mundo real.

---

# 1. ¿Qué es una red neuronal artificial?

Una **red neuronal artificial** es un modelo de Machine Learning inspirado en la estructura y funcionamiento del cerebro humano.

Está formada por **nodos interconectados llamados neuronas**, capaces de:

- recibir datos;
- procesarlos;
- aprender patrones;
- realizar predicciones;
- tomar decisiones.

La idea fundamental es que una red neuronal puede aprender relaciones complejas a partir de los datos.

---

# 2. La neurona: unidad básica

La unidad básica de una red neuronal artificial es la **neurona**, también denominada **perceptrón** en el material.

Una neurona recibe diferentes entradas, las procesa y produce una salida.

Sus componentes principales son:

- **Entradas**
- **Pesos**
- **Función de activación**

---

# 3. Entradas (Inputs)

Las entradas representan las características o información que recibe la neurona.

Normalmente son valores numéricos.

Por ejemplo:

```text
Entrada 1 ──►
Entrada 2 ──►  Neurona
Entrada 3 ──►
```

Las entradas contienen la información que el modelo utilizará para realizar una predicción.

---

# 4. Pesos (Weights)

Cada entrada está asociada a un **peso**.

El peso determina la fuerza o importancia de esa entrada.

```text
Entrada 1 ──► Peso 1 ──►
Entrada 2 ──► Peso 2 ──► Neurona
Entrada 3 ──► Peso 3 ──►
```

Los pesos son **parámetros ajustables**.

Durante el entrenamiento, la red aprende cuáles deben ser sus valores para mejorar sus predicciones.

---

# 5. Función de activación

La neurona calcula una suma ponderada de las entradas y luego aplica una **función de activación**.

La función de activación introduce **no linealidad** en la red.

Esto es fundamental porque permite que la red neuronal aprenda relaciones complejas entre los datos.

El proceso básico es:

```text
Entradas
   ↓
Suma ponderada
   ↓
Función de activación
   ↓
Salida
```

---

# 6. Cálculo de la salida

El material explica el proceso en tres pasos:

```text
1. Calcular la suma ponderada de las entradas
             ↓
2. Pasar la suma por la función de activación
             ↓
3. Obtener la salida de la neurona
```

Conceptualmente:

```text
z = x₁ × w₁ + x₂ × w₂ + ... + xₙ × wₙ

salida = función_de_activación(z)
```

Donde:

- `x` = entrada
- `w` = peso
- `z` = suma ponderada

---

# 7. Redes neuronales multicapa

Una sola neurona puede realizar cálculos relativamente sencillos.

El verdadero potencial aparece cuando muchas neuronas se organizan en **capas** y se conectan entre sí.

Una red puede estar formada por:

```text
Capa de entrada
       ↓
Capas ocultas
       ↓
Capa de salida
```

---

# 8. Capa de entrada

La **capa de entrada** es el punto donde ingresan los datos a la red.

Puede recibir diferentes tipos de información.

Por ejemplo:

- valores numéricos;
- características de clientes;
- píxeles de una imagen.

```text
Datos
 ↓
Capa de entrada
```

---

# 9. Capas ocultas

Las **capas ocultas** se encuentran entre la entrada y la salida.

Cada capa contiene varias neuronas que procesan la información recibida de la capa anterior.

A medida que los datos atraviesan las capas, la red puede aprender características cada vez más complejas y abstractas.

```text
Entrada
   ↓
Capa oculta 1
   ↓
Capa oculta 2
   ↓
Capa oculta 3
   ↓
Salida
```

---

# 10. Capa de salida

La **capa de salida** es la última capa de la red.

Produce el resultado final.

Dependiendo de la tarea, puede generar:

- una predicción;
- una clasificación;
- otro tipo de resultado.

```text
Capas ocultas
      ↓
Capa de salida
      ↓
Resultado
```

---

# 11. Interconexión y pesos

Las neuronas de las diferentes capas están conectadas mediante conexiones ponderadas.

Los pesos determinan la intensidad de la señal que pasa de una neurona a otra.

Durante el entrenamiento:

```text
Datos
  ↓
Red neuronal
  ↓
Predicción
  ↓
Ajuste de pesos
  ↓
Mejor rendimiento
```

La red aprende a modificar los pesos para mejorar sus predicciones o clasificaciones.

---

# 12. ¿Qué significa profundidad?

La **profundidad** de una red se relaciona con el número de **capas ocultas**.

```text
Pocas capas
     ↓
Red menos profunda

Muchas capas
     ↓
Red más profunda
```

Las redes más profundas tienen mayor capacidad para aprender patrones y relaciones complejas.

Sin embargo, también presentan algunos inconvenientes:

- requieren más recursos informáticos;
- pueden necesitar más datos;
- son más propensas al sobreajuste.

Por eso, elegir la profundidad adecuada es una decisión de diseño que depende de:

- la tarea;
- los datos disponibles.

---

# 13. ¿Por qué las redes profundas son potentes?

La combinación de:

- muchas neuronas;
- múltiples capas;
- conexiones entre neuronas;
- pesos ajustables;

permite que la red aprenda características cada vez más complejas.

```text
Datos simples
     ↓
Características
     ↓
Características más complejas
     ↓
Patrones abstractos
     ↓
Predicción / clasificación
```

Esta capacidad permite abordar problemas que serían difíciles de resolver mediante reglas programadas manualmente.

---

# 14. Aplicaciones reales

El material presenta varias aplicaciones importantes de las redes neuronales.

## Reconocimiento de imágenes

Las **redes neuronales convolucionales (CNN)** tienen un papel importante en visión por ordenador.

Aplicaciones mencionadas:

- reconocimiento facial;
- detección de objetos;
- análisis de imágenes médicas.

Por ejemplo:

```text
Imagen médica
     ↓
CNN
     ↓
Análisis de patrones
     ↓
Resultado
```

---

# 15. Procesamiento del lenguaje natural (NLP)

Las redes neuronales también se utilizan en el **procesamiento del lenguaje natural**.

El material menciona:

- traducción de idiomas;
- análisis de sentimientos;
- generación de textos.

También menciona específicamente:

- **RNN**
- **Modelos Transformer**

como arquitecturas utilizadas en aplicaciones de NLP.

---

# 16. Vehículos autónomos

Las redes neuronales desempeñan un papel importante en los vehículos autónomos.

Pueden utilizar información proveniente de:

- cámaras;
- LiDAR;
- radar;
- otros sensores.

El material resume tres funciones:

```text
Datos de sensores
       ↓
Percepción del entorno
       ↓
Predicciones
       ↓
Control del vehículo
```

El sistema puede:

- procesar datos de sensores;
- anticipar el comportamiento de vehículos, peatones y obstáculos;
- ayudar a controlar dirección, aceleración y frenado.

---

# 17. Sistemas de recomendación

Las redes neuronales también pueden utilizarse para crear recomendaciones personalizadas.

Ejemplos del material:

### Plataformas de vídeo

Recomendar películas y programas según:

- historial de visualización;
- preferencias del usuario.

### Compras online

Sugerir productos utilizando:

- historial de navegación;
- historial de compras.

### Aplicaciones musicales

Crear listas de reproducción personalizadas según los hábitos de escucha.

---

# 18. Desafíos de las redes neuronales

Las redes neuronales ofrecen grandes posibilidades, pero también presentan desafíos.

## Recursos computacionales

Las redes neuronales profundas tienen muchas capas y conexiones.

Por eso, su entrenamiento puede requerir importantes recursos informáticos.

---

## Cantidad de datos

El material destaca que las redes neuronales suelen depender de **grandes cantidades de datos etiquetados** para aprender eficazmente.

---

## Sobreajuste (Overfitting)

El **sobreajuste** ocurre cuando la red se especializa demasiado en los datos utilizados durante el entrenamiento.

El problema es que puede tener dificultades para generalizar a datos nuevos.

```text
Datos de entrenamiento
        ↓
Modelo demasiado especializado
        ↓
Muy buen rendimiento en entrenamiento
        ↓
Mal rendimiento en datos nuevos
```

---

# 19. Regularización

Una de las técnicas mencionadas para combatir el sobreajuste es la **regularización**.

La regularización introduce restricciones en el proceso de aprendizaje para evitar que el modelo se especialice demasiado en los datos de entrenamiento.

Objetivo:

```text
Evitar sobreajuste
       ↓
Mejor generalización
       ↓
Mejor rendimiento con datos nuevos
```

---

# 20. Aprendizaje por transferencia

El material también menciona el **aprendizaje por transferencia (Transfer Learning)**.

La idea es aprovechar conocimientos adquiridos en una tarea para mejorar el rendimiento en otra tarea.

Conceptualmente:

```text
Conocimiento aprendido
        ↓
Nueva tarea relacionada
        ↓
Mejor rendimiento
```

Es una estrategia que puede ayudar a reducir las necesidades de entrenamiento desde cero.

---

# 21. Arquitectura general

Podemos resumir una red neuronal multicapa así:

```text
                    RED NEURONAL

Datos
  │
  ▼
┌───────────────┐
│ Capa entrada  │
└───────┬───────┘
        │
        ▼
┌───────────────┐
│ Capa oculta   │
│ ○ ○ ○ ○ ○     │
└───────┬───────┘
        │
        ▼
┌───────────────┐
│ Capa oculta   │
│ ○ ○ ○ ○ ○     │
└───────┬───────┘
        │
        ▼
┌───────────────┐
│ Capa salida   │
└───────┬───────┘
        │
        ▼
   Predicción
```

---

# 22. Neurona vs. red neuronal

Es importante distinguir ambos conceptos.

### Neurona

Es una unidad individual:

```text
Entradas
   ↓
Pesos
   ↓
Función de activación
   ↓
Salida
```

### Red neuronal

Es un conjunto de muchas neuronas conectadas y organizadas en capas:

```text
Entradas
   ↓
Muchas neuronas
   ↓
Capas ocultas
   ↓
Muchas neuronas
   ↓
Salida
```

La potencia surge de la combinación de muchas unidades simples.

---

# 23. Conceptos fundamentales para recordar

| Concepto | Significado |
|---|---|
| Neurona | Unidad básica de una red neuronal |
| Perceptrón | Nombre utilizado en el material para una neurona artificial |
| Entrada | Información que recibe la neurona |
| Peso | Determina la importancia de una entrada |
| Función de activación | Introduce no linealidad |
| Capa de entrada | Recibe los datos |
| Capa oculta | Procesa y extrae características |
| Capa de salida | Produce el resultado |
| Profundidad | Cantidad de capas ocultas |
| Sobreajuste | El modelo se especializa demasiado en los datos de entrenamiento |
| Regularización | Técnica para ayudar a evitar el sobreajuste |
| Transfer Learning | Aprovecha conocimientos aprendidos en otra tarea |

---

# 24. Resumen final

Las redes neuronales artificiales son modelos de Machine Learning formados por **neuronas interconectadas**.

Una neurona:

```text
Entrada
   ↓
Peso
   ↓
Suma ponderada
   ↓
Función de activación
   ↓
Salida
```

Varias neuronas pueden organizarse en:

```text
Capa de entrada
       ↓
Capas ocultas
       ↓
Capa de salida
```

Las redes más profundas pueden aprender relaciones más complejas, aunque requieren más recursos y pueden ser más propensas al sobreajuste.

El material presenta aplicaciones en:

- reconocimiento de imágenes;
- procesamiento del lenguaje natural;
- vehículos autónomos;
- sistemas de recomendación.

También destaca desafíos como:

- necesidad de recursos computacionales;
- necesidad de grandes cantidades de datos;
- sobreajuste.

Y presenta como estrategias para afrontar estos problemas:

- **regularización**;
- **aprendizaje por transferencia**.

---

# Idea principal para recordar

> **Una red neuronal combina muchas neuronas simples organizadas en capas para aprender patrones cada vez más complejos a partir de los datos.**