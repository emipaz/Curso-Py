# Resumen: Manejo de Valores Duplicados en Pandas

## Conceptos clave

1. Los valores duplicados son registros que aparecen más de una vez en un conjunto de datos.

2. Los duplicados pueden surgir por:
   - Error humano.
   - Integración de múltiples fuentes.
   - Fallos de software.
   - Problemas durante la importación de datos.

3. Los duplicados afectan la calidad de los análisis y pueden producir resultados incorrectos.

4. También incrementan el uso de almacenamiento y reducen el rendimiento de procesamiento.

5. Pandas permite detectar duplicados mediante:

```python
df.duplicated()
```

6. Para visualizar las filas duplicadas:

```python
df[df.duplicated()]
```

7. Para contar duplicados:

```python
df.duplicated().sum()
```

8. Para eliminar duplicados manteniendo la primera aparición:

```python
df.drop_duplicates()
```

9. Para buscar duplicados en columnas específicas:

```python
df.duplicated(subset=["email"])
```

10. La mejor estrategia es prevenir duplicados mediante:
    - Validaciones de entrada.
    - Identificadores únicos.
    - Restricciones `UNIQUE` en bases de datos.
    - Procesos de captura de datos controlados.

## Funciones importantes

| Función | Descripción |
|----------|------------|
| `duplicated()` | Detecta filas duplicadas |
| `drop_duplicates()` | Elimina duplicados |
| `subset=` | Evalúa columnas específicas |
| `keep="first"` | Conserva la primera ocurrencia |
| `keep="last"` | Conserva la última ocurrencia |
| `keep=False` | Elimina todas las ocurrencias duplicadas |

## Flujo recomendado

```text
Detectar duplicados
        ↓
Analizar impacto
        ↓
Eliminar o corregir
        ↓
Validar resultados
        ↓
Implementar controles preventivos
```