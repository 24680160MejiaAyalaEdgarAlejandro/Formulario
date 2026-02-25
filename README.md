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

## 🏗️ Configuración del Workspace (Git Bash)

Para asegurar que las dependencias no entren en conflicto, aislamos el proyecto en un entorno virtual:

```bash
# 1. Crear directorio y entrar
mkdir Registro_Estudiantil_TAP
cd Registro_Estudiantil_TAP

# 2. Inicializar entorno virtual
python -m venv .venv
source .venv/Scripts/activate

# 3. Instalación de Flet (Full Package)
pip install flet


💻 Arquitectura del Código (Explicación Técnica)
1️⃣ Estética y Contenedores (UI)
El formulario no es plano; utiliza un diseño de Tarjeta (Card) con sombras y bordes redondeados para una apariencia moderna.

Python
card = ft.Container(
    content=formulario_columna,
    bgcolor="white",
    padding=40,
    border_radius=20,
    shadow=ft.BoxShadow(blur_radius=20, color="black12")
)
BoxShadow: Genera profundidad visual.

Border Radius: Suaviza las esquinas para un diseño "Premium".

2️⃣ El Motor de Validación (Lógica de Eventos)
Esta sección es la más importante. Gestiona el evento on_click del botón y verifica la integridad de los datos.

Python
def enviar_click(e):
    # Verificación de campos obligatorios
    for c in [txt_nombre, txt_control, txt_email, dd_carrera, dd_semestre]:
        if not c.value:
            c.border_color = "red" # Feedback visual de error
            hay_error = True
Validación de Email: Se implementó una lógica de segmentación de cadenas (split) para verificar la existencia del símbolo @ y un dominio válido con punto ..

3️⃣ Ventana Emergente (Confirmación Modal)
Una vez superadas las validaciones, el sistema invoca un AlertDialog.

Python
dlg_resumen = ft.AlertDialog(
    title=ft.Text("✅ REGISTRO EXITOSO"),
    content=txt_resumen, # Muestra el resumen de datos recogidos
    actions=[ft.TextButton("Finalizar", on_click=cerrar_dialogo)]
)
📊 Jerarquía de Componentes
Fragmento de código
graph TD
    A[Page] --> B[Container: Card]
    B --> C[Column: Layout]
    C --> D[Emoji Header: 👤]
    C --> E[Inputs: Nombre/Control/Email]
    C --> F[Dropdowns: Carrera/Semestre]
    C --> G[RadioGroup: Género]
    C --> H[Button: Registrar]
📦 Código Completo de Ejecución
Python
# Para ejecutar este proyecto, simplemente corre:
ft.run(main, view=ft.AppView.WEB_BROWSER)
WEB_BROWSER: Esta configuración garantiza que la aplicación se abra en una pestaña de tu navegador predeterminado, evitando errores de renderizado en sistemas Windows con permisos restringidos.
