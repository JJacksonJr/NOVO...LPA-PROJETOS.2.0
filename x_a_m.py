import os 

os.system("cls")

vetor_de_a=[]

vetor_M=[]


for i in range(10):
    numero=int(input(" Digite um numero "))

    vetor_de_a.append(numero)


mais_um_numero=int(input(" Digite mais um numero "))







for i in range(len(vetor_de_a)):

    multiplicacao= vetor_de_a[i] * mais_um_numero


    vetor_M.append(multiplicacao)


print(f" vetor completo de M: {vetor_M}")

