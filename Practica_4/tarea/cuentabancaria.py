from abc import ABC, abstractmethod


class CuentaBancaria(ABC):
    """Clase base abstracta para las cuentas bancarias."""

    def __init__(self, titular, cbu, saldo_inicial=0):
        self.titular = titular
        self._cbu = cbu
        # Se utiliza el setter para validar también el saldo inicial.
        self.saldo = saldo_inicial

    @property
    def cbu(self):
        """Permite consultar el CBU, pero no modificarlo mediante la propiedad."""
        return self._cbu

    @property
    def saldo(self):
        """Devuelve el saldo actual."""
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        """Impide asignar un saldo negativo."""
        if valor < 0:
            raise ValueError("El saldo no puede ser negativo.")
        self._saldo = valor

    def depositar(self, monto):
        """Suma dinero a la cuenta, si el monto es mayor que cero."""
        if monto <= 0:
            raise ValueError("El monto a depositar debe ser mayor a cero.")

        self.saldo = self.saldo + monto
        print(f"Depósito exitoso: ${monto:.2f}")

    def __str__(self):
        return (
            f"[{self.__class__.__name__}] "
            f"TITULAR: {self.titular} | "
            f"CBU: {self.cbu} | "
            f"SALDO: ${self.saldo:.2f}"
        )

    @abstractmethod
    def extraer(self, monto):
        """Cada tipo de cuenta implementa su propia regla de extracción."""
        pass
