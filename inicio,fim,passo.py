import os 

os.system("cls")


def contador(inicio,fim,passo):



    for i in range(inicio,fim,passo):

        print(i)


print(f" Contagem de 1 até 10 em 1 ")




        












contador( 1, 11, 1 )
print("fim")

print("")

print(" contagem de 10 até 0 em 2 ")

contador(10,0,-2)

print("fim")

print("")

print(" Vamos personalizar a sua contagem")

ini=int(input(" Digite o inicio "))

fi=int(input(" Digite o fim "))

pa=int(input(" Digite o passo "))


contador(ini,fi,pa)

print(" Fim")