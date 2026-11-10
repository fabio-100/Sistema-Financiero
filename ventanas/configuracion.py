
import customtkinter as ctk


def cambiar_tema(tema):
    if tema == "Claro":
        ctk.set_appearance_mode("Light")
    elif tema == "Oscuro":
        ctk.set_appearance_mode("Dark")
    else:
        ctk.set_appearance_mode("System")


def abrir_configuracion(ventana, nombre):

    config = ctk.CTkToplevel(ventana)
    config.title("Configuración")
    config.geometry("450x400")
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

    selector_tema = ctk.CTkOptionMenu(
        config,
        values=["Claro", "Oscuro", "Sistema"],
        command=cambiar_tema
    )
    selector_tema.pack(pady=10)

    ctk.CTkLabel(
        config,
        text="Sistema Financiero",
        font=("Arial", 16, "bold")
    ).pack(pady=10)

    ctk.CTkLabel(
        config,
        text="Versión 1.0",
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
