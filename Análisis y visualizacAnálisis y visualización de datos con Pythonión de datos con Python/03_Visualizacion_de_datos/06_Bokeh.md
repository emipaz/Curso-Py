# Personalización de Visualizaciones con Bokeh

## Resumen

**Bokeh** es una biblioteca de Python diseñada para crear visualizaciones de datos **interactivas** que pueden ejecutarse directamente en un navegador web. Además de generar gráficos, permite personalizarlos mediante colores, estilos, anotaciones y herramientas interactivas, mejorando la comunicación de los datos y la experiencia del usuario.

La capacidad de adaptar una visualización a las necesidades de la audiencia convierte a Bokeh en una excelente herramienta para el **Data Storytelling**, facilitando la exploración y comprensión de la información.

---

# Objetivos de aprendizaje

Al finalizar este tema podrás:

- Comprender qué es Bokeh y cuáles son sus principales características.
- Personalizar gráficos utilizando colores, estilos y temas.
- Modificar glifos, líneas, ejes y leyendas.
- Incorporar herramientas interactivas.
- Crear visualizaciones más claras, atractivas y accesibles.

---

# ¿Qué es Bokeh?

**Bokeh** es una biblioteca de Python especializada en la creación de **visualizaciones interactivas**.

Permite generar gráficos que pueden visualizarse directamente desde un navegador web sin necesidad de software adicional.

Es ampliamente utilizada para:

- Dashboards interactivos.
- Análisis exploratorio de datos.
- Ciencia de Datos.
- Business Intelligence.
- Aplicaciones web.
- Data Storytelling.

---

# Componentes principales de Bokeh

Toda visualización en Bokeh está formada por tres elementos principales.

## Figura (Figure)

Es el **lienzo** donde se dibuja toda la información.

Contiene:

- Ejes
- Cuadrículas
- Leyendas
- Glifos
- Herramientas interactivas

---

## Glifos (Glyphs)

Los glifos son los elementos gráficos que representan los datos.

Ejemplos:

- Círculos
- Puntos
- Líneas
- Barras
- Rectángulos
- Triángulos

Cada glifo representa una parte de la información.

---

## Fuente de datos (Data Source)

Es el conjunto de datos utilizado para construir la visualización.

Puede provenir de:

- DataFrames de Pandas.
- Archivos CSV.
- Bases de datos.
- APIs.
- Listas o arreglos de Python.

---

# Personalización de gráficos

Uno de los principales beneficios de Bokeh es su enorme capacidad de personalización.

---

# 1. Paletas de colores

Bokeh incluye numerosas paletas de colores predefinidas.

Estas permiten:

- Diferenciar categorías.
- Resaltar información importante.
- Mejorar la estética del gráfico.

También es posible crear paletas personalizadas para mantener la identidad visual de una empresa o proyecto.

### Buenas prácticas

- Utilizar colores consistentes.
- Evitar combinaciones difíciles de distinguir.
- Resaltar únicamente la información importante.

---

# 2. Temas (Themes)

Los temas permiten aplicar un estilo uniforme a múltiples visualizaciones.

Un tema puede definir automáticamente:

- Colores.
- Tipografías.
- Fondos.
- Bordes.
- Estilos de ejes.
- Apariencia general.

Su objetivo es mantener una apariencia profesional y consistente.

---

# 3. Personalización de glifos

Los glifos pueden modificarse para destacar determinados datos.

Es posible cambiar:

- Color.
- Tamaño.
- Transparencia.
- Forma.
- Borde.
- Opacidad.

Esto permite dirigir la atención del usuario hacia la información más importante.

---

# 4. Personalización de líneas

Las líneas también pueden configurarse de diferentes maneras.

Opciones disponibles:

- Color.
- Grosor.
- Transparencia.
- Línea continua.
- Línea punteada.
- Línea discontinua.

Estas modificaciones ayudan a distinguir distintas series de datos.

---

# Personalización de ejes y cuadrículas

Los ejes proporcionan la estructura del gráfico.

Es posible modificar:

- Etiquetas.
- Escalas.
- Tipografía.
- Rangos.
- Marcas.

Las cuadrículas ayudan a mejorar la lectura y comparación de los datos.

---

# Leyendas

Las leyendas identifican qué representa cada elemento del gráfico.

Una buena leyenda debe ser:

- Clara.
- Breve.
- Fácil de interpretar.

Su función es facilitar la comprensión de la visualización.

---

# Anotaciones

Las anotaciones permiten destacar información importante dentro del gráfico.

Pueden incluir:

- Texto.
- Flechas.
- Etiquetas.
- Rectángulos.
- Figuras.

Se utilizan para llamar la atención sobre:

- Valores destacados.
- Eventos importantes.
- Tendencias.
- Anomalías.

---

# Interactividad

Una de las características más importantes de Bokeh es su capacidad para crear gráficos interactivos.

Entre las herramientas disponibles se encuentran:

## Hover Tool

Muestra información adicional cuando el usuario coloca el cursor sobre un dato.

Permite visualizar:

- Valores.
- Categorías.
- Fechas.
- Información personalizada.

---

## Zoom

Permite ampliar zonas específicas del gráfico para observar más detalles.

---

## Pan

Desplaza la visualización horizontal o verticalmente.

---

## Reset

Devuelve la visualización a su estado original.

---

## Selección

Permite seleccionar elementos específicos del gráfico para analizarlos o relacionarlos con otras visualizaciones.

---

# Gráficos vinculados

Bokeh permite conectar varias visualizaciones.

Esto significa que una interacción en un gráfico puede afectar automáticamente a otros.

Por ejemplo:

- Seleccionar una categoría en un gráfico de barras puede resaltar los datos correspondientes en un gráfico de dispersión.

Esta funcionalidad mejora considerablemente el análisis exploratorio.

---

# Exportación

Las visualizaciones creadas con Bokeh pueden exportarse como:

- Archivos HTML independientes.
- Aplicaciones web.
- Dashboards interactivos mediante Bokeh Server.

Esto facilita compartir gráficos sin necesidad de instalar software adicional.

---

# Accesibilidad

Una visualización debe ser comprensible para todos los usuarios.

Al diseñar gráficos es recomendable:

- Utilizar colores con suficiente contraste.
- Incorporar etiquetas descriptivas.
- Evitar depender únicamente del color para transmitir información.
- Mantener una navegación sencilla.
- Utilizar tipografías legibles.

La accesibilidad mejora la experiencia de todos los usuarios.

---

# Beneficios de personalizar visualizaciones

Personalizar un gráfico permite:

- Resaltar la información más importante.
- Mejorar la comprensión de los datos.
- Guiar la atención del usuario.
- Facilitar la comunicación.
- Crear presentaciones más atractivas.
- Desarrollar narrativas basadas en datos (*Data Storytelling*).

---

# Conceptos clave

| Concepto | Descripción |
|----------|-------------|
| **Bokeh** | Biblioteca de Python para crear visualizaciones interactivas en la web. |
| **Figura (Figure)** | Lienzo donde se construye la visualización. |
| **Glifo (Glyph)** | Elemento gráfico que representa los datos. |
| **Fuente de datos (Data Source)** | Conjunto de datos utilizado por la visualización. |
| **Paleta de colores** | Conjunto de colores utilizados para representar la información. |
| **Tema (Theme)** | Configuración de estilo reutilizable para múltiples gráficos. |
| **Hover Tool** | Herramienta interactiva que muestra información al pasar el cursor sobre un dato. |
| **Pan** | Herramienta para desplazar el gráfico. |
| **Zoom** | Herramienta para ampliar una región del gráfico. |
| **Bokeh Server** | Servidor que permite publicar aplicaciones interactivas desarrolladas con Bokeh. |

---

# Buenas prácticas

- Utiliza colores con un propósito claro.
- No abuses de efectos visuales.
- Destaca únicamente la información relevante.
- Mantén un estilo uniforme utilizando temas.
- Agrega anotaciones cuando aporten contexto.
- Aprovecha la interactividad para mejorar la exploración de los datos.
- Diseña pensando en la accesibilidad.
- Prioriza siempre la claridad sobre la estética.

---

# Conclusión

Bokeh permite ir más allá de los gráficos estáticos al incorporar **personalización** e **interactividad** en las visualizaciones de datos. Gracias a sus herramientas para modificar colores, glifos, líneas, ejes, leyendas y anotaciones, es posible crear gráficos más claros, atractivos y adaptados a las necesidades de cada audiencia.

Además, funciones como **Hover**, **Zoom**, **Pan**, la vinculación entre gráficos y la exportación a HTML convierten a Bokeh en una excelente opción para desarrollar dashboards interactivos y aplicaciones de análisis de datos. Dominar estas capacidades mejora significativamente la comunicación de resultados y fortalece las habilidades de **Data Storytelling**, permitiendo transformar los datos en experiencias visuales dinámicas e impactantes.ç