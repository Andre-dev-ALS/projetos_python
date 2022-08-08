from decimal import Decimal

import menu


def chocolate():
    print("A bebida escolhida foi o chocolate")
    bebida_chocolate = 1.00
    print("Digite a quantidade dessa bebida que você quer comprar ")
    # variável que vai receber a quantidade de bebidas a ser comprada
    quantidade_bebida = str(input("informe aqui a quantidade "))

    # variável que será responsável de fazer os  controles dos  laços
    verifica = False
    # variável que vai receber os valores digitados de string convertidos para int
    valor = 0
    # repetição que vai executar sempre que uma quantidade menor que 1 seja digitada ou se um valor não  numérico seja    digitado
    while verifica == False and valor == 0:
        # condição para verificar se somente números foram digitados
        if quantidade_bebida.isnumeric():
            # conversão dos números para int
            valor = int(quantidade_bebida)
            verifica = True
        else:
            verifica = False

            # condição para verificar se o valor é  diferente de 0, caso verdadeiro vai se encerrar a repetição
        if valor != 0:
            verifica = True
        else:
            verifica = False
            print(
                "Erro ao informar a quantidade a ser comprada \n Possíveis motivos do erro: \n 1. Valor não numérico digitado \n 2. Valor menor que 1 foi digitado "
            )
            quantidade_bebida = str(input("Digite novamente a quantidade "))

        # variável que vai receber o preço total a ser pago

    preco_total_bebidas = bebida_chocolate * int(quantidade_bebida)
    print(f"O preço total da sua compra é de {preco_total_bebidas:.2f}")
    print("Informe a quantidade de moedas a ser inserida na máquina")
    print(
        "Observação: a máquina aceita apenas moedas de 0.10,0.50 centavos ou 1.00 real"
    )
    # variável que vai receber a  quantidade de moedas que vai ser colocada na máquina
    moedas = str(input("informe aqui a quantidade de moedas"))

    # reiniciando os valores das variáveis
    verifica = False
    valor = 0
    # repetição que vai sempre executar caso um valor não numérico ou menor que um seja digitado
    while verifica == False and valor <= 0:
        # condição para verificar se somente números foram digitados
        if moedas.isnumeric():
            # convertendo  a quantidade de moedas de str para int
            valor = int(moedas)
            verifica = True
        else:
            verifica = False

            # condição para verificar se o valor é  diferente de 0, caso verdadeiro vai se encerrar a repetição
        if valor != 0:
            verifica = True
        else:
            verifica = False
            print(
                "Erro ao informar a quantidade de moedas que serão colocadas \n Possíveis motivos do erro : \n 1. Um valor não numérico foi digitado \n 2. Um valor menor que um foi digitado"
            )
            moedas = str(input("digite novamente a quantidade"))

    # variável que vai receber o total de dinheiro colocado na máquina
    dinheiro_total = 0
    # repetição que vai executar x vezes de acordo com a quantidade de moedas que estará na máquina
    for contador in range(0, valor):
        print(f"A quantidade de moedas que vocÊ colocou na máquina foi de {valor}")
        print("Informe o valor de cada moeda colocada ")
        print("Digite 1 para 0.10 \n digite 2  para 0.50 \n digite 3 para 1.00")
        print(f"Qual é o valor da moeda {contador+1} ?")
        # variável que vai receber a opção que contém o valor da moeda
        valor_moedas = str(input("Digite aqui uma das opções"))

        # reiniciando o valor da variável
        verifica = False
        # laço de repetição qui  vai executar toda vez que uma opção que não exista tenha sido digitada
        while verifica == False:

            if valor_moedas.isnumeric:
                verifica = True
            else:
                verifica = False

            """condição que vai comparar a opção digitada com as opções válidas
            a condição que se tornar verdadeira vai ser atribuido o valor da moeda na  variável dinheiro_total"""

            if valor_moedas == "1":
                dinheiro_total += Decimal("0.1")
                verifica = True
            elif valor_moedas == "2":
                dinheiro_total += 0.50
                verifica = True
            elif valor_moedas == "3":
                dinheiro_total += 1.00
                verifica = True
            else:
                print(
                    "Erro ao informar o valor da moeda \n Possíveis motivos do erro: \n 1. Um valor não numérico foi digitado \n 2. Foi digitado uma opção que não existe "
                )
                valor_moedas = str(
                    input("Digite novamente a opção referente ao valor da moeda")
                )
                verifica = False

    dinheiro_total = float(dinheiro_total)
    # variável que vai receber o troco da compra
    troco = dinheiro_total - preco_total_bebidas
    # variável que vai receber um valor caso o dinheiro colocado na máquina não seja maior ou igual que o preço total da compra
    dinheiro_faltando = preco_total_bebidas - dinheiro_total
    # condição para verificar se foi feita a compra com sucesso ou não
    if dinheiro_total >= preco_total_bebidas:
        print("Compra efetuada com sucesso!!")

        print(f"O preço do produto é de {bebida_chocolate:.2f}")
        print(f"A quantidade dessa bebida que você comprou é de {quantidade_bebida}")
        print(f"O preço total da compra é de {preco_total_bebidas:.2f}")
        print(f"O total de dinheiro colocado foi de {dinheiro_total:.2f}")
        print(f"O seu troco é de {troco:.2f}")
    else:
        print("Falha na compra !! ")
        print("Motivo: você não colocou dinheiro suficiente para finalizar a compra ")
        print(f"O preço do produto é de {bebida_chocolate:.2f}")
        print(
            f"A quantidade dessa bebida que vocÊ tentou comprar foi de {quantidade_bebida}"
        )
        print(f"O preço total da sua compra foi de {preco_total_bebidas:.2f}")
        print(f"O total de dinheiro colocado foi de {dinheiro_total:.2f}")
        print(f"Coloque mais {dinheiro_faltando:.2f} para poder comprar a bebida")

    # opções que serão mostradas após a  finalização da compra ou na falha dela
    print("Escolha uma das opções a seguir ")
    print("Digite 1 para fazer uma nova compra dessa bebida")
    print("Digite 2 para voltar ao menu inicial")
    print("Digite 3 para finalizar o aplicativo ")
    opcao = str(input("digite uma das opções"))

    # reiniciando o valor da variável
    verifica = False
    # repetição que vai executar toda vez que for digitada uma opção inválida
    while verifica == False:

        if opcao.isnumeric:
            verifica = True
        else:
            verifica = False

        if opcao == "1":
            chocolate()
            verifica = True
        elif opcao == "2":
            menu.menu()
            verifica = True
        elif opcao == "3":
            print("Obrigado por ter escolhido o nosso  aplicativo ")
            print(" esperamos que você possa voltar logo ")
            verifica = True
        else:
            print(
                "Erro ao selecionar uma das opções \n possíveis motivos do erro : \n 1. valor não numérico foi digitado \n 2. uma opção inexistente foi digitada"
            )
            opcao = str(input("digite uma das opções"))
            verifica = False
