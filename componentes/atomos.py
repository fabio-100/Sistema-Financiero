import customtkinter as ctk

#Creamos una etiqueta

def crear_etiqueta(
    padre,texto,tamaño=14,
    color=("#243B64","#67678F"),
    negrita=False
):
    etiqueta = ctk.CTkLabel(
        padre,text=texto,
        font=("Arial", tamaño, "bold" if negrita else "normal"),
        text_color=color
    )

    return etiqueta

#Creamos un botón

def crear_boton(
    padre,texto,comando=None,
    color="#4169E1",
    color_hover="#34518A"
):
    boton = ctk.CTkButton(
        padre,text=texto,
        command=comando,
        fg_color=color,
        hover_color=color_hover,
        corner_radius=12,
        height=42,
        font=("Arial", 14, "bold")
    )

    return boton
