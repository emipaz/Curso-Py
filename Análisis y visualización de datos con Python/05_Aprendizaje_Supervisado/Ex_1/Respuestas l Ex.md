# Escenario

Usted es un desarrollador de Python que trabaja en un proyecto de Aprendizaje automático para predecir los resultados de los pacientes basándose en sus registros médicos utilizando el conjunto de datos de diabetes de los indios Pima, que contiene información valiosa sobre la salud de los pacientes. Sin embargo, descubre que el conjunto de datos contiene muchos más registros de personas sin diabetes que de personas con diabetes. Este desequilibrio puede dificultar que su modelo identifique con precisión a los pacientes con diabetes, lo que podría repercutir negativamente en su atención sanitaria.

Se le ha pedido que resuelva este desequilibrio mediante la generación de datos sintéticos para equilibrar el conjunto de datos. SMOTE (Synthetic Minority Over-sampling Technique) es una técnica que puede ayudar creando ejemplos sintéticos de la clase minoritaria (pacientes con diabetes) a partir de los ya existentes.
 
# Objetivo

El objetivo de esta actividad es dotarle de las habilidades necesarias para manejar conjuntos de datos desequilibrados en entornos sanitarios, concretamente para predecir la diabetes. Aprenderá a identificar y comprender el desequilibrio de clases, un reto común en los datos médicos donde una clase (por ejemplo, pacientes con diabetes) está significativamente infrarrepresentada en comparación con otra (por ejemplo, pacientes sin diabetes).

Para abordar este desequilibrio, utilizará SMOTE (Synthetic Minority Over-sampling Technique), un potente método de generación de datos sintéticos para equilibrar las clases. Por último, utilizará SMOTE para mejorar el rendimiento de un modelo de regresión logística para predecir la diabetes, demostrando el impacto de abordar el desequilibrio de clases en problemas sanitarios del mundo real.

# Instrucciones

Descargue el archivo Activity_Syntheticdatageneration.zip, guárdelo en el escritorio de su ordenador y extráigalo a una carpeta de fácil acceso. 

Abra la carpeta, que contiene los siguientes archivos

un archivo de Notebook de Jupyter llamado "Project_Synthetic Data Generation.ipynb".

un conjunto de datos de valores separados por comas (CSV) llamado "diabetes.csv".

## Paso 1: Importación de bibliotecas 

Prepare el escenario para su análisis importando todas las bibliotecas necesarias. El código para importar las bibliotecas requeridas (pandas, Matplotlib, componentes de Scikit-learn y SMOTE de imbalanced-learn) ya está disponible. 

Ejecute la celda.

## Paso 2: Cargar el conjunto de datos en un Dataframe pandas

A continuación, cargue el conjunto de datos de diabetes de los indios Pima en un DataFrame de pandas. Este conjunto de datos del mundo real es un valioso recurso para explorar los factores asociados a la diabetes en pacientes femeninas de ascendencia india Pima. Incluye varios indicadores de salud como los niveles de glucosa, la presión arterial, el IMC, etc., junto con la crucial columna "Resultado" que indica si la paciente tiene diabetes (1) o no (0).

Importe pandas con el alias pd.

Utilice .read_csv() para cargar el archivo 'diabetes.csv' en un DataFrame llamado diabetes_data.

Ejecute la celda. No habrá salida.

## Paso 3: Comprobar las dimensiones de los datos 

Ahora que tiene sus datos cargados, debería tener una visión rápida de su tamaño. Se le ha proporcionado el código para determinar el número de filas y columnas de su DataFrame utilizando el atributo .shape.

Ejecute la celda para ver el número de filas y columnas de sus datos. El conjunto de datos de muestra debería tener 768 filas y 9 columnas.

## Paso 4: Vista previa de los datos 

Como se ha observado en el paso anterior, el conjunto de datos tiene un gran número de filas. En lugar de verlas todas, echará un vistazo a su DataFrame utilizando la función head(), que mostrará las cinco primeras filas, permitiéndole ver los nombres de las columnas y los tipos de valores que contienen. Este primer vistazo le ayudará a familiarizarse con la estructura y el contenido de los datos.

Utilice el método head() para previsualizar el DataFrame diabetes_data.

Ejecute la celda y observe la salida para familiarizarse con sus datos.

## Paso 5: Obtener un resumen de los datos

En este paso, examinará la estructura de los datos con más detalle utilizando otra función, info(). Esta función proporciona un resumen conciso de cada columna, incluyendo su nombre y el tipo de datos que contiene (por ejemplo, números, texto). Esta información es crucial para comprender cómo trabajar con cada columna de forma eficaz y detectar cualquier posible problema de calidad de los datos.

Utilice el método info() para ver información detallada sobre el DataFrame diabetes_data.

Ejecute la celda para ver la información detallada sobre las columnas de su DataFrame.

## Paso 6: Comprobar si faltan valores

Ahora que tiene una idea más clara de la estructura de sus datos, debe comprobar si falta algún valor en su conjunto de datos. Los valores que faltan pueden afectar a su análisis y modelado, por lo que es crucial identificarlos desde el principio. Utilizará la combinación isnull().sum() para comprobar sistemáticamente si faltan valores en cada columna y proporcionar un recuento de cuántos hay en cada una.

Utilice .isnull() y .sum() en el DataFrame diabetes_data para comprobar si faltan valores en una sola línea de código.

Ejecute la celda para ver si alguna columna tiene valores faltantes.

Si la salida muestra ceros para todas las columnas, significa que su conjunto de datos está completo y no tiene valores perdidos. Si ve recuentos distintos de cero, indica la presencia de datos que faltan, que es posible que tenga que abordar en pasos posteriores.

## Paso 7: Análisis de la distribución de clases en busca de desequilibrios

Ahora que los datos están limpios y organizados, puede analizar la distribución de clases en busca de desequilibrios. Por ejemplo, puede comprobar cuántos casos pertenecen a cada clase (diabéticos o no diabéticos) en su conjunto de datos. Esto es crucial porque un desequilibrio significativo entre las clases puede obstaculizar la capacidad de su modelo para aprender eficazmente, lo que podría dar lugar a predicciones sesgadas. 

Para ello, se centrará en la columna "Resultado", que es la variable objetivo, ya que indica directamente si un paciente tiene diabetes o no. El código para contar las ocurrencias de cada clase se proporciona parcialmente: class_counts = diabetes_data['Outcome'].

Añada el método .value_counts() al final del código anterior para calcular cuántas veces aparece cada valor único (0 y 1) en la columna 'Outcome'.

El código para visualizar el gráfico te ha sido proporcionado.

Utilice plt.title() para dar a su gráfico este título significativo: "Distribución de Clases".

Utilice plt.show() y ejecute la celda para visualizar el gráfico.

## Paso 8: Separar características y objetivo 

COMO puede ver en el gráfico, el conjunto de datos está desequilibrado, con más casos negativos (Resultado = 0) que casos positivos (Resultado = 1). Este desequilibrio puede dar lugar a un modelo sesgado. Por ejemplo, dado que utilizará un modelo de regresión logística para predecir si un paciente tiene diabetes o no, el desequilibrio puede afectar negativamente a su rendimiento predictivo a la hora de identificar con precisión a los pacientes con diabetes.

Para asegurarse de que el modelo de Regresión logística aprende eficazmente tanto  de las clases mayoritarias (no diabéticos) como de las minoritarias (diabéticos), utilizará una técnica llamada SMOTE (Synthetic Minority Over-sampling Technique) en los próximos pasos. 

Sin embargo, primero necesita preparar y preprocesar sus datos para SMOTE dividiendo los datos en conjuntos de características (entrenamiento) y objetivo (prueba) y luego estandarizar las características (escalado de características). 

En este paso, comenzará el preprocesamiento de datos separando las características (la información que utilizará para hacer predicciones) de la variable objetivo (lo que desea predecir). Piense en las características como pistas y en el objetivo como la respuesta que intenta encontrar. En su conjunto de datos, la columna 'Outcome' le indica si un paciente tiene diabetes o no. Esto es lo que quieres predecir, así que es tu variable objetivo.

El código para crear un nuevo DataFrame llamado x utilizando la función drop() que contiene todas las columnas de diabetes_data excepto la columna 'Outcome' se ha proporcionado para usted. Estas columnas restantes son sus características - los indicadores de salud que utilizará para hacer predicciones.

Con sus características listas, es hora de definir su variable objetivo:

Utilice los corchetes [] para asignar la columna 'Outcome' del DataFrame diabetes_data a una variable y, que representa la variable objetivo.

El código para dividir sus características (x) y la variable objetivo (y) en conjuntos de entrenamiento y prueba utilizando train_test_split se ha proporcionado para usted. Esto asegura que su modelo aprende de una parte de los datos (conjunto de entrenamiento) y se evalúa en una parte separada, no vista (conjunto de pruebas), evitando el sobreajuste y proporcionando una evaluación más realista de su rendimiento.

Ejecute la célula. No habrá salida.

## Paso 9: Estandarizar características (escalado de características)

Para finalizar el preprocesamiento de los datos, tendrá que asegurarse de que todas sus características (indicadores de salud) tienen una escala similar. Esto es importante porque algunas características pueden tener valores mucho mayores que otras (por ejemplo, los niveles de glucosa comparados con la función de pedigrí de la diabetes). Este es el propósito del escalado de características, poner todas las características en una escala similar, evitando que una característica domine el proceso de aprendizaje del modelo. Es como asegurarse de que todo el mundo tiene la misma voz en una discusión de grupo.

El código para estandarizar las características utilizando StandardScaler se ha proporcionado para usted. Tenga en cuenta que se ha aplicado al conjunto de entrenamiento y al conjunto de pruebas. Esto es importante porque quiere evaluar el modelo en datos que han sido preprocesados de la misma manera que los datos de entrenamiento.

Ejecute la celda. No habrá salida.

## Paso 10. Aplique SMOTE a los datos de entrenamiento: Aplicar SMOTE a los Datos de entrenamiento 

Ahora tiene datos estandarizados con todas las características en una escala similar En este paso, finalmente utilizará estos datos para entrenar y evaluar su modelo de aprendizaje automático, lo que potencialmente conducirá a un rendimiento mejorado y a predicciones más justas. 

Utilizará SMOTE para ayudar a resolver el desequilibrio de clases anterior, que mostraba que había muchos más pacientes no diabéticos que diabéticos en el conjunto de datos. SMOTE (Synthetic Minority Over-sampling Technique) genera nuevos ejemplos sintéticos de la clase minoritaria (pacientes diabéticos) a partir de los ya existentes. Para ello, analiza cuidadosamente las características de los pacientes diabéticos existentes y, a continuación, crea nuevos ejemplos similares pero ligeramente diferentes. Esto ayuda a equilibrar el conjunto de datos, dando a nuestro modelo una oportunidad más justa de aprender los patrones asociados a la diabetes.

Para empezar a utilizar SMOTE, primero deberá aplicarlo a sus datos de entrenamiento para equilibrar la distribución de clases. Esto implica ajustar SMOTE a sus datos de entrenamiento escalados para aprender los patrones de las clases mayoritaria y minoritaria. A continuación, SMOTE generará muestras sintéticas para la clase minoritaria, colocándolas estratégicamente en el espacio de características para crear un conjunto de datos más equilibrado.

La primera línea de código que se le ha proporcionado importa la clase SMOTE del módulo imblearn.over_sampling, crea un objeto smote con un random_state de 42 para su reproducibilidad.

La siguiente línea de código para aplicar SMOTE a los datos de entrenamiento se proporciona parcialmente para usted: x_train_smote, y_train_smote = smote.

Complete el código añadiendo .fit_resample(x_train_scaled, y_train) al final de la línea parcialmente proporcionada anteriormente. Esto instruirá a SMOTE para que ajuste (es decir, aprenda los patrones de sus datos de entrenamiento x_train_scaled y y_train) y remuestree (es decir, genere muestras sintéticas para la clase minoritaria para equilibrar el conjunto de datos).

Ejecute la celda. No habrá salida.

## Paso 11: Visualización de la distribución de clases después de SMOTE

Ha aplicado con éxito SMOTE a sus Datos de entrenamiento. En este paso, finalmente podrá ver su impacto comparando la distribución de clases antes y después de SMOTE, tanto numérica como visualmente. Esto resaltará cómo SMOTE ha incrementado el número de ejemplos para la clase minoritaria (pacientes diabéticos).

El código proporcionado muestra la distribución de clases antes y después de aplicar SMOTE y, a continuación, visualiza la distribución equilibrada mediante un gráfico de recuento. Esto le permite observar cómo SMOTE ha abordado eficazmente el desequilibrio de clases generando muestras sintéticas para la clase minoritaria (pacientes con diabetes).

Ejecute la celda para visualizar el gráfico. 

## Paso 12: Inicializar los modelos de Regresión logística 

La visualización muestra que SMOTE ha equilibrado con éxito sus datos de entrenamiento. Ahora tiene el mismo número de ejemplos para las clases 'sin diabetes' (0) y 'diabetes' (1). Con este conjunto de datos equilibrado, es hora de entrenar el modelo de regresión logística, que aprenderá de ambas clases de forma más eficaz, reduciendo el Sesgo del observador hacia la clase mayoritaria que observamos anteriormente.

La Regresión logística es un algoritmo popular para tareas de clasificación como predecir si un paciente tiene diabetes o no. Sopesa la evidencia de diferentes factores (indicadores de salud) y luego calcula la probabilidad de que ocurra un evento (en este caso, que el paciente tenga diabetes) y clasifica al paciente en función de si esta probabilidad está por encima o por debajo de un determinado umbral.

En este paso, se inicializarán los modelos de regresión logística, uno que se entrenará con los datos originales desequilibrados y otro que se entrenará con los datos equilibrados generados por SMOTE.

La primera línea de código que inicializa el primer modelo original se ha proporcionado para usted.

La segunda línea de código que inicializa los datos equilibrados de SMOTE está parcialmente a tu disposición. Para completar esta línea de código:

Añada LogisticRegression(solver='liblinear', max_iter=200) a model_smote =.

Ejecute la celda. No habrá salida.

## Paso 13: Entrenar los modelos

Con sus modelos inicializados, ¡es hora de entrenar sus modelos de regresión logística! Utilizará el método de ajuste para enseñar a cada modelo los patrones y relaciones de sus respectivos conjuntos de datos. A continuación, comparará su rendimiento para ver cómo afecta SMOTE a su capacidad para predecir la diabetes con precisión, especialmente para la clase minoritaria (pacientes con diabetes).

Se le ha proporcionado la primera línea de código que entrena el modelo en el conjunto de datos original.

La segunda línea de código que entrena el segundo modelo en los datos equilibrados de SMOTE se ha proporcionado parcialmente para usted. Para completar esta línea de código:

Añada .fit(x_train_smote, y_train_smote) a model_smote.

Ejecute la celda. 

## Paso 14: Realice predicciones y prepárese para evaluar los modelos 

El código proporcionado pone a prueba sus modelos entrenados realizando predicciones en el conjunto de prueba no visto. Calcula no sólo las etiquetas predichas (diabéticas o no) sino también la probabilidad de cada predicción. A continuación, define una práctica función evaluate_model para evaluar el rendimiento de cada modelo utilizando métricas clave como exactitud, precisión, recuperación y ROC-AUC. Esta función también genera un informe de clasificación detallado, que proporciona una visión global de lo bien que cada modelo está clasificando tanto a los pacientes diabéticos como a los no diabéticos.

Ejecute la celda. No habrá salida.

## Paso 15: Evaluar el modelo en los datos originales

En este paso, verá cómo funciona el modelo que ha entrenado en los datos originales desequilibrados.

El código proporcionado utilizará la función evaluate_model que definió anteriormente para calcular e imprimir varias métricas de rendimiento para este modelo. Le dará una idea de lo bien que el modelo predice la diabetes en el conjunto de datos desequilibrados, sirviendo como línea de base para la comparación con el modelo entrenado en los datos equilibrados de SMOTE.

Ejecute la celda. 

## Paso 16: Evalúe el modelo con datos aumentados por SMOTE

También querrá ver cómo funciona el modelo que ha entrenado en los datos equilibrados utilizando SMOTE. 

El código proporcionado utilizará de nuevo la función evaluate_model para calcular e imprimir las métricas de rendimiento de este modelo. Esta evaluación revelará la eficacia con la que SMOTE ha abordado el desequilibrio de clases y ha mejorado la capacidad del modelo para predecir la diabetes, especialmente para la clase minoritaria (pacientes con diabetes).

Ejecute la celda. 

## Paso 17: Visualice y compare el rendimiento del modelo

Aunque tenga dos evaluaciones en forma numérica, será útil visualizar el rendimiento de ambos modelos utilizando curvas ROC para que sea fácil comunicar estos datos a otras personas. Las curvas ROC representan la tasa de positivos verdaderos (sensibilidad) frente a la tasa de falsos positivos (1-especificidad) para distintos umbrales de clasificación. Le ayudan a comprender lo bien que cada modelo distingue entre las dos clases (diabético y no diabético) a través de varios niveles de sensibilidad y especificidad. 

El código proporcionado genera curvas ROC tanto para el modelo original como para el mejorado con SMOTE, permitiéndole comparar visualmente su rendimiento y evaluar el impacto de SMOTE en la capacidad del modelo para discriminar entre las clases.

Ejecute la celda para visualizar el gráfico. 

Las curvas ROC ilustran visualmente la capacidad de diagnóstico de sus modelos. Cuanto más cerca esté la curva de la esquina superior izquierda, mayor será su área bajo la curva (AUC) y mejor será el rendimiento general del modelo. Un AUC más alto significa que el modelo es más eficaz a la hora de distinguir entre pacientes con y sin diabetes.

La curva azul, que representa el modelo entrenado en el conjunto de datos desequilibrados, muestra un rendimiento decente, mejor que la adivinación aleatoria (la línea diagonal). Sin embargo, podría mejorarse su capacidad para identificar con precisión a los pacientes diabéticos.

La curva naranja, generada a partir del modelo entrenado en el conjunto de datos equilibrado tras aplicar SMOTE, está más cerca de la esquina superior izquierda. Esto sugiere que equilibrar el conjunto de datos mejoró la capacidad del modelo para clasificar correctamente los casos positivos (pacientes con diabetes).

Resumen del proyecto: Generación de datos sintéticos

¡Enhorabuena! En este proyecto, ha utilizado con éxito SMOTE para abordar el desequilibrio de clases en el conjunto de datos de diabetes de los indios Pima. Al generar muestras sintéticas de la clase minoritaria (pacientes con diabetes), SMOTE mejoró el rendimiento de su modelo de regresión logística. El análisis de la curva ROC demostró visualmente esta mejora, mostrando una mayor tasa de positivos verdaderos (sensibilidad) para el modelo entrenado en el conjunto de datos equilibrado. Esto pone de relieve el valor de SMOTE para mejorar la precisión de los diagnósticos médicos, especialmente en escenarios críticos en los que la identificación de casos positivos es crucial. Recuerde que, aunque SMOTE es una herramienta potente, es esencial tener en cuenta las posibles contrapartidas, como el aumento de falsos positivos, en las aplicaciones sanitarias del mundo real. Gracias a este proyecto, habrá adquirido experiencia práctica en el manejo de datos desequilibrados y en la evaluación del rendimiento de los modelos, lo que le dotará de valiosas habilidades para construir modelos de aprendizaje automático eficaces y justos en el ámbito sanitario.

1.
Pregunta 1
### ¿Cuál es el objetivo de utilizar datos sintéticos en el contexto de este cuaderno? Selecciona la mejor respuesta.

- **Crear una representación más equilibrada de la clase minoritaria, mejorando la capacidad del modelo para predecir esa clase.**
- Para crear una representación más equilibrada de todas las clases, mejorando la precisión global del modelo.
- Reducir el número de características del conjunto de datos, lo que facilita el entrenamiento del modelo.
- Mejorar la precisión global del modelo, independientemente del desequilibrio de clases.

Buen trabajo
> Correcto Esto capta con precisión el objetivo principal de utilizar datos sintéticos en este contexto.

2.
Pregunta 2
## En el contexto del Aprendizaje automático, ¿cuál es la principal preocupación asociada a los conjuntos de datos desequilibrados, como se destaca en este Notebook? Seleccione la mejor respuesta.

- Los conjuntos de datos desequilibrados dificultan el logro de una gran precisión, incluso con modelos bien afinados.
- Los conjuntos de datos desequilibrados requieren más recursos informáticos para entrenar los modelos con eficacia.
- Los conjuntos de datos desequilibrados conducen a modelos demasiado complejos y propensos al sobreajuste.
- **Los conjuntos de datos desequilibrados pueden dar lugar a modelos sesgados hacia la clase mayoritaria, lo que conduce a un rendimiento deficiente en la clase minoritaria.**

Buen trabajo
> Correcto Esto capta con precisión el problema central de los conjuntos de datos desequilibrados, en los que el modelo puede tener dificultades para aprender los patrones de la clase infrarrepresentada.

3.
Pregunta 3
## Al utilizar SMOTE para generar datos sintéticos en este proyecto, ¿cuál de las siguientes consideraciones sobre privacidad es MÁS importante? Seleccione la mejor respuesta.


- **Verificación de que los datos sintéticos mantienen la privacidad de los datos originales del paciente.**
- Garantizar que los datos sintéticos puedan rastrearse fácilmente hasta los registros originales de los pacientes.
- Compartir libremente los datos sintéticos con terceras organizaciones.
- Publicar los datos sintéticos en línea tal cual, sin anonimizar los identificadores sensibles de los pacientes.

Buen trabajo
> Correcto Esto capta con precisión la esencia de separar las características y el objetivo, permitiendo que el modelo aprenda la relación entre ellos.

4.
Pregunta 4
## En el contexto de este Notebook, ¿cómo influyó el uso de SMOTE para equilibrar el conjunto de datos en la precisión del modelo de regresión logística? Seleccione la mejor respuesta.

- SMOTE disminuyó significativamente la precisión del modelo.
- SMOTE no influyó en la precisión del modelo.
- **SMOTE mejoró la precisión del modelo.**
- SMOTE disminuyó ligeramente la precisión del modelo.

Buen trabajo
> Correcto Sin embargo, es crucial revisar los valores específicos de precisión presentados en el cuaderno.

5.
Pregunta 5
## En el contexto de este cuaderno, ¿cuál de las siguientes opciones describe mejor la regresión logística? Seleccione la mejor respuesta.


- **Algoritmo de clasificación que predice la probabilidad de un resultado binario, como si un paciente tiene diabetes o no.**
- Algoritmo de agrupación que agrupa a pacientes similares en función de sus indicadores de salud.
- Algoritmo de Aprendizaje profundo que utiliza redes neuronales para aprender patrones complejos en los datos.
- Algoritmo de Aprendizaje automático utilizado para predecir valores numéricos continuos, como el nivel de azúcar en sangre de un paciente.

Buen trabajo
> Correcto Describe correctamente el papel de la Regresión logística en la predicción de resultados binarios a partir de características de entrada.

6.
Pregunta 6
## A la hora de generar y utilizar datos sintéticos en aplicaciones sanitarias, como la predicción de la diabetes que se analiza en este cuaderno, ¿cuál de las siguientes consideraciones éticas es MÁS crucial?

- Evaluar cuidadosamente los posibles sesgos y consecuencias imprevistas que los datos sintéticos podrían introducir en el modelo y sus predicciones.

- Dar prioridad a la generación de un gran volumen de datos sintéticos, aunque ello comprometa la calidad y representatividad de los datos.

- Centrarse únicamente en mejorar los parámetros de rendimiento del modelo, aunque ello signifique descuidar el posible impacto social de su despliegue.

- **Garantizar que los datos sintéticos reproduzcan a la perfección los datos originales, aunque ello implique incluir información sensible del paciente.**

Buen trabajo
> Correcto Se trata de una consideración ética fundamental. Los datos sintéticos, aunque beneficiosos, pueden introducir inadvertidamente sesgos o patrones inesperados que afecten a la imparcialidad y precisión del modelo.

7.
Pregunta 7
## A la hora de implantar un modelo de aprendizaje automático basado en datos sanitarios sintéticos en un entorno clínico real, ¿cuál de las siguientes consideraciones éticas es de vital importancia? Seleccione la mejor respuesta.


- Compartir abiertamente con el público las técnicas y parámetros de generación de datos sintéticos, independientemente de posibles usos indebidos o problemas de privacidad.
- **Validar minuciosamente el rendimiento del modelo con datos diversos y representativos del mundo real para minimizar posibles sesgos y garantizar resultados equitativos para todas las poblaciones de pacientes.**
- Maximizar los beneficios económicos de la implantación del modelo, aunque ello suponga limitar el acceso a la tecnología de las comunidades desatendidas o marginadas.
- Garantizar que el modelo alcance la mayor precisión posible, aunque ello suponga sacrificar la transparencia y la explicabilidad.

Buen trabajo
Correcto Se trata de una consideración ética fundamental. Garantizar que el modelo se generalice bien a diversas poblaciones de pacientes y no perpetúe los prejuicios existentes es primordial en las aplicaciones sanitarias.

8.
Pregunta 8
## ¿Qué representa visualmente la curva ROC en el contexto de la evaluación de los modelos de este cuaderno? Seleccione la mejor respuesta.


- La distribución de probabilidades previstas para las clases positiva y negativa.
- El compromiso entre complejidad y precisión del modelo.
- **El equilibrio entre la tasa de positivos verdaderos (sensibilidad) y la tasa de falsos positivos (1-especificidad) con diferentes umbrales de clasificación.**
- Relación entre el número de características y el rendimiento del modelo.

Buen trabajo
> Correcto Esto describe con exactitud lo que representa una curva ROC, que muestra la capacidad del modelo para distinguir entre clases en varios umbrales.

9.
Pregunta 9
## Basándose en el gráfico de comparación de la curva ROC, ¿cuál de las siguientes afirmaciones es la interpretación MÁS exacta? Seleccione la mejor respuesta.


- El modelo entrenado con los datos originales tiene una especificidad (tasa de verdaderos negativos) mayor que el modelo SMOTE, lo que sugiere que es mejor para identificar correctamente a los pacientes no diabéticos.
- Ambos modelos presentan un rendimiento idéntico, lo que indica que el SMOTE no influyó en la capacidad del modelo para discriminar entre pacientes diabéticos y no diabéticos.
- **El modelo entrenado con los datos equilibrados de SMOTE demuestra una mayor sensibilidad (tasa de verdaderos positivos) en comparación con el modelo original, lo que indica una mejor identificación de los pacientes con diabetes.**
- El modelo entrenado con los datos originales desequilibrados obtiene resultados significativamente mejores que el modelo entrenado con los datos equilibrados de SMOTE en términos de clasificación general.

Buen trabajo
> Correcto Esta es la clave de la comparación de las curvas ROC. La curva del modelo SMOTE está más cerca de la esquina superior izquierda, lo que significa una mayor sensibilidad.