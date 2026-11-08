import customtkinter as ctk

from tkinter import messagebox
from componentes.atomos import crear_etiqueta



# Formatea los importes en pesos argentinos
def formatear_monto(monto):
    return f"$ {monto:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


# Abre la ventana para ingresar o retirar dinero
def abrir_dialogo(ventana, tipo, gestor, actualizar_pantalla):

    dialogo = ctk.CTkToplevel(ventana)
    dialogo.title(tipo + " dinero")
    
    ancho = 380
    alto = 300 if tipo == "Ingreso" else 370

    dialogo.geometry(f"{ancho}x{alto}")
    dialogo.resizable(False, False)
    dialogo.configure(fg_color="#F4F7FC")
    dialogo.transient(ventana)

    dialogo.update_idletasks()

    ancho_pantalla = dialogo.winfo_screenwidth()
    alto_pantalla = dialogo.winfo_screenheight()

    x = (ancho_pantalla - ancho) // 2
    y = (alto_pantalla - alto) // 2

    dialogo.geometry(f"{ancho}x{alto}+{x}+{y}")
    dialogo.grab_set()

    crear_etiqueta(
        dialogo, tipo + " dinero", tamaño=22, negrita=True
    ).pack(pady=(20, 15))

    crear_etiqueta(
        dialogo, "Importe:", tamaño=14
    ).pack(anchor="w", padx=30)

    entrada_monto = ctk.CTkEntry(
        dialogo,
        height=38
    )
    entrada_monto.pack(fill="x", padx=30, pady=(5, 15))

    selector_categoria = None

    if tipo == "Retiro":
        crear_etiqueta(
            dialogo, "Categoría:", tamaño=14
        ).pack(anchor="w", padx=30)

        selector_categoria = ctk.CTkOptionMenu(
            dialogo,
            values=[
                "Seleccionar categoría",
                "Comida",
                "Servicios",
                "Transporte",
                "Entretenimiento",
                "Salud",
                "Educación",
                "Otros"
            ],
            height=38
        )
        selector_categoria.pack(fill="x", padx=30, pady=(5, 15))

        selector_categoria.set("Seleccionar categoría")

    # Valida y confirma la operación
    def confirmar():
        texto_monto = entrada_monto.get().strip()

        try:
            if "," in texto_monto:
                monto = float(
                    texto_monto.replace(".", "").replace(",", ".")
                )
            else:
                monto = float(texto_monto)

            if monto <= 0:
                raise ValueError

        except ValueError:
            messagebox.showerror(
                "Importe inválido",
                "Ingresá un importe válido mayor que cero.",
                parent=dialogo
            )
            return

        if tipo == "Ingreso":
            correcto, error = gestor.ingresar(monto)

        else:
            categoria = selector_categoria.get()

            if categoria == "Seleccionar categoría":
                messagebox.showerror(
                    "Falta una categoría",
                    "Tenés que seleccionar una categoría.",
                    parent=dialogo
                )
                return

            correcto, error = gestor.retirar(monto, categoria)

        if not correcto:
            messagebox.showerror(
                "No se pudo realizar la operación",
                error,
                parent=dialogo
            )
            return

        actualizar_pantalla()
        dialogo.destroy()

    ctk.CTkButton(
        dialogo,
        text="Confirmar",
        command=confirmar,
        fg_color="#269F73" if tipo == "Ingreso" else "#E75B63",
        hover_color="#21845F" if tipo == "Ingreso" else "#C94750",
        height=40,
        corner_radius=10
    ).pack(fill="x", padx=30, pady=(5, 8))

    ctk.CTkButton(
        dialogo,
        text="Cancelar",
        command=dialogo.destroy,
        fg_color="#DCE5F2",
        text_color="#243B64",
        hover_color="#C9D8EA",
        height=35,
        corner_radius=10
    ).pack(fill="x", padx=30)

    entrada_monto.focus()
