import os 

os.system("cls")



def fatorial(numero,show):

    f=1

    for i in range(numero,0,-1):
        
        f*=i

    return f








n=int(input(" Digite um numero "))

fatorial(n)

print(fatorial(n),show=True)

