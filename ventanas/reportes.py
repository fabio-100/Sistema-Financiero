
import customtkinter as ctk


def abrir_reportes(ventana, gestor):
    reportes = ctk.CTkToplevel(ventana)
    reportes.title("Reportes financieros")
    
    #Se centraliza la ventana emergente
    ancho = 650
    alto = 500

    pos_x = (reportes.winfo_screenwidth() - ancho) // 2
    pos_y = (reportes.winfo_screenheight() - alto) // 2

    reportes.geometry(f"{ancho}x{alto}+{pos_x}+{pos_y}")
    reportes.minsize(550, 400)
    reportes.transient(ventana)

    titulo = ctk.CTkLabel(
        reportes,
        text="Resumen financiero",
        font=("Arial", 24, "bold")
    )
    titulo.pack(pady=25)

    # Calcular ingresos y gastos
    ingresos = sum(
        op["monto"]
        for op in gestor.operaciones_registradas
        if op["tipo"] == "Ingreso"
    )

    gastos = sum(
        op["monto"]
        for op in gestor.operaciones_registradas
        if op["tipo"] == "Retiro"
    )

    cantidad = len(gestor.operaciones_registradas)

    # Mostrar saldo actual
    saldo = ctk.CTkLabel(
        reportes,
        text=f"Saldo actual: $ {gestor.saldo_actual:,.2f}",
        font=("Arial", 20, "bold")
    )
    saldo.pack(pady=15)

    # Mostrar ingresos
    etiqueta_ingresos = ctk.CTkLabel(
        reportes,
        text=f"Total de ingresos: $ {ingresos:,.2f}",
        font=("Arial", 16),
        text_color="green"
    )
    etiqueta_ingresos.pack(pady=10)

    # Mostrar gastos
    etiqueta_gastos = ctk.CTkLabel(
        reportes,
        text=f"Total de gastos: $ {gastos:,.2f}",
        font=("Arial", 16),
        text_color="red"
    )
    etiqueta_gastos.pack(pady=10)

    # Mostrar cantidad de operaciones
    etiqueta_cantidad = ctk.CTkLabel(
        reportes,
        text=f"Cantidad de operaciones: {cantidad}",
        font=("Arial", 16)
    )
    etiqueta_cantidad.pack(pady=10)

    # Botón cerrar
    boton_cerrar = ctk.CTkButton(
        reportes,
        text="Cerrar",
        command=reportes.destroy
    )
    boton_cerrar.pack(pady=25)
