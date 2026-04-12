import os 

os.system("cls")



def maior_numero(numero_1,numero_2):

    print(" Analisando OS valores ")

    maior_numero_s=max(numero_1,numero_2)

    if numero_1 == numero_2:

        print(" São iguais ")

    else:

        print(f" O maior numero é de: {maior_numero_s}")








valor_1=int(input(" Digite um valor "))

valor_2=int(input(" Digite um segundo valor "))



maior_numero(valor_1,valor_2)