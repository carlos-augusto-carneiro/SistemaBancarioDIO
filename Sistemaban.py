def depositar():
    global saldo
    print('Quanto deseja depositar?')
    valor = float(input())
    saldo = saldo+valor

def sacar():
    global limite
    global numero_saques
    global liite_saques
    global saldo

    print('Quanto deseja sacar?')
    saque = float(input())
    numero_saques =+ 1

    if numero_saques == liite_saques:
        print('Seu limite de saque foi excedido')
    elif (saldo - saque) <= -1:
        print('Voce não pode sacar vai ficar nagativado')
    else:
        if saque == limite or saque >= limite:
            print('Voce nao pode sacar esse valor, tente um menor')
        else:
            saldo = saldo - saque
            print('Voce sacou da sua conta %s' %(saque))
    
def Extrato():
    print('Esse é o seu extrato')
    print('Seu saldo é de: %s'%(saldo))
    
saldo = 0
limite = 500
numero_saques = 0 
liite_saques = 3

while True:

    print('Selecione a opção:')
    print('[1]-Depositar\n[2]-Sacar\n[3]-Extrato\n[4]-Sair')
    opcao = int(input())

    if opcao == 1:
        print('<<<<<<<< Voce acessou a area de depostio >>>>>>>>')
        depositar()

    elif opcao == 2:
        print('<<<<<<<< Voce acessou a area de saque >>>>>>>>')
        sacar()

    elif opcao == 3:
        print('<<<<<<<< Voce acessou a area de extrato >>>>>>>>')
        Extrato()

    elif opcao  == 4:
        print('<<<<<<<< Até logo, volte sempre!! >>>>>>>>')
        break

    else:
        print('ERRO, digite novamente')

