import os

# Algoritmo "CorpBank"

saldo: float = 500
saqueDia: float = 0
tentativasSenhas: int = 0

deposito: float = 0.0
saque: float = 0.0
operacao: int = 0
continuar: str = ""
transferir: float = 0.0
codigoDeTransferencia: str = ""
senha: str = ""
senhaParaLer: str = ""

senha = input("Defina a sua senha: ")
print("Senha definida!")
print()

print("                                                      ")
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
operacao = int(input("  > Opcao (1-5): "))

while True:
    if operacao == 1:
        print(f"Saldo atual: R$ {saldo:.2f}")

    elif operacao == 2:
        deposito = float(input("Quanto deseja depositar? R$ "))
        if deposito <= 0:
            print("Valor invalido! O valor tem que ser maior que zero.")
        else:
            senhaParaLer = input("Digite a sua senha: ")
            while senhaParaLer != senha:
                print("Senha errada!")
                senhaParaLer = input("Tente novamente: ")
            saldo = saldo + deposito
            print(f"Deposito realizado! Saldo atual: R$ {saldo:.2f}")

    elif operacao == 3:
        saque = float(input("Quanto deseja sacar? R$ "))
        if saque <= 0:
            print("Valor invalido! O valor tem que ser maior que zero.")
        else:
            if saqueDia >= 5000 or saque > 5000:
                print("Falha ao realizar o saque.")
                print("Limite de saque diário atingido! R$ 5000.00")
            else:
                senhaParaLer = input("Digite a sua senha: ")
                while senhaParaLer != senha:
                    print("Senha errada!")
                    senhaParaLer = input("Tente novamente: ")
                if saque > saldo:
                    print("Saldo insuficiente!")
                    print(f"Saldo atual: R$ {saldo:.2f}")
                else:
                    saldo = saldo - saque
                    saqueDia = saqueDia + saque
                    print("Saque realizado com sucesso!")
                    print(f"Saldo atual: R$ {saldo:.2f}")

    elif operacao == 4:
        transferir = float(input("Quanto deseja transferir? R$ "))
        if transferir <= 0:
            print("Valor invalido! Digite um valor maior que zero.")
        else:
            codigoDeTransferencia = input("Escreva o numero da conta: ")
            senhaParaLer = input("Digite a sua senha: ")
            while senhaParaLer != senha:
                print("Senha errada!")
                senhaParaLer = input("Tente novamente: ")
            if saqueDia >= 5000 or transferir > 5000:
                print("Você não pode transferir este valor! o limite de saque é de R$ 5000.00")
            else:
                if transferir > saldo:
                    print("Saldo insuficiente!")
                    print(f"Saldo atual: R$ {saldo:.2f}")
                else:
                    saldo = saldo - transferir
                    print(f"Transferência realizada com sucesso para a conta {codigoDeTransferencia}!")
                    print(f"Saldo atual: R$ {saldo:.2f}")
                    saqueDia = saqueDia + transferir

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
            operacao = int(input("  > Opcao (1-5): "))
        else:
            print("Saindo do sistema...")
            operacao = 5

    if operacao == 5:
        break