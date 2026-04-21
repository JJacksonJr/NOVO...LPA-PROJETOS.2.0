import os 

os.system("cls")


def mostrar_maior_menor(lista_dos_8_produtos):

    maior=max(lista_dos_8_produtos)
    menor=min(lista_dos_8_produtos)

    return maior,menor







lista_produtos=[]


for i in range(1,9,1):

    preco_produto=float(input("Digite o preço do produto "))

    lista_produtos.append(preco_produto)


    maior,menor=mostrar_maior_menor(lista_produtos)

print(f" O maior preço é: {maior} é o menor {menor}")