# pandas: Tu centro neurálgico de manipulación de datos

## Acaba de cargar un conjunto de datos en un DataFrame de pandas llamado df. Desea obtener una visión rápida del DataFrame, incluyendo los nombres de las columnas, los tipos de datos de cada columna y el número de valores no nulos. ¿Qué función de Pandas utilizarías para este propósito? Seleccione la mejor respuesta.

- shape
- describe()
- **info()**
- head()

Buen trabajo
> Correcto La función info() proporciona un resumen conciso del DataFrame, incluidos los nombres de las columnas, los tipos de datos y los valores no nulos.

## Usted tiene dos Pandas DataFrames, df1 y df2, que contienen información relacionada sobre los clientes. Necesita combinar estos DataFrames en un único DataFrame basado en una columna común llamada 'CustomerID'. ¿Qué función de Pandas utilizarías para esta operación? Seleccione la mejor respuesta.

- concat()
- **sort_values()**
- groupby()
- merge()

Buen trabajo
> Correcto La función merge() es la herramienta adecuada para combinar DataFrames basados en una o más columnas o índices comunes, que es exactamente lo que necesita hacer en este escenario utilizando la columna 'CustomerID'.

## Estás trabajando con un DataFrame en Pandas y necesitas realizar algunas operaciones básicas sobre él. ¿Cuál de las siguientes operaciones puede realizar utilizando la indexación y segmentación básica de DataFrame? Seleccione todo lo que corresponda.


- **Acceso a un valor específico mediante etiquetas de filas y columnas**

Buen trabajo
> Correcto Puede utilizar loc o at para acceder a valores específicos basados en etiquetas.

- **Modificación de los valores de determinadas celdas**

Buen trabajo
> Correcto Puede cambiar los valores de celdas específicas utilizando .loc o .iloc .

- **Selección de un rango de filas y columnas**

Buen trabajo
> Correcto Tanto iloc como loc pueden utilizarse para seleccionar rangos de filas y columnas.

Eliminación de filas en función de una condición

## Usted tiene un DataFrame que contiene datos de clientes, incluyendo sus nombres, edades e historial de compras. Quiere ordenar este DataFrame alfabéticamente por los apellidos de los clientes. ¿Qué método de Pandas utilizaría para realizar esta ordenación? Seleccione la mejor respuesta.

- sort_index()
- sort_values()**
- groupby()
- concat()

Buen trabajo
> ¡Correcto! El método sort_values() se utiliza para ordenar un DataFrame por sus columnas en Pandas.

## Está trabajando con un conjunto de datos que contiene datos de ventas de una tienda minorista. Quiere calcular las ventas totales de cada categoría de producto. ¿Cuál de las siguientes funciones de Pandas puede utilizar para realizar esta agregación? Seleccione todas las que correspondan.

- concat()
- **groupby()**

Buen trabajo
> Correcto La función groupby() se utiliza para agrupar datos y aplicar funciones de agregación.

- fusionar()
- **agregate() agg()**

Buen trabajo
> Correcto La función aggregate() se utiliza para aplicar funciones de agregación sobre datos agrupados.

## Estás trabajando con un DataFrame en Pandas y necesitas extraer las tres primeras filas para su posterior análisis. ¿Cómo lo conseguiría utilizando el método iloc, que se basa en la indexación de enteros? Seleccione la mejor respuesta.

- **df.iloc[:3]**
- df.iloc[0:2]
- df.iloc[1:3]
- df.iloc[3]

Buen trabajo
> Correcto! df.iloc[:3] selecciona las tres primeras filas utilizando indexación basada en posiciones enteras.

## Trabaja con un gran conjunto de datos y necesita realizar operaciones complejas como filtrar, ordenar y agregar datos. Quiere elegir una herramienta que esté específicamente diseñada para la manipulación y el análisis eficiente de datos. ¿Por qué elegirías Pandas en lugar de las listas y diccionarios tradicionales de Python para esta tarea? Seleccione la mejor respuesta.

- Genera automáticamente visualizaciones.
- **Es más rápido y eficaz para las operaciones de datos a gran escala.**
- Su sintaxis es más sencilla.
- Es la única biblioteca disponible para la manipulación de datos en Python.

Buen trabajo
> Correcto! Pandas está optimizado para operaciones de datos a gran escala, por lo que es más rápido y eficiente que las listas y diccionarios tradicionales de Python.

## Está trabajando con un gran conjunto de datos en Pandas y desea inspeccionar rápidamente las primeras filas para obtener una comprensión inicial de su estructura y contenido. ¿Qué función utilizarías para mostrar estas filas? Seleccione la mejor respuesta.

- **head()**
- primero()
- info()
- describir()

Buen trabajo
> Correcto La función head() se utiliza para mostrar las primeras filas de un DataFrame.