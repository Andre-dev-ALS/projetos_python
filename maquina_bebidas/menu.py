import cafe
import cafe_com_leite
import cha
import chocolate
def menu():

    # mostrando uma lista de opções  de bebidas para o usuário
    print("Escolha uma das opções da máquina de bebidas")
    print("Digite 1 para chá preço 0.50 ")
    print("Digite 2 para café preço 0.80 ")
    print("Digite 3 para chocolate preço 1.00 ")
    print("Digite 4 para café com leite preço 1.20 ")
    opcao = str(input("Digite aqui uma das opções"))


    """laço de repetição que vai repetir o bloco de código  caso a opção não exista
    isso vai  ocorrer até que uma opção válida seja selecionada """

    verifica = False

    while verifica == False:

        if opcao.isnumeric:
            verifica = True
        else:
            verifica = False

        if opcao == "1":
            cha.cha()
            verifica = True
        elif opcao == "2":
            cafe.cafe()
            verifica = True
        elif opcao == "3":
            chocolate.chocolate()
            verifica = True
        elif opcao == "4":
            cafe_com_leite.cafe_com_leite()
            verifica = True
        else:
            print(
                "Erro ao selecionar uma das opções \n possíveis motivos do erro : \n 1. valor não numérico foi digitado \n 2. uma opção inexistente foi digitada"
            )
            opcao = str(input("digite uma das opções"))
            verifica = False
            