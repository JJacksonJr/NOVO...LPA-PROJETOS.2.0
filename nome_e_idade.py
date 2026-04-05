import os 

os.system("cls")

lista_Dos_nomes=[]

lista_das_idades=[]




for i in range(0,3):
    nome=str(input("Digite seu nome ")).strip()

    lista_Dos_nomes.append(nome)

    idade=int(input("Digite sua idade "))

    lista_das_idades.append(idade)

for i in range(len(lista_das_idades)):
    if lista_das_idades[i] < 18:
        print(f"pessoas menores de idade= Nome: {lista_Dos_nomes[i]} -- idade:{lista_das_idades[i]}")




