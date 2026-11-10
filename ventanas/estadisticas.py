

import customtkinter as ctk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def abrir_estadisticas(ventana, gestor):

    panel = ctk.CTkToplevel(ventana)
    panel.title("Estadísticas financieras")
    panel.geometry("950x650")
    panel.configure(fg_color="#F4F7FC")
    panel.transient(ventana)
    panel.grab_set()

    ctk.CTkLabel(
        panel,
        text="ESTADÍSTICAS FINANCIERAS",
        font=("Arial", 25, "bold"),
        text_color="#243B64"
    ).pack(pady=20)

    # Cálculo de ingresos y egresos
    operaciones = gestor.operaciones_registradas

    ingresos = sum(
        op["monto"] for op in operaciones
        if op["tipo"] == "Ingreso"
    )

    egresos = sum(
        op["monto"] for op in operaciones
        if op["tipo"] == "Retiro"
    )

    # Tarjetas de resumen
    tarjetas = ctk.CTkFrame(panel, fg_color="transparent")
    tarjetas.pack(pady=10)

    datos = [
        ("INGRESOS", ingresos, "#269F73"),
        ("EGRESOS", egresos, "#E75B63"),
        ("SALDO ACTUAL", gestor.saldo_actual, "#4169E1")
    ]

    for titulo, monto, color in datos:
        tarjeta = ctk.CTkFrame(
            tarjetas, fg_color="white", corner_radius=12
        )
        tarjeta.pack(side="left", padx=12, ipadx=15, ipady=10)

        ctk.CTkLabel(
            tarjeta,
            text=titulo,
            font=("Arial", 12, "bold"),
            text_color=color
        ).pack(padx=15, pady=5)

        ctk.CTkLabel(
            tarjeta,
            text=f"$ {monto:,.2f}",
            font=("Arial", 19, "bold"),
            text_color="#243B64"
        ).pack(padx=15, pady=5)

    # Gráficos
    figura = Figure(figsize=(10, 4.5), dpi=100)

    # Gráfico de barras
    grafico = figura.add_subplot(121)

    grafico.bar(
        ["Ingresos", "Egresos"],
        [ingresos, egresos],
        color=["#269F73", "#E75B63"]
    )

    grafico.set_title("Ingresos y egresos")
    grafico.set_ylabel("Monto ($)")
    grafico.grid(axis="y", alpha=0.2)

    # Gráfico circular por categoría
    circular = figura.add_subplot(122)

    categorias = gestor.gastos_categoria

    if categorias and sum(categorias.values()) > 0:
        circular.pie(
            list(categorias.values()),
            labels=list(categorias.keys()),
            autopct="%1.1f%%",
            startangle=90,
            wedgeprops={"edgecolor": "white"}
        )
        circular.set_title("Gastos por categoría")
    else:
        circular.text(
            0.5, 0.5,
            "Todavía no hay gastos",
            ha="center",
            va="center"
        )
        circular.set_title("Gastos por categoría")

    figura.tight_layout()

    canvas = FigureCanvasTkAgg(figura, master=panel)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=15)
