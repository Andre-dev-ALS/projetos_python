from tkinter import W


def dividir():
    print("a operação matemática escolhida foi a divisão")
    valor1 = float(input("digite o valor do dividendo"))
    while valor1 < 0:
        valor1 = float(input("Valor inválido \n digite um valor positivo"))
    valor2 = float(input("digite o valor do divisor"))
    while valor2 < 0:
        valor2 = float(input("Valor inválido \n digite um valor positivo"))

    resultado = valor1 / valor2
    resto = valor1 % valor2
    print(f"O resultado da divisão é de {resultado:.2f}")
    print("o resto da divisão é", +resto)

    print("escolha uma das opções:")

    print("digite 1 para permanecer nessa mesma opção ")
    print("pressione 2 para voltar ao menu principal")
    print("pressione 3 para finalizar o programa")
    opção = int(input("digite  aqui uma das opções"))

    while opção < 1 or opção > 3:
        opção = int(input("digite uma opção existente"))

    if opção == 1:
        multiplica()
    elif opção == 2:
        menu.menu()
    else:
        print("programa finalizado com sucesso")

    return

    return
