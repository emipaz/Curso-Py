## Examen eda

## Acaba de recibir un nuevo conjunto de datos y, tras una inspección inicial, se da cuenta de que faltan valores. Un colega le sugiere que elimine inmediatamente todas las filas con datos que faltan. ¿Cómo debe proceder? Seleccione la mejor respuesta.

- Póngase de acuerdo con su colega y elimine todas las filas con valores omitidos. 
- **Identifique el patrón y la razón de los datos que faltan antes de decidir una estrategia.**
- Rellene todos los valores que faltan con ceros. 
- Ignore los valores que faltan y espere que no afecten a su análisis. 

Buen trabajo
> Correcto Comprender el patrón puede ayudar a determinar la estrategia de limpieza más adecuada.

## Estás examinando un conjunto de datos para una campaña de marketing y observas algunas incoherencias. ¿Cuáles de los siguientes son problemas de datos comunes que puede encontrar en un conjunto de datos? Seleccione todos los que corresponda. 

- **Valores perdidos.**

Buen trabajo
> Correcto Los valores que faltan son un problema habitual de los datos que hay que resolver.

- Campos de fecha con formato coherente.
- **Entradas duplicadas.**

Buen trabajo
> Correcto Las entradas duplicadas pueden sesgar su análisis y deben ser tratadas.

- **Texto inesperado en campos numéricos.**

Buen trabajo
> Correcto El texto en campos numéricos puede causar errores en el análisis y debe limpiarse.

## Está preparando un conjunto de datos para su análisis y descubre que faltan algunos valores. Decide utilizar la biblioteca de Pandas en Python para manejar estos valores perdidos. ¿Cuál de las siguientes afirmaciones es cierta sobre el manejo de valores perdidos en pandas? Seleccione todas las que correspondan. 

- **El método interpolate() puede utilizarse para estimar los valores que faltan basándose en otros valores del DataFrame.**

Buen trabajo
> Correcto El método interpolate() puede utilizarse para realizar interpolación lineal u otros tipos de interpolación para estimar valores perdidos.

- **El método dropna() elimina los valores que faltan del DataFrame.**

Buen trabajo
> Correcto El método dropna() se utiliza para eliminar filas o columnas con valores omitidos.

- **El método fillna() puede sustituir los valores que faltan por un valor especificado.**

Buen trabajo
> Correcto El método fillna() se utiliza para reemplazar los valores que faltan por un valor o método específico.

- El método isna() sustituye los valores perdidos por NaN.

## Está limpiando un conjunto de datos y descubre que muchas entradas tienen un valor de marcador de posición de "999" donde deberían estar los datos reales. Quiere cambiar todas las instancias de "999" a "NaN" para representar la información que falta correctamente. ¿Qué método de Pandas utilizaría para conseguirlo en todo el DataFrame? Seleccione la mejor respuesta.

  switch()
- subtitute()
- update()
- **replace()**

Buen trabajo
> Correcto El método replace() se utiliza para reemplazar las apariciones de un valor específico por otro valor en un DataFrame. 

## Está trabajando con un conjunto de datos que contiene una columna que representa el precio de los productos. Sin embargo, esta columna se almacena actualmente como texto e incluye algunas entradas con caracteres no numéricos. ¿Qué pasos seguiría para preparar estos datos para su conversión a un tipo de datos numérico en pandas? Seleccione todo lo que corresponda.


- Eliminación de todas las filas con valores omitidos
- **Garantizar que las columnas numéricas tengan el formato correcto**

Buen trabajo
> Correcto Asegurarse de que las columnas numéricas tienen el formato correcto es esencial para una conversión precisa del tipo de datos.

- **Comprobación de valores nulos antes de la conversión**

Buen trabajo
> Correcto Es importante comprobar si hay valores nulos antes de la conversión del tipo de datos para evitar errores.

- **Utilización de la función astype()**

Buen trabajo
> ¡Correcto! La función astype() se utiliza habitualmente para la conversión de tipos de datos en pandas.

## Ha cargado un conjunto de datos en un DataFrame de pandas y desea obtener rápidamente un resumen de sus propiedades estadísticas, como la media, la mediana y la desviación típica de cada columna numérica. ¿Qué función de Pandas le proporcionaría este resumen? Seleccione la mejor respuesta.

- summary() 
- value_counts() 
- **describe()**
- info() 

Buen trabajo
> Correcto La función describe calcula las estadísticas descriptivas de un DataFrame.

## Usted tiene un Archivo CSV llamado "datos_ventas.csv" que contiene información sobre transacciones de ventas. Desea cargar estos datos en un DataFrame de pandas para poder analizarlos. ¿Cuál de las siguientes funciones de pandas se utiliza para leer un Archivo CSV en un DataFrame? Seleccione la mejor respuesta. 


- import_csv
- **read_csv**
- load_csv
- to_csv

Buen trabajo
> Correcto La función read_csv se utiliza para leer un Archivo CSV en un DataFrame.

## Tienes un DataFrame de pandas llamado employee_data. Tu jefe te pide que corrijas una errata en uno de los nombres de los empleados. ¿Puede cambiar directamente el nombre dentro del DataFrame employee_data? Seleccione la mejor respuesta.


- Sólo puede modificar el índice, no los valores reales de los datos.
- **Sí, puede utilizar la indexación (como .loc o .iloc) para encontrar la celda específica y actualizar el nombre directamente.**
- Sólo puede añadir una nueva columna con los nombres corregidos y luego eliminar la antigua. 
- No, una vez creado un DataFrame, no se puede modificar ninguno de los datos existentes. Tendrá que crear un nuevo DataFrame.

Buen trabajo
> Correcto Los DataFrames son mutables, lo que permite la modificación directa de valores individuales.

## Estás trabajando en un proyecto de computación científica que implica cálculos numéricos extensos en grandes conjuntos de datos. ¿Qué tipo de datos de Python está optimizado específicamente para manejar estas tareas de cálculo intensivo y ofrece un rendimiento superior para las operaciones numéricas? Selecciona la mejor respuesta.

- set 
- list
- arrays 
- **NumPy arrays** 

Buen trabajo
> ¡Correcto! Las matrices NumPy están diseñadas específicamente para operaciones numéricas de alto rendimiento.

## Estás aprendiendo sobre diccionarios en Python y quieres entender las diferentes formas de crearlos. ¿Cuáles de los siguientes métodos son válidos para crear un diccionario? Selecciona todos los que correspondan.

- **Uso de llaves {}**

Buen trabajo
> Correcto Se pueden utilizar llaves para definir un diccionario.

- Uso de paréntesis ()
- Utilizando corchetes []
- **Uso de la función dict()**

Buen trabajo
> Correcto La función dict() puede utilizarse para crear un diccionario.