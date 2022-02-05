import cafe
import cafe_com_leite
import cha
import chocolate

print("Escolha uma das opções da cafeteira !")
print("Digite 1 para café preço 0.50 ")
print("Digite 2 para chá preço 0.80 ")
print("Digite 3 para chocolate preço 1.00 ")
print("Digite 4 para café com leite preço 1.20 ")
bebida = int(input("Digite aqui uma das opções"))

if bebida == 1:
    cafe.cafe()
elif bebida == 2:
    cha.cha()
elif bebida == 3:
    chocolate.chocolate()
elif bebida == 4:
    cafe_com_leite.cafe_com_leite()
else:
    print("opção inválida")

while bebida < 1 or bebida > 4:

    print("Digite 1 para café preço 0.50 ")
    print("Digite 2 para chá preço 0.80 ")
    print("digite 3 para chocolate preço 1.00 ")
    print("Digite 4 para café com leite preço 1.20 ")
    bebida = int(input("Digite uma das opções"))
    if bebida == 1:
        cafe.cafe()
    elif bebida == 2:
        print("você escolheu chá")
    elif bebida == 3:
        print("você escolheu chocolate")
    elif bebida == 4:
        print("você escolheu café com leite")
    else:
        print("opção inválida ")
