import os 

os.system("cls")




def pessoas_mais_18_anos(lista_idades):

    qtd_pessoas_mais_18=0

    for i in range(len(lista_idades)):

        if lista_idades[i] > 18:

            qtd_pessoas_mais_18+=1

    return qtd_pessoas_mais_18


def pessoas_menos_5_anos(lista_5_anos):

    qtd_pessoas_menos_5=0

    for i in range(len(lista_5_anos)):

        if lista_5_anos[i] < 5:

            qtd_pessoas_menos_5+=1

    return qtd_pessoas_menos_5




def maior_idade_lida(maior_lida):

    maior_idade=max(maior_lida)

    return maior_idade




def media_das_idades(media_idade):

    soma_total=sum(media_idade)

    tamanho=len(media_idade)

    media= soma_total / tamanho


    return media,soma_total






lista_de_idades=[]


for i in range (1,11,1):

    idade=int(input("Digite sua idade "))

    lista_de_idades.append(idade)

qtd_18=pessoas_mais_18_anos(lista_de_idades)

qtd_5=pessoas_menos_5_anos(lista_de_idades)

maior_idade=maior_idade_lida(lista_de_idades)

media_total,soma=media_das_idades(lista_de_idades)


print(f" A soma total das notas: {soma}")
print(f"A média é de: {media_total}")
print(f" tem {qtd_18} pessoas com mais de 18 anos ")
print(f" tem {qtd_5} pessoas com menos de 5 anos ")