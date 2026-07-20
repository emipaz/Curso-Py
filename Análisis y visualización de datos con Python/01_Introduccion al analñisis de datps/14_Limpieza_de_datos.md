# Limpieza de Datos 101 (Data Cleaning)

## ¿Qué es la limpieza de datos?
La limpieza de datos (Data Cleaning, Data Wrangling o Data Munging) es el proceso de transformar datos brutos, incompletos o inconsistentes en datos limpios, estructurados y listos para el análisis.

Su objetivo es:
- Mejorar la calidad de los datos.
- Garantizar resultados confiables.
- Facilitar el análisis y la creación de modelos.
- Estandarizar encabezados y formatos.

---

# ¿Por qué es importante?

Los datos son la base de cualquier análisis, modelo de Machine Learning o toma de decisiones.

### Beneficios de los datos limpios
- Mayor precisión en los análisis.
- Modelos más confiables.
- Menos errores y depuración.
- Mejor colaboración entre equipos.
- Conclusiones más sólidas y accionables.

### Riesgos de trabajar con datos sucios
- Resultados engañosos.
- Predicciones incorrectas.
- Decisiones equivocadas.
- Sesgos en los modelos.

---

# Problemas comunes de calidad de datos

## 1. Valores faltantes (Missing Values)

Son datos ausentes dentro del conjunto de datos.

### Causas comunes
- Errores de carga.
- Fallos de sensores.
- Información no disponible.
- Errores humanos.

### Problemas que generan
- Sesgo estadístico.
- Pérdida de precisión.
- Análisis incompletos.

### Ejemplo
En una base de clientes faltan edades o ingresos de algunos usuarios.

---

## 2. Valores atípicos (Outliers)

Son valores que se alejan significativamente del comportamiento normal del conjunto de datos.

### Ejemplo
En un análisis inmobiliario:

| Casa | Precio |
|--------|---------|
| Casa A | 100.000 |
| Casa B | 120.000 |
| Casa C | 110.000 |
| Mansión | 5.000.000 |

La mansión puede distorsionar el promedio.

### Problemas
- Alteran estadísticas.
- Afectan modelos predictivos.
- Generan conclusiones incorrectas.

---

## 3. Inconsistencias

Ocurren cuando los mismos datos aparecen con formatos diferentes.

### Ejemplos

#### Encabezados distintos

```text
Customer ID
customer_id
CustomerID
```

#### Direcciones distintas

```text
Street
St.
STREET
```

#### Nombres distintos

```text
John Doe
Doe, John
```

### Consecuencias
- Dificultan unir datasets.
- Generan duplicados.
- Complican filtros y agrupaciones.

---

# Estrategias para resolver problemas de calidad

## 1. Eliminar datos faltantes

Consiste en eliminar filas o columnas que contienen valores nulos.

### Ventajas
- Fácil de implementar.
- Rápido.

### Desventajas
- Puede eliminar información valiosa.
- Puede introducir sesgos.
- Reduce el tamaño del dataset.

---

## 2. Imputar valores faltantes

La imputación consiste en reemplazar valores faltantes por valores estimados.

### Métodos básicos

#### Media

```text
Edad promedio = 35
Valor faltante → 35
```

#### Mediana

```text
Edades:
20, 22, 25, 27, 60

Mediana = 25
```

#### Moda

```text
Ciudad:
Buenos Aires
Rosario
Buenos Aires

Moda = Buenos Aires
```

### Métodos avanzados

#### Imputación por regresión

Predice valores faltantes utilizando otras variables.

#### Imputación múltiple

Genera varias estimaciones posibles considerando la incertidumbre de los datos.

---

# Tratamiento de valores atípicos

## Opción 1: Eliminarlos

Cuando:
- Son errores evidentes.
- Provienen de sensores defectuosos.
- Son datos irrelevantes.

## Opción 2: Capping

Limitar valores extremos a un umbral.

Ejemplo:

```text
Valor máximo permitido = 100

120 → 100
150 → 100
```

## Opción 3: Estadísticas robustas

Utilizar métricas menos sensibles a outliers:

- Mediana
- Rango intercuartílico (IQR)

## Opción 4: Algoritmos robustos

En Machine Learning:

```python
from sklearn.preprocessing import RobustScaler

scaler = RobustScaler()
X_scaled = scaler.fit_transform(X)
```

---

# Resolver inconsistencias con Python

## replace()

Permite reemplazar valores específicos.

```python
import pandas as pd

df["ciudad"] = df["ciudad"].replace({
    "Bs As": "Buenos Aires",
    "Baires": "Buenos Aires"
})
```

### Resultado

```text
Bs As  → Buenos Aires
Baires → Buenos Aires
```

---

## apply()

Permite aplicar funciones personalizadas.

```python
df["nombre"] = df["nombre"].apply(
    lambda x: x.title()
)
```

### Resultado

```text
juan perez → Juan Perez
MARIA LOPEZ → Maria Lopez
```

---

## Expresiones regulares

Útiles para estandarizar textos.

```python
import re

texto = re.sub(r"\bSt\.\b", "Street", texto)
```

---

# Casos prácticos

## Caso 1: Clientes con edades faltantes

Problema:
- Algunos clientes no tienen edad registrada.

Solución:
- Imputar usando la edad promedio o clientes similares.

---

## Caso 2: Temperaturas extremas

Problema:
- Aparecen registros de 250°C.

Solución:
- Verificar errores.
- Eliminar o corregir utilizando datos históricos.

---

## Caso 3: Nombres inconsistentes

Problema:

```text
John Doe
Doe, John
```

Solución:
- Convertir todos los nombres al mismo formato.

---

# Consideraciones importantes

La limpieza de datos no debe utilizarse para manipular resultados.

### Buenas prácticas

- Documentar todos los cambios.
- Justificar las decisiones tomadas.
- Mantener trazabilidad.
- Evitar introducir sesgos.
- Conservar la representatividad de los datos.

---

# Herramientas Python más utilizadas

| Biblioteca | Uso |
|------------|-----|
| Pandas | Limpieza y transformación de datos |
| NumPy | Operaciones numéricas |
| Scikit-Learn | Escalado e imputación avanzada |
| Regex (re) | Limpieza de texto |
| RobustScaler | Manejo de outliers |

---

# Resumen Final

✅ La limpieza de datos es una etapa crítica del análisis de datos.

✅ Los problemas más comunes son:
- Valores faltantes.
- Valores atípicos.
- Inconsistencias.

✅ Las principales técnicas incluyen:
- Eliminación de datos.
- Imputación.
- Tratamiento de outliers.
- Estandarización de formatos.

✅ Herramientas como Pandas, NumPy y Scikit-Learn facilitan el proceso.

✅ La calidad de los datos determina directamente la calidad de los análisis, modelos y decisiones obtenidas.