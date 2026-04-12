import os 

os.system("cls")


def notas(n):

    maior=max(n)

    menor=min(n)

    tamanho=len(n)

    media=sum(n)/ tamanho

    return print(f" Maior: {maior}  Menor: {menor} tamanho: {tamanho} media: {media}")



    








lista_de_notas=[]

while True:

    nota_s=int(input("Digite sua nota"))

    lista_de_notas.append(nota_s)

    opcao=str(input(" Deseja continuar ? s ou n ")).strip().lower()

    if opcao =="n":
        break

reposta=notas(lista_de_notas)


print(f"{reposta}")

