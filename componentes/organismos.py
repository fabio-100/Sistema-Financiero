
import customtkinter as ctk

print("ORGANISMOS:", __file__)
from componentes.atomos import crear_etiqueta
from componentes.moleculas import crear_tarjeta_categoria


# Crea el menú lateral

def crear_menu_lateral(padre, nombre, comando_historial=None, comando_reportes=None):
    menu = ctk.CTkFrame(
        padre,
        width=260,
        fg_color="#EAF1FA",
        corner_radius=0
    )
    menu.grid_propagate(False)

    crear_etiqueta(
        menu, "●", tamaño=42, color="#4169E1"
    ).pack(pady=(25, 0))

    crear_etiqueta(
        menu, "Usuario:", tamaño=13, color="#64748B"
    ).pack(pady=(5, 0))

    crear_etiqueta(
        menu, nombre, tamaño=17, negrita=True
    ).pack(pady=(0, 25))

    opciones = [
        ("⌂   Inicio", None),
        ("▤   Historial", comando_historial),
        ("▥   Reportes", comando_reportes),
        ("◷   Estadísticas", None),
        ("⚙   Configuración", None)
    ]

    for opcion, comando in opciones:
        boton = ctk.CTkButton(
            menu,
            text=opcion,
            command=comando,
            fg_color="#D5E5FC" if "Inicio" in opcion else "transparent",
            text_color="#243B64",
            hover_color="#D5E5FC",
            anchor="w",
            height=45,
            corner_radius=9,
            font=("Arial", 14, "bold" if "Inicio" in opcion else "normal")
        )
        boton.pack(fill="x", padx=15, pady=5)

    return menu



# Crea el panel de gastos por categoría
def crear_panel_categorias(padre):
    panel = ctk.CTkFrame(
        padre,
        fg_color="#FFFFFF",
        corner_radius=12,
        border_width=1,
        border_color="#DCE5F2"
    )

    crear_etiqueta(
        panel, "Gastos por categoría", tamaño=17, negrita=True
    ).pack(anchor="w", padx=18, pady=(9, 4))

    panel.contenedor_categorias = ctk.CTkFrame(
        panel, fg_color="transparent"
    )
    panel.contenedor_categorias.pack(
        fill="both", expand=True, padx=0, pady=(0, 4)
    )

    actualizar_panel_categorias(panel, {})

    return panel


# Actualiza los gastos mostrados en el panel
def actualizar_panel_categorias(panel, gastos):
    for widget in panel.contenedor_categorias.winfo_children():
        widget.destroy()

    colores = {
        "Comida": "#F5A45B",
        "Servicios": "#38A7E8",
        "Entretenimiento": "#A477DD",
        "Transporte": "#69B875",
        "Salud": "#E477A5",
        "Educación": "#D6A43B",
        "Otros": "#9AA5B1"
    }

    total = sum(gastos.values())

    for nombre, color in colores.items():
        monto = gastos.get(nombre, 0)
        porcentaje = (monto / total * 100) if total > 0 else 0

        tarjeta = crear_tarjeta_categoria(
            panel.contenedor_categorias,
            nombre,
            f"{monto:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
            porcentaje,
            color
        )
        tarjeta.pack(fill="x", padx=18, pady=2)


# Crea el panel de reportes rápidos
def crear_panel_reportes(padre):
    panel = ctk.CTkFrame(
        padre,
        fg_color="#FFFFFF",
        corner_radius=12,
        border_width=1,
        border_color="#DCE5F2"
    )

    crear_etiqueta(
        panel, "Reportes rápidos", tamaño=17, negrita=True
    ).pack(anchor="w", padx=16, pady=(9, 4))

    ctk.CTkButton(
        panel,
        text="▤   Generar comprobante\n      Ver detalle de una operación",
        fg_color="#5689E8",
        hover_color="#3E70CE",
        height=54,
        corner_radius=10,
        anchor="w",
        font=("Arial", 12, "bold")
    ).pack(fill="both", expand=True, padx=12, pady=4)

    ctk.CTkButton(
        panel,
        text="◷   Ver estadísticas\n      Resumen de gastos e ingresos",
        fg_color="#9671D0",
        hover_color="#7954B5",
        height=54,
        corner_radius=10,
        anchor="w",
        font=("Arial", 12, "bold")
    ).pack(fill="both", expand=True, padx=12, pady=4)

    return panel
