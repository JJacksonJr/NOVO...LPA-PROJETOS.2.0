import os 



os.system("cls")


def operacao_soma(numero1,numero2):

    soma= numero1 + numero2

    return soma



def operacao_subtracao(numero1,numero2):

    subtracao= numero1 - numero2

    return subtracao



def operacao_divisão(numero1,numero2):

    divisao= numero1 / numero2

    return divisao


def operacao_multiplicacao(numero1,numero2):

    multiplicacao= numero1 * numero2


    return multiplicacao






n1=int(input("Digite um numero "))

n2=int(input("Digite um segundo número "))

soma=operacao_soma(n1,n2)

subtracao= operacao_subtracao(n1,n2)

divisao=operacao_divisão(n1,n2)

multiplicacao=operacao_multiplicacao(n1,n2)

print("")
print(f"Soma: {n1} + {n2} = {soma}")
print("")
print(f"subtracao: {n1} - {n2} = {subtracao}")
print("")
print(f"divisao: {n1} / {n2} = {divisao}")
print("")
print(f"multiplicacao: {n1} * {n2} = {multiplicacao}")


