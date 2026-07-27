
## Está entrenando un modelo de Reconocimiento de imágenes para identificar diferentes tipos de flores. Tiene un conjunto de datos de imágenes pequeño y la precisión del modelo es baja. Quiere mejorar el rendimiento del modelo aumentando el tamaño y la diversidad de los datos de entrenamiento. ¿Qué técnica puedes utilizar para conseguirlo? Selecciona la mejor respuesta.

- Ajuste de hiperparámetros
- **Aumento de datos**
- Validación cruzada
- Ingeniería de funciones

> Correcto El aumento de datos es una técnica utilizada para generar nuevos datos de entrenamiento aplicando diversas transformaciones a los datos existentes. Esto puede ayudar a mejorar la precisión y la capacidad de generalización del modelo.

## Su equipo está desarrollando un modelo de aprendizaje automático para detectar defectos en los productos fabricados. Disponen de una cantidad razonable de datos reales, pero no cubren todos los tipos de defectos o escenarios posibles. Desea mejorar la capacidad de su modelo para generalizar y tratar defectos raros o inusuales. ¿Qué enfoque puede utilizar para complementar los datos existentes y hacer frente a este reto? Seleccione la mejor respuesta.

- Aprendizaje activo
- **Generación de datos sintéticos**
- Métodos conjuntos
- Aprendizaje no supervisado

> Correcto Los datos sintéticos pueden crear ejemplos artificiales de defectos, incluidos los que son raros o difíciles de capturar en los datos del mundo real, lo que ayuda al modelo a aprender a reconocer una gama más amplia de posibles problemas.

## Está entrenando a un chatbot para que ofrezca atención al cliente en una tienda online. Quiere asegurarse de que el chatbot entiende y responde adecuadamente a una amplia gama de consultas de los usuarios, incluso si contienen ligeros errores gramaticales o variaciones en la redacción. ¿Qué técnica de aumento de texto sería la MÁS eficaz para lograr este objetivo? Seleccione la mejor respuesta.

- Recorte de imágenes
- Traducción inversa
- Sustitución de sinónimos
- **Inserción/deleción aleatoria**

> Corregir Esta técnica introduce pequeñas variaciones en el texto, como añadir o eliminar palabras, que pueden ayudar al chatbot a ser más resistente a los errores gramaticales y a los diferentes estilos de redacción que suelen aparecer en las consultas de los usuarios.

## Está construyendo un modelo para identificar diferentes tipos de aeronaves en imágenes. Su conjunto de datos actual consiste principalmente en imágenes tomadas desde el lateral de la aeronave. Desea mejorar la capacidad del modelo para reconocer aeronaves desde distintos puntos de vista. ¿Qué técnica de aumento de imágenes sería la MÁS útil para responder a esta necesidad específica? Seleccione la mejor respuesta.

- Voltear
- **Rotación**
- Cultivo
- Ajustes de brillo

> Correcto Rotando las imágenes se crearían nuevos ejemplos de entrenamiento que mostrarían los aviones desde varios ángulos, mejorando la capacidad del modelo para reconocerlos independientemente de su orientación en la imagen.

## Está desarrollando un modelo de Aprendizaje automático para clasificar imágenes de lesiones cutáneas como benignas o malignas. Desea utilizar el aumento de datos para mejorar el rendimiento del modelo, pero le preocupa introducir sesgos o sobreajustes. ¿Cuál de las siguientes estrategias sería la MÁS importante a tener en cuenta en este caso? Seleccione la mejor respuesta.

- Céntrate principalmente en aumentos básicos como rotaciones y volteretas.
- **Mantenga transformaciones realistas y conserve la coherencia de las etiquetas.**
- Dar prioridad a los aumentos que aumentan el tamaño del conjunto de datos, independientemente de su impacto en las imágenes individuales.
- Aplique una amplia gama de aumentos con la máxima intensidad.

> Correcto En imagen médica, es crucial que los aumentos reflejen variaciones realistas en el aspecto de la lesión y no alteren el verdadero diagnóstico (etiqueta). Las transformaciones poco realistas podrían inducir a error al modelo, y el cambio de etiquetas haría que los datos fueran incorrectos.