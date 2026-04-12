import os 


os.system("cls")



def delta(a,b,c):

    formula=b**2 - 4 * a * c

    return formula







a_=int(input("Digite um valor "))

b_=int(input("Digite um valor "))

c_=int(input("Digite um valor "))

reposta=delta(a_,b_,c_)

print(f" O valor é de: {reposta}")