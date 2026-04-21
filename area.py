import os 

os.system("cls")



def calculando_area(base,altura):

    Area= base * altura

    return Area



def condicao(situacao):

    if situacao <100:

        return "TERRENO POPULAR"
    
    elif situacao >=100 and situacao <=500:

        return "TERRENO MASTE"
    
    elif situacao > 500:

        return "TERRENO ViP"




largura=float(input("Digite a base do terreno"))

comprimento=float(input("Digite a altura do terreno"))

area=calculando_area(largura,comprimento)

print(f"A Aréa do terreno é: {area}")

print(f"{condicao(area)}")

