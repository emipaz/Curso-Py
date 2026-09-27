# Regresión Lineal con Python y Scikit-learn

## 1. ¿Qué es la regresión lineal?

La **regresión lineal** es una técnica de Machine Learning que permite:

- descubrir relaciones entre variables;
- analizar cómo unas variables se relacionan con otra;
- realizar predicciones sobre valores futuros.

En el curso se utiliza un ejemplo de **predicción de precios de viviendas**.

El objetivo es predecir el precio de una casa utilizando características como:

- cantidad de dormitorios;
- superficie;
- ubicación;
- otras características de la propiedad.

---

# 2. Antes de crear el modelo: preparar los datos

Antes de entrenar un modelo de Machine Learning, los datos deben estar preparados y organizados.

El curso destaca especialmente el uso de **Pandas** para esta etapa.

```text
Datos originales
       ↓
Limpieza
       ↓
Exploración
       ↓
Transformación
       ↓
Datos preparados
       ↓
Modelo de Machine Learning
```

> Un modelo no puede funcionar correctamente si los datos con los que se entrena tienen problemas importantes.

---

# 3. Pandas para preparar los datos

**Pandas** proporciona herramientas para:

- manipular datos;
- limpiar datos;
- transformar datos;
- explorar conjuntos de datos;
- trabajar con estructuras como `DataFrame`.

El curso utiliza Pandas para cargar el conjunto de datos y organizarlo antes de construir el modelo.

Un `DataFrame` permite trabajar con los datos en una estructura similar a una tabla:

```text
dormitorios | superficie | ubicación | precio
------------|------------|-----------|--------
2           | 80         | ...       | ...
3           | 120        | ...       | ...
4           | 180        | ...       | ...
```

---

# 4. Explorar los datos

Antes de entrenar el modelo, es importante conocer los datos.

El curso propone realizar una primera exploración para:

- observar la estructura del conjunto de datos;
- identificar posibles problemas;
- obtener estadísticas básicas;
- analizar la distribución de las variables.

Conceptualmente:

```text
Cargar datos
     ↓
Observar datos
     ↓
Estadísticas básicas
     ↓
Visualizar distribuciones
     ↓
Detectar problemas
```

---

# 5. Valores faltantes

Los conjuntos de datos reales pueden contener **valores faltantes**.

Estos valores pueden provocar análisis incompletos o afectar el rendimiento del modelo.

Por eso, antes de continuar es necesario identificar y gestionar los datos faltantes.

```text
Datos
 ↓
¿Hay valores faltantes?
 ↓
Sí → Gestionarlos
 ↓
Datos preparados
```

El curso destaca que este paso ayuda a mantener la integridad del análisis.

---

# 6. Crear o transformar características

En algunos casos puede ser necesario:

- crear nuevas características;
- transformar características existentes.

Estas modificaciones pueden ayudar a mejorar el rendimiento del modelo.

El curso relaciona esta etapa con el **conocimiento del dominio** y la creatividad del analista.

```text
Características originales
          ↓
Transformación / nuevas características
          ↓
Características útiles para el modelo
```

---

# 7. Variables independientes y variable objetivo

Antes de entrenar el modelo debemos separar:

### Variables independientes (`X`)

Son las características que utilizamos para realizar la predicción.

En el ejemplo:

```text
X =
- dormitorios
- superficie
- ubicación
- ...
```

### Variable objetivo (`y`)

Es el valor que queremos predecir.

En el ejemplo:

```text
y = precio de la vivienda
```

Por lo tanto:

```text
Características X
       ↓
Modelo de regresión lineal
       ↓
Precio estimado ŷ
```

---

# 8. Separar los datos: entrenamiento y prueba

Los datos se dividen en dos conjuntos:

### Training set

Se utiliza para **entrenar el modelo**.

### Test set

Se utiliza para **evaluar el modelo con datos que no utilizó durante el entrenamiento**.

```text
Dataset
   │
   ├──────────────► Training set
   │                    ↓
   │                 Entrenar
   │                    ↓
   │                  Modelo
   │
   └──────────────► Test set
                        ↓
                    Evaluar
```

Esto permite comprobar cómo funciona el modelo frente a datos nuevos.

---

# 9. Crear el modelo de regresión lineal

Una vez preparados los datos, se crea un modelo de **regresión lineal** utilizando `Scikit-learn`.

La idea general es:

```python
from sklearn.linear_model import LinearRegression

modelo = LinearRegression()

modelo.fit(X_train, y_train)
```

El método:

```python
modelo.fit(X_train, y_train)
```

utiliza los datos de entrenamiento para aprender la relación entre las características `X` y el objetivo `y`.

---

# 10. Realizar predicciones

Una vez entrenado el modelo, podemos utilizarlo para realizar predicciones sobre los datos de prueba.

```python
y_pred = modelo.predict(X_test)
```

Conceptualmente:

```text
X_test
  ↓
Modelo entrenado
  ↓
y_pred
```

`y_pred` contiene los valores que el modelo predijo.

---

# 11. Comparar predicciones con valores reales

Una forma de analizar el comportamiento del modelo es comparar:

- valores reales;
- valores predichos.

```text
Valor real       Predicción
   250000          245000
   300000          310000
   400000          390000
```

Cuanto más cercanas sean las predicciones a los valores reales, mejor será el comportamiento del modelo.

---

# 12. Visualización con Matplotlib

El curso utiliza `matplotlib.pyplot` para visualizar:

- valores reales;
- valores predichos.

Se puede utilizar un gráfico de dispersión:

```python
import matplotlib.pyplot as plt

plt.scatter(y_test, y_pred)
plt.xlabel("Valores reales")
plt.ylabel("Valores predichos")
plt.show()
```

El objetivo es visualizar la diferencia entre las predicciones y los valores reales.

---

# 13. Evaluar el modelo

No alcanza con entrenar un modelo y obtener predicciones.

También debemos **medir su rendimiento**.

En este ejemplo, el curso utiliza:

- **MSE (Mean Squared Error)**
- **R² (R-squared)**

Estas métricas permiten evaluar qué tan bien funciona el modelo de regresión.

---

# 14. MSE — Error Cuadrático Medio

El **MSE** mide el error promedio entre los valores predichos y los valores reales, elevando los errores al cuadrado.

Una característica importante es que:

> **Un MSE más bajo indica un mejor rendimiento.**

Por ejemplo:

```text
Modelo A → MSE = 10
Modelo B → MSE = 5
```

El modelo B presenta un MSE menor.

Por lo tanto:

```text
MSE menor
   ↓
Menor error promedio
   ↓
Mejor rendimiento
```

---

# 15. R² — R-squared

El **R²**, o coeficiente de determinación, indica qué tan bien se ajusta el modelo a los datos.

El curso destaca que:

> **Un valor de R² más alto, cercano a 1, indica un buen ajuste.**

Por ejemplo:

```text
Modelo A → R² = 0.60
Modelo B → R² = 0.90
```

Según esta métrica, el modelo B presenta un mejor ajuste.

```text
R² más alto
     ↓
Mejor ajuste
```

---

# 16. MSE vs. R²

Es importante no confundir la interpretación de estas métricas.

| Métrica | Mejor resultado |
|---|---|
| MSE | Más bajo |
| R² | Más alto, cercano a 1 |

Por ejemplo:

```text
MSE ↓  → mejor
R²  ↑  → mejor
```

---

# 17. Flujo completo del proyecto

El proceso presentado en el curso puede resumirse así:

```text
1. Cargar los datos
        ↓
2. Explorar los datos
        ↓
3. Limpiar los datos
        ↓
4. Gestionar valores faltantes
        ↓
5. Crear / transformar características
        ↓
6. Separar X e y
        ↓
7. Dividir Training / Test
        ↓
8. Crear modelo de regresión lineal
        ↓
9. Entrenar el modelo
        ↓
10. Realizar predicciones
        ↓
11. Visualizar resultados
        ↓
12. Evaluar con MSE y R²
```

---

# 18. Bibliotecas utilizadas

El curso menciona tres bibliotecas principales:

```python
import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression
```

Y para visualizar:

```python
import matplotlib.pyplot as plt
```

### Pandas

Se utiliza principalmente para:

```text
Carga
 ↓
Limpieza
 ↓
Transformación
 ↓
Exploración
```

### NumPy

Se utiliza para operaciones numéricas.

### Scikit-learn

Se utiliza para construir y entrenar el modelo de Machine Learning.

### Matplotlib

Se utiliza para visualizar los resultados.

---

# 19. Ejemplo completo simplificado

El flujo básico presentado en el curso puede representarse con este código:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


# Cargar los datos
df = pd.read_csv("housing.csv")


# Separar características y variable objetivo
X = df[["bedrooms", "sqft", "location"]]
y = df["price"]


# Dividir los datos
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)


# Crear el modelo
modelo = LinearRegression()


# Entrenar
modelo.fit(X_train, y_train)


# Realizar predicciones
y_pred = modelo.predict(X_test)


# Evaluar
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)


print("MSE:", mse)
print("R²:", r2)


# Visualizar
plt.scatter(y_test, y_pred)

plt.xlabel("Valores reales")
plt.ylabel("Valores predichos")

plt.show()
```

> **Nota:** el código es una representación simplificada del flujo mostrado en el curso. Los nombres exactos de las columnas dependen del dataset utilizado.

---

# 20. Ejemplo conceptual

Supongamos que queremos predecir el precio de una vivienda.

Tenemos:

```text
Dormitorios = 3
Superficie = 120 m²
Ubicación = X
```

Estos datos se introducen en el modelo:

```text
             ┌─────────────────┐
Dormitorios ─►                 │
Superficie  ─► Regresión lineal├──► Precio estimado
Ubicación   ─►                 │
             └─────────────────┘
```

El modelo aprende las relaciones existentes en los datos de entrenamiento y utiliza esas relaciones para generar una predicción.

Después comparamos:

```text
Precio real       Precio predicho
    300.000           290.000
```

y utilizamos las métricas para evaluar el rendimiento.

---

# 21. Ideas fundamentales del curso

### 1. Los datos son fundamentales

El éxito de Machine Learning no depende solamente del algoritmo.

La **calidad y preparación de los datos** son fundamentales.

### 2. Primero preparar, después modelar

```text
Datos → Limpieza → Exploración → Modelo
```

No debemos saltarnos la preparación de los datos.

### 3. Separar entrenamiento y prueba

El modelo debe evaluarse utilizando datos que no haya utilizado para entrenarse.

### 4. Las predicciones deben evaluarse

No alcanza con obtener `y_pred`.

Hay que comparar las predicciones con los valores reales.

### 5. MSE y R² tienen interpretaciones diferentes

```text
MSE → cuanto menor, mejor

R² → cuanto mayor y más cercano a 1, mejor
```

---

# 22. Conceptos que conviene recordar

```text
Pandas
→ preparación y exploración de datos

NumPy
→ operaciones numéricas

Scikit-learn
→ construcción y entrenamiento del modelo

Matplotlib
→ visualización

X
→ variables independientes / características

y
→ variable objetivo

Training set
→ datos utilizados para entrenar

Test set
→ datos utilizados para evaluar

y_pred
→ predicciones del modelo

MSE
→ mide el error; menor es mejor

R²
→ mide el ajuste; mayor es mejor
```

---

# 23. Idea principal

> **La regresión lineal permite aprender relaciones entre variables para realizar predicciones de valores continuos. Pero antes de construir el modelo, es fundamental preparar y comprender los datos.**

El flujo que debemos recordar es:

```text
DATOS
  ↓
Pandas
  ↓
Limpieza y exploración
  ↓
X e y
  ↓
Training / Test
  ↓
Regresión Lineal
  ↓
Predicciones
  ↓
MSE + R²
  ↓
Evaluación del modelo
```