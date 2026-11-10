
import customtkinter as ctk


def abrir_historial(ventana, gestor):
    historial = ctk.CTkToplevel(ventana)
    historial.title("Historial de operaciones")

    #Se centraliza la ventana emergente
    ancho = 850
    alto = 550

    pos_x = (historial.winfo_screenwidth() - ancho) // 2
    pos_y = (historial.winfo_screenheight() - alto) // 2

    historial.geometry(f"{ancho}x{alto}+{pos_x}+{pos_y}")
    historial.minsize(700, 450)
    
    historial.transient(ventana)

    # Título
    titulo = ctk.CTkLabel(
        historial,
        text="Historial de operaciones",
        font=("Arial", 24, "bold")
    )
    titulo.pack(pady=20)

    # Encabezados de la tabla
    encabezado = ctk.CTkFrame(historial)
    encabezado.pack(fill="x", padx=20, pady=5)

    columnas = ["Fecha", "Tipo", "Categoría", "Monto", "Estado"]

    for columna in columnas:
        etiqueta = ctk.CTkLabel(
            encabezado,
            text=columna,
            font=("Arial", 13, "bold")
        )
        etiqueta.pack(side="left", expand=True, padx=5, pady=10)

    # Área desplazable para mostrar todas las operaciones
    lista = ctk.CTkScrollableFrame(historial)
    lista.pack(fill="both", expand=True, padx=20, pady=10)

    operaciones = gestor.operaciones_registradas

    if not operaciones:
        mensaje = ctk.CTkLabel(
            lista,
            text="Todavía no hay operaciones registradas."
        )
        mensaje.pack(pady=20)

    else:
        for operacion in reversed(operaciones):
            fila = ctk.CTkFrame(lista)
            fila.pack(fill="x", pady=3)

            monto = operacion["monto"]
            tipo = operacion["tipo"]

            signo = "+" if tipo == "Ingreso" else "-"
            monto_texto = f"{signo} $ {monto:,.2f}"

            datos = [
                operacion["fecha"],
                tipo,
                operacion["categoria"],
                monto_texto,
                "Completado"
            ]

            for dato in datos:
                etiqueta = ctk.CTkLabel(
                    fila,
                    text=dato
                )
                etiqueta.pack(side="left", expand=True, padx=5, pady=10)

    # Botón para cerrar
    boton_cerrar = ctk.CTkButton(
        historial,
        text="Cerrar",
        command=historial.destroy
    )
    boton_cerrar.pack(pady=15)
