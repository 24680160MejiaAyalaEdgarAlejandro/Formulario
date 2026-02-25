🚀 REGISTRO ESTUDIANTIL PRO - T.A.P 🎓
📑 Descripción del Proyecto
Desarrollo de una interfaz de usuario avanzada para el control de registros estudiantiles. Este proyecto implementa una lógica de validación reactiva, donde la interfaz responde en tiempo real a las entradas del usuario, utilizando el framework flet bajo el lenguaje python.

🛠️ Tecnologías y Entorno
[!IMPORTANT]
DISEÑO REACTIVO: El formulario cambia el color de los bordes a ROJO automáticamente si detecta campos vacíos o formatos de correo inválidos.

🏗️ Configuración del Workspace (Git Bash)
Para asegurar que las dependencias no entren en conflicto, aislamos el proyecto en un entorno virtual. Esto garantiza que la versión de Flet utilizada sea la correcta para el código desarrollado.

Bash
# 1. Crear directorio y entrar
mkdir Registro_Estudiantil_TAP
cd Registro_Estudiantil_TAP

# 2. Inicializar entorno virtual
python -m venv .venv
source .venv/Scripts/activate

# 3. Instalación de Flet (Full Package)
pip install flet
🎨 Estética y Contenedores (UI)
El formulario no es plano; utiliza un diseño de Tarjeta (Card) con sombras y bordes redondeados para una apariencia moderna. Se utiliza un ft.Container como envoltorio principal para controlar el espaciado y la elevación visual.

Python
# Creación del contenedor tipo "Card"
card = ft.Container(
    content=columna_principal,
    bgcolor="white",
    padding=40,
    border_radius=20, # Bordes redondeados
    shadow=ft.BoxShadow(blur_radius=20, color="black12"), # Sombra sutil
    width=520
)
🧠 Motor de Validación (Lógica de Eventos)
Se implementó un manejador de eventos que actúa como filtro de seguridad. Antes de permitir el registro, el sistema verifica que todos los campos obligatorios contengan datos y que el correo electrónico cumpla con el estándar estructural (@ y dominio).

Python
def enviar_click(e):
    hay_error = False
    
    # Validación de campos vacíos
    for c in [txt_nombre, txt_control, txt_email, dd_carrera, dd_semestre]:
        if not c.value:
            c.border_color = "red"
            hay_error = True
        else:
            c.border_color = "#4D2A32"

    # Validación estructural de Email
    if "@" not in txt_email.value or "." not in txt_email.value.split("@")[-1]:
        txt_email.border_color = "red"
        hay_error = True
🏁 Ventana Emergente (Confirmación Modal)
Una vez que los datos pasan las pruebas de validación, el sistema utiliza un componente ft.AlertDialog registrado en el overlay de la página. Esto permite mostrar un resumen final sin abandonar la pantalla actual.

Python
# Definición del diálogo de éxito
dlg_resumen = ft.AlertDialog(
    title=ft.Text("✅ REGISTRO EXITOSO"),
    content=txt_resumen, # Aquí se inyectan los datos capturados
    actions=[ft.TextButton("Entendido", on_click=cerrar_dialogo)]
)

# Apertura del modal
page.dialog = dlg_resumen
dlg_resumen.open = True
page.update()
📦 Código Completo
Aquí tienes la integración final de todos los módulos explicados anteriormente:

Python
import flet as ft

def main(page: ft.Page):
    page.title = "Registro TAP - Final"
    page.bgcolor = "#F0F0F0"
    page.theme_mode = ft.ThemeMode.LIGHT
    
    # 1. Componentes de la Ventana Modal
    txt_resumen = ft.Text("", size=16)
    def cerrar_dialogo(e):
        dlg_resumen.open = False
        page.update()

    dlg_resumen = ft.AlertDialog(
        title=ft.Text("✅ Datos Registrados"),
        content=txt_resumen,
        actions=[ft.TextButton("Cerrar", on_click=cerrar_dialogo)]
    )
    page.overlay.append(dlg_resumen)

    # 2. Controles del Formulario
    txt_nombre = ft.TextField(label="Nombre Completo", border_color="#4D2A32")
    txt_control = ft.TextField(label="N° de Control", border_color="#4D2A32")
    txt_email = ft.TextField(label="Email Institucional", border_color="#4D2A32")

    dd_carrera = ft.Dropdown(
        label="Carrera",
        options=[ft.dropdown.Option("Ingeniería en Sistemas"), ft.dropdown.Option("Ingeniería Industrial")]
    )

    # 3. Lógica de Envío
    def enviar_click(e):
        if not txt_nombre.value or "@" not in txt_email.value:
            txt_nombre.border_color = "red"
            page.update()
        else:
            txt_resumen.value = f"Nombre: {txt_nombre.value}\nCarrera: {dd_carrera.value}"
            dlg_resumen.open = True
            page.update()

    # 4. Construcción de UI
    page.add(
        ft.Container(
            content=ft.Column([
                ft.Text("👤", size=50),
                ft.Text("REGISTRO ESCOLAR", size=22, weight="bold"),
                txt_nombre, txt_control, txt_email, dd_carrera,
                ft.Button(content=ft.Text("REGISTRAR"), on_click=enviar_click, width=300)
            ], horizontal_alignment="center", spacing=15),
            bgcolor="white", padding=40, border_radius=20, width=500
        )
    )

ft.run(main, view=ft.AppView.WEB_BROWSER)
