# Explicación del cuestionario

Una forma sencilla de resolver este tipo de preguntas es identificar **qué error quiere evitar el problema**.

En clasificación existen dos errores principales:

- **Falso Positivo (FP):** el modelo dice que algo es positivo cuando en realidad no lo es.
- **Falso Negativo (FN):** el modelo dice que algo es negativo cuando en realidad sí era positivo.

Según cuál de esos errores sea más grave, elegiremos una métrica distinta.

---
Pregunta 1
## Usted es un científico de datos que trabaja en un modelo de aprendizaje automático para predecir la pérdida de clientes en una empresa de telecomunicaciones. Debe elegir la métrica de evaluación más adecuada para valorar el rendimiento de su modelo. ¿Qué métrica de evaluación sería más útil para determinar en qué medida su modelo de predicción de abandono de clientes identifica a los clientes que realmente tienen probabilidades de abandonarlo? Seleccione la mejor respuesta.

- Precisión
- **(Recall)Número de respuestas pertinentes**
- Precisión
- Puntuación F1

> Correcto La recuperación mide la capacidad del modelo para identificar correctamente los casos positivos (clientes que abandonarán), minimizando los falsos negativos. Esto es crucial para la intervención proactiva con el fin de retener a los clientes.

### Predicción de abandono de clientes (Customer Churn)

**Respuesta correcta:** ✅ Recall

#### ¿Qué dice el enunciado?

> "...identificar a los clientes que realmente tienen probabilidades de abandonarlo."

La frase importante es **identificar a todos los clientes que van a abandonar la empresa**.

Lo peor que podría ocurrir es que un cliente con intención de irse **no sea detectado** por el modelo.

Ese error se llama:

**Falso Negativo (FN)**

Como queremos minimizar los falsos negativos, debemos utilizar **Recall**.

Recall responde a la pregunta:

> **De todos los clientes que realmente abandonarán la empresa, ¿cuántos logró detectar el modelo?**

Cuanto mayor sea el Recall, menos clientes perderemos sin haber intentado retenerlos.

---

Pregunta 2
## Estás desarrollando un modelo para detectar transacciones fraudulentas con tarjeta de crédito para un banco. Es crucial identificar tantas transacciones fraudulentas como sea posible, incluso si esto significa marcar ocasionalmente una transacción legítima para una revisión posterior. ¿Qué métrica de la Matriz de confusión sería más importante priorizar en este escenario? Seleccione la mejor respuesta.

- Falso positivo
- Precisión
- (Recall) Número de respuestas pertinentes
- Verdadero negativo

> Correcto La recuperación mide la capacidad de identificar todos los casos positivos reales (transacciones fraudulentas), minimizando los falsos 

### Detección de fraude bancario

**Respuesta correcta:** ✅ Recall

#### ¿Qué dice el enunciado?

> "...identificar tantas transacciones fraudulentas como sea posible..."

Además agrega:

> "...aunque alguna transacción legítima sea marcada para revisión."

Esto significa que el banco **prefiere revisar algunas operaciones normales antes que dejar pasar un fraude**.

El error más costoso sería:

**Falso Negativo**

Un fraude que el modelo no detecta.

Por eso debemos maximizar el **Recall**.

Una falsa alarma (Falso Positivo) puede revisarse manualmente.

Un fraude no detectado implica pérdidas económicas.

___

Pregunta 3
## Está desarrollando un modelo de Aprendizaje automático para un proveedor de servicios de correo electrónico con el fin de filtrar los mensajes de spam. Es importante que los correos electrónicos legítimos no se clasifiquen erróneamente como spam y se envíen a la carpeta de correo no deseado. ¿Qué métrica debe priorizarse al evaluar el rendimiento de su modelo de detección de spam para garantizar que los correos electrónicos importantes no se clasifiquen erróneamente? Seleccione la mejor respuesta.

- Puntuación F1
- (Recall) Número de respuestas pertinentes
- **Precisión**
- Exactitud (Accuracy)

> Correcto La precisión mide la exactitud de las predicciones positivas (identificación del spam). Una alta precisión garantiza que cuando un correo electrónico se clasifica como spam, se trata realmente de spam, minimizando los falsos positivos (clasificación errónea de correos electrónicos legítimos).


### Filtro de correo electrónico con spam

**Respuesta correcta:** ✅ Precisión

#### ¿Qué dice el enunciado?

> "Es importante que los correos legítimos no sean enviados a la carpeta de spam."

Ahora el problema cambió completamente.

Ya no queremos detectar todos los spam.

Lo importante es **no bloquear correos importantes**.

El error que queremos evitar es:

**Falso Positivo**

El modelo dice:

"Es spam"

cuando en realidad era un correo legítimo.

La métrica adecuada es **Precision**.

Precision responde:

> **De todos los correos que marqué como spam, ¿cuántos realmente eran spam?**

Una Precision alta significa que casi nunca bloquearemos un correo importante.

___

Pregunta 4
## Usted es un científico de datos que construye un modelo para predecir los precios de las acciones. Está comparando dos modelos diferentes y observa que el Modelo A tiene un MSE de 10, mientras que el Modelo B tiene un MSE de 5. ¿Cuál de las siguientes afirmaciones es cierta basándose en los valores MSE de los dos modelos? ¿Cuál de las siguientes afirmaciones es cierta basándose en los valores de MSE de los dos modelos? Seleccione la mejor respuesta.

- El MSE no puede utilizarse para comparar la precisión de distintos modelos.
- **El modelo B es más preciso que el modelo A.**
- El modelo A es más preciso que el modelo B.
- Ambos modelos tienen la misma precisión.

> Correcto Un MSE más bajo indica que las predicciones del modelo están, por término medio, más cerca de los valores reales. Por lo tanto, el modelo B es más preciso.

### Comparación mediante MSE

**Respuesta correcta:** ✅ Modelo B

Modelo A

MSE = 10

Modelo B

MSE = 5

#### ¿Por qué?

MSE significa:

**Mean Squared Error (Error Cuadrático Medio)**

Mide qué tan lejos están las predicciones del valor real.

Cuanto menor sea el MSE:

- menor error
- mejores predicciones

Como:

5 < 10

El Modelo B posee menor error y por lo tanto mejores predicciones.

___

Pregunta 5
## Está trabajando con un conjunto de datos que contiene algunos valores atípicos y le preocupa que estos valores puedan influir de forma desproporcionada en la evaluación del rendimiento de su modelo. Quiere elegir una métrica de regresión que sea menos sensible a los valores atípicos. ¿Qué métrica sería la más adecuada en esta situación? Seleccione la mejor respuesta.

- **Error medio absoluto (MAE)**
- Una combinación de MSE y R-cuadrado
- Error cuadrático medio (ECM)
- R-cuadrado

Buen trabajo
> Correcto El MAE es menos sensible a los valores atípicos porque calcula la media de las diferencias absolutas entre los valores previstos y los reales. Esto significa que los grandes errores procedentes de valores atípicos no tendrán un impacto desproporcionado en la métrica.


### Datos con valores atípicos

**Respuesta correcta:** ✅ MAE

### ¿Qué dice el enunciado?

> "...menos sensible a valores atípicos."

La palabra clave es:

**Outliers**

El curso explica que:

**MSE**

eleva al cuadrado los errores.

Esto hace que un error muy grande influya muchísimo en el resultado.

En cambio:

**MAE**

utiliza el valor absoluto.

Todos los errores pesan de forma proporcional.

Por eso MAE es más robusto cuando existen valores extremos.


Pregunta 6
## Imagine que está desarrollando un modelo de Aprendizaje automático para predecir fallos en los equipos de una planta de fabricación. Su objetivo es minimizar el tiempo de inactividad y los costes de mantenimiento identificando posibles fallos antes de que se produzcan. ¿Qué métricas de evaluación sería más importante priorizar en este escenario? Seleccione la mejor respuesta.

- Precisión y puntuación F1
- Precisión y error cuadrático medio (ECM)
- Precisión y recuperación
- **Recall y ROC-AUC**

Buen trabajo
> Correcto La recuperación es crucial porque mide la capacidad del modelo para identificar todos los fallos reales, minimizando el riesgo de pasar por alto posibles tiempos de inactividad. ROC-AUC ayuda a evaluar la capacidad del modelo para distinguir entre equipos que fallan y los que no fallan en función de diferentes umbrales.

### Mantenimiento predictivo

**Respuesta correcta:** ✅ Recall + ROC-AUC

#### ¿Qué dice el enunciado?

> "...identificar posibles fallos antes de que ocurran."

Nuevamente queremos detectar **todos los fallos posibles**.

Perder un fallo significa:

- detener una máquina
- perder producción
- aumentar los costos

Por eso la primera métrica importante es:

**Recall**

Además aparece:

**ROC-AUC**

¿Por qué?

Porque no solamente interesa detectar fallos.

También queremos un modelo que sea capaz de distinguir correctamente entre:

- equipos que fallarán
- equipos que no fallarán

ROC-AUC evalúa precisamente esa capacidad utilizando distintos umbrales de clasificación.

El propio curso menciona que ROC-AUC ofrece una visión más completa del rendimiento del clasificador.
