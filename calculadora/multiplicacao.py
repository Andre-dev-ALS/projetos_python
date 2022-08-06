
import menu


def multiplica():
    print("a operação matemática escolhida foi a multiplicação")
    print("pressione 0 para saber o resultado")
    valor1 = float(input("digite o primeiro valor"))
    resposta = 1
    total = float

    while valor1 < 0:
        valor1 = float(input("Valor inválido \n digite um número positivo"))

    if valor1 == 0:
        resposta = valor1
    else:
        total = valor1
    contador = 0
    while valor1 != 0:
        valor1 = int(input("digite outro valor para multiplicar"))
        contador = contador + 1

        while valor1 < 0:
            valor1 = float(input("Valor inválido \n digite um valor positivo"))
        if valor1 == 0:
            resposta = valor1
        else:
            total = total * valor1

    if resposta == 0:
        print(f"A quantidade de valores digitados foi de {contador}")
        print(f"O resultado da multiplicação de todos os valores é de {total:.2f}")

    print("escolha uma das opções:")

    print("pressione 1 para fazer outra conta com essa mesma opção de operação matemática ")
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
