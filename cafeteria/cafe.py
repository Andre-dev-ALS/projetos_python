import menu


def cafe():
    print("a bebida escolhida foi o café")
    café = 0.50
    print("Digite a quantidade dessa bebida que você quer comprar ")
    quantidade_bebida = int(input("informe aqui a quantidade "))
    while quantidade_bebida < 1:
        print("ops você não pode digitar um valor negativo ")
        quantidade_bebida = int(input("Informe a quantidade que você quer comprar "))
    preço_total_bebidas = café * quantidade_bebida

    print(f"O preço total da sua compra é de {preço_total_bebidas:.2f}")
    print("Informe a quantidade de moedas a ser inserida na máquina")
    print(
        "observação: a máquina aceita apenas moedas de 0.10,0.50 centavos ou 1.00 real"
    )
    moedas = int(input("informe aqui a quantidade de moedas"))
    dinheiro_total = 0
    for contador in range(0, moedas):
        print(f"Você colocou {moedas} moedas na máquina")
        print("informe o valor de cada moeda colocada ")
        print("Digite 1 para 0.10 \n digite 2  para 0.50 \n digite 3 para 1.00")
        print(f"Qual é o valor da moeda {contador+1} ?")
        valor_moedas = int(input("Digite aqui uma das opções"))

        if valor_moedas == 1:
            dinheiro_total = dinheiro_total + 0.10
        elif valor_moedas == 2:
            dinheiro_total = dinheiro_total + 0.50
        elif valor_moedas == 3:
            dinheiro_total = dinheiro_total + 1.00
        else:
            print("Ops você digitou uma opção inválida , digite novamente")
            valor_moedas = int(input("Digite uma das opções"))
        while valor_moedas < 1 or valor_moedas > 3:

            if valor_moedas == 1:
                dinheiro_total = dinheiro_total + 0.10
            elif valor_moedas == 2:
                dinheiro_total = dinheiro_total + 0.50
            elif valor_moedas == 3:
                dinheiro_total = dinheiro_total + 1.00
            else:
                print("Ops vocÊ digitou uma opção inválida, digite novamente")
                valor_moedas = int(input("escolha uma das opções "))
    troco = dinheiro_total - preço_total_bebidas
    dinheiro_faltando = preço_total_bebidas - dinheiro_total
    if dinheiro_total < preço_total_bebidas:
        print("falha na compra !! ")
        print("motivo: você não colocou dinheiro suficiente para comprar a bebida")
        print(f"o preço do produto é de {café:.2f}")
        print(
            f"a quantidade dessa bebida que você quer comprar é de {quantidade_bebida}"
        )
        print(f"O preço total da compra é de {preço_total_bebidas:.2f}")
        print(f"o total de dinheiro colocado foi de {dinheiro_total:.2f}")
        print(f"coloque mais {dinheiro_faltando:.2f} para poder comprar a bebida")
    else:
        print("Compra efetuada com sucesso!!")
        print(f"o preço do produto é de {café:.2f}")
        print(f"A quantidade dessa bebida que vocÊ comprou é de {quantidade_bebida}")
        print(f"O preço total da sua compra foi de {preço_total_bebidas:.2f}")
        print(f"o total de dinheiro colocado foi {dinheiro_total:.2f}")
        print(f"O seu troco é de {troco:.2f}")

    print("escolha uma das opções a seguir ")
    print("digite 1 para fazer uma nova compra dessa bebida")
    print("digite 2 para voltar ao menu inicial")
    print("digite 3 para finalizar o aplicativo ")
    opção = int(input("digite uma das opções"))
    while opção < 1 or opção > 3:
        print("ops você digitou uma opção inválida \n por favor digite novamente")

    if opção == 1:
        cafe()
    elif opção == 2:
        menu.menu()
    elif opção == 3:
        print("obrigado por ter escolhido a nossa cafeteria ")
        print("esperamos que você possa voltar logo ")
    else:
        opção = int(input("digite uma das opções"))
