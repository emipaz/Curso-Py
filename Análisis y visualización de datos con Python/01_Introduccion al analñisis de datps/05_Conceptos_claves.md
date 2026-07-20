# Conceptos Clave en el Análisis de Datos

## Introducción

El análisis de datos permite transformar información en conocimiento útil para tomar decisiones informadas y desarrollar soluciones basadas en evidencia.

Para comprender correctamente cualquier análisis es necesario dominar algunos conceptos fundamentales:

- Población.
- Muestra.
- Variables.
- Tipos de variables.
- Tipos de datos.
- Calidad de los datos.

---

# Población y Muestra

## Población

La **población** es el conjunto completo de individuos, objetos o elementos que se desean estudiar.

### Ejemplos

| Problema | Población |
|-----------|------------|
| Analizar hábitos de compra | Todos los clientes |
| Estudiar votantes | Todos los ciudadanos habilitados |
| Analizar estudiantes | Todos los alumnos de una universidad |

---

## Muestra

Una **muestra** es un subconjunto representativo de la población.

### ¿Por qué usar muestras?

Porque estudiar toda la población suele ser:

- Costoso.
- Lento.
- Impracticable.

### Ventajas

- Reduce costos.
- Reduce tiempo.
- Facilita el análisis.

---

## Importancia de la representatividad

Una muestra debe reflejar las características de la población.

### Mala muestra

```text
Clientes encuestados:
- Solo jóvenes
- Solo una ciudad
- Solo usuarios premium
```

Resultado:

- Conclusiones sesgadas.

### Buena muestra

```text
Clientes:
- Distintas edades
- Distintas regiones
- Distintos niveles de gasto
```

Resultado:

- Conclusiones más confiables.

---

## Ejemplo

### Librería online

**Población**

```text
Todos los clientes de la librería
```

**Muestra**

```text
1000 clientes seleccionados aleatoriamente
```

Información analizada:

- Compras realizadas.
- Edad.
- Género.
- Comportamiento de navegación.

Objetivo:

- Crear un sistema de recomendación de libros.

---

# Variables

## Definición

Las variables son las características o atributos que medimos u observamos.

Son la materia prima del análisis de datos.

---

## Ejemplos de variables

### Datos demográficos

- Edad.
- Género.
- Ubicación.
- Nivel de ingresos.

### Historial de compras

- Cantidad de compras.
- Gasto total.
- Géneros favoritos.

### Navegación web

- Tiempo en el sitio.
- Páginas visitadas.
- Clicks realizados.

### Opiniones

- Valoraciones.
- Encuestas.
- Comentarios.

---

# Tipos de Variables

## 1. Variables Numéricas (Cuantitativas)

Representan cantidades medibles.

---

### Variables Discretas

Solo pueden tomar valores específicos.

Generalmente números enteros.

### Ejemplos

```text
Número de visitas a un sitio web
Cantidad de productos comprados
Número de estrellas de una valoración
```

Valores posibles:

```text
1, 2, 3, 4...
```

No existen:

```text
2.5 visitas
3.7 productos
```

---

### Variables Continuas

Pueden tomar cualquier valor dentro de un rango.

### Ejemplos

```text
Peso
Temperatura
Tiempo en una página web
Altura
```

Valores posibles:

```text
70
70.5
70.25
70.257
```

---

## 2. Variables Categóricas (Cualitativas)

Representan categorías o grupos.

---

### Variables Nominales

No tienen orden natural.

### Ejemplos

```text
Color favorito
Marca de teléfono
País de origen
Tipo de cocina
```

Ejemplo:

```text
Rojo
Azul
Verde
```

Ningún color es "mayor" que otro.

---

### Variables Ordinales

Poseen un orden lógico.

### Ejemplos

#### Nivel educativo

```text
Primaria
Secundaria
Universidad
Posgrado
```

#### Satisfacción del cliente

```text
Malo
Regular
Bueno
Excelente
```

Existe orden, pero no una distancia numérica exacta.

---

# Resumen de Variables

| Tipo | Subtipo | Ejemplo |
|--------|----------|----------|
| Numérica | Discreta | Cantidad de compras |
| Numérica | Continua | Peso |
| Categórica | Nominal | Color |
| Categórica | Ordinal | Nivel educativo |

---

# Variables en Python y Pandas

## DataFrame

Pandas utiliza la estructura llamada **DataFrame**.

### Concepto

```text
Columnas → Variables
Filas → Observaciones
```

Ejemplo:

| Edad | Género | Ingreso |
|--------|---------|----------|
| 25 | Masculino | 50000 |
| 30 | Femenino | 60000 |

---

## Código de ejemplo

```python
import pandas as pd

data = {
    "age": [25, 30, 35, 40],
    "gender": ["male", "female", "male", "female"],
    "income": [50000, 60000, 75000, 55000]
}

df = pd.DataFrame(data)

# Convertir género a variable categórica
df["gender"] = df["gender"].astype("category")

# Promedio de ingresos
print(df["income"].mean())

# Conteo por género
print(df["gender"].value_counts())
```

---

# Tipos de Datos en Python

## Enteros (int)

```python
edad = 25
```

Ejemplos:

```text
-10
0
100
```

---

## Flotantes (float)

```python
precio = 19.99
```

Ejemplos:

```text
3.14
5.75
100.50
```

---

## Cadenas (str)

```python
nombre = "Juan"
```

Ejemplos:

```text
"Hola"
"Python"
"Análisis de Datos"
```

---

## Booleanos (bool)

```python
activo = True
```

Valores posibles:

```python
True
False
```

---

## Listas (list)

```python
numeros = [1, 2, 3, 4]
```

Permiten almacenar múltiples elementos.

---

## Diccionarios (dict)

```python
persona = {
    "nombre": "Ana",
    "edad": 30
}
```

Almacenan pares:

```text
clave → valor
```

---

# Estructuras Especializadas para Datos

## NumPy

Optimizado para:

- Cálculos numéricos.
- Álgebra lineal.
- Procesamiento eficiente.

Ejemplo:

```python
import numpy as np

datos = np.array([10, 20, 30])

print(np.mean(datos))
```

---

## Pandas

Optimizado para:

- Datos tabulares.
- Filtrado.
- Agrupación.
- Transformación de datos.

Ejemplo:

```python
df[df["income"] > 50000]
```

---

# Los Tipos de Variables Determinan el Análisis

## Variable Numérica

Ejemplo:

```text
Gasto de clientes
```

Análisis posibles:

- Media.
- Mediana.
- Desviación estándar.
- Histogramas.

---

## Variable Categórica

Ejemplo:

```text
Nivel de satisfacción
```

Análisis posibles:

- Frecuencias.
- Porcentajes.
- Gráficos de barras.

---

# Retos en el Análisis de Datos

## 1. Sesgo de muestreo

Ocurre cuando la muestra no representa correctamente la población.

Consecuencia:

```text
Resultados engañosos
```

---

## 2. Errores de medición

Pueden surgir por:

- Encuestas incorrectas.
- Datos incompletos.
- Errores humanos.

---

## 3. Datos faltantes

Ejemplo:

| Edad | Ingreso |
|--------|----------|
| 25 | 50000 |
| 30 | NULL |

Soluciones:

- Eliminar registros.
- Imputar valores.

---

## 4. Valores atípicos (Outliers)

Ejemplo:

```text
Ingresos:
50000
55000
60000
9000000
```

El último valor puede distorsionar el análisis.

---

# Conceptos Fundamentales para Recordar

| Concepto | Definición |
|-----------|------------|
| Población | Conjunto completo de elementos a estudiar |
| Muestra | Subconjunto representativo de la población |
| Variable | Característica observada o medida |
| Discreta | Variable numérica con valores enteros |
| Continua | Variable numérica con valores infinitos dentro de un rango |
| Nominal | Categorías sin orden |
| Ordinal | Categorías con orden |
| DataFrame | Tabla de datos en Pandas |
| Outlier | Valor extremadamente diferente al resto |
| Sesgo | Distorsión que afecta las conclusiones |

---

# Conclusiones

- La población representa el universo completo de estudio.
- Las muestras permiten analizar poblaciones de forma práctica.
- Las variables son los elementos fundamentales del análisis.
- Existen variables numéricas y categóricas, cada una con distintos subtipos.
- Python y Pandas ofrecen estructuras optimizadas para trabajar con datos.
- Comprender los tipos de variables permite elegir correctamente las técnicas de análisis y visualización.
- La calidad de los datos es tan importante como el análisis mismo.
- Estos conceptos constituyen la base de cualquier proyecto de análisis de datos o ciencia de datos.