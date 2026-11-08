import customtkinter as ctk

from ventanas.inicio import crear_inicio

# Configuración de la aplicación
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


# Centra la ventana en la pantalla
def centrar_ventana(ventana, ancho, alto):
    ventana.update_idletasks()

    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()

    x = (ancho_pantalla - ancho) // 2
    y = (alto_pantalla - alto) // 2 - 30

    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")


# Abre la pantalla principal reutilizando la ventana inicial
def iniciar_aplicacion(nombre):

    ventana_inicio.unbind("<Return>")

    # Elimina los elementos de la pantalla de bienvenida
    for widget in ventana_inicio.winfo_children():
        widget.destroy()

    ventana_inicio.title("Sistema de Administración Financiera")
    ventana_inicio.geometry("1200x650")
    ventana_inicio.minsize(1000, 600)
    ventana_inicio.resizable(True, True)
    ventana_inicio.configure(fg_color="#F4F7FC")

    crear_inicio(ventana_inicio, nombre)

    centrar_ventana(ventana_inicio, 1200, 650)


# Solicita el nombre del usuario
def solicitar_nombre():
    nombre = entrada_nombre.get().strip()

    if not nombre:
        etiqueta_error.configure(
            text="Por favor, ingresá tu nombre."
        )
        return

    iniciar_aplicacion(nombre)


# Ventana inicial
ventana_inicio = ctk.CTk()
ventana_inicio.title("Bienvenido")
ventana_inicio.geometry("380x250")
ventana_inicio.resizable(False, False)
ventana_inicio.configure(fg_color="#F4F7FC")

crear_etiqueta_bienvenida = ctk.CTkLabel(
    ventana_inicio,
    text="¡Bienvenido!",
    font=("Arial", 25, "bold"),
    text_color="#243B64"
)
crear_etiqueta_bienvenida.pack(pady=(30, 15))

ctk.CTkLabel(
    ventana_inicio,
    text="Ingresá tu nombre para comenzar",
    font=("Arial", 14),
    text_color="#64748B"
).pack(pady=(0, 12))

entrada_nombre = ctk.CTkEntry(
    ventana_inicio,
    placeholder_text="Tu nombre",
    width=280,
    height=40
)
entrada_nombre.pack(pady=5)

etiqueta_error = ctk.CTkLabel(
    ventana_inicio,
    text="",
    text_color="#D94B55",
    font=("Arial", 12)
)
etiqueta_error.pack()

ctk.CTkButton(
    ventana_inicio,
    text="Comenzar",
    command=solicitar_nombre,
    width=280,
    height=40,
    corner_radius=10,
    fg_color="#4169E1",
    hover_color="#3155B5"
).pack(pady=10)

ventana_inicio.bind("<Return>", lambda evento: solicitar_nombre())

# Centra la ventana de bienvenida
centrar_ventana(ventana_inicio, 380, 250)

ventana_inicio.mainloop()
