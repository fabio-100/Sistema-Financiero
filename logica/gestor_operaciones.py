
from datetime import datetime


# Administra los datos y las operaciones financieras
class GestorOperaciones:

    def __init__(self):
        self.saldo_actual = 0.0
        self.operaciones_registradas = []
        self.gastos_categoria = {}

    # Registra un ingreso
    def ingresar(self, monto):
        if monto <= 0:
            return False, "El importe debe ser mayor que cero."

        self.saldo_actual += monto
        self.registrar_operacion("Ingreso", "Ingreso", monto)

        return True, ""

    # Registra un retiro
    def retirar(self, monto, categoria):
        if monto <= 0:
            return False, "El importe debe ser mayor que cero."

        if not categoria:
            return False, "Tenés que seleccionar una categoría."

        if monto > self.saldo_actual:
            return False, "No tenés saldo suficiente para realizar este retiro."

        self.saldo_actual -= monto

        self.gastos_categoria[categoria] = (
            self.gastos_categoria.get(categoria, 0) + monto
        )

        self.registrar_operacion("Retiro", categoria, monto)

        return True, ""

    # Guarda los datos de cada operación
    def registrar_operacion(self, tipo, categoria, monto):
        self.operaciones_registradas.append({
            "fecha": datetime.now().strftime("%d/%m/%Y %H:%M"),
            "tipo": tipo,
            "categoria": categoria,
            "monto": monto
        })
