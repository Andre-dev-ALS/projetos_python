import menu


def subtrair():
    print("a operação matemática escolhida foi a subtração")
    print("pressione 0 para saber o resultado")
    valor1 = float(input("digite o primeiro valor"))
    resultado = valor1

    while valor1 < 0:
        valor1 = float("Valor inválido \n digite um valor positivo")
    contador = 0
    while valor1 != 0:
        contador = contador + 1
        valor1 = float(input("digite um valor para subtrair"))
        while valor1 < 0:
            valor1 = float(input("valorinválido \n digite um valor positivo"))
        resultado = resultado - valor1
    print(f"A quantidade de valores digitados foi de {contador}")
    if valor1 == 0:
        print(
            f"o resultado da subtração  de todos os valores digitados é de {resultado:.2f}"
        )

    print("escolha uma das opções :  ")
    print(
        "pressione 1 para fazer outra conta com essa mesma opção de operação matemática "
    )
    print("pressione 2 para voltar ao menu principal")
    print("pressione 3 para finalizar o programa")
    opção = int(input("digite  aqui uma das opções"))

    while opção < 1 or opção > 3:
        opção = int(input("digite uma opção existente"))

    if opção == 1:
        subtrair()
    elif opção == 2:
        menu.menu()
    else:
        print("programa finalizado com sucesso")
