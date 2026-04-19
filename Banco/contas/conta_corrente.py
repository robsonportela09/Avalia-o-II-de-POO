from contas.conta import Conta


class ContaCorrente(Conta): 
    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido.")

        elif valor > self.get_saldo(): #comunica o saldo 
            print("Saldo insuficiente.")

        elif valor > 1000:
            print("Limite por saque de R$ 1000.00")

        else: #Saque
            self._retirar_saldo(valor)
            self._historico.adicionar(
                f"Saque Conta Corrente: R$ {valor:.2f}"
            )
            print("Saque realizado com sucesso.")