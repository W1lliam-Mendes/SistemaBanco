import os

# Algoritmo "CorpBank"

saldo: float = 500
saqueDia: float = 0
tentativasSenhas: int = 0
LIMITE_TENTATIVAS: int = 3

deposito: float = 0.0
saque: float = 0.0
operacao: int = 0
continuar: str = ""
transferir: float = 0.0
codigoDeTransferencia: str = ""
senha: str = ""
senhaParaLer: str = ""


def exibirMenu():
    print("+====================================================+")
    print("+----------------------------------------------------+")
    print("|   ____ ___  ____  ____   ____    _    _   _ _  __  |")
    print("|  / ___/ _ \\|  _ \\|  _ \\ | __ )  / \\  | \\ | | |/ /  |")
    print("| | |  | | | | |_) | |_) ||  _ \\ / _ \\ |  \\| | ' /   |")
    print("| | |__| |_| |  _ <|  __/ | |_) / ___ \\| |\\  | . \\   |")
    print("|  \\____\\___/|_| \\_\\_|    |____/_/   \\_\\_| \\_|_|\\_\\  |")
    print("|                                                    |")
    print("|          >> Menos burocracia, mais lucro <<        |")
    print("+----------------------------------------------------+")
    print("|  [1]  Verificar Saldo                              |")
    print("|  [2]  Realizar Deposito                            |")
    print("|  [3]  Sacar Dinheiro                               |")
    print("|  [4]  Transferir                                   |")
    print("|  [5]  Sair do Sistema                              |")
    print("+====================================================+")


def lerOperacao() -> int:
    while True:
        try:
            return int(input("  > Opcao (1-5): "))
        except ValueError:
            print("Entrada invalida! Digite um numero entre 1 e 5.")


def lerValor(mensagem: str) -> float:
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Entrada invalida! Digite um valor numerico.")


def verificarSenha() -> bool:
    global tentativasSenhas
    tentativasSenhas = 0
    while tentativasSenhas < LIMITE_TENTATIVAS:
        senhaParaLer = input("Digite a sua senha: ")
        if senhaParaLer == senha:
            tentativasSenhas = 0
            return True
        tentativasSenhas += 1
        restantes = LIMITE_TENTATIVAS - tentativasSenhas
        if restantes > 0:
            print(f"Senha errada! Tentativas restantes: {restantes}")
        else:
            print("Numero de tentativas excedido! Operacao cancelada.")
    return False


# -- Início --

senha = input("Defina a sua senha: ")
print("Senha definida!")
print()

exibirMenu()
operacao = lerOperacao()

while True:
    if operacao == 1:
        print(f"Saldo atual: R$ {saldo:.2f}")

    elif operacao == 2:
        deposito = lerValor("Quanto deseja depositar? R$ ")
        if deposito <= 0:
            print("Valor invalido! O valor tem que ser maior que zero.")
        else:
            if verificarSenha():
                saldo = saldo + deposito
                print(f"Deposito realizado! Saldo atual: R$ {saldo:.2f}")

    elif operacao == 3:
        saque = lerValor("Quanto deseja sacar? R$ ")
        if saque <= 0:
            print("Valor invalido! O valor tem que ser maior que zero.")
        else:
            if saqueDia >= 5000 or saque > 5000:
                print("Falha ao realizar o saque.")
                print("Limite de saque diario atingido! R$ 5000.00")
            else:
                if verificarSenha():
                    if saque > saldo:
                        print("Saldo insuficiente!")
                        print(f"Saldo atual: R$ {saldo:.2f}")
                    else:
                        saldo = saldo - saque
                        saqueDia = saqueDia + saque
                        print("Saque realizado com sucesso!")
                        print(f"Saldo atual: R$ {saldo:.2f}")

    elif operacao == 4:
        transferir = lerValor("Quanto deseja transferir? R$ ")
        if transferir <= 0:
            print("Valor invalido! Digite um valor maior que zero.")
        else:
            codigoDeTransferencia = input("Escreva o numero da conta: ")
            if saqueDia >= 5000 or transferir > 5000:
                print("Voce nao pode transferir este valor! O limite diario e de R$ 5000.00")
            else:
                if verificarSenha():
                    if transferir > saldo:
                        print("Saldo insuficiente!")
                        print(f"Saldo atual: R$ {saldo:.2f}")
                    else:
                        saldo = saldo - transferir
                        saqueDia = saqueDia + transferir
                        print(f"Transferencia realizada com sucesso para a conta {codigoDeTransferencia}!")
                        print(f"Saldo atual: R$ {saldo:.2f}")

    elif operacao == 5:
        print("Saindo do sistema...")

    else:
        print("Opcao invalida! Tente novamente.")

    if operacao != 5:
        print()
        continuar = input("Deseja continuar? (S/N): ")
        if continuar in ("S", "s", "Sim", "sim"):
            os.system("cls" if os.name == "nt" else "clear")
            print()
            print()
            print()
            exibirMenu()
            operacao = lerOperacao()
        else:
            print("Saindo do sistema...")
            operacao = 5

    if operacao == 5:
        break