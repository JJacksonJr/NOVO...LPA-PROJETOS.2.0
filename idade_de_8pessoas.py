import os 

os.system("cls")

lista_de_idade_8_pessoas=[]

media=0

soma=0

maior=0

posicao_do_maior=[]


for i in range(0,8):

    idade=int(input("digite sua idade"))

    lista_de_idade_8_pessoas.append(idade)

maior=max(lista_de_idade_8_pessoas)#Pra encontrar o indici do maior numero , tem que botar a variavel antes 




for i in range(len(lista_de_idade_8_pessoas)):

    if lista_de_idade_8_pessoas[i] > 25 :
        print(f" indice das idades maiores que 25: indice {i}")

    if lista_de_idade_8_pessoas[i] == maior:
        posicao_do_maior.append(i)








soma=sum(lista_de_idade_8_pessoas)


media= soma / 8

print(f" A posição em que digitamos a maior idade é : {posicao_do_maior}")

print(f" A soma das idades é de : {soma}")

print(f" A media das idades das  pessoas cadastradas é de : {media}")

print(f" A maior idade é de : {maior} ")



