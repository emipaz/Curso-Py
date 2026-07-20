# Manejo de Valores Duplicados en Python con Pandas

## Introducción

Los **valores duplicados** son uno de los problemas más comunes durante la limpieza de datos (*Data Cleaning*). Ocurren cuando un mismo registro aparece más de una vez en un conjunto de datos.

Estos duplicados pueden afectar significativamente la calidad del análisis, producir informes incorrectos y conducir a decisiones equivocadas.

---

# ¿Qué son los valores duplicados?

Un valor duplicado es cualquier dato que aparece más de una vez dentro de un conjunto de datos.

Los duplicados pueden presentarse como:

- Filas completas repetidas.
- Valores repetidos dentro de una columna.
- Registros parcialmente duplicados.

## Ejemplo

| ID | Nombre | Edad |
|----|---------|------|
| 1 | Juan | 30 |
| 2 | Ana | 25 |
| 1 | Juan | 30 |

La tercera fila es un duplicado de la primera.

---

# ¿Cómo se generan los duplicados?

## 1. Error humano

Una persona puede ingresar accidentalmente la misma información más de una vez.

### Ejemplo

```text
Juan Pérez
Juan Pérez
```

---

## 2. Integración de múltiples fuentes

Al combinar bases de datos diferentes, un mismo registro puede existir en ambas.

### Ejemplo

```text
Base de Datos A
---------------
Cliente: Juan

Base de Datos B
---------------
Cliente: Juan
```

Al fusionarlas aparecen duplicados.

---

## 3. Errores de software

Fallos en sistemas de captura o sincronización pueden generar registros repetidos.

---

## 4. Problemas de importación

Durante la carga de archivos CSV, Excel o bases de datos pueden insertarse registros varias veces.

---

# ¿Por qué son un problema?

## 1. Distorsionan los análisis estadísticos

Los duplicados alteran métricas importantes.

### Ejemplo

Edades reales:

```text
20, 30, 40
```

Promedio:

```text
30
```

Con duplicados:

```text
20, 30, 40, 40
```

Nuevo promedio:

```text
32.5
```

Resultado incorrecto.

---

## 2. Generan informes erróneos

Los reportes pueden mostrar:

- Más clientes de los reales.
- Más ventas de las realizadas.
- Más transacciones de las existentes.

---

## 3. Ocupan espacio innecesario

Los registros duplicados consumen almacenamiento adicional.

---

## 4. Reducen el rendimiento

Mayor cantidad de registros implica:

- Consultas más lentas.
- Procesamiento más costoso.
- Uso innecesario de memoria.

---

# Trabajando con duplicados en Pandas

## Importar Pandas

```python
import pandas as pd
```

---

## Cargar un archivo CSV

```python
df = pd.read_csv("datos.csv")
```

---

# Detectar duplicados

## Encontrar filas duplicadas

```python
duplicados = df.duplicated()
print(duplicados)
```

Resultado:

```text
0    False
1    False
2     True
```

- `False` → registro único.
- `True` → registro duplicado.

---

## Mostrar únicamente las filas duplicadas

```python
filas_duplicadas = df[df.duplicated()]
print(filas_duplicadas)
```

---

## Contar duplicados

```python
df.duplicated().sum()
```

Ejemplo:

```text
15
```

Significa que existen 15 filas duplicadas.

---

# Eliminar duplicados

## Mantener la primera ocurrencia (predeterminado)

```python
df = df.drop_duplicates()
```

Equivale a:

```python
df = df.drop_duplicates(keep="first")
```

---

## Mantener la última ocurrencia

```python
df = df.drop_duplicates(keep="last")
```

### Ejemplo

Antes:

| ID | Nombre |
|----|---------|
| 1 | Juan |
| 1 | Juan |

Después:

Se conserva la última fila.

---

## Eliminar todas las ocurrencias duplicadas

```python
df = df.drop_duplicates(keep=False)
```

### Ejemplo

Antes:

| ID | Nombre |
|----|---------|
| 1 | Juan |
| 1 | Juan |
| 2 | Ana |

Después:

| ID | Nombre |
|----|---------|
| 2 | Ana |

Todas las filas duplicadas desaparecen.

---

# Buscar duplicados según columnas específicas

A veces una fila completa no está duplicada, pero ciertas columnas sí.

## Ejemplo

```python
df.duplicated(subset=["email"])
```

Busca clientes con el mismo correo electrónico.

---

## Eliminar duplicados por una columna

```python
df = df.drop_duplicates(subset=["email"])
```

---

# Ejemplo completo

```python
import pandas as pd

# Cargar datos
df = pd.read_csv("clientes.csv")

# Mostrar cantidad de duplicados
print("Duplicados:", df.duplicated().sum())

# Mostrar registros duplicados
print(df[df.duplicated()])

# Eliminar duplicados
df = df.drop_duplicates()

# Guardar datos limpios
df.to_csv("clientes_limpios.csv", index=False)

print("Proceso completado.")
```

---

# Prevención de duplicados

Eliminar duplicados es importante, pero prevenirlos es aún mejor.

## 1. Mejorar la captura de datos

- Capacitar al personal.
- Utilizar formularios estandarizados.
- Automatizar procesos.

---

## 2. Validaciones de entrada

Verificar si el registro ya existe antes de guardarlo.

### Ejemplo

```python
if email in lista_emails:
    print("Cliente ya registrado")
```

---

## 3. Utilizar identificadores únicos

Cada registro debe poseer un identificador irrepetible.

### Ejemplos

- ID Cliente
- DNI
- CUIT
- UUID

---

## 4. Restricciones en bases de datos

### SQL

```sql
CREATE TABLE clientes (
    id INT PRIMARY KEY,
    email VARCHAR(100) UNIQUE
);
```

La restricción `UNIQUE` impide correos duplicados.

---

# Comparación de métodos

| Método | Objetivo |
|----------|----------|
| duplicated() | Detectar duplicados |
| drop_duplicates() | Eliminar duplicados |
| subset= | Revisar columnas específicas |
| keep="first" | Mantener primer registro |
| keep="last" | Mantener último registro |
| keep=False | Eliminar todos los duplicados |

---

# Flujo recomendado

```text
Datos originales
        ↓
Detectar duplicados
        ↓
Analizar impacto
        ↓
Identificar causa
        ↓
Eliminar duplicados
        ↓
Validar resultados
        ↓
Implementar controles preventivos
        ↓
Datos limpios
```

---

# Buenas prácticas

✅ Revisar duplicados antes de comenzar cualquier análisis.

✅ Utilizar identificadores únicos.

✅ Implementar validaciones durante la captura de datos.

✅ Documentar las reglas utilizadas para eliminar duplicados.

✅ Verificar el impacto de la eliminación sobre el análisis.

---

# Conclusiones

- Los valores duplicados son una fuente frecuente de errores en el análisis de datos.
- Pueden alterar estadísticas, informes y modelos de Machine Learning.
- Pandas proporciona herramientas sencillas para detectar y eliminar duplicados mediante `duplicated()` y `drop_duplicates()`.
- La prevención es tan importante como la corrección.
- Mantener datos libres de duplicados mejora la calidad, precisión y confiabilidad de cualquier proyecto de análisis de datos.