"""Módulo reutilizable de quizzes interactivos para notebooks (JupyterLab y VS Code).

Incluye:
- aplicar_estilos(): inyecta CSS para que los widgets se vean bien en tema claro/oscuro.
- crear_quiz(): pregunta de opción múltiple (una sola respuesta correcta).
- crear_quiz_multiple(): pregunta multi-respuesta (seleccionar todas las correctas).
"""

from IPython.display import display, HTML
from ipywidgets import widgets, Output
import string

# ---------------------------------------------------------------------------
# CSS adaptativo: hace legibles los widgets tanto en JupyterLab como en VS Code.
# VS Code usa una arquitectura vieja de ipywidgets que no entiende temas y
# fuerza background blanco; este CSS lo corrige y crea un puente con el tema.
# ---------------------------------------------------------------------------
CSS_QUIZ = """
<style>
/* 1) Hacer el contenedor de widgets transparente.
      En VS Code ese contenedor es .cell-output-ipywidget-background y viene
      con 'background: white' forzado; lo sobreescribimos. */
.cell-output-ipywidget-background {
    background-color: transparent !important;
}

/* 2) Puente entre el tema de VS Code y las variables que leen los widgets.
      Si no existen (p.ej. JupyterLab) se ignora y se usa el bloque de abajo. */
:root {
    --jp-widgets-color: var(--vscode-editor-foreground, inherit);
    --jp-widgets-font-size: var(--vscode-editor-font-size, inherit);
}

/* 3) Colorear el texto de las etiquetas/opciones del quiz.
      Hereda del tema en JupyterLab; en VS Code usa el color ya mapeado. */
.widget-label,
.widget-description,
.lm-Widget .widget-radio label,
.lm-Widget .widget-checkbox label,
.widget-radio,
.widget-checkbox,
.jupyter-widgets {
    color: var(--jp-widgets-color, var(--jp-ui-font-color1, inherit)) !important;
    background: transparent !important;
}

/* 4) Fondo de los botones legible y acorde al tema. */
.jupyter-button, .widget-button {
    background: var(--vscode-button-background, #333) !important;
    color: var(--vscode-button-foreground, #fff) !important;
    border-radius: 4px;
}

/* 5) En JupyterLab con tema oscuro, garantizar texto claro de respaldo. */
body[data-jp-theme-light="false"] .widget-label,
body[data-jp-theme-light="false"] .widget-description,
body[data-jp-theme-light="false"] .lm-Widget .widget-radio label,
body[data-jp-theme-light="false"] .lm-Widget .widget-checkbox label {
    color: #e8e8e8 !important;
}
</style>
"""


def aplicar_estilos():
    """Inyecta el CSS que hace legibles los widgets del quiz según el tema."""
    display(HTML(CSS_QUIZ))


def _letras(n):
    """Devuelve las n primeras letras del alfabeto (A, B, C, ...)."""
    return list(string.ascii_uppercase[:n])


def _html_resultado(correcto, titulo, detalle, explicacion):
    color = "#2ecc71" if correcto else "#e74c3c"
    return f"""
    <div style="color: var(--jp-content-font-color1); font-size: 14px;">
        <p style="color:{color}; font-weight:bold;">{titulo}</p>
        <p>{detalle}</p>
        {f'<p style="color: #e0e0e0;">💡 {explicacion}</p>' if explicacion else ''}
    </div>
    """


def crear_quiz(opciones, correcta, explicacion="", nombre=""):
    """Pregunta de opción múltiple con una única respuesta correcta.

    - opciones: lista de textos de las opciones (se numeran A, B, C...).
    - correcta: letra de la respuesta correcta (p.ej. 'A').
    - explicacion: texto que se muestra junto al resultado (opcional).
    - nombre: etiqueta que precede al widget (opcional, p.ej. la pregunta).
    """
    letras = _letras(len(opciones))
    radio = widgets.RadioButtons(
        options=[(f"{l}) {o}", l) for l, o in zip(letras, opciones)],
        description=nombre,
        layout=widgets.Layout(width='100%'),
        disabled=False,
        style={'description_color': 'var(--jp-ui-font-color1)'},
    )
    boton = widgets.Button(
        description="Ver respuesta",
        layout=widgets.Layout(width='auto'),
    )
    salida = Output()

    def al_verificar(b):
        salida.clear_output()
        with salida:
            correcto = radio.value == correcta
            if correcto:
                titulo = f"✅ ¡Correcto! Respuesta {correcta}."
                detalle = ""
            else:
                titulo = f"❌ Incorrecto. La respuesta correcta es {correcta}."
                detalle = ""
            display(HTML(_html_resultado(correcto, titulo, detalle, explicacion)))

    boton.on_click(al_verificar)
    display(radio, boton, salida)


def crear_quiz_multiple(opciones, correctas, explicacion=""):
    """Pregunta multi-respuesta: seleccionar TODAS las opciones correctas.

    - opciones: lista de textos de las opciones (se numeran A, B, C...).
    - correctas: lista/set de letras correctas (p.ej. ['A', 'C', 'D']).
    - explicacion: texto que se muestra junto al resultado (opcional).
    """
    letras = _letras(len(opciones))
    correctas = set(correctas)

    checks = [
        widgets.Checkbox(
            value=False,
            description=f"{l}) {o}",
            indent=False,
            layout=widgets.Layout(width='100%'),
            style={'description_color': 'var(--jp-ui-font-color1)'},
        )
        for l, o in zip(letras, opciones)
    ]
    boton = widgets.Button(
        description="Ver respuesta",
        layout=widgets.Layout(width='auto'),
    )
    salida = Output()

    def verificar(b):
        salida.clear_output()
        elegidas = {letras[i] for i, c in enumerate(checks) if c.value}

        with salida:
            if elegidas == correctas:
                display(HTML(_html_resultado(
                    True,
                    f"✅ ¡Correcto! Seleccionaste {', '.join(sorted(correctas))}.",
                    "",
                    explicacion,
                )))
            else:
                faltan = correctas - elegidas
                sobran = elegidas - correctas
                partes = []
                if faltan:
                    partes.append(f"Te faltaron: {', '.join(sorted(faltan))}")
                if sobran:
                    partes.append(f"Sobran: {', '.join(sorted(sobran))}")
                if not partes:
                    partes.append("No seleccionaste ninguna opción.")
                partes.append(f"Las correctas son {', '.join(sorted(correctas))}.")
                display(HTML(_html_resultado(
                    False,
                    "❌ Incorrecto.",
                    "<br>".join(partes),
                    explicacion,
                )))

    boton.on_click(verificar)
    display(*checks, boton, salida)
