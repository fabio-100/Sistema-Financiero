
import customtkinter as ctk

def centrar_ventana(ventana, ancho, alto):
    ventana.update_idletasks()

    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()

    x = (ancho_pantalla - ancho) // 2
    y = (alto_pantalla - alto) // 2

    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")


def cambiar_tema(tema, config):
    if tema == "Claro":
        ctk.set_appearance_mode("Light")
    elif tema == "Oscuro":
        ctk.set_appearance_mode("Dark")
    config.destroy()


def abrir_configuracion(ventana, nombre):

    config = ctk.CTkToplevel(ventana)
    config.transient(ventana)
    config.lift()
    config.focus_force()
    config.title("Configuración")
    centrar_ventana(config, 450, 400)
    config.resizable(False, False)

    ctk.CTkLabel(
        config,
        text="⚙ Configuración",
        font=("Arial", 24, "bold")
    ).pack(pady=25)

    ctk.CTkLabel(
        config,
        text=f"Usuario: {nombre}",
        font=("Arial", 15)
    ).pack(pady=10)

    ctk.CTkLabel(
        config,
        text="Apariencia del sistema",
        font=("Arial", 15, "bold")
    ).pack(pady=(15, 5))

    if ctk.get_appearance_mode() == "Light":
        tema_actual = "Claro"
    else:
        tema_actual = "Oscuro"

    tema_var = ctk.StringVar(value=tema_actual)

    selector_tema = ctk.CTkOptionMenu(
        config,
        values=["Claro", "Oscuro"],
        variable=tema_var,
        command=lambda tema: cambiar_tema(tema,config)
    )
    selector_tema.pack(pady=10)

    ctk.CTkLabel(
        config,
        text="Sistema Financiero",
        font=("Arial", 16, "bold")
    ).pack(pady=10)

    ctk.CTkLabel(
        config,
        text="Versión 1.1",
        font=("Arial", 13),
        text_color="gray"
    ).pack(pady=5)

    ctk.CTkButton(
        config,
        text="Cerrar",
        command=config.destroy,
        fg_color="#5689E8",
        hover_color="#3E70CE"
    ).pack(pady=25)
