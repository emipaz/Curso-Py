# Selección de Visualizaciones en Power BI

## 1. La importancia de elegir la visualización correcta

Una buena visualización permite:

- Comunicar información de forma clara.
- Resaltar patrones y tendencias.
- Facilitar la interpretación de los datos.
- Apoyar la toma de decisiones.

Elegir un gráfico incorrecto puede dificultar la comprensión e incluso llevar a conclusiones erróneas.

---

# Gráfico Circular (Pie Chart)

## ¿Qué es?

Representa un conjunto de datos como un círculo dividido en porciones, donde cada segmento muestra la proporción de una categoría respecto del total.

### Casos de uso

- Participación de mercado.
- Ventas por categoría.
- Distribución porcentual.
- Composición de un total.

### Ventajas

- Muy fácil de interpretar.
- Muestra rápidamente la proporción entre categorías.
- Excelente para pocas categorías.

### Limitaciones

- No funciona bien con muchas categorías.
- Los segmentos pequeños son difíciles de comparar.
- Puede resultar confuso cuando existen muchas porciones.
- No es adecuado cuando se requiere alta precisión.

---

# Gráfico de Barras (Bar Chart)

## ¿Qué es?

Representa los datos mediante barras horizontales o verticales cuya longitud es proporcional al valor.

### Casos de uso

- Comparar categorías.
- Comparar ventas.
- Comparar cantidades.
- Rankings.

### Ventajas

- Muy fácil de leer.
- Permite comparar múltiples categorías.
- Admite grandes cantidades de datos.
- Las diferencias son evidentes.

### Limitaciones

- Puede volverse muy extenso con demasiadas categorías.
- No es el mejor gráfico para mostrar tendencias temporales.
- Un mal escalado de los ejes puede inducir a interpretaciones incorrectas.

---

# Histograma (Histogram)

## ¿Qué es?

Agrupa datos numéricos en intervalos (*bins*) para mostrar la frecuencia con que aparecen los valores.

### Casos de uso

- Distribución de edades.
- Distribución de ventas.
- Distribución de ingresos.
- Distribución de tiempos.

### Ventajas

- Resume grandes cantidades de datos.
- Permite identificar:
  - Distribución normal.
  - Asimetrías.
  - Valores atípicos (*outliers*).
  - Concentraciones de datos.

### Limitaciones

- La elección del ancho de los intervalos afecta la interpretación.
- Diferentes configuraciones pueden producir gráficos muy distintos.
- Puede ocultar detalles importantes.

---

# Gráfico de Líneas (Line Chart)

## ¿Qué es?

Conecta puntos de datos mediante líneas para mostrar la evolución de una variable a lo largo del tiempo.

### Casos de uso

- Evolución de ventas.
- Series temporales.
- Inventario.
- Tráfico web.
- Indicadores financieros.

### Ventajas

- Ideal para mostrar tendencias.
- Permite observar:
  - Crecimientos.
  - Descensos.
  - Estacionalidades.
  - Cambios en el tiempo.

### Limitaciones

- Puede sugerir tendencias inexistentes cuando existen pocos datos.
- Varias líneas pueden dificultar la lectura.
- Requiere un buen uso de colores y leyendas.

---

# Gráfico de Dispersión (Scatter Plot)

## ¿Qué es?

Representa cada observación como un punto en un plano cartesiano para mostrar la relación entre dos variables.

### Casos de uso

- Buscar correlaciones.
- Análisis predictivo.
- Modelos de regresión.
- Detección de valores atípicos.

### Ventajas

- Permite identificar relaciones entre variables.
- Detecta tendencias.
- Facilita descubrir agrupamientos y anomalías.

### Limitaciones

- Puede saturarse con grandes volúmenes de datos.
- Los puntos pueden superponerse.
- En ocasiones requiere aplicar filtros o técnicas adicionales para mejorar la visualización.

---

# Tablas (Tables)

## ¿Qué son?

Organizan los datos en filas y columnas mostrando los valores exactos.

### Casos de uso

- Informes financieros.
- Listados de clientes.
- Reportes detallados.
- Información que requiere precisión.

### Ventajas

- Presentan datos exactos.
- Facilitan la comparación detallada.
- Ideales cuando la precisión es prioritaria.

### Limitaciones

- Poco atractivas visualmente.
- Resultan difíciles de interpretar con grandes volúmenes de datos.
- No muestran tendencias de forma inmediata.

---

# Comparación de visualizaciones

| Visualización | Mejor uso | Ventajas | Limitaciones |
|---------------|-----------|-----------|--------------|
| **Gráfico Circular** | Mostrar proporciones | Muy intuitivo y simple | No recomendable con muchas categorías |
| **Gráfico de Barras** | Comparar categorías | Muy versátil y fácil de leer | Poco adecuado para tendencias temporales |
| **Histograma** | Analizar distribuciones | Revela patrones estadísticos | Sensible al tamaño de los intervalos |
| **Gráfico de Líneas** | Mostrar tendencias en el tiempo | Excelente para series temporales | Puede inducir interpretaciones erróneas con pocos datos |
| **Gráfico de Dispersión** | Analizar relaciones entre variables | Detecta correlaciones y valores atípicos | Puede saturarse con muchos puntos |
| **Tabla** | Mostrar datos exactos | Máxima precisión | Escaso impacto visual |

---

# ¿Cómo elegir la visualización adecuada?

Antes de crear un gráfico, pregúntate:

- ¿Quiero comparar categorías?
  - **Gráfico de barras**

- ¿Quiero mostrar porcentajes de un total?
  - **Gráfico circular**

- ¿Quiero analizar una distribución?
  - **Histograma**

- ¿Quiero mostrar una evolución en el tiempo?
  - **Gráfico de líneas**

- ¿Quiero estudiar la relación entre dos variables?
  - **Gráfico de dispersión**

- ¿Necesito mostrar cifras exactas?
  - **Tabla**

---

# Conceptos clave

| Concepto | Descripción |
|----------|-------------|
| **Visualización de datos** | Representación gráfica de la información para facilitar su análisis. |
| **Gráfico Circular** | Muestra la composición de un todo mediante porciones. |
| **Gráfico de Barras** | Compara cantidades entre distintas categorías. |
| **Histograma** | Representa la distribución de datos numéricos agrupados en intervalos. |
| **Gráfico de Líneas** | Muestra la evolución de una variable a lo largo del tiempo. |
| **Gráfico de Dispersión** | Representa la relación entre dos variables mediante puntos. |
| **Tabla** | Presenta datos exactos organizados en filas y columnas. |
| **Outlier** | Valor atípico que se aleja significativamente del resto de los datos. |
| **Correlación** | Relación existente entre dos variables. |
| **Serie temporal** | Conjunto de datos registrados en distintos momentos del tiempo. |

---

# Buenas prácticas

- Selecciona el gráfico según el objetivo del análisis.
- Evita sobrecargar una visualización con demasiada información.
- Utiliza escalas adecuadas para no distorsionar los datos.
- Emplea colores consistentes y fáciles de interpretar.
- Prioriza siempre la claridad sobre la estética.
- Utiliza tablas únicamente cuando sea necesario mostrar valores exactos.
- Complementa las visualizaciones con títulos, etiquetas y leyendas claras.

---

# Conclusión

Cada tipo de visualización en Power BI está diseñado para responder diferentes necesidades analíticas. Los gráficos circulares muestran proporciones, los gráficos de barras comparan categorías, los histogramas analizan distribuciones, los gráficos de líneas revelan tendencias temporales, los diagramas de dispersión descubren relaciones entre variables y las tablas proporcionan precisión.

Seleccionar la visualización adecuada permite transformar los datos en información clara y accionable, facilitando la comunicación con las partes interesadas y mejorando la toma de decisiones basada en datos.