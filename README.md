
🚀 REGISTRO ESTUDIANTIL PRO - T.A.P 🎓
📑 Introducción al Proyecto
Este repositorio contiene el desarrollo de una aplicación avanzada de escritorio y web orientada a la gestión de datos escolares. El proyecto no solo se enfoca en la captura de información, sino en la implementación de una Experiencia de Usuario (UX) profesional mediante el uso de contenedores estilizados y lógica reactiva.

🛠️ Configuración del Workspace y Entorno Virtual
Para garantizar que la aplicación se ejecute sin conflictos de librerías, utilizamos un entorno aislado. Esto permite que el proyecto sea portable y fácil de instalar en cualquier equipo.

Ejecuta estos comandos en tu Git Bash:

Bash
# 1. Creación del directorio raíz del proyecto
mkdir Registro_Estudiantil_TAP
cd Registro_Estudiantil_TAP

# 2. Creación del entorno virtual (.venv)
python -m venv .venv

# 3. Activación del entorno (Indispensable para instalar Flet)
source .venv/Scripts/activate

# 4. Instalación de la dependencia principal
pip install flet
🏗️ Arquitectura del Código: Explicación por Módulos
1. Estética y Contenedores (Diseño UI)
A diferencia de los formularios planos convencionales, este sistema utiliza un diseño basado en Tarjetas (Cards). Aplicamos sombras dinámicas y bordes redondeados para generar una sensación de profundidad y modernidad.

Código del Contenedor:

Python
card = ft.Container(
    content=columna_principal,
    bgcolor="white",
    padding=40,
    border_radius=20, # Bordes curvos profesionales
    shadow=ft.BoxShadow(blur_radius=20, color="black12"), # Sombra suave
    width=520
)
2. Motor de Validación y Lógica de Eventos
El corazón de la aplicación es el manejador de eventos del botón. Este módulo actúa como un "filtro de seguridad" que inspecciona cada campo antes de procesar la información.

Validación de Vacíos: Recorre los componentes y cambia su propiedad border_color a rojo si el usuario olvidó algún dato.

Validación Estructural: El email es analizado para confirmar la presencia del símbolo @ y un dominio válido.

Lógica de Validación:

Python
def enviar_click(e):
    if not txt_nombre.value or not txt_email.value:
        txt_nombre.border_color = "red"
        page.update() # Refresco visual inmediato
3. Sistema de Confirmación (Ventana Modal)
Para evitar la saturación de la pantalla principal, los resultados se muestran en un AlertDialog. Este componente solo se activa si todas las validaciones previas son exitosas, ofreciendo un resumen limpio de la operación.

📦 Código Completo de la Aplicación
Aquí se integra la configuración de la página, los controles de entrada y la lógica de visualización en un solo script robusto:

Python
import flet as ft
import re

def main(page: ft.Page):
    # Configuración de la ventana
    page.title = "Registro Escolar TAP"
    page.bgcolor = "#F0F0F0"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # --- VENTANA MODAL ---
    txt_resumen = ft.Text("", size=16)
    dlg_resumen = ft.AlertDialog(
        title=ft.Text("✅ Registro Confirmado"),
        content=txt_resumen,
        actions=[ft.TextButton("Cerrar", on_click=lambda _: setattr(dlg_resumen, "open", False) or page.update())]
    )
    page.overlay.append(dlg_resumen)

    # --- CONTROLES DE ENTRADA ---
    txt_nombre = ft.TextField(label="Nombre Completo", border_color="#4D2A32")
    txt_control = ft.TextField(label="Número de Control", border_color="#4D2A32")
    txt_email = ft.TextField(label="Email Institucional", border_color="#4D2A32")

    dd_carrera = ft.Dropdown(
        label="Carrera",
        expand=True,
        options=[ft.dropdown.Option("Ingeniería en Sistemas"), ft.dropdown.Option("Ingeniería Civil")]
    )

    rg_genero = ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value="M", label="Masculino"),
            ft.Radio(value="F", label="Femenino")
        ], alignment=ft.MainAxisAlignment.CENTER)
    )

    # --- FUNCIÓN DE ENVÍO ---
    def enviar_click(e):
        if not txt_nombre.value or "@" not in txt_email.value:
            txt_nombre.border_color = "red"
            page.update()
        else:
            txt_resumen.value = f"Alumno: {txt_nombre.value}\nCarrera: {dd_carrera.value}"
            dlg_resumen.open = True
            page.update()

    # --- BOTÓN Y DISEÑO FINAL ---
    btn_registrar = ft.Button(content=ft.Text("REGISTRAR", weight="bold"), on_click=enviar_click, width=300)

    card = ft.Container(
        content=ft.Column([
            ft.Text("👤", size=50),
            ft.Text("REGISTRO ESCOLAR", size=22, weight="bold", color="#4D2A32"),
            txt_nombre, txt_control, txt_email, dd_carrera, rg_genero,
            btn_registrar
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=15),
        bgcolor="white", padding=40, border_radius=20,
        shadow=ft.BoxShadow(blur_radius=20, color="black12"), width=500
    )

    page.add(card)

# Ejecución en navegador para máxima estabilidad
ft.run(main, view=ft.AppView.WEB_BROWSER)
