class Cliente: #Info cliente
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def get_nome(self):
        return self.__nome

    def get_cpf(self):
        return self.__cpf