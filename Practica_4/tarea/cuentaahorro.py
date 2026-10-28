from tarea.cuentabancaria import CuentaBancaria


class CuentaAhorro(CuentaBancaria):
    """Cuenta que solo permite extraer si tiene saldo suficiente."""

    TASA_INTERES = 0.001  # 0,1 %

    def extraer(self, monto):
        if monto <= 0:
            raise ValueError("El monto a extraer debe ser mayor a cero.")

        if monto <= self.saldo:
            self.saldo = self.saldo - monto
            print(f"Extracción exitosa: ${monto:.2f}")
        else:
            print("Extracción rechazada: saldo insuficiente.")

    def aplicar_interes(self):
        """Suma al saldo el interés del 0,1 %."""
        interes = self.saldo * self.TASA_INTERES
        self.saldo = self.saldo + interes
        print(f"Interés aplicado: ${interes:.2f}")
