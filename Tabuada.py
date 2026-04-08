import os 

os.system("cls")


def tabuada(multi):

    print("")

    print("")

    print(f" TABUADA  // MULTIPLICAÇÃO")

    for i in range(11):

        resultado= multi * i


        print(f" {multi} * {i} == {resultado}")

    


while True:
    
    n=int(input(" Digite um numero "))

    tabuada(n)