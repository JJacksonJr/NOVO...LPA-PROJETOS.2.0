import os


os.system("cls")



def homens_cadastro(genero,lista_idade):

    qtd_h=0

    soma_h_idade=0


    for i in range(len(genero)):

        if genero[i] =="m":

            qtd_h+=1

            soma_h_idade+=lista_idade[i]

        if qtd_h == 0:

            qtd_h=0

    media_das_idades= soma_h_idade / qtd_h

    return qtd_h,soma_h_idade,media_das_idades




def mulher_cadastro(genero,lista_idade):

    qtd_mulher=0

    qtd_mulher_acima_de_20=0

    for i in range(len(genero)):# pecorrer todos os índices de genero

        if genero[i] =="f":  
            
            qtd_mulher+=1

            if lista_idade[i] > 20:
                qtd_mulher_acima_de_20+=1

            

    return qtd_mulher,qtd_mulher_acima_de_20





def media_do_grupo(lista_idade):

    soma_do_grupo=sum(lista_idade)

    tamanho=len(lista_idade)



    media_tudo= soma_do_grupo / tamanho


    return media_tudo













lista_genero=[]

lista_idades=[]

for i in range(1,6,1):

    sexo=str(input("Digite seu gênero ")).strip().lower()

    idade=int(input("Digite sua idade "))

    lista_idades.append(idade)
    lista_genero.append(sexo)





qtd_homens,soma_total_idades_h,media_h=homens_cadastro(lista_genero,lista_idades)

qtd_mulher,qtd_mulher_acima_20=mulher_cadastro(lista_genero,lista_idades)

media_tudo=media_do_grupo(lista_idades)


print(f"quantidade de h: {qtd_homens} soma_total das idades dos homens: {soma_total_idades_h} e a média: {media_h}")

print(f"A quantdidade de mulheres: {qtd_mulher} e acima de 20 anos: {qtd_mulher_acima_20}")

print(f"A média de tudo é de; {media_tudo}")