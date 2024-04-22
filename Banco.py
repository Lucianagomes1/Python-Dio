menu = """
[d] Deposito
[s] Saque
[e] Extrato
[q] Sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Deposito")
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        print("Saque")
        valor = float(input("Informe o valor do saque: "))
        if valor <= saldo and valor <= 500 and numero_saques < LIMITE_SAQUES:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            print(f"Operação realizado: R$ {valor:.2f}")
            numero_saques += 1
            if numero_saques >= LIMITE_SAQUES:
                print("Número máximo de saques diários atingido.")
        else:
            print("""
                  Operação falhou! 
                  Valor maior do que o permitido ou 
                  saldo insuficiente ou 
                  limite de saques diários atingido.
                  """)

    elif opcao == "e":
        print("Extrato")
        print(extrato)

    elif opcao == "q":
        print("Saindo...")
        break

    else:
        print("Opção inválida.")
