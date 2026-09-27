# Datos sintéticos: privacidad y uso responsable

## 1. Problema: pocos datos reales

El escenario plantea un proyecto de **detección de fraudes** para un cliente que dispone de muy pocos datos reales.

Los datos reales son muy valiosos para Machine Learning, pero pueden ser difíciles de obtener, especialmente en sectores sensibles como:

- Finanzas
- Salud
- Información personal

Por este motivo aparecen los **datos sintéticos**.

---

## 2. ¿Qué son los datos sintéticos?

Los datos sintéticos son datos **generados artificialmente** que buscan reproducir características y patrones de los datos reales.

Una analogía utilizada en el curso es:

> En lugar de tomar fotografías de miles de pájaros para entrenar un modelo, podemos crear pájaros digitales realistas.

La idea sería:

```text
DATOS REALES
     ↓
Patrones y características
     ↓
Generación de datos sintéticos
     ↓
DATOS SINTÉTICOS
```

Los datos sintéticos pueden utilizarse para ampliar los datos disponibles cuando conseguir datos reales resulta difícil.

## 3. ¿Son simplemente datos inventados?

No exactamente.

El objetivo de los datos sintéticos no es generar información completamente aleatoria, sino crear datos que reproduzcan patrones y características relevantes de la realidad.

Por ejemplo, en un sistema de fraude:

```text	
Datos reales
    ↓
Patrones de transacciones
    ↓
Datos sintéticos
    ↓
Nuevos ejemplos para entrenar o probar modelos
```

Por eso el curso los describe como una especie de "espejo digital de la realidad".

## 4. El problema de la privacidad

En el caso de datos financieros, la privacidad es especialmente importante.

Los datos pueden contener información sensible que permita identificar o conocer detalles de personas concretas.

Por eso, además de generar datos sintéticos, es importante utilizarlos de manera responsable.

El curso menciona dos conceptos:

- Anonimización
- Privacidad diferencial

## 5. Anonimización

La anonimización consiste, según la explicación del curso, en eliminar información que permita identificar directamente a una persona.

Por ejemplo:

```text
ANTES

Nombre: Juan Pérez
Dirección: Calle X
Edad: 42
Monto: 1500


DESPUÉS

Edad: 42
Monto: 1500
```

Se eliminan datos como:

- nombres
- direcciones
- Información personal o sensible

La idea es conservar los patrones y tendencias sin identificar directamente a un individuo.

## 6. Privacidad diferencial

La privacidad diferencial es una técnica más compleja.

La explicación del curso la presenta como la incorporación de una capa de ruido cuidadosamente calculada a los datos.

Conceptualmente:

```text
Datos
  ↓
Agregar ruido controlado
  ↓
Datos con protección de privacidad
```

	

El objetivo es dificultar que alguien pueda realizar ingeniería inversa para descubrir información específica sobre una persona.

## 7. Anonimización vs. privacidad diferencial

| Concepto                   | Idea principal                                                                                                      |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Anonimización**          | Eliminar información que identifica directamente a una persona                                                      |
| **Privacidad diferencial** | Agregar ruido cuidadosamente calculado para dificultar la identificación o reconstrucción de información individual |


Ambas técnicas buscan reducir los riesgos relacionados con la privacidad.

## 8. Datos sintéticos + privacidad

El objetivo es encontrar un equilibrio:

```text	
             DATOS
               │
       ┌───────┴────────┐
       │                │
   Utilidad          Privacidad
       │                │
       └───────┬────────┘
               ↓
       Uso responsable
       de los datos
```

La idea central del vídeo es que los datos sintéticos pueden ofrecer nuevas posibilidades para trabajar con datos, pero no deben utilizarse sin considerar los aspectos éticos y de privacidad.

## 9. Aplicación al fraude financiero

El escenario planteado es:

```text
PROBLEMA
   ↓
Pocos datos reales de fraude
   +
Datos financieros sensibles
   ↓
Dificultad para entrenar modelos
   ↓
DATOS SINTÉTICOS
   ↓
Más posibilidades para desarrollar
modelos de detección de fraude
```

Los datos sintéticos pueden ayudar a superar la falta de datos disponibles, mientras que técnicas relacionadas con la privacidad buscan reducir los riesgos asociados con información sensible.

## 10. Idea fundamental del vídeo

La idea principal es:

Los datos sintéticos pueden ampliar las posibilidades del Machine Learning cuando los datos reales son escasos o sensibles, pero deben utilizarse de manera responsable y teniendo en cuenta la privacidad.

El curso presenta esta combinación como:

```text
Datos sintéticos
        +
Anonimización
        +
Privacidad diferencial
        ↓
Uso responsable de los datos
        ↓
Innovación con menor riesgo
```


## Conceptos que debemos recordar

- Datos sintéticos: datos generados artificialmente que buscan reproducir patrones de datos reales.
- Anonimización: eliminación de información personal que permite identificar directamente a una persona.
- Privacidad diferencial: incorporación de ruido cuidadosamente calculado para proteger información individual.
- Uso responsable: aprovechar los datos para innovar sin ignorar los riesgos de privacidad y ética.
- Aplicación del curso: detección de fraude financiero con pocos datos reales.
