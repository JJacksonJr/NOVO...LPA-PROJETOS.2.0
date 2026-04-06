import os

os.system("cls")


vetor_A=[]

vetor_B=[]

vetor_soma=[]


n=int(input(" Digite um valor pra n "))

for i in range(n):

    a=int(input(" Digite um valor pra vetor A"))

    vetor_A.append(a)

    b=int(input(" Digite um valor pra b "))

    vetor_B.append(b)


    vetor_soma.append(vetor_A[i] + vetor_B[i])



print(f" A soma total: {vetor_soma}")





