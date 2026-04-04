import os 

os.system("cls")

lista_de_15_numeros=[]



for i in range(0,3):
    numero=int(input("Digite um numero"))

    lista_de_15_numeros.append(numero)


print(f" Todo vetor: {lista_de_15_numeros}")

for i in range(len(lista_de_15_numeros)):

    if lista_de_15_numeros[i] % 10 ==0:
        
        print(f" indice:{i} ")
