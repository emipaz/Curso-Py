# Datos sintéticos con SDV en Python

## 1. ¿Qué es SDV?

**SDV (Synthetic Data Vault)** es una biblioteca de Python que permite crear **datos sintéticos** a partir de datos reales.

https://github.com/sdv-dev/SDV/



La idea básica es:

```text
Datos reales
     ↓
SDV aprende sus patrones
     ↓
Modelo generativo
     ↓
Datos sintéticos
```

Los datos sintéticos no son simplemente una copia de los datos originales.

El objetivo es generar nuevos registros que mantengan características y relaciones similares a los datos reales.

Por ejemplo, si tenemos:

| edad | monto | país | fraude |
|---:|---:|---|---:|
| 25 | 120 | AR | 0 |
| 41 | 350 | AR | 0 |
| 67 | 2500 | US | 1 |
| 52 | 1800 | BR | 1 |

SDV puede aprender patrones de este conjunto y generar nuevos registros similares:

| edad | monto | país | fraude |
|---:|---:|---|---:|
| 31 | 145 | AR | 0 |
| 45 | 420 | AR | 0 |
| 63 | 2310 | US | 1 |
| 56 | 1700 | BR | 1 |

Los registros generados son **sintéticos**.

---

# 2. ¿Para qué utilizar datos sintéticos?

El curso presenta principalmente cuatro problemas:

### Escasez de datos

Puede que tengamos pocos datos reales disponibles.

Los datos sintéticos permiten aumentar el conjunto de entrenamiento.

```text
1000 registros reales
        ↓
       SDV
        ↓
5000 registros sintéticos
        ↓
Conjunto aumentado
```

---

### Privacidad

En determinados sectores los datos reales pueden ser sensibles.

Por ejemplo:

- datos médicos
- información financiera
- información de clientes

Los datos sintéticos pueden utilizarse para desarrollar y probar modelos reduciendo la necesidad de trabajar directamente con determinados datos reales.

**Importante:** generar datos sintéticos no significa automáticamente que exista privacidad perfecta. La calidad y las garantías de privacidad deben evaluarse según el método utilizado.

---

### Desequilibrio de clases

Un problema muy común en clasificación.

Por ejemplo:

```text
Transacciones reales

No fraude:  99.000
Fraude:      1.000
```

El modelo tiene muchos ejemplos de transacciones normales pero pocos ejemplos de fraude.

Los datos sintéticos pueden utilizarse para aumentar la cantidad de ejemplos de la clase minoritaria.

```text
Antes:

No fraude  ████████████████████ 99.000
Fraude     █                    1.000


Después:

No fraude  ████████████████████ 99.000
Fraude     █████████████████     20.000
```

Esto puede ayudar al modelo a aprender mejor los patrones asociados con el fraude.

---

### Datos faltantes o insuficientes

Los datos sintéticos también pueden utilizarse como parte de estrategias para ampliar o diversificar los datos disponibles.

Esto puede ayudar cuando los datos originales son:

- escasos
- incompletos
- poco variados
- difíciles de obtener

---

# 3. Instalar SDV

Lo recomendable es instalar SDV en un entorno virtual separado.

## Windows

Crear un entorno virtual:

```bash
python -m venv .venv
```

Activarlo:

```bash
.venv\Scripts\activate
```

Actualizar `pip`:

```bash
python -m pip install --upgrade pip
```

Instalar SDV:

```bash
pip install sdv
```

También podemos instalar pandas:

```bash
pip install pandas
```

---

## Linux / WSL

Crear el entorno:

```bash
python3 -m venv .venv
```

Activarlo:

```bash
source .venv/bin/activate
```

Actualizar `pip`:

```bash
python -m pip install --upgrade pip
```

Instalar SDV:

```bash
pip install sdv
```

---

## Verificar la instalación

```python
import sdv

print(sdv.__version__)
```

Si aparece un número de versión, SDV está instalado correctamente.

La documentación oficial recomienda utilizar un entorno virtual independiente cuando aparecen conflictos de dependencias. :contentReference[oaicite:1]{index=1}

---

# 4. Ejemplo práctico: detectar fraude

Supongamos que un banco tiene información sobre transacciones.

Tenemos las siguientes variables:

```text
edad
monto
horas_desde_ultima_transaccion
pais
fraude
```

La variable:

```text
fraude
```

es nuestra variable objetivo.

Por ejemplo:

```text
0 → transacción legítima
1 → transacción fraudulenta
```

---

# 5. Crear un pequeño conjunto de datos

Para aprender podemos crear un ejemplo artificial pequeño.

```python
import pandas as pd

data = pd.DataFrame({
    "edad": [25, 31, 45, 52, 67, 23, 39, 58],
    "monto": [120, 250, 450, 1800, 2500, 90, 320, 2100],
    "horas_desde_ultima_transaccion": [
        12, 8, 5, 1, 2, 15, 7, 1
    ],
    "pais": [
        "AR", "AR", "AR", "BR",
        "US", "AR", "AR", "US"
    ],
    "fraude": [
        0, 0, 0, 1,
        1, 0, 0, 1
    ]
})

print(data)
```

El resultado representa transacciones reales simplificadas.

---

# 6. Crear los metadatos

SDV necesita conocer la estructura de nuestro DataFrame.

```python
from sdv.metadata import Metadata

metadata = Metadata.detect_from_dataframe(data)
```

Los metadatos describen información sobre las columnas del DataFrame.

Por ejemplo:

```text
edad                         → numérica
monto                        → numérica
horas_desde_ultima_transaccion → numérica
pais                         → categórica
fraude                       → categórica/binaria
```

---

# 7. Crear el sintetizador

SDV dispone de diferentes sintetizadores.

Para comenzar utilizaremos:

```python
GaussianCopulaSynthesizer
```

Importamos:

```python
from sdv.single_table import GaussianCopulaSynthesizer
```

Creamos el modelo:

```python
synthesizer = GaussianCopulaSynthesizer(
    metadata
)
```

---

# 8. Entrenar SDV

Ahora SDV aprende los patrones de nuestros datos reales.

```python
synthesizer.fit(data)
```

Conceptualmente:

```text
                 DATOS REALES
                      │
                      ▼
              ┌───────────────┐
              │      SDV      │
              │               │
              │ aprende       │
              │ distribuciones│
              │ y relaciones  │
              └───────┬───────┘
                      │
                      ▼
             MODELO SINTÉTICO
```

La documentación de SDV describe justamente este proceso como:

1. crear el sintetizador a partir de los metadatos
2. entrenarlo con los datos reales
3. generar nuevos datos sintéticos

:contentReference[oaicite:2]{index=2}

---

# 9. Generar datos sintéticos

Ahora podemos generar nuevos registros.

Por ejemplo, 50 filas:

```python
synthetic_data = synthesizer.sample(
    num_rows=50
)
```

Podemos observarlas:

```python
print(synthetic_data.head())
```

O:

```python
synthetic_data.info()
```

---

# 10. Comparar datos reales y sintéticos

Podemos comparar algunas estadísticas.

```python
print("Datos reales:")
print(data.describe())

print("\nDatos sintéticos:")
print(synthetic_data.describe())
```

También podemos observar la distribución de la variable `fraude`:

```python
print("Datos reales:")
print(data["fraude"].value_counts())

print("\nDatos sintéticos:")
print(synthetic_data["fraude"].value_counts())
```

Esto nos permite comprobar si los datos generados mantienen aproximadamente las características de los datos originales.

---

# 11. Combinar datos reales y sintéticos

Una de las aplicaciones que muestra el curso es aumentar el conjunto de entrenamiento.

Podemos hacer:

```python
data_aumentada = pd.concat(
    [data, synthetic_data],
    ignore_index=True
)
```

Ahora:

```python
print(data.shape)
print(synthetic_data.shape)
print(data_aumentada.shape)
```

Conceptualmente:

```text
DATOS REALES
     +
DATOS SINTÉTICOS
     ↓
DATOS AUMENTADOS
     ↓
ENTRENAMIENTO DEL MODELO
```

---

# 12. Ejemplo aplicado al fraude

Supongamos que tenemos:

```text
Datos reales:

99.000 transacciones normales
 1.000 transacciones fraudulentas
```

Existe un fuerte desequilibrio.

Podemos utilizar datos sintéticos para aumentar la clase minoritaria.

La idea sería:

```text
                     DATOS REALES
                          │
             ┌────────────┴────────────┐
             │                         │
          FRAUDE                  NO FRAUDE
           1.000                   99.000
             │
             ▼
          SDV
             │
             ▼
     DATOS SINTÉTICOS
        DE FRAUDE
             │
             ▼
     AUMENTAR TRAINING
```

El objetivo es proporcionar al modelo más ejemplos de situaciones fraudulentas.

---

# 13. SDV no reemplaza al modelo de Machine Learning

Es importante separar dos conceptos.

SDV genera datos.

Por ejemplo:

```text
SDV
 ↓
datos sintéticos
```

Después podemos utilizar esos datos para entrenar otro modelo:

```text
Datos reales
     +
Datos sintéticos
     ↓
Modelo de Machine Learning
     ↓
Predicción de fraude
```

Por ejemplo, podríamos utilizar:

- Logistic Regression
- Decision Tree
- Random Forest
- Neural Network

SDV no es necesariamente el modelo final que predice el fraude.

---

# 14. Ejemplo completo simplificado

```python
import pandas as pd

from sdv.metadata import Metadata
from sdv.single_table import GaussianCopulaSynthesizer


# --------------------------------
# 1. Datos reales
# --------------------------------

data = pd.DataFrame({
    "edad": [25, 31, 45, 52, 67, 23, 39, 58],
    "monto": [120, 250, 450, 1800, 2500, 90, 320, 2100],
    "horas_desde_ultima_transaccion": [
        12, 8, 5, 1, 2, 15, 7, 1
    ],
    "pais": [
        "AR", "AR", "AR", "BR",
        "US", "AR", "AR", "US"
    ],
    "fraude": [
        0, 0, 0, 1,
        1, 0, 0, 1
    ]
})


# --------------------------------
# 2. Detectar metadatos
# --------------------------------

metadata = Metadata.detect_from_dataframe(data)


# --------------------------------
# 3. Crear sintetizador
# --------------------------------

synthesizer = GaussianCopulaSynthesizer(
    metadata
)


# --------------------------------
# 4. Entrenar con datos reales
# --------------------------------

synthesizer.fit(data)


# --------------------------------
# 5. Generar datos sintéticos
# --------------------------------

synthetic_data = synthesizer.sample(
    num_rows=50
)


# --------------------------------
# 6. Mostrar datos sintéticos
# --------------------------------

print(synthetic_data.head())


# --------------------------------
# 7. Combinar datos
# --------------------------------

data_aumentada = pd.concat(
    [data, synthetic_data],
    ignore_index=True
)


print("Datos reales:", data.shape)
print("Datos sintéticos:", synthetic_data.shape)
print("Datos aumentados:", data_aumentada.shape)
```

---

# 15. ¿Qué está pasando realmente?

El flujo completo puede entenderse así:

```text
              DATOS REALES
                   │
                   ▼
             ┌───────────┐
             │  Metadata │
             └─────┬─────┘
                   │
                   ▼
             ┌───────────┐
             │    SDV    │
             │           │
             │   fit()   │
             └─────┬─────┘
                   │
             Aprende patrones
             de los datos
                   │
                   ▼
             ┌───────────┐
             │   sample  │
             └─────┬─────┘
                   │
                   ▼
          DATOS SINTÉTICOS
                   │
                   ▼
       ┌─────────────────────┐
       │ Datos reales        │
       │        +            │
       │ Datos sintéticos    │
       └──────────┬──────────┘
                  │
                  ▼
          MODELO DE MACHINE
             LEARNING
                  │
                  ▼
             PREDICCIONES
```

---

# 16. ¿Qué sintetizador estamos utilizando?

En este ejemplo utilizamos:

```python
GaussianCopulaSynthesizer
```

Es un sintetizador basado en métodos estadísticos que aprende las distribuciones de las columnas y las relaciones entre ellas.

La documentación de SDV lo recomienda como un buen punto de partida para datos tabulares por su rapidez, calidad y facilidad de personalización. :contentReference[oaicite:3]{index=3}

SDV también dispone de otros sintetizadores, por ejemplo:

```text
GaussianCopulaSynthesizer
        ↓
Métodos estadísticos

CTGANSynthesizer
        ↓
GAN / Deep Learning

TVAESynthesizer
        ↓
Variational Autoencoder
```

Para empezar a aprender, **GaussianCopulaSynthesizer es una opción mucho más sencilla** que empezar directamente con GANs.

---

# 17. Datos sintéticos para entrenamiento y pruebas

Los datos sintéticos pueden utilizarse en dos momentos diferentes.

## Entrenamiento

Podemos aumentar los datos disponibles:

```text
Datos reales
     +
Datos sintéticos
     ↓
TRAIN
     ↓
Modelo
```

Esto puede ayudar cuando tenemos pocos datos o clases desequilibradas.

---

## Pruebas

También podemos generar escenarios adicionales:

```text
Modelo entrenado
       ↓
Datos sintéticos
       ↓
TEST
       ↓
Evaluar comportamiento
```

Por ejemplo, podemos utilizar datos sintéticos para explorar escenarios poco frecuentes o casos extremos.

El objetivo es comprobar si el modelo mantiene un comportamiento adecuado en situaciones diferentes.

---

# 18. Una advertencia importante

Los datos sintéticos **no sustituyen automáticamente a los datos reales**.

La idea correcta es:

```text
Datos reales
      +
Datos sintéticos
      ↓
Mayor cantidad y variedad de ejemplos
```

Pero siempre debemos comprobar que los datos sintéticos sean suficientemente representativos.

Un modelo podría aprender patrones incorrectos si los datos sintéticos no representan adecuadamente la realidad.

Por eso debemos comparar:

- distribuciones
- proporciones de clases
- relaciones entre variables
- valores extremos
- rendimiento del modelo

---

# 19. Idea fundamental del curso

La idea que debemos recordar es:

> **Los datos sintéticos son un complemento de los datos reales que puede ayudar a superar problemas de escasez, privacidad y desequilibrio de clases.**

El flujo general es:

```text
PROBLEMA
   │
   ├── pocos datos
   ├── datos sensibles
   ├── clases desequilibradas
   └── poca variedad
          │
          ▼
       DATOS
      SINTÉTICOS
          │
          ▼
    DATASET AUMENTADO
          │
          ▼
    MACHINE LEARNING
          │
          ▼
       MODELO
          │
          ▼
     PREDICCIONES
```

## Fuentes

- Documentación oficial de SDV: instalación y primeros pasos. :contentReference[oaicite:4]{index=4}
- Documentación de `GaussianCopulaSynthesizer`. :contentReference[oaicite:5]{index=5}
- Documentación general sobre el flujo de modelado de SDV. :contentReference[oaicite:6]{index=6}