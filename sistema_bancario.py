import random
import time
saldo = 1000.00

# inicializa extrato e usuário
extrato = "Extrato:"
usuario = {'nome': '', 'idade': '' , 'email': '', 'cpf': ''}

opcoes = {
    '1': 'Saque',
    '2': 'Depósito',
    '3': 'Extrato',
    '4': 'Cadastrar Usuário',
    '5': 'Cadastrar Conta Bancaria',
    '6': 'Sair'
}

opcoes_conta_bancaria = {
    '1': 'Conta Corrente',
    '2': 'Conta Poupança',
    '3': 'Conta Salário'
}

numero_conta = "0001" + str(random.randint(10000, 99999))

def exibir_menu():
    print("Menu:")
    for chave, valor in opcoes.items():
        print(f"{chave} - {valor}")
    escolha = input("Selecione uma opção: ")
    if escolha == '1':
        sacar()
    elif escolha == '2':
        depositar()
    elif escolha == '3':
        exibir_extrato()
    elif escolha == '4':
        cadastrar_usuario()
    elif escolha == '5':
        cadastrar_conta_bancaria()
    elif escolha == '6':
        print("Saindo do sistema. Obrigado por usar nosso serviço!")
        exit()

def sacar():
    global saldo, extrato
    try:
        valor = float(input("Digite o valor do saque: R$ "))
    except ValueError:
        print("Erro: O valor do saque deve ser um número válido.")
        return
    if valor > saldo:
        print(f"Saldo insuficiente para saque. O saldo atual é R$ {saldo:.2f}")
        return
    saldo -= valor
    extrato += f"\nSaque: R$ {valor:.2f}"
    print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
    print(f"Saldo atual: R$ {saldo:.2f}")

def depositar():
    global saldo, extrato
    try:
        valor = float(input("Digite o valor do depósito: R$ "))
    except ValueError:
        print("Erro: O valor do depósito deve ser um número válido.")
        return
    saldo += valor
    extrato += f"\nDepósito: R$ {valor:.2f}"
    print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    print(f"Saldo atual: R$ {saldo:.2f}")
    
def cadastrar_usuario():
    global usuario
    nome = input("Digite seu nome: ")
    try:
        idade = int(input("Digite sua idade: "))
    except ValueError:
        print("Erro: A idade deve ser um número inteiro.")
        return
    email = input("Digite seu email: ")
    usuario['nome'] = nome
    usuario['idade'] = idade
    usuario['email'] = email
    try:
        usuario['cpf'] = int(input("Digite seu CPF (Apenas os numeros, sem ""."", e com exatos 11 dígitos): "))
        if usuario['cpf'] == ['cpf']:
            print("Erro: O CPF já está cadastrado no sistema.")
            return
    except ValueError:
        print("Erro: O CPF deve conter apenas números.")
        return
    
    
    else:
        print("Usuário cadastrado com sucesso.")

def exibir_extrato():
    print("\n" + extrato)
    print(f"\nSaldo atual: R$ {saldo:.2f}")

def cadastrar_conta_bancaria():
    global numero_conta
    
    print("Tipos de Conta Bancária:")
    for chave, valor in opcoes_conta_bancaria.items():
        print(f"{chave} - {valor}")
    tipo_conta = input("Selecione o tipo de conta bancária: ")
    if tipo_conta in opcoes_conta_bancaria:
        print(f"Conta {opcoes_conta_bancaria[tipo_conta]} cadastrada com sucesso.")
    else:
        print("Opção inválida para tipo de conta bancária.")
    print(f"Número da conta: {numero_conta}")

while True:
    exibir_menu()
