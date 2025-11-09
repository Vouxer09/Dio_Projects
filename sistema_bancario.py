def main():
    LIMITE_SAQUE = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    opcoes = {
        "1": "Depositar",
        "2": "Sacar",
        "3": "Extrato",
        "4": "Novo usuário",
        "5": "Nova conta",
        "6": "Exibir usuários",
        "7": "Sair"
    }
    while True:
        print("\n========= MENU =========")
        for chave, valor in opcoes.items():
            print(f"{chave} - {valor}")

        opcao = input("Selecione uma das opções acima: \n")
        if opcao == "1":
            depositar(saldo, 0, extrato)
        
        elif opcao == "2":
            sacar(saldo = saldo, valor = 0, extrato = extrato, limite = limite, numero_saques = numero_saques, limite_saques = LIMITE_SAQUE)
        
        elif opcao == "3":
            exibir_extrato(saldo, extrato)
        
        elif opcao == "4":
            criar_usuario(usuarios)
        
        elif opcao == "5":
            criar_conta(AGENCIA, contas, usuarios)
        
        elif opcao == "6":
            
            if not usuarios:
                print("Nenhum usuário cadastrado.")
            else:
                for usuario in usuarios:
                    print(usuario)
        
        elif opcao == "7":
            print("Encerrando o sistema. Obrigado por usar nosso banco!")
            break
        
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

def depositar(saldo, valor, extrato):
    try:
        valor = float(input("Informe o valor do depósito: "))
    except ValueError:
        print("Operação falhou! O valor informado é inválido.")
        return saldo, extrato
    
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso.")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
    try:
        valor = float(input("Informe o valor do saque: "))
    except ValueError:
        print("Operação falhou! O valor informado é inválido.")
        return saldo, extrato, numero_saques
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques diários excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso.")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):

    print("\n================ EXTRATO ================")
    if extrato == "":
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=========================================")

def criar_usuario(usuarios):
    try:
        cpf = int(input("Informe o CPF (somente números(sem . nem / )): "))
    except ValueError:
        print("CPF inválido. Operação cancelada.")
        return 
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(AGENCIA, contas, usuarios):
    cpf = int(input("Informe o CPF do usuário: "))
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        numero_conta = len(contas) + 1
        conta = {"agencia": AGENCIA, "numero_conta": numero_conta, "usuario": usuario}
        contas.append(conta)
        print("Conta criada com sucesso!")
    else:
        print("Usuário não encontrado. Processo de criação de conta encerrado.")
        return

main()

