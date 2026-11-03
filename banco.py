class Conta:
    def __init__(self, titular, numero_conta, saldo=0.0):
        self.titular = titular
        self.numero_conta = numero_conta
        self.saldo = saldo
        self.saldo_guardado = 0.0
        self.historico = []

    def mostrar(self):
        print("\n--- Dados da Conta ---")
        print(f"Titular: {self.titular}")
        print(f"Número da Conta: {self.numero_conta}")
        print(f"Saldo Disponível: R$ {self.saldo:.2f}")
        print(f"Saldo Guardado: R$ {self.saldo_guardado:.2f}")
        print("-" * 50)

    def depositar(self, valor):
        if valor <= 0:
            return False, "O valor deve ser maior que zero."

        saldo_anterior = self.saldo
        self.saldo += valor

        self.historico.append(
            f"Depósito de R$ {valor:.2f}"
        )

        print(f"\nDepósito de R$ {valor:.2f} realizado!")
        print(f"Saldo anterior: R$ {saldo_anterior:.2f}")
        print(f"Valor depositado: R$ {valor:.2f}")
        print(f"Novo saldo: R$ {self.saldo:.2f}")

        return True, f"Depósito de R$ {valor:.2f} realizado!"

    def sacar(self, valor):
        if valor <= 0:
            return False, "O valor deve ser maior que zero."

        if valor > self.saldo:
            return False, "Saldo insuficiente."

        saldo_anterior = self.saldo
        self.saldo -= valor

        self.historico.append(
            f"Saque de R$ {valor:.2f}"
        )

        print(f"\nSaque de R$ {valor:.2f} realizado!")
        print(f"Saldo anterior: R$ {saldo_anterior:.2f}")
        print(f"Valor sacado: R$ {valor:.2f}")
        print(f"Saldo restante: R$ {self.saldo:.2f}")

        return True, f"Saque de R$ {valor:.2f} realizado!"

    def guardar_dinheiro(self, valor):
        if valor <= 0:
            return False, "O valor deve ser maior que zero."

        if valor > self.saldo:
            return False, "Saldo insuficiente."

        saldo_anterior = self.saldo

        self.saldo -= valor
        self.saldo_guardado += valor

        self.historico.append(
            f"Guardou R$ {valor:.2f}"
        )

        print(f"\nR$ {valor:.2f} guardados!")
        print(f"Saldo anterior: R$ {saldo_anterior:.2f}")
        print(f"Valor guardado: R$ {valor:.2f}")
        print(f"Saldo disponível: R$ {self.saldo:.2f}")
        print(f"Total guardado: R$ {self.saldo_guardado:.2f}")

        return True, f"R$ {valor:.2f} guardados!"

    def resgatar_dinheiro(self, valor):
        if valor <= 0:
            return False, "O valor deve ser maior que zero."

        if valor > self.saldo_guardado:
            return False, "Saldo guardado insuficiente."

        saldo_guardado_anterior = self.saldo_guardado

        self.saldo_guardado -= valor
        self.saldo += valor

        self.historico.append(
            f"Resgatou R$ {valor:.2f}"
        )

        print(f"\nR$ {valor:.2f} resgatados!")
        print(
            f"Valor guardado anteriormente: "
            f"R$ {saldo_guardado_anterior:.2f}"
        )
        print(f"Valor resgatado: R$ {valor:.2f}")
        print(
            f"Saldo guardado restante: "
            f"R$ {self.saldo_guardado:.2f}"
        )
        print(f"Saldo disponível: R$ {self.saldo:.2f}")

        return True, f"R$ {valor:.2f} resgatados!"