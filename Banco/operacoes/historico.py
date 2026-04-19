class Historico:
    def __init__(self):
        self.__operacoes = []

    def adicionar(self, texto):
        self.__operacoes.append(texto)

    def listar(self):
        if len(self.__operacoes) == 0:
            print("Nenhuma operação realizada.")
        else:
            for item in self.__operacoes:
                print(item)