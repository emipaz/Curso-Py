# Explicación de la Indexación en Pandas

## Introducción

La indexación es uno de los conceptos más importantes de **Pandas**, ya que permite localizar, seleccionar, filtrar y modificar datos dentro de un DataFrame de forma rápida y eficiente.

En conjuntos de datos grandes, una buena indexación permite acceder directamente a la información deseada sin recorrer todo el DataFrame, mejorando significativamente el rendimiento y la productividad.

---

# ¿Por qué es importante la indexación?

Los conjuntos de datos modernos pueden contener:

- Miles de filas.
- Millones de registros.
- Cientos de columnas.

La indexación actúa como un sistema de búsqueda que permite:

- ✅ Encontrar datos rápidamente.
- ✅ Filtrar información relevante.
- ✅ Realizar análisis complejos.
- ✅ Transformar datos eficientemente.
- ✅ Mejorar el rendimiento de las consultas.

---

# Métodos principales de indexación

Pandas ofrece dos métodos fundamentales:

## 1. `.loc[]` → Indexación basada en etiquetas

Utiliza los nombres reales de filas y columnas.

### Sintaxis

```python
df.loc[fila, columna]
```

### Ejemplo

```python
df.loc["customer_123", "purchase_amount"]
```

Obtiene:

```text
Importe de compra del cliente customer_123
```

### Ventajas

- Más legible.
- Fácil de entender.
- Ideal cuando los índices tienen significado.

---

## 2. `.iloc[]` → Indexación basada en posiciones

Utiliza posiciones numéricas comenzando desde cero.

### Sintaxis

```python
df.iloc[fila, columna]
```

### Ejemplo

```python
df.iloc[5, 2]
```

Obtiene:

```text
Fila 6, columna 3
```

### Ventajas

- Independiente de las etiquetas.
- Útil cuando los índices no son relevantes.
- Ideal para seleccionar rangos por posición.

---

# Comparación rápida

| Método | Basado en |
|----------|------------|
| `.loc[]` | Etiquetas |
| `.iloc[]` | Posiciones numéricas |

### Ejemplo

Supongamos:

| Índice | Nombre | Edad |
|---------|---------|------|
| A | Ana | 25 |
| B | Luis | 30 |

```python
df.loc["A"]
```

Devuelve:

```text
Ana
25
```

Mientras que:

```python
df.iloc[0]
```

Devuelve la primera fila independientemente de su etiqueta.

---

# Indexación Booleana

Permite filtrar datos usando condiciones.

También se conoce como:

- Boolean Indexing
- Masking

---

## Ejemplo simple

Seleccionar clientes con más de 10 compras:

```python
df[df["number_of_purchases"] > 10]
```

---

## Varias condiciones

Clientes Platino con más de 10 compras:

```python
df[
    (df["membership_level"] == "Platinum")
    &
    (df["number_of_purchases"] > 10)
]
```

---

# Operadores booleanos

| Operador | Significado |
|-----------|------------|
| `&` | AND |
| \| | OR |
| `~` | NOT |

### Ejemplo

```python
df[
    (df["edad"] > 30)
    &
    (df["ciudad"] == "Madrid")
]
```

---

# Acceso rápido a valores individuales

## `.at[]`

Acceso por etiqueta.

```python
df.at["customer_123", "email"]
```

---

## `.iat[]`

Acceso por posición.

```python
df.iat[5, 2]
```

---

# ¿Por qué usar `.at` y `.iat`?

Están optimizados para:

- Recuperar un único valor.
- Modificar una sola celda.
- Mejor rendimiento.

---

# Modificación de datos

La indexación también permite actualizar valores.

### Ejemplo

Actualizar nivel de membresía:

```python
df.loc[
    "customer_123",
    "membership_level"
] = "Gold"
```

Resultado:

```text
customer_123 → Gold
```

---

# Indexación Multinivel (MultiIndex)

Permite trabajar con estructuras jerárquicas.

Ejemplo:

```text
Año
 └── Mes
      └── Producto
```

### Casos de uso

- Ventas por región y año.
- Datos financieros.
- Series temporales complejas.

---

## Ejemplo conceptual

```python
df.loc[(2025, "Enero")]
```

Permite acceder directamente a un nivel específico de la jerarquía.

---

# Método `query()`

Ofrece una sintaxis similar a SQL.

---

## Ejemplo tradicional

```python
df[
    (df["edad"] > 30)
    &
    (df["ciudad"] == "Madrid")
]
```

---

## Con `query()`

```python
df.query(
    "edad > 30 and ciudad == 'Madrid'"
)
```

### Ventajas

- Más legible.
- Similar a SQL.
- Útil para consultas complejas.

---

# Caso práctico 1: Ventas

Obtener ventas totales del Producto A en la región Norte:

```python
total_sales = (
    df.loc[
        (df["Product"] == "Product A")
        &
        (df["Region"] == "North")
    ]["Sales"]
    .sum()
)
```

Resultado:

```text
Ventas totales de Producto A en Norte
```

---

# Caso práctico 2: Atención al cliente

Obtener correo y teléfono de John Doe:

```python
customer_info = df.loc[
    df["Name"] == "John Doe",
    ["Email", "Phone"]
]
```

Resultado:

| Email | Phone |
|---------|--------|
| ... | ... |

---

# Buenas prácticas

## 1. Elegir el método correcto

| Situación | Método |
|------------|---------|
| Buscar por nombre | `.loc` |
| Buscar por posición | `.iloc` |
| Filtrar datos | Boolean Indexing |
| Valor único | `.at` / `.iat` |

---

## 2. Encadenar operaciones

```python
resultado = (
    df[df["ventas"] > 100]
    .sort_values("ventas")
    .head(10)
)
```

Beneficios:

- Menos variables temporales.
- Código más limpio.

---

## 3. Priorizar claridad

Evitar expresiones excesivamente complejas.

✔ Fácil de leer.

✔ Fácil de mantener.

---

## 4. Gestionar valores faltantes

Antes de indexar:

```python
df.fillna(0)
```

o

```python
df.dropna()
```

Evita errores inesperados.

---

## 5. Aprovechar MultiIndex

Cuando exista una jerarquía natural:

```text
País
 └── Provincia
      └── Ciudad
```

La estructura será más organizada y eficiente.

---

# Resumen Final

✅ La indexación es el mecanismo que permite localizar y manipular datos dentro de un DataFrame.

✅ Los métodos principales son:

- `.loc[]` → etiquetas.
- `.iloc[]` → posiciones.

✅ La indexación booleana permite filtrar datos mediante condiciones.

✅ `.at[]` y `.iat[]` ofrecen acceso rápido a valores individuales.

✅ `query()` proporciona una sintaxis similar a SQL.

✅ MultiIndex permite trabajar con datos jerárquicos complejos.

### Regla práctica

```text
¿Conoces el nombre?
      ↓
    .loc

¿Conoces la posición?
      ↓
    .iloc

¿Necesitas filtrar?
      ↓
Indexación Booleana

¿Necesitas un solo valor?
      ↓
.at o .iat
```

> La indexación es para un DataFrame lo que un índice es para un libro: permite encontrar exactamente la información que necesitas sin recorrerlo completo.