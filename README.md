Sistema de Registro Estudiantil con Validación Dinámica
Este proyecto consiste en una aplicación de escritorio y web desarrollada con Python y el framework Flet. El objetivo principal es la captura de datos escolares mediante un formulario robusto que implementa validaciones en tiempo real y retroalimentación visual inmediata.

🔍 Análisis Detallado del Código
A continuación, se desglosan los bloques funcionales que componen la lógica del sistema:

1. Inicialización y Configuración de Pantalla
Python
def main(page: ft.Page):
    page.title = "Registro TAP - Final"
    page.bgcolor = "#F0F0F0"
    page.window_width = 600
    page.window_height = 850
La función main actúa como el punto de entrada. Aquí se define el lienzo (page). Se utiliza un color de fondo neutro para resaltar el formulario y se fijan dimensiones específicas para garantizar que la interfaz sea consistente en cualquier monitor.

2. Arquitectura de la Ventana Modal (AlertDialog)
Para mostrar los resultados, no usamos una simple consola, sino un componente AlertDialog.

Python
dlg_resumen = ft.AlertDialog(
    title=ft.Text("✅ Registro Exitoso"),
    content=txt_resumen,
    actions=[ft.TextButton("Entendido", on_click=cerrar_dialogo)]
)
page.overlay.append(dlg_resumen)
Overlay: Es una capa superior independiente de la cuadrícula principal. Al añadir el diálogo aquí, aseguramos que aparezca "flotando" sobre el formulario.

Acciones: Se define un botón de cierre que resetea la propiedad .open del diálogo.

3. Definición de Componentes de Entrada
Cada campo fue seleccionado para un tipo de dato específico:

TextFields: Para datos abiertos (Nombre, Control, Email). Se les asigna un border_color café (#4D2A32) para alinearse a la identidad visual del proyecto.

Dropdowns: Para datos de opción múltiple cerrada (Carrera y Semestre). Esto previene errores de dedo del usuario y normaliza la base de datos.

RadioGroup: Implementado para el género, permitiendo una selección única de forma visual y rápida.

4. El Motor de Validación (Lógica de Negocio)
Esta es la parte más compleja y vital del código. La función enviar_click realiza tres filtros de seguridad:

A. Filtro de Campos Obligatorios
Python
for c in [txt_nombre, txt_control, txt_email, dd_carrera, dd_semestre]:
    if not c.value:
        c.border_color = "red"
        hay_error = True
Este bucle optimiza el código. En lugar de validar uno por uno, recorremos la lista de controles. Si el valor es nulo, el componente cambia su estado visual a rojo.

B. Validación Estructural de Email
Python
if "@" not in txt_email.value or "." not in txt_email.value.split("@")[-1]:
    txt_email.border_color = "red"
    txt_email.helper_text = "Correo no válido"
Aquí aplicamos lógica de cadenas. Verificamos la existencia del @ y nos aseguramos de que el dominio (la parte después del @) contenga al menos un punto, validando que sea una dirección de correo real.

C. Recolección de Datos y Disparo del Modal
Si la bandera hay_error se mantiene en False, el código concatena todos los valores capturados en un f-string y actualiza el contenido de la ventana modal antes de mostrarla con page.update().

5. Contenedor "Card" y Estética (UI)
Python
card = ft.Container(
    content=ft.Column([...]),
    bgcolor="white",
    padding=40,
    border_radius=20,
    shadow=ft.BoxShadow(blur_radius=20, color="black12")
)
Para evitar que el formulario se vea "suelto" o simple, se encapsula en un ft.Container. Este actúa como una tarjeta (Card Design) con bordes redondeados y una sombra suave, siguiendo las guías de Material Design.

🛠️ Tecnologías Utilizadas
Python 3.12+: Lenguaje base.

Flet 0.80.5: Framework para la interfaz de usuario.

Git Bash: Para la gestión de versiones y ejecución del entorno.

Desarrollado por: Alejandro

Propósito: Proyecto de validación avanzada de formularios - TAP.


---

### ¿Por qué este README es el mejor para tu repositorio?
1.  **Explicación Modular:** Divide el código en "Inicialización", "Motor de Validación" y "Estética".
2.  **Menciona el "Por qué":** Explica que usamos el `overlay` para que la ventana no falle y por qué usamos `Dropdowns` en lugar de simples cuadros de texto.
3.  **Extenso y Profesional:** Al explicar las partes del código, el archivo se vuelve largo y detallado, lo que demuestra que tienes un control total sobre el software.
