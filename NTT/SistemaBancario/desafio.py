from datetime import date

menu = """

Selecione a opção desejada:
[D] Depositar
[S] Sacar
[E] Extrato
[Q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
num_saques = 0
LIMITE_SAQUES = 3
data = (date.today()).strftime('%d/%m/%Y')

while True:

    opcao = input(menu)

    if opcao == "D":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo   += valor
            extrato += f"{data} - Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!\n")
        
        else:
            print("Operação não realizada. Informe um valor maior que zero\n")

    elif opcao == "S":
        valor = float(input("Informe o valor do saque: "))

        saldo_insuficiente  = valor > saldo
        limite_excedido     = valor > limite
        qtd_saques_excedido = num_saques >= LIMITE_SAQUES

        if saldo_insuficiente:
            print("Operção não realizada! Saldo Insuficiente.\n")
        
        elif limite_excedido:
            print("Operação não realizada!. Valor do saque maior do que o limite permitido.\n")

        elif qtd_saques_excedido:
            print("Operação não realizada! Quantidade máxima de saques excedido.\n")

        elif valor > 0:
            saldo -= valor
            extrato += f"{data} - Saque: R$ {valor:.2f}\n"
            num_saques += 1
            print("Saque realizado com sucesso!\n")

        else:
            print("Operação solicitada não encontrada. Informe um valor maior que zero.\n")

    elif opcao == "E":
        print("EXTRATO".center(37,"#"))
        print(extrato)
        print(f"{data} - Saldo: R$ {saldo:.2f}")
        print("".center(37,"#"))

    elif opcao == "Q":
        break

    else:
        print("Operação não realizada! Informe uma opção válida")
