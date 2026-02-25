import flet as ft

def main(page: ft.Page):
    page.title = "Registro TAP - Final"
    page.bgcolor = "#F0F0F0"
    page.theme_mode = ft.ThemeMode.LIGHT
    
    # --- VENTANA MODAL (AlertDialog) ---
    txt_resumen = ft.Text("", size=16)
    
    def cerrar_dialogo(e):
        dlg_resumen.open = False
        page.update()

    dlg_resumen = ft.AlertDialog(
        title=ft.Text("✅ Registro Exitoso"),
        content=txt_resumen,
        actions=[ft.TextButton("Entendido", on_click=cerrar_dialogo)]
    )
    
    # Agregamos el diálogo a la página desde el inicio
    page.overlay.append(dlg_resumen)

    # --- CONTROLES ---
    txt_nombre = ft.TextField(label="Nombre Completo", border_color="#4D2A32")
    txt_control = ft.TextField(label="N° de Control", border_color="#4D2A32")
    txt_email = ft.TextField(label="Email Institucional", border_color="#4D2A32")

    dd_carrera = ft.Dropdown(
        label="Carrera",
        expand=True,
        options=[
            ft.dropdown.Option("Ingeniería en Sistemas"),
            ft.dropdown.Option("Ingeniería Civil"),
            ft.dropdown.Option("Ingeniería Industrial"),
            ft.dropdown.Option("Ingeniería Mecatronica"),
            ft.dropdown.Option("Contador Publico"),
        ]
    )

    dd_semestre = ft.Dropdown(
        label="Semestre",
        width=150,
        options=[ft.dropdown.Option(str(i)) for i in range(1, 11)]
    )
    
    rg_genero = ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value="Masculino", label="Masculino"),
            ft.Radio(value="Femenino", label="Femenino"),
        ], alignment=ft.MainAxisAlignment.CENTER)
    )

    # --- LÓGICA DE VALIDACIÓN Y ENVÍO ---
    def enviar_click(e):
        hay_error = False
        
        # 1. Validación de campos vacíos
        for c in [txt_nombre, txt_control, txt_email, dd_carrera, dd_semestre]:
            if not c.value:
                c.border_color = "red"
                hay_error = True
            else:
                c.border_color = "#4D2A32"

        # 2. VALIDACIÓN DE EMAIL (Corregida)
        if txt_email.value:
            # Verificamos que tenga '@' y un '.' después del arroba
            if "@" not in txt_email.value or "." not in txt_email.value.split("@")[-1]:
                txt_email.border_color = "red"
                txt_email.helper_text = "Correo no válido"
                hay_error = True
            else:
                txt_email.helper_text = ""

        # 3. Validación de Género
        if not rg_genero.value:
            hay_error = True

        if hay_error:
            page.update()
        else:
            # 4. PREPARAR RESUMEN Y MOSTRAR VENTANA
            txt_resumen.value = (
                f"Nombre: {txt_nombre.value}\n"
                f"Control: {txt_control.value}\n"
                f"Email: {txt_email.value}\n"
                f"Carrera: {dd_carrera.value}\n"
                f"Semestre: {dd_semestre.value}\n"
                f"Género: {rg_genero.value}"
            )
            
            # Abrir diálogo (Forma forzada para 0.80.5)
            dlg_resumen.open = True
            page.update()

    btn_enviar = ft.Button(
        content=ft.Text("REGISTRAR ALUMNO", weight="bold"),
        on_click=enviar_click,
        width=300
    )

    # --- DISEÑO ---
    card = ft.Container(
        content=ft.Column([
            ft.Text("👤", size=50), 
            ft.Text("REGISTRO ESCOLAR", size=22, weight="bold", color="#4D2A32"),
            txt_nombre,
            txt_control,
            txt_email,
            ft.Row([dd_carrera, dd_semestre]),
            rg_genero,
            btn_enviar
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=15),
        bgcolor="white",
        padding=40,
        border_radius=20,
        width=520,
        shadow=ft.BoxShadow(blur_radius=20, color="black12")
    )

    page.add(card)

ft.run(main, view=ft.AppView.WEB_BROWSER)