# Preguntas EDA

## Estás trabajando con un conjunto de datos que tiene diversos tipos de datos y formatos. ¿Cuáles de las siguientes son técnicas para garantizar la coherencia de los datos y la facilidad de uso para el análisis? Seleccione todas las que corresponda.


- **Conversión de tipos de datos**

Buen trabajo
> Correcto La conversión de tipos de datos garantiza la coherencia de los datos transformándolos en formatos adecuados.

- Ignorar los valores que faltan
- **Imputación**

Buen trabajo
> Correcto La imputación es un método habitual para sustituir los valores que faltan por valores estimados o calculados.

- **Detección de valores atípicos**

Buen trabajo
> Correcto La detección de valores atípicos consiste en identificar los valores extremos que se desvían del patrón general de los datos.

## ¿Cuál es un uso común del Análisis exploratorio de datos (EDA)? Seleccione todo lo que corresponda.

- **Creación de visualizaciones**

Buen trabajo
> Correcto Las visualizaciones como los gráficos se utilizan con frecuencia en EDA.

- **Generar agregaciones**

Buen trabajo
> Correcto Los gráficos de dispersión suelen utilizarse para identificar relaciones entre variables continuas.

- Recopilación de datos
- **Creación de estadísticas descriptivas**

Buen trabajo
> Correcto Las estadísticas descriptivas como la media, la varianza y la desviación típica ayudan a sacar conclusiones basadas en los datos.

## Está trabajando con un conjunto de datos que contiene algunos valores perdidos. Decide que, para su análisis específico, es mejor eliminar cualquier fila que contenga valores perdidos para evitar posibles sesgos o errores en sus cálculos. ¿Qué método de Pandas utilizaría para conseguirlo? Seleccione la mejor respuesta.

- fillna()
- notnull()
- **dropna()**
- isnull()

Buen trabajo
> Correcto El método dropna() se utiliza para eliminar valores perdidos de un DataFrame.

## Estás analizando los datos de un experimento científico y observas varios valores atípicos. ¿Qué es un valor atípico en un conjunto de datos? Selecciona la mejor respuesta.

- Un punto de datos que siempre es incorrecto
- Punto de datos que se encuentra dentro del intervalo intercuartílico
- **Punto de datos que difiere significativamente de otras observaciones**
- Punto de datos que coincide exactamente con la media del conjunto de datos

Buen trabajo
> Correcto Los valores atípicos son puntos de datos que difieren significativamente de otras observaciones del conjunto de datos.

## Está analizando los datos de ventas de una tienda y se da cuenta de que algunos registros de compra de clientes aparecen varias veces en el conjunto de datos. Se da cuenta de que estos registros duplicados podrían sesgar su análisis y llevar a conclusiones inexactas sobre las tendencias de ventas y el comportamiento de los clientes. ¿Cuál es la razón principal para eliminar estos registros duplicados durante el proceso de limpieza de datos? Seleccione la mejor respuesta.

- **Para evitar distorsionar los resultados de los análisis.**
- Para aumentar la velocidad de procesamiento.
- Para ahorrar espacio de almacenamiento.
- Para mantener la integridad de los datos.

Buen trabajo
> Correcto Los registros duplicados pueden distorsionar los resultados de los análisis inflando artificialmente las cifras de ventas o falseando las pautas de compra de los clientes.

## Está trabajando con un conjunto de datos que contiene información de clientes, incluidos nombres, direcciones e historial de compras. Descubre que algunos registros de clientes se han introducido varias veces sin querer, creando entradas redundantes. ¿Cuál de las siguientes técnicas sería más eficaz para identificar y tratar estas entradas repetidas a fin de garantizar la precisión de los análisis y los informes? Seleccione todas las que correspondan.

- Ordenar el conjunto de datos para encontrar duplicados
- **Marcar duplicados con una nueva columna**

Buen trabajo
> Correcto Marcar los duplicados con una nueva columna puede ayudar a identificarlos y gestionarlos posteriormente.

- **Quitar duplicados con .drop_duplicates()**

Buen trabajo
> Correcto El método .drop_duplicates() se utiliza habitualmente para eliminar valores duplicados de un conjunto de datos.

- Utilización del método .replace() para tratar los duplicados

## Está trabajando con un conjunto de datos de información sobre clientes y se da cuenta de que faltan algunas direcciones. Quiere asegurarse de que sus análisis y campañas de marketing no se vean afectados negativamente por esta información incompleta. ¿Cuáles de las siguientes son razones potenciales para que falten estas direcciones? Seleccione todas las que correspondan.

- **Usuarios que se saltan una pregunta**

Buen trabajo
> Correcto Los usuarios pueden saltarse una pregunta, intencionadamente o no, durante el proceso de recogida de datos.

- Tipos de datos incorrectos
- **Errores en la introducción de datos**

Buen trabajo
> Correcto El error humano desempeña un papel importante en la falta de datos.

- Elevada varianza de los datos