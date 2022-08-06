import adicao
import divisao
import multiplicacao
import subtracao


def menu():
    print("escolha a operação matemática  ")
    print("digite 1 para soma")
    print("digite 2 para subtração")
    print("digite 3 para multiplicação")
    print("digite 4 para subtração")
    operacao = int(input("digite aqui a opção desejada"))

    if operacao == 1:
        adicao.soma()
    else:
        if operacao == 2:
            subtracao.subtrair()
        else:
            if operacao == 3:
                multiplicacao.multiplica()
            else:
                if operacao == 4:
                    divisao.dividir()
                else:
                    print("ops valor inválido")

    while operacao < 1 or operacao > 4:
        operacao = int(input("digite aqui a opção desejada"))

        if operacao == 1:
            adicao.soma()
        else:
            if operacao == 2:
                subtracao.subtrair()
            else:
                if operacao == 3:
                    multiplicacao.multiplica()
                if operacao == 4:
                    divisao.dividir()
                else:
                    print("ops valor inválido")
    return
