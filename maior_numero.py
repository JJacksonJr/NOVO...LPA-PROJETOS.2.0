import os 

os.system("cls")

def maior(list):

    print(" Analisando resultados ")

    maior_numero=max(list)

    for i in range(len(list)):

        print(f"{list[i]}")

    print(f" O maior numero da lista é : {maior_numero}")




vetor=[2,9,4,8]
vetor_2=[10,2,6]


maior(vetor)

maior(vetor_2)



