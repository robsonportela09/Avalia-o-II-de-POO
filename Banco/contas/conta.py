from operacoes.historico import Historico


class Conta: #Info da conta
    def __init__(self, numero, cliente):
        self.__numero = numero
        self.__cliente = cliente
        self.__saldo = 0.0
        self._historico = Historico()

    def get_numero(self):
        return self.__numero

    def get_cliente(self):
        return self.__cliente

    def get_saldo(self):
        return self.__saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            self._historico.adicionar(
                f"Depósito de R$ {valor:.2f}"
            )
            print("O seu depósito foi realizado com sucesso.")
        else:
            print("Valor inválido.")

    def sacar(self, valor):
        pass

    def _retirar_saldo(self, valor):
        self.__saldo -= valor

    def mostrar_historico(self):
        self._historico.listar()