# Visualización de datos con Python

Resumen del módulo 03 para crear una presentación en Gamma.

---

# 1. Idea central del módulo

La visualización de datos transforma datos crudos en conocimiento comprensible.

- Python no solo sirve para programar: permite analizar, representar y comunicar información.
- Los gráficos ayudan a descubrir patrones, tendencias, relaciones y valores atípicos.
- Una buena visualización debe facilitar la toma de decisiones, no solo verse atractiva.
- El objetivo final es convertir datos en mensajes claros y accionables.

---

# 2. ¿Por qué visualizar datos?

Las tablas y números suelen ocultar información importante.

- Permite encontrar tendencias a lo largo del tiempo.
- Ayuda a comparar categorías o grupos.
- Facilita detectar outliers y comportamientos inusuales.
- Mejora la comunicación con audiencias técnicas y no técnicas.
- Apoya decisiones basadas en evidencia.

---

# 3. Elegir el gráfico correcto

Cada tipo de gráfico responde a una pregunta distinta.

| Necesidad | Visualización recomendada |
|---|---|
| Comparar categorías | Gráfico de barras |
| Mostrar evolución temporal | Gráfico de líneas |
| Analizar relaciones | Gráfico de dispersión |
| Ver distribuciones | Histograma o diagrama de caja |
| Mostrar proporciones | Gráfico circular |
| Ver intensidades o correlaciones | Mapa de calor |

La elección incorrecta puede confundir o distorsionar el mensaje.

---

# 4. Matplotlib: base de la visualización en Python

Matplotlib es una biblioteca flexible para crear gráficos estáticos de alta calidad.

- Se usa mucho en ciencia de datos, investigación y análisis exploratorio.
- Permite crear gráficos de líneas, barras, dispersión, histogramas y subplots.
- Ofrece control detallado sobre títulos, ejes, etiquetas, leyendas, colores y estilos.
- Es ideal para reportes, notebooks y gráficos destinados a impresión o documentación.

Ejemplos de funciones clave:

- `plt.plot()` para líneas.
- `plt.bar()` para barras.
- `plt.hist()` para histogramas.
- `plt.scatter()` para dispersión.
- `plt.title()`, `plt.xlabel()` y `plt.ylabel()` para mejorar la lectura.

---

# 5. Seaborn: visualización estadística

Seaborn complementa a Matplotlib con gráficos estadísticos más expresivos.

- Simplifica la creación de visualizaciones con buen diseño por defecto.
- Es útil para explorar distribuciones, relaciones y comparaciones entre grupos.
- Facilita trabajar con datasets estructurados en `pandas`.
- Ayuda a detectar patrones en análisis exploratorio de datos.

Casos típicos:

- Histogramas y distribuciones.
- Boxplots para ver dispersión y outliers.
- Gráficos de relación entre variables.
- Heatmaps para correlaciones.

---

# 6. Plotly: gráficos interactivos

Plotly permite pasar de gráficos estáticos a experiencias explorables.

- Incorpora zoom, pan, hover, selección y controles interactivos.
- Plotly Express permite crear gráficos profesionales con pocas líneas de código.
- Es útil para análisis exploratorio, dashboards, reportes dinámicos y aplicaciones web.
- El usuario puede explorar detalles sin modificar el código.

Principales usos:

- Scatter plots interactivos.
- Series temporales con range slider.
- Mapas coropléticos.
- Dashboards con filtros y KPIs.

---

# 7. Bokeh: visualizaciones web interactivas

Bokeh se enfoca en gráficos interactivos listos para la web.

- Permite crear visualizaciones con zoom, pan, hover y selección.
- Puede exportar gráficos como archivos HTML independientes.
- Trabaja con tres componentes principales: `Figure`, glifos y `ColumnDataSource`.
- Es útil para dashboards interactivos y visualizaciones con muchos datos.

Fortalezas principales:

- Interactividad nativa.
- Buen rendimiento.
- Layouts con múltiples gráficos.
- Personalización de colores, herramientas y anotaciones.

---

# 8. Dash: dashboards con Python

Dash permite construir aplicaciones web analíticas usando Python.

- Usa componentes como `html`, `dcc.Graph`, dropdowns, sliders, inputs y checklists.
- El layout define lo que se muestra en pantalla.
- Los callbacks conectan entradas del usuario con salidas visuales.
- Permite crear dashboards que filtran y actualizan gráficos en tiempo real.

Conceptos clave:

- `app.layout`: estructura visible de la app.
- `Input`: componente que dispara una actualización.
- `Output`: componente que recibe el resultado.
- `State`: valor leído sin disparar automáticamente el callback.

---

# 9. Comparación de herramientas

| Herramienta | Mejor uso | Ventaja principal |
|---|---|---|
| Matplotlib | Gráficos estáticos y publicaciones | Máximo control y alta calidad |
| Seaborn | Análisis estadístico exploratorio | Visualizaciones claras con poco código |
| Plotly | Exploración interactiva | Zoom, hover, filtros y dashboards |
| Bokeh | Visualizaciones web interactivas | HTML, layouts y rendimiento |
| Dash | Aplicaciones analíticas | Dashboards web con callbacks |
| Power BI / Superset | Business Intelligence | Paneles empresariales y monitoreo |

No existe una única herramienta mejor: la elección depende del objetivo, audiencia y nivel de interactividad requerido.

---

# 10. Data Storytelling

El Data Storytelling combina datos, visualizaciones y narrativa.

Una historia con datos debe explicar:

- Qué ocurrió.
- Por qué ocurrió.
- Qué significa.
- Qué decisiones pueden tomarse.

Estructura recomendada:

1. Presentar el contexto.
2. Explorar los datos.
3. Mostrar hallazgos.
4. Explicar implicancias.
5. Cerrar con recomendaciones o próximos pasos.

---

# 11. Diseño de presentaciones efectivas

Una presentación basada en datos debe adaptarse a su audiencia.

- Audiencia ejecutiva: necesita KPIs, tendencias, conclusiones y recomendaciones.
- Audiencia técnica: puede requerir metodología, detalle y análisis profundo.
- Audiencia no técnica: necesita lenguaje claro, gráficos simples y pocas métricas por diapositiva.

Buenas prácticas:

- Una idea principal por diapositiva.
- Títulos descriptivos.
- Colores consistentes.
- Tipografía legible.
- Contraste adecuado.
- Espacio en blanco para reducir saturación.

---

# 12. Carga cognitiva

La carga cognitiva es el esfuerzo mental necesario para comprender una visualización.

Una visualización efectiva reduce el esfuerzo innecesario.

- Evitar ruido visual: sombras, 3D, bordes excesivos y colores sin propósito.
- Usar jerarquía visual para dirigir la atención.
- Dividir información compleja en bloques pequeños.
- Mostrar detalles progresivamente cuando sea necesario.
- Incorporar interactividad solo si ayuda a explorar mejor los datos.

Idea clave:

> La mejor visualización no es la que muestra más información, sino la que permite entender el mensaje con menos esfuerzo.

---

# 13. Sesgos y errores comunes

Un análisis visual puede ser incorrecto si los datos o la interpretación están sesgados.

Sesgos frecuentes:

- Muestra insuficiente.
- Sesgo de supervivencia.
- Sesgo de muestreo.
- Sesgo de confirmación.
- Sesgo de anclaje.

Errores habituales:

- Confundir correlación con causalidad.
- Ignorar valores atípicos.
- Eliminar datos faltantes sin evaluar impacto.
- Manipular escalas.
- Usar gráficos que exageran diferencias.

---

# 14. Flujo recomendado de trabajo

Un proyecto de visualización debería seguir un proceso claro.

```text
Datos
  ↓
Limpieza y revisión de calidad
  ↓
Análisis exploratorio
  ↓
Selección del gráfico adecuado
  ↓
Diseño visual claro
  ↓
Storytelling
  ↓
Presentación o dashboard
  ↓
Decisión basada en evidencia
```

---

# 15. Conclusión

La visualización de datos con Python une técnica, análisis y comunicación.

- Matplotlib y Seaborn permiten explorar y explicar datos de forma clara.
- Plotly, Bokeh y Dash agregan interactividad y dashboards.
- El diseño visual mejora la comprensión.
- El storytelling convierte hallazgos en decisiones.
- La detección de sesgos protege la calidad del análisis.

Mensaje final:

> Visualizar datos no consiste solo en crear gráficos: consiste en comunicar evidencia de manera clara, honesta y útil.

---

# Sugerencia para Gamma

Usar este Markdown como base y pedir a Gamma:

> Crear una presentación educativa, clara y profesional para estudiantes de análisis de datos. Mantener una diapositiva por cada sección, usar estilo moderno, pocos textos por slide, gráficos conceptuales, íconos de Python/datos y una paleta sobria con buen contraste.
