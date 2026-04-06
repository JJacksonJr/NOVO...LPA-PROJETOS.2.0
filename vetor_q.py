import os 

os.system("cls")


lista_Q_20=[]

posicao_do_maior_numero_da_lista=[]

posicao_do_menor_numero_da_lista=[]

for i in range(3):

    numero_positivos=int(input(" Digite só numeros positivos "))

    lista_Q_20.append(numero_positivos)

maior_valor=max(lista_Q_20)

menor_valor=min(lista_Q_20)


for i in range(len(lista_Q_20)):

    if lista_Q_20[i] == maior_valor:

        posicao_do_maior_numero_da_lista.append(i)


    if lista_Q_20[i] == menor_valor:

        posicao_do_menor_numero_da_lista.append(i)




print(f" O maior valor da lista é : {maior_valor}--- e o seu indice é {posicao_do_maior_numero_da_lista}")

print(f" O maior valor da lista é : {menor_valor}--- e o seu indice é {posicao_do_menor_numero_da_lista}")

