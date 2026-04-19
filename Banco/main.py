from clientes.cliente import Cliente
from contas.conta_corrente import ContaCorrente
from contas.conta_poupanca import ContaPoupanca

contas = [] #Lista que armazena as contas
numero_conta = 1 #Numeração da conta


def buscar_conta(numero): #Função que busca a conta a partir do número
    for conta in contas:
        if conta.get_numero() == numero:
            return conta
    return None


while True:
    # MENU 
    print("\n==== CAIXA ELETRÔNICO - Banco Master ======\n")
    print("1 - Criar Conta")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Consultar Saldo")
    print("5 - Histórico")
    print("0 - Sair")
    print("\nDúvidas? SAC: 88 4002-8922")

    opcao = input("\nEscolha: ") #Escolha do usuário

    if opcao == "1": 
        nome = input("Digite o seu nome: ")
        cpf = input("Digite o seu CPF: ")
        
        print("\nInforme o tipo de conta desejado:")
        print("1 - Conta Corrente")
        print("2 - Conta Poupança")
        tipo = input("\nTipo: ")

        cliente = Cliente(nome, cpf)
        # ESTRUTURA CONDICIONAL VALIDANDO OS FATOS
        if tipo == "1":
            conta = ContaCorrente(numero_conta, cliente)

        elif tipo == "2":
            conta = ContaPoupanca(numero_conta, cliente)

        else:
            print("Tipo inválido.")
            continue

        contas.append(conta)
        print(f"Conta criada com número {numero_conta}")
        numero_conta += 1 #automatiza o número da conta

    elif opcao == "2": 
        numero = int(input("Número da conta: "))
        conta = buscar_conta(numero) #Função que busca a conta 

        if conta: #Depósito
            valor = float(input("Insira o valor para depósito: "))
            conta.depositar(valor)
        else:
            print("Conta não encontrada.")

    elif opcao == "3": #Busca a conta
        numero = int(input("Informe o número da conta: "))
        conta = buscar_conta(numero)

        if conta:
            valor = float(input("Informe o valor do saque: "))
            conta.sacar(valor)
        else:
            print("Conta não encontrada.")

    elif opcao == "4":
        numero = int(input("Número da conta: "))
        conta = buscar_conta(numero)

        if conta:
            print(f"Seu saldo é: R$ {conta.get_saldo():.2f}")
        else:
            print("Conta não encontrada.")

    elif opcao == "5":
        numero = int(input("Número da conta: "))
        conta = buscar_conta(numero)

        if conta: #histórico conta
            conta.mostrar_historico()
        else:
            print("Conta não encontrada.")

    elif opcao == "0":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida.")
