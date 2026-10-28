from tarea.cuentabancaria import CuentaBancaria


class CuentaCheque(CuentaBancaria):
    """Cuenta que cobra un costo fijo por cada extracción exitosa."""

    def __init__(self, titular, cbu, saldo_inicial=0, costo_emision=50):
        super().__init__(titular, cbu, saldo_inicial)

        if costo_emision < 0:
            raise ValueError("El costo de emisión no puede ser negativo.")
        self.costo_emision = costo_emision

    def extraer(self, monto):
        if monto <= 0:
            raise ValueError("El monto a extraer debe ser mayor a cero.")

        total = monto + self.costo_emision
        if total <= self.saldo:
            self.saldo = self.saldo - total
            print(
                f"Extracción exitosa: ${monto:.2f} "
                f"(costo de emisión: ${self.costo_emision:.2f})"
            )
        else:
            print(
                "Extracción rechazada: saldo insuficiente para cubrir "
                "el monto y la comisión."
            )
