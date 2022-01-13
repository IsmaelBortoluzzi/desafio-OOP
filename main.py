from classes import *

banco = Banco({}, {})
contador = 1000


def validate(nome, num_conta):

    e_cliente = None
    conta_existe = None
    e_dono = None
    try:
        e_cliente = banco.clientes[nome]
        conta_existe = banco.contas[num_conta]
        e_dono = banco.clientes[nome].conta[num_conta]
        return True
    except:
        if not e_cliente:
            print("Você não é cliente do banco")
        elif not conta_existe:
            print("A conta não existe")
        elif not e_dono:
            print("Você não é o titular desta conta")
        return False


while True:
    print("O que deseja fazer?")
    print("1. Me Cadastrar")
    print("2. Cria Conta")
    print("3. Sacar")
    print("4. Depositar")
    print("0. Sair")
    opcao = input("Sua opcao? (1 2 3 4 ou 0) ")

    if opcao == "1":
        nome = input("Qual seu nome?")
        idade = int(input("Qual sua idade?"))
        banco.add_cliente(Cliente(nome, idade, {}))

    elif opcao == "2":
        nome = input("Criar a conta no nome de quem? ")

        for k, v in banco.clientes.items():
            if v.nome == nome:
                break
        else:
            print("Você não possui cadastro no Banco!")
            continue

        tipo = input("Digite 1 para conta corrente, 2 para poupança: ")

        conta = None
        if tipo == "1":
            conta = ContaPoupanca(str(contador), 0.0)
        elif tipo == "2":
            conta = ContaCorrente(str(contador), 0.0)

        banco.contas[str(contador)] = conta
        print(f"sua conta é {contador}")
        banco.clientes[nome].add_conta(conta)
        contador += 1

    elif opcao == "3":
        nome = input("conta está nome de quem? ")
        num_conta = input("Qual o numero da conta")

        if not validate(nome, num_conta):
            continue

        quantia = float(input("Qual a quantia"))
        banco.contas[num_conta].sacar(quantia)

    elif opcao == "4":
        nome = input("conta está nome de quem? ")
        num_conta = input("Qual o numero da conta")

        if not validate(nome, num_conta):
            continue

        quantia = float(input("Qual a quantia"))
        banco.contas[num_conta].depositar(quantia)

    else:
        break


for k, v in banco.clientes.items():
    print(k, v)
print("\n")

for k, v in banco.contas.items():
    print(k, v)
print("\n")

for k, v in banco.clientes.items():
    print(k, v.conta)
print("\n")
