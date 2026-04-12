import os 

os.system("cls")



def sucessor_antecessor(n1):

    a= n1 +1
    
    b= n1 -1

    return a,b




numero=int(input("Digite um numero "))


resultado=sucessor_antecessor(numero)

print(f"{resultado}")