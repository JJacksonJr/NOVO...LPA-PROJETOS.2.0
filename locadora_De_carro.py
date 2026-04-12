import os 

os.system("cls")




def locadora(Km_pecorridos,dias):

    custos_km=Km_pecorridos * 0.20

    custo_dias= dias * 90


    total_de_tudo= custos_km + custo_dias

    return total_de_tudo










Km_pecorridoss=float(input("Digite Km pecorridos "))

dias_alugados=int(input("Digite os dias alugados "))


total=locadora(Km_pecorridoss,dias_alugados)

print(f" O Custo total é de : {total}")