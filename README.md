T.A.P_Registro_Estudiantil 📋🐍
Sistema de Registro Escolar dinámico
Desarrollo de una interfaz de captura de datos utilizando el framework Flet para Python. Este repositorio documenta la creación de un formulario con validaciones avanzadas, manejo de estados visuales y retroalimentación mediante ventanas modales.

[!CAUTION]
Requisitos: Flet v0.80.5 o versiones compatibles.
Verifica tu entorno ejecutando pip show flet en tu terminal.

[!NOTE]
📥 ACCESOS RÁPIDOS

🛠️ Configuración del Entorno
Para el correcto funcionamiento del formulario, se recomienda el uso de un entorno virtual aislado:

Bash
# Crear carpeta del proyecto
mkdir Registro_Escolar
cd Registro_Escolar

# Configurar entorno virtual
py -m venv .venv
source .venv/Scripts/activate

# Instalar framework
pip install flet
🏗️ Estructura de la Interfaz
La aplicación se basa en una jerarquía de contenedores que prioriza la Experiencia de Usuario (UX).

1. Configuración de la Página
Python
def main(page: ft.Page):
    page.title = "Registro TAP"
    page.window_width = 600
    page.window_height = 850
    page.bgcolor = "#F0F0F0" # Gris neutro para contraste
Se definen dimensiones fijas para asegurar que el diseño "tipo Card" se mantenga centrado y proporcional.

2. Definición de Componentes de Entrada
Se utilizan controles específicos para cada tipo de dato, mejorando la integridad de la información:

Python
# Campos de texto con identidad visual
txt_nombre = ft.TextField(label="Nombre Completo", border_color="#4D2A32")
txt_email = ft.TextField(label="Email Institucional", border_color="#4D2A32")

# Menús desplegables para evitar errores de captura
dd_carrera = ft.Dropdown(
    label="Carrera",
    options=[ft.dropdown.Option("Ingeniería en Sistemas"), ...]
)
🧠 Lógica de Validación y Eventos
El corazón del proyecto es la función enviar_click, encargada de procesar la información antes de su almacenamiento.

Sistema de Feedback Visual
Si un campo se encuentra vacío, el sistema modifica dinámicamente sus atributos de estilo:

Python
for c in [txt_nombre, txt_control, txt_email, dd_carrera, dd_semestre]:
    if not c.value:
        c.border_color = "red" # Alerta visual inmediata
        hay_error = True
Validación de Formato (Email)
Se implementa una lógica de comprobación de cadenas para asegurar que el correo electrónico cumpla con una estructura válida:

Python
if "@" not in txt_email.value or "." not in txt_email.value.split("@")[-1]:
    txt_email.border_color = "red"
    txt_email.helper_text = "Correo no válido"
🏁 Componentes de Confirmación
Una vez validada la información, se utiliza un sistema de capas (overlay) para mostrar un resumen de los datos.

Python
# Definición del diálogo de éxito
dlg_resumen = ft.AlertDialog(
    title=ft.Text("✅ Registro Exitoso"),
    content=txt_resumen, # Muestra los datos capturados
    actions=[ft.TextButton("Entendido", on_click=cerrar_dialogo)]
)
page.overlay.append(dlg_resumen)
Flujo Jerárquico Final
Bash
page (Principal)
└── Container (Card Blanco)
    └── Column (Organizador Vertical)
        ├── Icon / Emoji 👤
        ├── TextFields (Entradas)
        ├── Dropdowns (Selección)
        ├── RadioGroup (Género)
        └── Button (Disparador de eventos)
🚀 Ejecución de la Aplicación
Para iniciar el sistema en modo navegador y evitar bloqueos de ventanas en Windows:

Python
ft.run(main, view=ft.AppView.WEB_BROWSER)
Desarrollado por: César

Repositorio: T.A.P - Ejercicios de Interfaces Gráficas.*Extenso y Profesional:** Al explicar las partes del código, el archivo se vuelve largo y detallado, lo que demuestra que tienes un control total sobre el software.
