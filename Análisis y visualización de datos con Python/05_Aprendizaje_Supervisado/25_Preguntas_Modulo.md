# Preguntas del Módulo Aprendizaje Supervisado

## Pregunta 1
Imagine que está desarrollando un sistema de recomendación para una Plataforma de comercio electrónico. El sistema debe analizar el historial de navegación del usuario, los patrones de compra y las valoraciones de los productos para ofrecer sugerencias de productos personalizadas. ¿Cuál de las siguientes técnicas de Aprendizaje automático podría emplearse en este escenario? Seleccione todas las que corresponda.

- **[x] Aprendizaje no supervisado**
- **[x] Aprendizaje supervisado**
- **[x] Aprendizaje por refuerzo**
- [ ] Procesamiento del lenguaje natural (PLN)

> **Explicación:** Un sistema de recomendación puede utilizar aprendizaje supervisado (para predecir valoraciones o compras basadas en datos históricos etiquetados), aprendizaje no supervisado (para agrupar clientes con gustos similares) y aprendizaje por refuerzo (para aprender dinámicamente de las interacciones continuas de los usuarios).

---

## Pregunta 2
Un equipo está desarrollando un modelo de Aprendizaje automático para identificar transacciones fraudulentas con tarjetas de crédito. Están utilizando un conjunto de datos de transacciones etiquetadas, donde cada transacción está marcada como fraudulenta o auténtica. ¿Qué papel desempeñan las etiquetas "fraudulento" y "auténtico" en esta situación? Seleccione la mejor respuesta.

- **[x] Son los resultados previstos.**
- [ ] Describen los modelos utilizados.
- [ ] Representan los algoritmos utilizados.
- [ ] Son las características de las transacciones.

> **Explicación:** En el aprendizaje supervisado, las etiquetas (labels) representan las salidas o resultados reales que el modelo intenta aprender a predecir.

---

## Pregunta 3
Una empresa de comercio electrónico quiere mejorar su sistema de recomendación de productos para ofrecer una experiencia de compra más personalizada a sus clientes. ¿Qué enfoques de Aprendizaje automático serían más eficaces para lograr este objetivo? Seleccione todo lo que corresponda.

- [ ] Desarrolle un sistema basado en reglas que recomiende productos en función de criterios predefinidos como la popularidad, la marca o el rango de precios.
- **[x] Aplicar técnicas de Aprendizaje no supervisado para segmentar a los clientes en grupos con preferencias similares, lo que permite realizar recomendaciones específicas.**
- **[x] Emplear algoritmos de Aprendizaje supervisado para predecir las preferencias de los clientes en función de su historial de navegación y sus compras anteriores.**
- **[x] Utilizar modelos de Aprendizaje de refuerzo para recompensar al sistema por las recomendaciones acertadas y penalizarlo por las sugerencias irrelevantes.**

> **Explicación:** Los tres paradigmas de Machine Learning (Supervisado, No Supervisado y Refuerzo) son métodos de aprendizaje automáticos muy eficaces para personalización. El sistema basado en reglas no es un método de aprendizaje automático, sino lógica de programación tradicional estática.

---

## Pregunta 4
Un equipo de investigación médica ha desarrollado un modelo de aprendizaje automático para ayudar en el diagnóstico precoz de una enfermedad rara. Es crucial identificar el mayor número posible de casos potenciales, aunque ello implique que algunos individuos sanos se sometan a más pruebas. ¿Qué métrica(s) derivada(s) de la matriz de confusión debería(n) priorizarse a la hora de evaluar el rendimiento del modelo? Seleccione la mejor respuesta.

- [ ] Puntuación F1
- [ ] Precisión
- **[x] Número de respuestas pertinentes** *(Recall / Sensibilidad)*
- [ ] Precisión

> **Explicación:** Cuando lo más grave es no detectar un caso positivo (es decir, evitar los falsos negativos), se debe maximizar el **Recall** (traducido en el curso como *"Número de respuestas pertinentes"*, Sensibilidad o Exhaustividad), ya que mide la proporción de casos reales detectados del total existente.

---

## Pregunta 5
Un científico de datos está desarrollando un modelo para predecir los precios de las acciones. Le preocupan especialmente los errores importantes, ya que podrían provocar pérdidas financieras significativas. ¿Qué métrica de regresión sería la más adecuada para evaluar el rendimiento de su modelo, dada su preocupación por los errores importantes? Seleccione la mejor respuesta.

- [ ] Una combinación de MAE y R-cuadrado
- [ ] R-cuadrado
- **[x] Error cuadrático medio (ECM)** *(MSE)*
- [ ] Error medio absoluto (MAE)

> **Explicación:** El Error Cuadrático Medio (ECM o MSE) eleva los errores al cuadrado antes de promediarlos. Esto penaliza severamente los errores grandes o atípicos, convirtiéndola en la métrica ideal cuando se quieren evitar fallos significativos.

---

## Pregunta 6
A un ingeniero de Aprendizaje automático se le encarga construir un modelo para predecir la pérdida de clientes. Deciden utilizar una red neuronal debido a su capacidad para aprender patrones complejos en los datos. ¿Cuál de las siguientes opciones describe mejor el papel de la función de activación en las neuronas de esta red neuronal? Seleccione la mejor respuesta.

- [ ] La función de activación calcula la diferencia entre el resultado previsto y el resultado real para cada cliente del conjunto de datos.
- [ ] La función de activación representa la fuerza o la importancia de las características individuales del cliente, como el historial de compras o las métricas de compromiso, a la hora de determinar la rotación.
- **[x] La función de activación introduce la no linealidad en la salida de la neurona, lo que permite a la red modelar intrincadas relaciones entre las características del cliente y el comportamiento de abandono.**
- [ ] La función de activación ajusta la salida de la neurona independientemente de las características de entrada, lo que permite una mayor flexibilidad a la hora de modelar el comportamiento del churn.

> **Explicación:** Sin funciones de activación, la red neuronal solo podría aproximar funciones lineales, comportándose como una simple regresión. La función de activación introduce no-linealidad, permitiendo a la red aprender fronteras de decisión y patrones muy complejos.

---

## Pregunta 7
Un científico de datos está construyendo un modelo de regresión logística para clasificar los correos electrónicos como spam o no spam. ¿Qué pasos hay que seguir en el proceso de creación del modelo? Seleccione todas las que correspondan.

- **[x] Visualización de la distribución de correos electrónicos spam y no spam para comprender los patrones subyacentes en los datos**
- **[x] Entrenamiento del algoritmo de regresión logística en una parte de los datos de correo electrónico, donde a cada característica se le asigna un peso que indica su importancia en la clasificación**
- **[x] Selección de características relevantes de los correos electrónicos, como la información del remitente, las palabras clave del asunto y el contenido del correo electrónico, para mejorar la precisión del modelo**
- **[x] Recopilación y limpieza de los datos de correo electrónico, incluido el tratamiento de los valores que faltan y la conversión de los datos categóricos en formato numérico**

> **Explicación:** Todos estos pasos forman parte del flujo de trabajo estándar de Machine Learning: (1) recolección y limpieza, (2) selección de características, (3) análisis visual/exploración de datos (EDA), y (4) entrenamiento del algoritmo.

---

## Pregunta 8
Un estudiante está aprendiendo sobre árboles de decisiones en un curso de Aprendizaje automático. Quiere entender cómo los distintos parámetros, como max_depth y min_samples_split, pueden afectar al rendimiento de un modelo de árbol de decisiones. ¿Qué sección de la documentación de Scikit-learn proporcionaría la información más relevante? Seleccione la mejor respuesta.

- **[x] Sección de la Guía del usuario sobre árboles de decisiones** *(User Guide)*
- [ ] Tutoriales sobre modelos basados en árboles
- [ ] Ejemplos de aplicación del Árbol de decisiones
- [ ] Referencia API para DecisionTreeClassifier

> **Explicación:** Mientras que la API Reference es como un diccionario de parámetros, la Guía del Usuario (User Guide) es una sección explicativa y teórica que profundiza en los conceptos de cómo estos hiperparámetros impactan el rendimiento del árbol (prevención del sobreajuste, poda, etc.).

---

## Pregunta 9
Una empresa está desarrollando un nuevo sistema de conducción autónoma, pero tiene dificultades para recopilar suficientes datos reales para entrenar eficazmente sus modelos de aprendizaje automático. Les preocupa especialmente entrenar al sistema para que pueda enfrentarse a situaciones raras y peligrosas, como circular por carreteras heladas o encontrarse con obstáculos inesperados. ¿Cómo podrían resolver este problema los datos sintéticos? Selecciona la mejor respuesta.

- [ ] Al controlar directamente las acciones del coche en pruebas reales, se garantiza su seguridad y se evitan accidentes
- [ ] Al mejorar la precisión de los sensores utilizados en el coche autoconducido, permitiéndole percibir mejor su entorno
- **[x] Generando entornos y escenarios simulados que son difíciles o inseguros de reproducir en pruebas reales**
- [ ] Sustituyendo por completo la necesidad de datos del mundo real, lo que agiliza y abarata el proceso de desarrollo

> **Explicación:** Los datos sintéticos en la conducción autónoma permiten simular de forma completamente segura escenarios de alto riesgo o infrecuentes (accidentes virtuales, clima extremo), sin poner vidas humanas en riesgo.

---

## Pregunta 10
Un ingeniero de Aprendizaje automático está desarrollando un modelo para predecir la pérdida de clientes en una empresa de telecomunicaciones. Tiene acceso a un conjunto limitado de datos reales de clientes, que incluye información confidencial como registros de llamadas e historial de facturación. ¿Cuáles son las ventajas de utilizar datos sintéticos en esta situación? Seleccione todo lo que corresponda.

- **[x] Se pueden generar datos sintéticos para aumentar el conjunto de datos reales, proporcionando ejemplos más diversos para entrenar el modelo de predicción de bajas.**
- **[x] Los datos sintéticos pueden compartirse con colaboradores externos sin infringir la normativa sobre privacidad, ya que no contienen información personal sensible.**
- [ ] Los datos sintéticos pueden utilizarse para sustituir completamente la necesidad de datos reales de los clientes, eliminando los costes y complejidades de la recopilación de datos.
- **[x] Los datos sintéticos pueden utilizarse para crear simulaciones realistas del comportamiento de los clientes, lo que permite al ingeniero probar el rendimiento del modelo en diferentes escenarios.**

> **Explicación:** Las ventajas clave de los datos sintéticos son la ampliación de datos (data augmentation), la protección de la privacidad al compartir datos no reales anonimizados, y la posibilidad de simular escenarios de prueba variados para evaluar la robustez del modelo. Sin embargo, nunca sustituyen por completo a los datos reales de los clientes.