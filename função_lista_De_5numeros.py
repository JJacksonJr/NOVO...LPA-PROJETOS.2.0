import os 

os.system("cls")

qtd_de_numeros_inseridos=0

lista_numero5=[]

for i in range(1,6,1):
    
    numero = int(input(f"Digite o {i+0}º número: "))

    qtd_de_numeros_inseridos+=1

    lista_numero5.append(numero)




def funcao_par(lista_par):

    quantidade_pares = 0

    soma_pares=0

    media_pares=0

    for i in range(len(lista_par)):
        
        if lista_par[i] % 2 ==0:
            
            quantidade_pares+=1
            
            soma_pares+=lista_par[i]

        if quantidade_pares ==0:

            media_pares=0
        
        else:

            media_pares=soma_pares / quantidade_pares

    return quantidade_pares,soma_pares,media_pares
    

qtd_pares,soma_pares,media_pares=funcao_par(lista_numero5)


def funcao_impar(lista_impar):

    quantidade_impares=0

    soma_impares=0

    media_impares=0

    for i in range(len(lista_impar)):
        
        if lista_impar [i] % 2 ==1:
            
            quantidade_impares+=1
            
            soma_impares+=lista_impar[i]
            
        if quantidade_impares ==0:

            media_impares=0

        else:

            media_impares= soma_impares / quantidade_impares

    return quantidade_impares,soma_impares,media_impares


qtd_impares,soma_impares,media_impares=funcao_impar(lista_numero5)


def numero_positivo(lista_positivo):

    quantidade_positivos=0

    for i in range(len(lista_positivo)):
        
        if lista_positivo[i] > 0:
            
            quantidade_positivos+=1

    return quantidade_positivos

qtd_positivos=numero_positivo(lista_numero5)   



def numero_negativo(lista_negativo):

    quantidade_negativos=0

    for i in range(len(lista_negativo)):
        
        if lista_negativo[i] <0:
            
            quantidade_negativos+=1

    return quantidade_negativos
    
qtd_negativos=numero_negativo(lista_numero5)



def maior_menor(lista_maior_menor):
    
    maior_numero=max(lista_maior_menor)
    menor_numero=min(lista_maior_menor)

    return maior_numero,menor_numero


maior,menor=maior_menor(lista_numero5)


def media_de_tudo(lista_tudo):

    soma_total=sum(lista_tudo)

    tamanho=len(lista_tudo)

    media= soma_total / tamanho

    return media



media_tudo=media_de_tudo(lista_numero5)



def numeros_invertidos(lista_dos_invertidos):

    vetor_invertido=[]

    for i in range(len(lista_dos_invertidos)-1,-1,-1):

        vetor_invertido.append(lista_dos_invertidos[i])
        

    return vetor_invertido




invertido=numeros_invertidos(lista_numero5)








# Imprimindo as estatísticas
print("\nEstatísticas dos números:")

print(f"Quantidade de pares: {qtd_pares}")
      
print(f"Quantidade de ímpares: {qtd_impares}")

print(f"Quantidade de positivos: {qtd_positivos}")

print(f"Quantidade de numeros negativos {qtd_negativos}")

print(f"Quantidade de numeros inseridos: {qtd_de_numeros_inseridos}")
      
print(f"O maior numero : {maior}")
      
print(f"O menor numero: {menor}")
      
print(f"media de pares: {media_pares}")
      
print(f"media de impares: {media_impares}")
      
print(f"media de tudo : {media_tudo}")

print(f" lista_invertidos: {invertido}")
      
