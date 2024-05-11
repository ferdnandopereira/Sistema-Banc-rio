#-*- coding: utf-8 -*-
from menu import menu

saldo = 0.0
limite = 500
extrato = " "
numero_saques = 0
LIMITE_SAQUES = 3

def main():

    while True:
        menu()
        opcao = int(input("Selecione uma opção: "))

        if opcao == 1:
            valor = float(input("Informe o valor do depósito - R$: "))
            if valor > 0:
                saldo = saldo + valor
                extrato += print(f'Valor do Depósito - R$: {valor:.2f}')
                print(f'Valor do Depósito - R$: {valor:.2f}')
                print("\n")
            else:
                print("Valor informado é inválido.")
                print("Operação falhou !")
                print("\n")
        elif opcao == 2:
            valor = float(input("Informe o valor do Saque - R$: "))

            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = numero_saques >= LIMITE_SAQUES
            if excedeu_saldo:
                print("Você não têm saldo o suficiente.")
                print("Operação falhou !")
                print("\n")
            elif excedeu_limite:
                print("O valor do saque excede o limite.")
                print("Operação falhou !")
                print("\n")
            elif excedeu_saques:
                print("Número máximo de saques excedido")
                print("Operação falhou !")
                print("\n")
            elif valor > 0:
                saldo -= valor
                extrato = extrato + valor
                extrato += print(f'Saque - R$ {valor:.2f}')
                print(f'Valor do Saque - R$: {valor:.2f}')
                print("\n")
                numero_saques = numero_saques + 1
            else:
                print("O valor informado é inválido.")
                print("Operação falho !")
                print("\n")
        elif opcao == 3:
            print("==== EXTRATO ====")
            print("Não forma realizadas movimentaçãoes." if not extrato else extrato)
            print(f'Saldo - R$: {saldo:.2f}')
            print("==== FIM DO DEMOSTRATIVO DE EXTRATO ====")
        elif opcao == 4:
            print("Saindo do programa...")
            print("\n")
            print("Programa Finalizado.")
            break
        else:
            print("Entrada inválida. Por favor selecione outra opção.")


if __name__ == "__main__":
    main()
