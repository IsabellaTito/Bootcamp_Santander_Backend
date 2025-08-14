menu = '''
    [0] Déposito
    [1] Saque
    [2] Extrato
    [3] Sair
'''

saldo = 0
limite = 500
extrato = []
n_saques = 0
LIMITE_SAQUES = 3

while(True):
    escolha = int(input(menu))

    if escolha == 0:
        dep = float(input("Quanto deseja depositar? "))
        if(not dep<=0):
            saldo+=dep
            extrato.append(f"Depósito: R${dep:.2f}")
            print("Depósito realizado com sucesso!\nDeseja executar mais alguma ação?")   
        else:
            print("Valor para depósito inválido!\nDeseja executar mais alguma ação?")
            
    elif escolha == 1:
        if(n_saques<LIMITE_SAQUES):
            saque = float(input("Informe o valor para saque: "))
            if(saque > limite):
                print("Valor para saque maior do que o permitido!\nTente novamente.")                
            elif((saldo-saque)<0):
                print("Saldo Insuficiente!\n Deseja executar mais alguma ação?")    
            else:
                saldo-=saque
                extrato.append(f"Saque: R${saldo:.2f}")
                n_saques+=1
                print("Saque realizado com sucesso!\nDeseja executar mais alguma ação?")        
        else:
            print("Limite diário de saques excedido!\nDeseja executar mais alguma ação?")

    elif escolha == 2:
        if(not extrato):
            print("Não foram realizadas movimentações.\nDeseja executar mais alguma ação?")    
        else:
            for i in extrato:
                print(i)
            print(f"Saldo: R${saldo:.2f}")
            print("Deseja executar mais alguma ação?")
                    
    else:
        print("Encerrando atividade...")
        break




