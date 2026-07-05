# Introducción a Matplotlib y los Gráficos Básicos


# Objetivos de aprendizaje

Al finalizar este tema serás capaz de:

- Comprender la importancia de Matplotlib en el análisis de datos.
- Identificar los principales tipos de gráficos básicos.
- Reconocer cuándo utilizar cada visualización.
- Comprender cómo los gráficos facilitan la interpretación y comunicación de los datos.
- Conocer los beneficios de utilizar visualizaciones en proyectos de análisis de datos.

---

# ¿Qué es Matplotlib?

**Matplotlib** es una biblioteca de Python especializada en la creación de gráficos y visualizaciones de datos.

Permite generar desde gráficos simples hasta visualizaciones altamente personalizadas para:

- Ciencia de Datos.
- Machine Learning.
- Inteligencia Artificial.
- Ingeniería.
- Finanzas.
- Investigación científica.
- Desarrollo de aplicaciones.

Su principal objetivo es transformar datos numéricos en información visual fácil de interpretar.

---

# ¿Por qué son importantes los gráficos?

Las visualizaciones permiten convertir grandes cantidades de datos en información comprensible.

Los gráficos ayudan a:

- Detectar tendencias.
- Encontrar patrones.
- Descubrir relaciones entre variables.
- Identificar valores atípicos (*outliers*).
- Comunicar resultados de manera efectiva.

---

# Beneficios de utilizar gráficos

## 1. Claridad

Los gráficos simplifican datos complejos y los convierten en representaciones visuales fáciles de comprender.

### Beneficios

- Reducen la complejidad.
- Facilitan la interpretación.
- Mejoran la comprensión de la información.

---

## 2. Descubrimiento de información (*Insights*)

Las visualizaciones permiten encontrar información que no resulta evidente al observar únicamente tablas de datos.

Permiten detectar:

- Tendencias.
- Patrones.
- Correlaciones.
- Valores atípicos.
- Cambios importantes.

---

## 3. Comunicación

Los gráficos facilitan la comunicación tanto con públicos técnicos como no técnicos.

Una imagen suele transmitir información de forma mucho más rápida que una tabla de datos.

---

## 4. Apoyo a la toma de decisiones

Al presentar la información de forma clara y resumida, los gráficos permiten tomar decisiones fundamentadas en datos (*Data Driven Decisions*).

---

# Tipos de gráficos básicos en Matplotlib

## 1. Gráfico de Líneas (Line Plot)

### ¿Qué es?

Une los puntos de datos mediante líneas para representar la evolución de una variable.

### ¿Cuándo utilizarlo?

- Series temporales.
- Evolución de ventas.
- Cotización de acciones.
- Temperaturas.
- Tráfico web.
- Rendimiento de aplicaciones.

### Ventajas

- Muestra claramente tendencias.
- Permite observar cambios a lo largo del tiempo.
- Facilita detectar patrones cíclicos.
- Ideal para datos cronológicos.

### Ejemplo

Analizar el precio diario de una acción durante seis meses.

El gráfico permite identificar:

- Tendencia general.
- Crecimientos.
- Caídas.
- Periodos de estabilidad.
- Volatilidad.

---

## 2. Gráfico de Dispersión (Scatter Plot)

### ¿Qué es?

Representa cada observación mediante un punto en un plano cartesiano utilizando dos variables numéricas.

### ¿Cuándo utilizarlo?

- Buscar correlaciones.
- Análisis predictivo.
- Modelos de regresión.
- Detección de valores atípicos.

### Ventajas

- Permite estudiar la relación entre variables.
- Detecta agrupamientos.
- Identifica anomalías.
- Facilita descubrir correlaciones.

### Ejemplo

Relacionar:

- Horas de estudio.
- Calificación obtenida en un examen.

El gráfico puede mostrar una correlación positiva entre ambas variables.

---

## 3. Gráfico de Barras (Bar Plot)

### ¿Qué es?

Representa datos categóricos mediante barras verticales u horizontales cuya longitud es proporcional al valor.

### ¿Cuándo utilizarlo?

- Comparar categorías.
- Comparar ventas.
- Rankings.
- Resultados por producto.
- Comparación entre regiones.

### Ventajas

- Muy fácil de interpretar.
- Excelente para comparar categorías.
- Permite identificar rápidamente el mayor y el menor valor.

### Ejemplo

Comparar las ventas de distintos productos de una tienda para identificar el producto más vendido.

---

# Comparación de los gráficos básicos

| Tipo de gráfico | Mejor uso | Ejemplo |
|-----------------|-----------|----------|
| **Gráfico de Líneas** | Mostrar tendencias a lo largo del tiempo | Evolución del precio de una acción |
| **Gráfico de Dispersión** | Analizar relaciones entre variables | Horas de estudio vs. calificaciones |
| **Gráfico de Barras** | Comparar categorías | Ventas por producto |

---

# Beneficios de utilizar gráficos básicos

## Simplifican la comunicación

Transforman datos complejos en representaciones fáciles de comprender para cualquier audiencia.

---

## Permiten descubrir patrones

Ayudan a identificar rápidamente:

- Tendencias.
- Correlaciones.
- Agrupamientos.
- Valores atípicos.

---

## Facilitan la toma de decisiones

Los gráficos presentan la información de forma clara, permitiendo fundamentar decisiones basadas en evidencia.

---

## Favorecen el Data Storytelling

Los gráficos permiten construir una narrativa basada en datos.

Una buena visualización responde preguntas como:

- ¿Qué ocurrió?
- ¿Por qué ocurrió?
- ¿Qué tendencias existen?
- ¿Qué conclusiones pueden extraerse?

---

# Conceptos clave

| Concepto | Descripción |
|----------|-------------|
| **Matplotlib** | Biblioteca de Python para crear gráficos y visualizaciones de datos. |
| **Visualización de datos** | Representación gráfica de la información para facilitar su análisis e interpretación. |
| **Gráfico de Líneas** | Muestra la evolución de una variable mediante líneas que conectan puntos de datos. |
| **Gráfico de Dispersión** | Representa la relación entre dos variables utilizando puntos. |
| **Gráfico de Barras** | Compara valores entre diferentes categorías mediante barras. |
| **Correlación** | Relación existente entre dos variables. |
| **Outlier (Valor atípico)** | Observación que se aleja significativamente del resto de los datos. |
| **Serie temporal** | Conjunto de datos registrados en diferentes momentos del tiempo. |
| **Insight** | Hallazgo o conocimiento obtenido a partir del análisis de datos. |
| **Data Storytelling** | Comunicación de hallazgos mediante gráficos y narrativa. |

---

# Buenas prácticas

- Selecciona el gráfico según el objetivo del análisis.
- Evita incluir información innecesaria.
- Utiliza títulos descriptivos.
- Etiqueta correctamente los ejes.
- Usa colores con moderación y de forma consistente.
- Destaca únicamente la información importante.
- Prioriza siempre la claridad sobre la estética.

---

# Conclusión

Los gráficos básicos de **Matplotlib** constituyen el punto de partida para cualquier proyecto de visualización de datos en Python. Los gráficos de líneas permiten analizar tendencias temporales, los gráficos de dispersión ayudan a descubrir relaciones entre variables y los gráficos de barras facilitan la comparación entre categorías.

Además de mejorar la comprensión de los datos, estas visualizaciones permiten comunicar resultados de manera efectiva, apoyar la toma de decisiones y construir narrativas basadas en evidencia (*Data Storytelling*). Dominar estos gráficos proporciona una base sólida para explorar posteriormente las capacidades avanzadas de Matplotlib y desarrollar visualizaciones cada vez más completas e impactantes.