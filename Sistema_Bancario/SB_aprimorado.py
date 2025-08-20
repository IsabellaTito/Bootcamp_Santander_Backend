import textwrap

def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar contas
    [nu]\tNovo Usuário
    [sa]\tSair
    =>   """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /): #chamadas por posição
    if valor > 0:
        saldo+=valor
        extrato+= f"Depósito: \tR$ {valor:.2f}\n"
        print("\n ||||| Depósito realizado com sucesso! |||||")
    else:
        print("\n ### Operação falhou! O valor informado é inválido. ###")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques): #O caractere faz com que os argumentos sejam nomeados
    if (valor > saldo):
        print("\n### Operação falhou! Você não tem saldo suficiente. ###")
    
    elif (valor > limite):
        print("\n### Operação falhou! O valor do saque excede o limite. ###")
    
    elif (numero_saques>=limite_saques):
        print("\n### Operação falhou! Número máximo de saques excedido. ###")
    
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques+=1
        print("\n ||||| Saque realizado com sucesso! |||||")
    
    else:
        print("\n### Operação falhou! O valor informado é inválido. ###")
    
    return saldo, extrato

def exibir_extrato(saldo,/,*,extrato): #saldo é posicional e o argumento extrato é nomeado
    print("\n ================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR${saldo:.2f}")
    print("\n =========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario:
        print("\n### Já existe usuário com esse CPF! ###")
        return

    nome = input("Informe o nome completo: ")
    data_nasc = input("Informe a data de nascimento (dd-mm-aaaa): ")
    end = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome":nome, "data_nascimento":data_nasc, "cpf":cpf, "endereco": end})

    print("\n ||||| Usuário criado com sucesso! |||||")

def filtrar_usuario(cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"]==cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, num_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n ||||| Conta criada com sucesso! |||||")
        return {"agencia":agencia, "num_conta": num_conta, "usuario":usuario}
    
    print("\n #### Usuario não encontrado, fluxo de criação de conta encerrado! ####")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta["agencia"]}
            C/C:\t\t{conta["num_conta"]}
            Titular:\t{conta["usuario"]["nome"]}
        """

        print("="*100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo = saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
        
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "nu":
            criar_usuario(usuarios)
        
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao == "lc":
            listar_contas(contas)
        
        elif opcao == "sa":
            break
        
        else:
            print("Operação inválida, por favor seleciona novamente a operação desejada.")

if __name__ == "__main__":
    main()