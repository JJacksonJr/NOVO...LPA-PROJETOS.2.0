import os 



os.system("cls")


def dolar(numero):

    Eua= numero / 5.01

    return Eua





n=float(input("Digite um valor em Reais R$ "))

resultado=dolar(n)


print(f"O valor de reais para dolar é de : {resultado}")