from contas.conta import Conta


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido.")

        elif valor > self.get_saldo():#comunica o saldo
            print("Saldo insuficiente.")

        else:
            self._retirar_saldo(valor)
            self._historico.adicionar(
                f"Saque Conta Poupança: R$ {valor:.2f}"
            )
            print("Saque realizado com sucesso.")