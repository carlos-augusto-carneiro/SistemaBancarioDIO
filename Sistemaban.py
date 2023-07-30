dic = {}

cliente = []
contas = []


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
    
def criarCliente():
    print('Digite seu nome:')
    nome = str(input())
    print('Digite sua data de nascimento:')
    nascimento = str(input())
    print('Digite seu CPF:')
    cpf = str(input())
    print('Digite o logradouro:')
    logradouro = str(input())
    print('Digite seu bairro:')
    bairro = str(input)
    print('Digite sua cidade/estado:')
    cidade = str(input())
    print('Digite sua senha:')
    senha = str(input())

    cliente.append(nome)
    cliente.append(nascimento)
    cliente.append(cpf)
    cliente.append(logradouro)
    cliente.append(bairro)
    cliente.append(cidade)
    cliente.append(senha)

def criarConta():
    print('Digite seu cpf:')
    cpf = str(input())

    if cpf in cliente:
        print('Digite sua agencia:')
        agencia = str(input())
        print('Digite sua numero da conta:')
        numero = str(input())
        print('Digite seu usuario:')
        usuario = str(input())

        contas.append(agencia)
        contas.append(numero)
        contas.append(usuario)
        contas.append(cpf)

    else:
        print('Voce nao está ainda cadastrado como cliente')

saldo = 0
limite = 500
numero_saques = 0 
liite_saques = 3


while True:

    print('Selecione a opção:')
    print('[1]-login\n[2]-Criar cliente\n[3]-Criar conta\n[4]-Sair')
    op = int(input())

    if op == 1:
        print('Seu cpf:')
        cpf = str(input())
        print('Sua senha:')
        senha = str(input())

        if (cpf in cliente) and (senha in cliente):
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

'''    elif op == 2:
        print('Seu cpf:')
        cpf = str(input())
        print('Sua senha:')
        senha = str(input())

        if (cpf in cliente) and (senha in cliente):

'''