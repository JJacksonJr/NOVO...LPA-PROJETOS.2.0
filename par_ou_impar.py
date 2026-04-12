import os 


os.system("cls")



def par_ou_impar(numero):

    if numero % 2==0:

        print(f" O Numero {numero} é Par ")

    else:

        print(f" O Numero {numero}  é impar ")









numero_1=int(input(" Digite um numero"))


par_ou_impar(numero_1)