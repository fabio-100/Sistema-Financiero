
import customtkinter as ctk

print("MOLECULAS:", __file__)
from componentes.atomos import crear_etiqueta


# Crea una tarjeta con título y valor
def crear_tarjeta_dato(padre, titulo, valor):
    tarjeta = ctk.CTkFrame(
        padre,
        fg_color=("#FFFFFF","#101014"),
        corner_radius=14,
        border_width=1,
        border_color=("#DCE5F2","#101014"),
    )

    crear_etiqueta(
        tarjeta, titulo, tamaño=13, color="#718096"
    ).pack(anchor="w", padx=16, pady=(12, 3))

    crear_etiqueta(
        tarjeta, valor, tamaño=23, negrita=True
    ).pack(anchor="w", padx=16, pady=(0, 12))

    return tarjeta


# Crea un botón grande para las operaciones
def crear_boton_operacion(padre, titulo, subtitulo, color, comando=None):
    boton = ctk.CTkButton(
        padre,
        text=f"{titulo}\n{subtitulo}",
        command=comando,
        fg_color=color,
        hover_color=color,
        corner_radius=20,
        height=100,
        font=("Arial", 16, "bold")
    )
    return boton


# Crea una tarjeta compacta para mostrar un gasto por categoría
def crear_tarjeta_categoria(padre, categoria, monto, porcentaje, color):
    tarjeta = ctk.CTkFrame(padre, fg_color="transparent")

    # Muestra el nombre y el importe en la misma línea
    fila = ctk.CTkFrame(tarjeta, fg_color="transparent")
    fila.pack(fill="x")

    crear_etiqueta(
        fila, categoria, tamaño=11, negrita=True
    ).pack(side="left")

    crear_etiqueta(
        fila, f"$ {monto}  ({porcentaje:.1f}%)", tamaño=10
    ).pack(side="right")

    # Barra de porcentaje
    barra = ctk.CTkProgressBar(
        tarjeta,
        height=5,
        corner_radius=8,
        progress_color=color
    )
    barra.pack(fill="x", pady=(1, 0))
    barra.set(porcentaje / 100)

    return tarjeta