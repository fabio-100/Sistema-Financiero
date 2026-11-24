import customtkinter as ctk
from ventanas.historial import abrir_historial
from ventanas.reportes import abrir_reportes
from ventanas.estadisticas import abrir_estadisticas
from ventanas.configuracion import abrir_configuracion
from logica.gestor_operaciones import GestorOperaciones
from ventanas.operaciones import abrir_dialogo
from componentes.atomos import crear_etiqueta
from componentes.moleculas import crear_boton_operacion
from componentes.organismos import (
    crear_menu_lateral,
    crear_panel_categorias,
    crear_panel_reportes,
    actualizar_panel_categorias
)


# Formatea los importes en pesos argentinos
def formatear_monto(monto):
    return f"$ {monto:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


# Crea la pantalla principal
def crear_inicio(ventana, nombre):

    gestor = GestorOperaciones()

    contenido = ctk.CTkFrame(ventana, fg_color=("#F4F7FC", "#171720"))
    contenido.pack(fill="both", expand=True)

    contenido.grid_columnconfigure(0, weight=0)
    contenido.grid_columnconfigure(1, weight=8)
    contenido.grid_columnconfigure(2, weight=2)
    contenido.grid_rowconfigure(0, weight=1)
    contenido.grid_columnconfigure(0, minsize=260)

    # Menú lateral
    menu = crear_menu_lateral(
    contenido,
    nombre,
    comando_historial=lambda: abrir_historial(ventana, gestor),
    comando_reportes=lambda: abrir_reportes(ventana, gestor),
    comando_estadisticas=lambda: abrir_estadisticas(ventana, gestor),
    comando_configuracion=lambda: abrir_configuracion(ventana, nombre)
)
    menu.grid(row=0, column=0, sticky="nsew")

    # Panel central
    central = ctk.CTkFrame(contenido, fg_color="transparent")
    central.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
    central.grid_columnconfigure(0, weight=1)
    central.grid_rowconfigure(3, weight=1)

    crear_etiqueta(
        central, f"¡Hola, {nombre}!", tamaño=27, negrita=True
    ).grid(row=0, column=0, sticky="w")

    # Tarjeta de saldo
    saldo = ctk.CTkFrame(
        central,
        fg_color=("#E6F6F0","#202022"),
        corner_radius=14,
        border_width=1,
        border_color=("#BDE5D5","#101014"),
        height=135
    )
    saldo.grid(row=1, column=0, sticky="ew", pady=(0, 10))
    saldo.grid_propagate(False)

    crear_etiqueta(
        saldo, "Saldo actual", tamaño=15
    ).pack(anchor="w", padx=20, pady=(12, 0))

    etiqueta_saldo = crear_etiqueta(
        saldo, formatear_monto(gestor.saldo_actual),
        tamaño=30, negrita=True
    )
    etiqueta_saldo.pack(anchor="w", padx=20, pady=(0, 6))

    # Botones de ingreso y retiro
    operaciones = ctk.CTkFrame(central, fg_color="transparent", height=110)
    operaciones.grid(row=2, column=0, sticky="new", pady=(0, 10))
    operaciones.grid_propagate(False)
    operaciones.grid_columnconfigure((0, 1), weight=1)
    operaciones.grid_rowconfigure(0, weight=1)

    # Panel de últimas operaciones
    historial = ctk.CTkFrame(
        central,
        fg_color=("#FFFFFF","#101014"),
        corner_radius=12,
        border_width=1,
        border_color=("#DCE5F2","#101014"),
    )
    historial.grid(row=3, column=0, sticky="nsew")

    crear_etiqueta(
        historial, "Últimas operaciones", tamaño=17, negrita=True
    ).pack(anchor="w", padx=16, pady=5)

    encabezados = ["Fecha y hora", "Tipo", "Categoría", "Monto", "Estado"]
    fila_encabezados = ctk.CTkFrame(historial, fg_color="transparent")
    fila_encabezados.pack(fill="x", padx=12)

    for encabezado in encabezados:
        crear_etiqueta(
            fila_encabezados, encabezado, tamaño=11, negrita=True
        ).pack(side="left", expand=True, padx=2)

    contenedor_historial = ctk.CTkFrame(
        historial, fg_color="transparent"
    )
    contenedor_historial.pack(fill="both", expand=True, padx=12)

    # Panel derecho
    derecho = ctk.CTkFrame(contenido, fg_color="transparent")
    derecho.grid(row=0, column=2, sticky="nsew", padx=(0, 18), pady=20)
    derecho.grid_columnconfigure(0, weight=1)
    derecho.grid_rowconfigure(0, weight=5)
    derecho.grid_rowconfigure(1, weight=5)

    categorias = crear_panel_categorias(derecho)
    categorias.grid(row=0, column=0, sticky="nsew", pady=(0, 15))

    reportes = crear_panel_reportes(
        derecho,
        comando_estadisticas=lambda: abrir_estadisticas(ventana, gestor)
    )
    reportes.grid(row=1, column=0, sticky="nsew")

    # Actualiza el historial de operaciones
    def actualizar_historial():
        for widget in contenedor_historial.winfo_children():
            widget.destroy()

        if not gestor.operaciones_registradas:
            crear_etiqueta(
                contenedor_historial,
                "Todavía no hay operaciones",
                tamaño=13,
                color="#718096"
            ).pack(pady=25)
            return

        for operacion in reversed(gestor.operaciones_registradas[-5:]):
            fila = ctk.CTkFrame(
                contenedor_historial, fg_color="transparent"
            )
            fila.pack(fill="x", pady=7)

            monto = (
                "+" if operacion["tipo"] == "Ingreso" else "-"
            ) + formatear_monto(operacion["monto"])

            datos = [
                operacion["fecha"],
                operacion["tipo"],
                operacion["categoria"],
                monto,
                "Completado"
            ]

            for indice, dato in enumerate(datos):
                color = (
                    "#269F73" if operacion["tipo"] == "Ingreso"
                    else "#D94B55"
                ) if indice in (1, 3) else ("#243B64","#67678F")

                crear_etiqueta(
                    fila, dato, tamaño=10, color=color
                ).pack(side="left", expand=True, padx=2)

    # Actualiza el saldo y las categorías
    def actualizar_pantalla():
        etiqueta_saldo.configure(
            text=formatear_monto(gestor.saldo_actual)
        )

        actualizar_historial()

        actualizar_panel_categorias(
            categorias, gestor.gastos_categoria
        )

    # Conecta los botones con las ventanas de operación
    crear_boton_operacion(
        operaciones,
        "+  Ingresar dinero",
        "Agregar fondos a tu cuenta",
        "#269F73",
        comando=lambda: abrir_dialogo(
            ventana, "Ingreso", gestor, actualizar_pantalla
        )
    ).grid(row=0, column=0, sticky="ew", padx=(0, 8))

    crear_boton_operacion(
        operaciones,
        "−  Retirar dinero",
        "Realizar un gasto",
        "#E75B63",
        comando=lambda: abrir_dialogo(
            ventana, "Retiro", gestor, actualizar_pantalla
        )
    ).grid(row=0, column=1, sticky="ew", padx=(8, 0))

    # Barra inferior
    barra = ctk.CTkFrame(ventana, height=28, fg_color=("#EAF1FA","#101014"))
    barra.pack(fill="x", side="bottom")

    crear_etiqueta(
        barra, "●  Sistema en funcionamiento",
        tamaño=11, color="#269F73"
    ).pack(side="left", padx=15, pady=5)

    actualizar_historial()
