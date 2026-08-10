# Entrenamiento y pruebas con datos sintéticos en Python

## 1. ¿Por qué utilizar datos sintéticos?

En muchos proyectos de Machine Learning aparecen problemas relacionados con los datos.

Los principales problemas mencionados en el curso son:

- **Escasez de datos:** puede ser difícil obtener un conjunto de datos grande y diverso.
- **Privacidad:** los datos reales pueden contener información confidencial.
- **Desequilibrio de clases:** algunas clases pueden tener muchos más ejemplos que otras.
- **Datos ruidosos o incompletos:** pueden dificultar el entrenamiento del modelo.

Los datos sintéticos permiten generar datos artificiales que **imitan las propiedades estadísticas de los datos reales**.

> **Idea clave:** los datos sintéticos permiten aumentar y diversificar los datos disponibles para mejorar el entrenamiento y las pruebas de los modelos.

---

# 2. Problema 1: escasez de datos

Obtener una cantidad suficiente de datos reales puede ser difícil y llevar mucho tiempo.

Por ejemplo:

```text
Datos reales
    ↓
Cantidad limitada
    ↓
Pocos ejemplos para entrenar
    ↓
Modelo con dificultades para aprender

Los datos sintéticos permiten generar ejemplos adicionales:

Datos reales
    +
Datos sintéticos
    ↓
Conjunto de entrenamiento más grande
    ↓
Más ejemplos para aprender
```	

Los datos sintéticos deben imitar las propiedades estadísticas de los datos reales.

## 3. Problema 2: privacidad

En algunos proyectos trabajamos con información confidencial.

Ejemplos mencionados en el curso:

- Registros médicos.
- Información financiera.

Las normas de privacidad pueden restringir el uso de datos reales.

Los datos sintéticos permiten conservar los patrones esenciales de los datos sin utilizar directamente toda la información real.

```text	
Datos reales confidenciales
          ↓
Restricciones de privacidad
          ↓
Datos sintéticos
          ↓
Mantener patrones importantes
          +
Proteger la privacidad
```	

## 4. Problema 3: desequilibrio de clases

En problemas de clasificación puede ocurrir que una clase tenga muchos más ejemplos que otra.

Por ejemplo, en detección de fraude:

- Transacciones no fraudulentas → mayoría
- Transacciones fraudulentas    → minoría

Esto genera un desequilibrio de clases.

El problema es que el modelo puede aprender principalmente de la clase mayoritaria y funcionar peor al identificar la clase minoritaria.

Los datos sintéticos pueden utilizarse para aumentar la cantidad de ejemplos de la clase minoritaria.

Antes:

```text
Clase 0 → ████████████████████
Clase 1 → ██
```	

Después:

```text
Clase 0 → ████████████████████
Clase 1 → ████████████████████
```	

El objetivo es conseguir una distribución de clases más equilibrada.

## 5. Problema 4: datos incompletos o ruidosos

El curso también menciona el uso de datos sintéticos para introducir variaciones y aumentar el conjunto de datos existente.

Esto puede ayudar al modelo a gestionar mejor:

- Entradas ruidosas.
- Datos incompletos.
- Diferentes variaciones de los datos.

El curso denomina a este proceso aumento de datos, cuyo objetivo es ampliar o diversificar el conjunto de datos para mejorar el entrenamiento.

## 6. Ejemplo del curso: detección de fraude

El escenario práctico utilizado es la creación de un modelo para detectar transacciones fraudulentas con tarjetas de crédito.

Tenemos:

```text
Datos reales
    ↓
Cantidad limitada
    +
Desequilibrio importante entre clases
    ↓
Problemas para entrenar el modelo
```	

La variable objetivo es una variable binaria llamada class.

```text
class = 0 → transacción no fraudulenta
class = 1 → transacción fraudulenta
```

La mayoría de las transacciones pertenecen a la clase 0.

Por lo tanto:

- Clase 0 → mayoría
- Clase 1 → minoría

## 7. Bibliotecas utilizadas

El curso utiliza:

- SDV (Synthetic Data Vault) → generación de datos sintéticos.
- Scikit-learn → herramientas de Machine Learning.

La idea general es utilizar SDV para generar datos artificiales que se parezcan a la distribución de los datos reales.

## 8. Flujo general del proyecto

El proyecto puede representarse de esta manera:

```text
Datos reales
     ↓
Analizar problemas
     ↓
Escasez / desequilibrio
     ↓
Generar datos sintéticos
     ↓
Combinar datos reales + sintéticos
     ↓
Dataset aumentado
     ↓
Entrenar modelo
     ↓
Evaluar modelo
```	

Pero los datos sintéticos también pueden utilizarse durante las pruebas:

```text
Datos sintéticos
     ↓
Generar escenarios diferentes
     ↓
Casos extremos
     ↓
Posibles ataques adversarios
     ↓
Probar robustez del modelo
```	

## 9. Generación de datos sintéticos

El curso presenta una operación denominada:

- `Generate Synthetic Data`

El ejemplo genera 50 filas de datos sintéticos.

Conceptualmente:

´´´python
# Ejemplo conceptual basado en el flujo mostrado en el curso

from svd.single_table import GenerateSyntheticData

synthetic_data = GenerateSyntheticData(
    cantidad=50
)
```

Estos datos proporcionan material adicional para entrenar el modelo.

El curso explica el objetivo de generar las 50 filas, pero no presenta en el texto transcripto todos los detalles de implementación de la función utilizada.

## 10. Combinar datos reales y sintéticos

Después de generar los datos sintéticos, se combinan con los datos reales.

```text
Datos reales
     +
Datos sintéticos
     ↓
Datos aumentados
```	

Conceptualmente, en Python esto puede representarse mediante una concatenación:

```python
# Ejemplo conceptual basado en el flujo mostrado en el curso
	
import pandas as pd

datos_aumentados = pd.concat(
    [datos_reales, datos_sinteticos],
    ignore_index=True
)
```

El resultado es un único conjunto de datos con mayor cantidad de ejemplos.

## 11. Importante: misma cantidad de filas

El curso destaca una cuestión técnica importante:

Todas las columnas nuevas deben tener el mismo número de filas que los datos reales.

Si las columnas tienen diferentes cantidades de filas pueden aparecer errores al:

- Concatenar datos.
- Realizar análisis.
- Ejecutar diferentes operaciones sobre el DataFrame.

Por eso, antes de combinar los datos debemos comprobar que las dimensiones sean compatibles.

Por ejemplo:

```python
print(datos_reales.shape)
print(datos_sinteticos.shape)
```

Y después:

```python
datos_aumentados = pd.concat(
    [datos_reales, datos_sinteticos],
    ignore_index=True
)
```

## 12. ¿Qué conseguimos al combinar los datos?

Al combinar los datos reales y sintéticos obtenemos un conjunto:

- Más grande.
- Más diverso.
- Más equilibrado.

Esto proporciona al modelo más ejemplos de los que aprender.

```text
Datos reales
     │
     ├── Información existente
     │
     └──────────────┐
                    ↓
             Datos aumentados
                    ↑
     ┌──────────────┘
     │
Datos sintéticos
     │
     ├── Más ejemplos
     ├── Mayor diversidad
     └── Equilibrio de clases
```

## 13. Datos sintéticos durante el entrenamiento

Los datos sintéticos pueden utilizarse para aumentar el conjunto de entrenamiento.

En el ejemplo de fraude:

```text
Datos reales
     ↓
Datos sintéticos
     ↓
Equilibrar clases
     ↓
Combinar
     ↓
Dataset de entrenamiento
     ↓
Entrenar modelo de detección de fraude
```



El objetivo es que el modelo tenga más oportunidades de aprender las características de ambas clases:

```text
Transacciones legítimas
        +
Transacciones fraudulentas
        ↓
Modelo de detección de fraude
```

## 14. Datos sintéticos durante las pruebas

Una idea importante del curso es que los datos sintéticos no solamente sirven para entrenar modelos.

También pueden utilizarse durante la fase de prueba.

Podemos generar datos sintéticos que representen:

- Diferentes escenarios.
- Casos extremos.
- Posibles ataques adversarios.

Esto permite evaluar la robustez del modelo.

```text
Modelo entrenado
       ↓
Datos de prueba sintéticos
       ↓
Escenarios variados
       ↓
Casos extremos
       ↓
Posibles vulnerabilidades
```

## 15. ¿Qué significa robustez?

En el contexto presentado por el curso, la robustez está relacionada con la capacidad del modelo para mantener un buen comportamiento frente a diferentes condiciones.

Las pruebas con datos sintéticos pueden revelar vulnerabilidades que quizás no aparezcan utilizando únicamente los datos normales.

```text
Datos de prueba normales
        ↓
Evaluación

Datos sintéticos variados
        ↓
Casos extremos
        ↓
Detectar vulnerabilidades
        ↓
Mejorar el modelo
```

## 16. Ataques adversarios

El curso menciona específicamente la posibilidad de generar datos de prueba que representen posibles ataques adversarios.

El objetivo es utilizar estos datos para:

- Evaluar la robustez.
- Detectar vulnerabilidades.
- Ajustar el modelo.
- Mejorar su resiliencia.

La idea general es:

```text
Modelo
  ↓
Ataques / escenarios sintéticos
  ↓
Observar comportamiento
  ↓
Detectar vulnerabilidades
  ↓
Mejorar modelo
```

## 17. Impacto de los datos sintéticos

Según el curso, la utilización de datos sintéticos puede mejorar diferentes aspectos del proyecto.

### Precisión

Al equilibrar la distribución de las clases, el modelo puede funcionar mejor tanto para las transacciones fraudulentas como para las no fraudulentas.

###Robustez

Las pruebas con escenarios sintéticos pueden revelar vulnerabilidades.

Esto permite mejorar la capacidad del modelo para resistir diferentes situaciones.

### Generalización

El aumento y la diversificación de los datos pueden ayudar al modelo a funcionar en diferentes condiciones.

### Velocidad de desarrollo

La generación de datos sintéticos proporciona un conjunto de datos disponible rápidamente.

Esto puede acelerar el desarrollo del proyecto.

## 18.  Resumen del caso de fraude

```text	
PROBLEMA
──────────────────────────────
Pocos datos reales
        +
Desequilibrio de clases
        +
Necesidad de probar diferentes escenarios
```

```text
SOLUCIÓN
──────────────────────────────
Generar datos sintéticos con SDV
        ↓
Aumentar los datos
        ↓
Equilibrar las clases
        ↓
Combinar datos reales + sintéticos
        ↓
Entrenar el modelo
        ↓
Generar datos sintéticos de prueba
        ↓
Evaluar casos extremos
        ↓
Detectar vulnerabilidades
        ↓
Mejorar el modelo
```

## 19. Concepto importante: los datos sintéticos NO sustituyen a los reales

Esta es una de las conclusiones principales del curso.

Los datos sintéticos no sustituyen a los datos reales. Son un complemento valioso.

La idea es:

```text
Datos reales
     +
Datos sintéticos
     ↓
Mejor conjunto de entrenamiento y pruebas
```

Los datos reales siguen siendo importantes porque representan situaciones reales.

Los datos sintéticos permiten complementar esos datos cuando existen limitaciones.

## 20. Ejemplo completo conceptual en Python

El flujo presentado en el curso puede resumirse con un código conceptual:

```python
import pandas as pd

# Datos reales
datos_reales = pd.read_csv("transacciones.csv")

# Generar datos sintéticos
# La implementación concreta depende de SDV
datos_sinteticos = generar_datos_sinteticos(
    datos_reales,
    cantidad=50
)

# Combinar datos reales y sintéticos
datos_aumentados = pd.concat(
    [
        datos_reales,
        datos_sinteticos
    ],
    ignore_index=True
)

# Comprobar dimensiones
print("Datos reales:", datos_reales.shape)
print("Datos sintéticos:", datos_sinteticos.shape)
print("Datos aumentados:", datos_aumentados.shape)
```



Este código representa el flujo conceptual explicado en el curso: generar datos sintéticos y combinarlos con los datos reales.

## 21. Flujo de Machine Learning con datos sintéticos

Una visión completa sería:


```text
                 DATOS REALES
                      │
                      ↓
              Analizar el dataset
                      │
          ┌───────────┼───────────┐
          ↓           ↓           ↓
       Escasez   Desequilibrio  Privacidad
          │           │           │
          └───────────┼───────────┘
                      ↓
             DATOS SINTÉTICOS
                      │
                      ↓
              Aumentar dataset
                      │
                      ↓
          Datos reales + sintéticos
                      │
                      ↓
             Entrenamiento
                      │
                      ↓
                  MODELO
                      │
                      ↓
             Datos de prueba
                      │
                      ↓
        Datos sintéticos adicionales
                      │
                      ↓
          Casos extremos / ataques
                      │
                      ↓
                EVALUACIÓN
                      │
                      ↓
           Mejorar y ajustar modelo
```

## 22. Ideas fundamentales del vídeo

1. Los datos sintéticos son datos artificiales que imitan propiedades
   de los datos reales.

2. Pueden utilizarse cuando existe escasez de datos.

3. Pueden ayudar a trabajar con información confidencial
   preservando los patrones esenciales.

4. Pueden utilizarse para abordar el desequilibrio de clases.

5. También pueden utilizarse para aumentar y diversificar
   conjuntos de datos.

6. SDV (Synthetic Data Vault) es la biblioteca utilizada en
   el ejemplo para generar datos sintéticos.

7. Los datos sintéticos pueden combinarse con datos reales
   para crear un dataset aumentado.

8. También pueden utilizarse durante las pruebas del modelo.

9. Los datos sintéticos de prueba pueden representar casos
   extremos y posibles ataques adversarios.

10. Pueden contribuir a mejorar la precisión, robustez,
    generalización y velocidad de desarrollo.

11. Los datos sintéticos no sustituyen a los datos reales.

12. Son un complemento que permite aprovechar mejor los
    modelos de Machine Learning.
23. Idea final

Los datos sintéticos permiten ampliar y diversificar los datos disponibles, equilibrar clases y crear escenarios de prueba que serían difíciles, costosos, peligrosos o imposibles de obtener en el mundo real.

En el ejemplo del curso:

```text
Fraude con tarjetas
       ↓
Datos reales limitados
       +
Clases desequilibradas
       ↓
SDV genera datos sintéticos
       ↓
Datos reales + sintéticos
       ↓
Entrenamiento
       ↓
Datos sintéticos de prueba
       ↓
Casos extremos y ataques adversarios
       ↓
Evaluación
       ↓
Modelo más robusto
```

## Conclusió:

Los datos sintéticos son una herramienta poderosa para mejorar proyectos de Machine Learning, tanto en la fase de entrenamiento como en la fase de prueba, pero deben utilizarse como complemento de los datos reales y no como sustituto.