Instrucciones
Actividad: Crear un fragmento "calcular área
Bienvenido al entorno de laboratorio de Visual Studio Code En este laboratorio sin calificación, practicará el trabajo con fragmentos de código reutilizables.

Escenario
Estás desarrollando una herramienta de geometría interactiva para estudiantes. Para facilitarles el cálculo del área de rectángulos, usted decide crear un fragmento de código que genere una plantilla para este cálculo común.

Su tarea
Cree un fragmento de código en su IDE que genere una plantilla para calcular el área de un rectángulo.

Utilice marcadores de posición para las variables de longitud y anchura.

Pruebe su fragmento de código calculando el área de un rectángulo con una longitud de 5 y un ancho de 3.

Pasos
1. Para empezar, crearás el fragmento de código "calcular área" en este IDE con los siguientes pasos para que puedas utilizarlo en tus scripts de Python.

2. Navega hasta Archivo -> Preferencias -> Configurar fragmentos de código de usuario. Luego busque o desplácese hacia abajo en el desplegable resultante para seleccionar 'Python' de la lista de opciones. Esto abrirá el archivo python.json donde añadirá su fragmento de código.

3. Reemplace todo en python.json (incluyendo los comentarios del fragmento de código y las llaves) con el siguiente código:  

```json
{
    "calculate_area": {
        "prefix": "calc_area",
        "body": [
            "def calculate_area(length, width):",
            "  \"\"\"Calculates the area of a rectangle.\"\"\"",
            "  # Calculate the area",
            "  area = length * width",
            "  ",
            "  return area",
            "  # Output the area",
        ],
    }
}
```

1. Guarde el archivo python. json después de añadir el fragmento de código, y luego abra main.py desde el explorador de archivos a la izquierda.

1. Ahora intenta insertar tu fragmento de código escribiendo calc_area en main.py y pulsando tabulador cuando veas que aparece la sugerencia de IntelliSense para calc_area.

2. Tu cursor debería situarse automáticamente en el primer marcador de posición, length. Establece length como 5 y width como 3 en el fragmento de código que acabas de crear. Puede utilizar el tabulador para saltar al siguiente marcador de posición después de añadir cada valor.

3. Ahora prueba el fragmento de código ejecutando el script main.py y comprueba si obtienes la salida correcta en el terminal. Para ello, abre el terminal utilizando el atajo de teclado Ctrl+` o a través del menú (Ver -> Terminal) y luego introduce python3 main.py en el terminal. Tenga cuidado de seguir estas instrucciones sobre cómo ejecutar el programa; el menú Ejecutar o el botón derecho del ratón > Ejecutar no funcionan en el entorno simulado. Debe utilizar la ventana del terminal como se indica.

4. Después de ejecutar el script main.py, deberías ver la siguiente salida: 15

5. Si obtienes la salida correcta, entonces has terminado y puedes hacer clic en el botón Marcar como completado y cerrar este laboratorio. Sin embargo, si no obtuviste la salida correcta, entonces vuelve sobre los pasos anteriores, verificando si el fragmento se agregó correctamente a python.json y luego aplica el código del fragmento a main.py.  