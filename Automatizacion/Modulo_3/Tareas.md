# Programación de tareas: Cron vs Programador de Tareas vs SchTasks

## Introducción

Existen varias formas de automatizar procesos dependiendo del sistema operativo:

- **Cron** → Linux/Unix
- **Programador de Tareas** → Interfaz gráfica de Windows
- **SchTasks** → Línea de comandos de Windows

Los tres permiten ejecutar programas, scripts o comandos de forma automática según una programación definida.

---

# Comparación general

| Función | Cron | Programador de Tareas | SchTasks |
|----------|------|------------------------|----------|
| Entorno | Linux/Unix | Windows | Windows |
| Interfaz gráfica | ❌ | ✅ | ❌ |
| Línea de comandos | ✅ | ❌ | ✅ |
| Automatizable | ✅ | Limitado | ✅ |
| Versionable en Git | ✅ | ❌ | ✅ |
| Ideal para DevOps | ✅ | ❌ | ✅ |
| Curva de aprendizaje | Media | Baja | Media |

---

# 1. Cron (Linux)

Cron es el programador de tareas clásico de Linux y Unix. Permite ejecutar comandos o scripts en horarios definidos, como cada hora, cada noche o al iniciar el sistema. Es muy útil para backups, limpieza de archivos, sincronización y tareas de mantenimiento.

## Editar tareas

Para crear o modificar la programación de tareas del usuario actual:

```bash
crontab -e
```

Esto abre el archivo de cron en el editor configurado del sistema. Cada línea representa una tarea con su horario y comando.

## Ver tareas

Para listar todas las tareas programadas del usuario actual:

```bash
crontab -l
```

Esto sirve para revisar o confirmar qué tareas están activas antes de hacer cambios.

## Ejemplos

### Todos los días a las 08:00

Este patrón ejecuta una tarea cada día a las 08:00.

```cron
0 8 * * *
```

### Cada hora

Se usa cuando una tarea debe repetirse una vez por hora.

```cron
0 * * * *
```

### Cada 5 minutos

Ideal para tareas frecuentes como monitoreo, limpieza o sincronización corta.

```cron
*/5 * * * *
```

### Todos los lunes a las 09:00

El `1` representa el día de la semana (lunes en este caso).

```cron
0 9 * * 1
```

### Al arrancar el sistema

El comando se ejecuta cuando el sistema se inicia.

```cron
@reboot
```

## Ejemplo Python

Un caso típico es ejecutar un script de Python cada día a cierta hora.

```cron
0 8 * * * python /scripts/app.py
```

En este ejemplo, el sistema lanza Python y ejecuta el archivo `/scripts/app.py` a las 08:00.

---

# Estructura de Cron

```text
┌──────── minuto (0-59)
│ ┌────── hora (0-23)
│ │ ┌──── día del mes (1-31)
│ │ │ ┌── mes (1-12)
│ │ │ │ ┌ día de la semana (0-7)
│ │ │ │ │
* * * * *
```

Ejemplo:

```cron
30 14 * * *
```

Ejecuta a las 14:30 todos los días.

---

# 2. Programador de Tareas (UI)

El Programador de Tareas de Windows es la opción más visual para quienes no quieren escribir comandos. Sirve para automatizar tareas como backups, reinicios, ejecuciones de scripts o arranque de aplicaciones sin necesidad de usar la terminal.

## Abrir

Se puede abrir desde la terminal o desde el menú de Windows:

```text
Win + R
taskschd.msc
```

o buscar:

```text
Programador de tareas
```

Esta interfaz permite crear tareas con un flujo guiado y facilitar la configuración de horarios.

---

## Crear tarea

El proceso general es:

1. Crear tarea básica.
2. Definir nombre.
3. Seleccionar frecuencia.
4. Seleccionar acción.
5. Elegir programa o script.

Es útil cuando quieres automatizar algo en Windows sin memorizar sintaxis de comandos.

---

## Ejemplo

Script:

```text
C:\Scripts\backup.bat
```

Frecuencia:

```text
Diariamente
08:00
```

Resultado:

```text
Todos los días a las 08:00
```

---

## Tipos de disparadores

### Al iniciar Windows

```text
Al iniciar el sistema
```

Equivalente a:

```cron
@reboot
```

### Al iniciar sesión

```text
Al iniciar sesión
```

### Diario

```text
Todos los días
```

### Semanal

```text
Lunes, Martes, etc.
```

### Mensual

```text
Día específico del mes
```

---

## Ventajas

✅ Muy fácil de usar
✅ No requiere comandos
✅ Permite ver historial gráfico
✅ Configuración avanzada disponible

---

## Desventajas

❌ Difícil de versionar
❌ Poco práctico para automatización masiva
❌ Menos amigable para DevOps

---

# 3. SchTasks (CLI de Windows)

SchTasks es la versión en línea de comandos del Programador de Tareas de Windows. Es especialmente útil cuando quieres automatizar tareas desde scripts, deployments, PowerShell o infraestructura que se configura en texto, en lugar de hacerlo visualmente.

Es el equivalente más cercano a `cron` en Windows, porque permite crear, consultar y administrar tareas desde la terminal.

---

## Ver tareas

Este comando lista las tareas programadas del sistema o del usuario actual:

```cmd
schtasks /query
```

Vista detallada:

```cmd
schtasks /query /v /fo list
```

La opción `/v /fo list` muestra información más completa, como el estado de la tarea, el usuario que la ejecuta y la ruta del programa.

---

## Crear una tarea diaria

Este ejemplo crea una tarea que se ejecuta cada día a las 08:00:

```cmd
schtasks /create ^
 /tn "Backup Diario" ^
 /tr "C:\Scripts\backup.bat" ^
 /sc daily ^
 /st 08:00
```

Aquí se define el nombre de la tarea (`/tn`), el programa que corre (`/tr`) y la frecuencia (`/sc daily`).

---

## Ejecutar ahora

Si quieres disparar la tarea inmediatamente, aunque no haya llegado el horario programado:

```cmd
schtasks /run /tn "Backup Diario"
```

Esto es útil para pruebas o ejecución manual de diagnóstico.

---

## Detener tarea

Cuando una tarea ya está corriendo y quieres forzar su detención:

```cmd
schtasks /end /tn "Backup Diario"
```

---

## Eliminar tarea

Para borrar la programación de una tarea en particular:

```cmd
schtasks /delete /tn "Backup Diario" /f
```

La bandera `/f` fuerza la eliminación sin pedir confirmación.

---

## Ver detalle de una tarea

Si necesitas revisar la configuración exacta de una tarea, incluyendo usuario, ruta y política:

```cmd
schtasks /query ^
 /tn "Backup Diario" ^
 /v ^
 /fo list
```

---

# Equivalencias Cron → SchTasks

Si ya sabes cómo funciona cron, esta sección te ayuda a traducir la misma idea a SchTasks. La lógica es parecida: defines un horario y un comando, pero la sintaxis cambia según el sistema operativo.

## Todos los días a las 08:00

Cron:

```cron
0 8 * * *
```

SchTasks:

```cmd
schtasks /create ^
 /tn "Backup Diario" ^
 /tr "C:\Scripts\backup.bat" ^
 /sc daily ^
 /st 08:00
```

---

## Todos los lunes a las 09:00

Cron:

```cron
0 9 * * 1
```

SchTasks:

```cmd
schtasks /create ^
 /tn "Lunes" ^
 /tr "C:\Scripts\script.bat" ^
 /sc weekly ^
 /d MON ^
 /st 09:00
```

---

## Al iniciar el sistema

Cron:

```cron
@reboot
```

SchTasks:

```cmd
schtasks /create ^
 /tn "Startup" ^
 /tr "C:\Scripts\script.bat" ^
 /sc onstart
```

---

## Al iniciar sesión

Cron:

No tiene equivalente directo.

SchTasks:

```cmd
schtasks /create ^
 /tn "Login" ^
 /tr "C:\Scripts\script.bat" ^
 /sc onlogon
```

---

# Ejecutar Python

En muchos proyectos, la automatización se usa para lanzar scripts de Python sin intervención manual. Esto es muy común en tareas de procesamiento, reportes, limpieza de datos o sincronización con APIs.

## Cron

```cron
*/30 * * * * python script.py
```

Este ejemplo ejecuta el script cada 30 minutos.

---

## Programador de tareas

Programa:

```text
C:\Python314\python.exe
```

Argumentos:

```text
C:\Scripts\script.py
```

Frecuencia:

```text
Cada 30 minutos
```

---

## SchTasks

```cmd
schtasks /create ^
 /tn "PythonJob" ^
 /tr "\"C:\Python314\python.exe\" \"C:\Scripts\script.py\"" ^
 /sc hourly
```

---

# Ejecutar PowerShell

Cuando necesitas ejecutar un script de PowerShell, normalmente usas `powershell.exe` y apuntás al archivo `.ps1`:

```cmd
schtasks /create ^
 /tn "Limpieza" ^
 /tr "powershell.exe -ExecutionPolicy Bypass -File C:\Scripts\limpieza.ps1" ^
 /sc daily ^
 /st 22:00
```

Esto resulta útil para tareas de mantenimiento, limpieza de sistema o automatización de entornos Windows.

---

# Ejecutar como SYSTEM

Similar a ejecutar algo como `root` en Linux. Algunas tareas necesitan permisos altos para modificar archivos del sistema o ejecutar acciones administrativas.

```cmd
schtasks /create ^
 /tn "AdminTask" ^
 /tr "C:\Scripts\admin.bat" ^
 /sc daily ^
 /st 01:00 ^
 /ru SYSTEM
```

---

# Exportar e importar tareas

Cuando quieres guardar la configuración de una tarea para moverla a otra máquina o dejarla versionada en Git, puedes exportarla a XML.

## Exportar

```cmd
schtasks /query ^
 /tn "Backup Diario" ^
 /xml > backup.xml
```

Esto guarda la configuración de la tarea en un archivo XML.

## Importar

```cmd
schtasks /create ^
 /xml backup.xml ^
 /tn "Backup Diario"
```

Esto permite recrear la tarea en otra máquina o entorno con la misma configuración.

Ideal para:

- Git
- Infraestructura como código
- Backups de configuración

---

# Resumen mental

| Acción | Cron | SchTasks |
|--------|------|----------|
| Crear tarea | crontab -e | schtasks /create |
| Ver tareas | crontab -l | schtasks /query |
| Borrar tarea | editar crontab | schtasks /delete |
| Ejecutar tarea | comando manual | schtasks /run |
| Al iniciar sistema | @reboot | /sc onstart |
| Inicio de sesión | N/A | /sc onlogon |

---

# Recomendación

### Usuario común

Usar:

```text
Programador de tareas
```

### Administrador de sistemas

Usar:

```text
Cron
```

o

```text
SchTasks
```

### Desarrollador Python / DevOps

Preferir:

```text
Cron (Linux)
SchTasks (Windows)
```

porque permiten:

- Automatización reproducible
- Scripts versionables
- Integración con Git
- Infraestructura como código
- Despliegues automatizados

---

# 4. `schedule` en Python

La librería `schedule` es una forma de programar tareas directamente dentro de un programa Python. En lugar de depender de cron o del Programador de Tareas del sistema operativo, el propio script se queda ejecutando y, según un intervalo o horario definido, dispara funciones específicas.

Es decir, funciona como un "programador de tareas" pero dentro del mismo código de Python.

## ¿Cuándo usarla?

Se usa cuando:

- querés automatizar acciones dentro de una app o servicio
- necesitas ejecutar tareas cada cierto tiempo mientras el programa está corriendo
- querés probar lógica de automatización sin configurar cron o SchTasks

## Instalarla

```bash
pip install schedule
```

## Ejemplo básico

```python
import schedule
import time


def tarea_diaria():
    print("Ejecutando tarea automática...")


schedule.every(10).seconds.do(tarea_diaria)

while True:
    schedule.run_pending()
    time.sleep(1)
```

Este ejemplo ejecuta la función `tarea_diaria()` cada 10 segundos mientras el programa siga activo.

## Ejemplos comunes

### Cada minuto

```python
schedule.every(1).minute.do(tarea_diaria)
```

### Cada hora

```python
schedule.every().hour.do(tarea_diaria)
```

### Todos los días a las 08:00

```python
schedule.every().day.at("08:00").do(tarea_diaria)
```

### Cada lunes a las 09:00

```python
schedule.every().monday.at("09:00").do(tarea_diaria)
```

## Diferencia clave

- `cron` y `SchTasks` programan tareas a nivel del sistema operativo.
- `schedule` programa tareas dentro de un proceso de Python que debe seguir ejecutándose.

Por eso, `schedule` es muy útil para scripts pequeños, servicios internos o automatizaciones que necesitan correr mientras la app esté en funcionamiento.

## Cuándo elegir cada opción

- Usá `cron` o `SchTasks` si la tarea debe ejecutarse aunque tu programa esté cerrado.
- Usá `schedule` si la tarea está ligada al programa Python que ya está corriendo.

En resumen, `schedule` no reemplaza a cron ni a SchTasks como automatización del sistema, pero sí es una excelente opción para programar tareas dentro de un proyecto Python.
