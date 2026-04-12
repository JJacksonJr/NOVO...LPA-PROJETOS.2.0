import os 

os.system("cls")


def dobro_terca(n):

    dobro=n *2

    terca= n / 3

    return dobro,terca





numero=float(input("Digite um numero "))


dobro_,terca_=dobro_terca(numero)


print(f" O dobro desse numero é {dobro_} e a terça parte é {terca_}")