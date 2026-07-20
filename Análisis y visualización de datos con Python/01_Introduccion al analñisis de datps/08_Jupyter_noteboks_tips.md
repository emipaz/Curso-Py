# Jupyter Notebook: Resumen Completo

## ¿Qué es Jupyter Notebook?

Jupyter Notebook es un entorno interactivo que combina:

- Código Python
- Texto formateado (Markdown)
- Visualizaciones
- Documentación

Permite ejecutar código en pequeñas unidades llamadas **celdas** y ver los resultados inmediatamente.

### Ventajas

- Experimentación rápida
- Análisis de datos interactivo
- Prototipado
- Documentación integrada
- Visualización de resultados en tiempo real

---

# Interfaz de Jupyter Notebook

## Explorador de archivos

Ubicado generalmente en la parte izquierda.

Permite:

- Crear notebooks nuevos
- Abrir notebooks existentes
- Navegar carpetas

## Área de trabajo

Espacio principal donde:

- Se escribe código
- Se ejecutan celdas
- Se visualizan resultados
- Se agrega documentación

## Barra de herramientas

Permite:

- Ejecutar celdas
- Crear nuevas celdas
- Cambiar tipos de celdas
- Guardar notebooks
- Personalizar la interfaz

---

# Tipos de Celdas

## 1. Celdas de Código

Contienen código Python.

### Ejemplo

```python
import pandas as pd

df = pd.read_csv("datos.csv")
df.head()
```

Ejecutar una celda

Shift + Enter

Resultado:

Ejecuta la celda
Muestra la salida debajo
Selecciona la siguiente celda
2. Celdas Markdown

Permiten documentar el notebook.

Se utilizan para:

Títulos
Explicaciones
Listas
Imágenes
Enlaces
Fórmulas matemáticas
Ejemplo
# Título principal

## Subtítulo

- Elemento 1
- Elemento 2

**Texto en negrita**

*Texto en cursiva*
Uso de Markdown
Encabezados
# Título 1
## Título 2
### Título 3
Listas
Viñetas
- Python
- Pandas
- NumPy
Numeradas
1. Cargar datos
2. Limpiar datos
3. Analizar datos
Enlaces
[OpenAI](https://openai.com)
Imágenes
![Descripción](imagen.png)
Fórmulas Matemáticas

Inline:

$E=mc^2$

Bloque:

$$
x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}
$$
Visualización de Datos

Jupyter se integra perfectamente con bibliotecas de visualización.

Matplotlib
import matplotlib.pyplot as plt

plt.plot([1,2,3,4])
plt.show()
Beneficios
Gráficos dentro del notebook
Exploración interactiva
Presentación de resultados
Comandos Mágicos (Magic Commands)

Son comandos especiales que comienzan con %.

Mostrar gráficos dentro del notebook
%matplotlib inline

Permite visualizar gráficos directamente en las celdas.

Medir tiempo de ejecución
%timeit sum(range(1000))

Sirve para:

Optimizar código
Comparar implementaciones
Medir rendimiento
Mostrar directorio actual
%pwd

Resultado:

C:\Usuarios\Proyecto
Listar archivos
%ls

Muestra los archivos y carpetas del directorio actual.

Ejecutar script externo
%run script.py

Permite ejecutar un archivo Python completo desde el notebook.

Atajos de Teclado Útiles
Crear celda debajo
B
Crear celda arriba
A
Eliminar celda
DD
Convertir a código
Y
Convertir a Markdown
M
Ejecutar celda
Shift + Enter
Entrar en modo edición
Enter
Salir de modo edición
Esc
Extensiones Útiles

Jupyter permite agregar funcionalidades extra.

Jupyter NB Extensions Configurator

Características:

Gestión visual de extensiones
Fácil activación/desactivación
Extensiones populares
Table of Contents

Genera índice automático.

Code Folding

Permite contraer bloques de código.

Variable Inspector

Muestra variables activas.

Autopep8

Formatea código automáticamente.

Compartir y Colaborar
GitHub

Permite publicar notebooks y compartirlos fácilmente.

Flujo típico
git add .
git commit -m "Análisis inicial"
git push
NBViewer

Permite visualizar notebooks online sin ejecutarlos.

Ideal para:

Portafolios
Documentación
Compartir resultados
Exportación

Jupyter puede exportarse a:

HTML
PDF
Markdown
Python (.py)
Ejemplo
File → Download As → PDF