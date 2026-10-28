from tarea.cuentabancaria import CuentaBancaria


class CuentaCorriente(CuentaBancaria):
    """Cuenta que permite usar un descubierto hasta un límite establecido."""

    def __init__(self, titular, cbu, saldo_inicial=0, limite_descubierto=500):
        super().__init__(titular, cbu, saldo_inicial)

        if limite_descubierto < 0:
            raise ValueError("El límite de descubierto no puede ser negativo.")
        self.limite_descubierto = limite_descubierto

    def extraer(self, monto):
        if monto <= 0:
            raise ValueError("El monto a extraer debe ser mayor a cero.")

        disponible = self.saldo + self.limite_descubierto
        if monto <= disponible:
            # Puede quedar negativo dentro del descubierto autorizado.
            # No se usa el setter porque la clase base prohíbe saldos negativos.
            self._saldo = self.saldo - monto
            print(f"Extracción exitosa: ${monto:.2f}")
        else:
            print("Extracción rechazada: límite de descubierto excedido.")
