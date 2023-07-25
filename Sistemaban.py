
def depositar():
    pass

def sacar():
    pass

def Extrato():
    pass




while True:

    print('Selecione a opção:')
    print('[1]-Depositar\n[2]-Sacar\n[3]-Extrato\n[4]-Sair')
    opcao = int(input())

    if opcao == 1:
        print('<<<<<<<< Voce acessou a area de depostio >>>>>>>>')
        depositar

    elif opcao == 2:
        print('<<<<<<<< Voce acessou a area de saque >>>>>>>>')
        sacar

    elif opcao == 3:
        print('<<<<<<<< Voce acessou a area de extrato >>>>>>>>')
        Extrato

    elif opcao  == 4:
        print('<<<<<<<< Até logo, volte sempre!! >>>>>>>>')
        break

