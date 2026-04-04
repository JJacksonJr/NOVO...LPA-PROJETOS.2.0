import os

os.system("cls")

lista_de_10_numeros=[]



for i in range(0,3):
    numero=int(input("digite um numero "))

    lista_de_10_numeros.append(numero)


for i in range(len(lista_de_10_numeros)):

    if lista_de_10_numeros[i] % 2 ==0:

        print(f" Numeros pares: {lista_de_10_numeros[i]} -- indice: {i} ")

