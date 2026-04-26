import os 


os.system("cls")



def inflacionar_preco(preco):

    novo_preco=0

    if preco <100:

        novo_preco = preco + (preco * 0.10)

    elif preco >=100:

        novo_preco = preco + (preco * 0.20)

    return novo_preco











pre=float(input("Digite o valor do seu produto "))

preco_infla=inflacionar_preco(pre)

print(f"O Preço inflacionado de {pre} é de: {preco_infla}")