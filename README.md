# 🚀 Tópicos Avanzados de Programación - Unidad 1: Interfaces Gráficas (GUI)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flet](https://img.shields.io/badge/flet-D1345B?style=for-the-badge&logo=google-chrome&logoColor=white)
![VS Code](https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual-studio-code&logoColor=white)

Este repositorio contiene la implementación técnica y documentación teórica de la **Unidad 1**. El proyecto central es un **Sistema de Registro Estudiantil** desarrollado con **Flet**, un framework moderno que permite construir interfaces interactivas en Python con capacidades multi-plataforma.

---

## 📑 Contenido Teórico (Puntos 1.1 al 1.4)

### 1.1 Creación de interfaz gráfica para usuarios
La interfaz se construyó bajo un modelo de **contenedores y layouts**. Se utilizó un `ft.Container` como "Card" principal para agrupar los elementos, aplicando propiedades de diseño como `border_radius` (bordes redondeados) y `BoxShadow` (sombras dinámicas) para mejorar la experiencia de usuario (UX).

### 1.2 Tipos de eventos
El sistema gestiona principalmente dos tipos de eventos:
* **Eventos de Acción (`on_click`):** Disparados por el botón de registro.
* **Eventos de Cambio de Estado:** Controlados por la lógica de validación que modifica las propiedades visuales de los componentes en tiempo real.

### 1.3 Manejo de eventos
Se implementó un **Manejador de Eventos (Event Handler)** llamado `enviar_click`. Esta función actúa como el cerebro del formulario: intercepta los datos, los valida y decide si muestra una alerta de error o la ventana modal de éxito.

### 1.4 Manejo de componentes gráficos de control
Se utilizaron los controles más avanzados de la biblioteca Material Design:
* `TextField`: Entrada de texto con validación de máscara y vacíos.
* `Dropdown`: Menú de selección rígida para Carrera y Semestre.
* `RadioGroup`: Selección de opción única para el género del estudiante.
* `AlertDialog`: Ventana modal para confirmación de datos.

---

## 🛠️ Explicación Detallada del Código

### A. La Estructura de Validación
```python
for c in [txt_nombre, txt_control, txt_email, dd_carrera, dd_semestre]:
    if not c.value:
        c.border_color = "red"
        hay_error = True

Gemini ha dicho
¡Claro que sí, César! Vamos a armar un README.md de nivel profesional. Este archivo es la "cara" de tu proyecto; si un reclutador o tu profesor lo ve, debe entender que no solo copiaste código, sino que dominas la arquitectura de componentes y la lógica de eventos.


Explicación: Se utiliza un bucle que recorre una lista de objetos. Si la propiedad .value está vacía, se dispara un cambio de propiedad visual (border_color), transformando el
 borde café en rojo. Esto cumple con el requisito de Feedback Visual.

B. Validación de Email
Python
if "@" not in txt_email.value or "." not in txt_email.value.split("@")[-1]:
    txt_email.border_color = "red"
Explicación: No solo se revisa que no esté vacío, sino que mediante lógica de strings verificamos la existencia del símbolo arroba y un punto en el dominio, asegurando la integridad del dato.

C. La Ventana Modal (AlertDialog)
Python
page.overlay.append(dlg_resumen) # Registro en la capa superior
dlg_resumen.open = True         # Disparo visual
Explicación: Para que el resumen aparezca, el componente AlertDialog se inserta en el overlay de la página. Al ser una aplicación reactiva, es necesario llamar a page.update()
 para que el navegador renderice el cambio de estado de la ventana de cerrada a abierta.

🚀 Cómo ejecutar el proyecto
Clonar el repositorio:

Bash
git clone [https://github.com/TU_USUARIO/TU_REPOSITORIO.git](https://github.com/TU_USUARIO/TU_REPOSITORIO.git)
Crear y activar entorno virtual:

Bash
python -m venv .venv
source .venv/Scripts/activate  # En Windows
Instalar dependencias:

Bash
pip install flet
Correr la aplicación:

Bash
python form.py
