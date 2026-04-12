import os 

os.system("cls")




def area_servico(b,h):

    Area= b * h

    litros=Area/2

    return Area,litros








base=int(input(" Digite a base "))

altura=int(input("Digite a altura"))

area,Litros=area_servico(base,altura)

print(f" A Aréa a ser pintada é de: {area} e a tinta necessarias pra poder completar o servico é de: {Litros}")