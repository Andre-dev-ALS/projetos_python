import menu


def soma():
    print("a operação matemática escolhida foi a adição")
    print("pressione 0 para saber o resultado")
    valor1 = float(input("digite o primeiro valor"))
    while valor1 < 0:
        valor1 = float(input("Valor inválido \n digite um valor positivo"))
    resultado = 0
    resultado = resultado + valor1
    contador = 0
    while valor1 != 0:
        contador = contador + 1
        valor1 = float(input("digite um valor para somar"))
        resultado = resultado + valor1
    print(f"A quantidade de valores digitados foi de {contador}")
    if valor1 == 0:
        print(f"o resultado de todos os valores digitados é de {resultado:.2f}")

    print("escolha uma das opções :  ")
    print(
        "pressione 1 para fazer outra conta com essa mesma opção de operação matemática "
    )
    print("pressione 2 para voltar ao menu principal")
    print("pressione 3 para finalizar o programa")
    opcao = int(input("digite  aqui uma das opções"))

    while opcao < 1 or opcao > 3:
        opcao = int(input("digite uma opção existente"))

    if opcao == 1:
        soma()
    elif opcao == 2:
        menu.menu()
    else:
        print("programa finalizado com sucesso")

    return
