# 🚀 REGISTRO ESTUDIANTIL PRO - T.A.P 🎓

## 📑 Descripción del Proyecto
Desarrollo de una interfaz de usuario avanzada para el control de registros estudiantiles. Este proyecto implementa una lógica de **validación reactiva**, donde la interfaz responde en tiempo real a las entradas del usuario, utilizando el framework **Flet** bajo el lenguaje **Python**.

---

### 🛠️ Tecnologías y Entorno
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
![Flet](https://img.shields.io/badge/flet-D1345B?style=for-the-badge&logo=flet&logoColor=white) 
![Git Bash](https://img.shields.io/badge/Git%20Bash-F05032?style=for-the-badge&logo=git&logoColor=white) 
![VS Code](https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual-studio-code&logoColor=white)

> [!IMPORTANT]
> **DISEÑO REACTIVO:** El formulario cambia el color de los bordes a **ROJO** automáticamente si detecta campos vacíos o formatos de correo inválidos.

---
🏗️ Configuración del Workspace (Git Bash)
Para asegurar que las dependencias no entren en conflicto, aislamos el proyecto en un entorno virtual:

Bash
# 1. Crear directorio y entrar
mkdir Registro_Estudiantil_TAP
cd Registro_Estudiantil_TAP

# 2. Inicializar entorno virtual
python -m venv .venv
source .venv/Scripts/activate

# 3. Instalación de Flet (Full Package)
pip install flet
🔬 Análisis Modular del Código (Las 10 Partes Clave)
A continuación, se explica la arquitectura del sistema dividida en sus 10 componentes fundamentales:

1️⃣ Importación de Librerías y Módulos
Para este proyecto requerimos el núcleo de flet para la interfaz y el módulo re (Regular Expressions) para la validación avanzada de cadenas de texto.

Python
import flet as ft
import re
2️⃣ Configuración Global de la Página (Viewport)
Se establecen las propiedades de la ventana, el color de fondo y la alineación para que el formulario siempre aparezca centrado perfectamente.

Python
def main(page: ft.Page):
    page.title = "Registro TAP - Pro"
    page.bgcolor = "#F0F0F0"
    page.window_width = 600
    page.window_height = 800
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
3️⃣ Definición de la Ventana Modal (AlertDialog)
Creamos el componente que mostrará el resumen de datos. Se registra en el overlay para que flote sobre la interfaz sin interrumpir el flujo.

Python
txt_resumen = ft.Text("", size=16)
dlg_resumen = ft.AlertDialog(
    title=ft.Text("✅ Registro Exitoso"),
    content=txt_resumen,
    actions=[ft.TextButton("Cerrar", on_click=lambda _: setattr(dlg_resumen, "open", False) or page.update())]
)
page.overlay.append(dlg_resumen)
4️⃣ Componentes de Entrada de Texto (Inputs)
Instanciamos los campos para Nombre, Control y Email, definiendo de antemano el color de borde institucional.

Python
txt_nombre = ft.TextField(label="Nombre Completo", border_color="#4D2A32")
txt_control = ft.TextField(label="N° de Control", border_color="#4D2A32")
txt_email = ft.TextField(label="Email Institucional", border_color="#4D2A32")
5️⃣ Menús de Selección Rígida (Dropdowns)
Para evitar errores de escritura en datos críticos, usamos Dropdowns para Carrera y Semestre, garantizando la integridad de los datos.

Python
dd_carrera = ft.Dropdown(
    label="Carrera",
    expand=True,
    options=[ft.dropdown.Option("Ingeniería en Sistemas"), ft.dropdown.Option("Ingeniería Civil")]
)
dd_semestre = ft.Dropdown(
    label="Semestre",
    width=150,
    options=[ft.dropdown.Option(str(i)) for i in range(1, 11)]
)
6️⃣ Selección de Opción Única (RadioGroup)
Implementamos el sistema de elección de género mediante botones de radio organizados horizontalmente.

Python
rg_genero = ft.RadioGroup(
    content=ft.Row([
        ft.Radio(value="M", label="Masculino"),
        ft.Radio(value="F", label="Femenino"),
    ], alignment=ft.MainAxisAlignment.CENTER)
)
7️⃣ Lógica de Validación Reactiva (El "Cerebro")
Aquí es donde ocurre la magia: el código inspecciona cada control. Si detecta un campo vacío, cambia el color a rojo inmediatamente.

Python
def enviar_click(e):
    hay_error = False
    for c in [txt_nombre, txt_control, txt_email, dd_carrera, dd_semestre]:
        if not c.value:
            c.border_color = "red"
            hay_error = True
        else:
            c.border_color = "#4D2A32"
8️⃣ Validación Estructural de Email (Regex)
No solo revisamos que no esté vacío; verificamos que la estructura del correo sea válida (usuario@dominio.com).

Python
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if txt_email.value and not re.match(email_pattern, txt_email.value):
        txt_email.border_color = "red"
        hay_error = True
9️⃣ Ensamblado del Contenedor "Card"
Agrupamos todos los elementos en un contenedor estilizado con sombras y bordes redondeados para lograr una estética profesional.

Python
card = ft.Container(
    content=ft.Column([
        ft.Text("👤", size=50),
        ft.Text("REGISTRO ESCOLAR", size=22, weight="bold"),
        txt_nombre, txt_control, txt_email,
        ft.Row([dd_carrera, dd_semestre]),
        rg_genero,
        ft.ElevatedButton("REGISTRAR", on_click=enviar_click, bgcolor="#4D2A32", color="white")
    ], horizontal_alignment="center", spacing=15),
    bgcolor="white", padding=40, border_radius=20, shadow=ft.BoxShadow(blur_radius=20)
)
🔟 Punto de Entrada y Renderizado Web
Finalmente, ejecutamos la aplicación forzando la vista en el navegador para máxima compatibilidad.

Python
page.add(card)
ft.run(main, view=ft.AppView.WEB_BROWSER)
📸 Código Completo Para Copiar
Python
import flet as ft
import re

def main(page: ft.Page):
    page.title = "Registro Estudiantil Final"
    page.bgcolor = "#F0F0F0"
    page.window_width = 550
    page.window_height = 800
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    # --- DIALOGO ---
    txt_resumen = ft.Text("", size=16)
    dlg_resumen = ft.AlertDialog(
        title=ft.Text("✅ Datos Guardados"),
        content=txt_resumen,
        actions=[ft.TextButton("Cerrar", on_click=lambda _: setattr(dlg_resumen, "open", False) or page.update())]
    )
    page.overlay.append(dlg_resumen)

    # --- INPUTS ---
    txt_nombre = ft.TextField(label="Nombre", border_color="#4D2A32")
    txt_control = ft.TextField(label="N° Control", border_color="#4D2A32")
    txt_email = ft.TextField(label="Email", border_color="#4D2A32")
    dd_carrera = ft.Dropdown(label="Carrera", expand=True, options=[ft.dropdown.Option("Sistemas")])
    dd_semestre = ft.Dropdown(label="Semestre", width=120, options=[ft.dropdown.Option(str(i)) for i in range(1, 9)])
    rg_genero = ft.RadioGroup(content=ft.Row([ft.Radio(value="M", label="M"), ft.Radio(value="F", label="F")]))

    # --- VALIDACION ---
    def enviar_click(e):
        hay_error = False
        for c in [txt_nombre, txt_control, txt_email, dd_carrera, dd_semestre]:
            if not c.value:
                c.border_color = "red"
                hay_error = True
            else:
                c.border_color = "#4D2A32"
        
        if not hay_error:
            txt_resumen.value = f"Nombre: {txt_nombre.value}\nControl: {txt_control.value}"
            dlg_resumen.open = True
            page.update()
        page.update()

    # --- UI ---
    page.add(ft.Container(
        content=ft.Column([
            ft.Text("👤", size=50),
            txt_nombre, txt_control, txt_email,
            ft.Row([dd_carrera, dd_semestre]),
            rg_genero,
            ft.ElevatedButton("REGISTRAR", on_click=enviar_click, width=250)
        ], horizontal_alignment="center", spacing=15),
        bgcolor="white", padding=30, border_radius=20, width=450, shadow=ft.BoxShadow(blur_radius=15)
    ))

ft.run(main, view=ft.AppView.WEB_BROWSER)
