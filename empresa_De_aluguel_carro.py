import os 


os.system("cls")



def carros_populares(carros_popular,dias_aluguel,km_pecorridos):

    total_dias_pagos=0

    valor_total_De_km_apagar=0

    if carros_popular =="popular":

        total_dias_pagos= dias_aluguel * 90

    if km_pecorridos <= 100:

        valor_total_De_km_apagar= km_pecorridos * 0.20

    elif km_pecorridos > 100:

        valor_total_De_km_apagar = km_pecorridos * 0.10

    print(f"carro_popular: O valor total de dias a ser pago é : {total_dias_pagos} e o valor total de km é de; {valor_total_De_km_apagar}")





def carros_luxos(carros_luxo,dias_aluguel_luxo,km_pecorridos_luxo):

    total_dias_luxo=0

    valor_total_de_km_pecorrido_luxo=0

    if carros_luxo =="luxo":

        total_dias_luxo= dias_aluguel_luxo *150

    if km_pecorridos_luxo <=200:

        valor_total_de_km_pecorrido_luxo= km_pecorridos_luxo * 0.30

    elif km_pecorridos_luxo > 200:

        valor_total_de_km_pecorrido_luxo = km_pecorridos_luxo * 0.25

    print(f"carro_luxo: o valor total de dias a  ser pago: {total_dias_luxo} e o total a ser pago km: {valor_total_de_km_pecorrido_luxo}")

    


    







tipo_de_carro=str(input("Digite o tipo de carro (popular ou luxo)")).strip().lower()

quantos_Dias_aluguel=int(input("Digite quantos dias vc alugou "))

quantos_km_pecorrido=int(input("Digite quantos kms pecorridos "))

if tipo_de_carro =="popular":

    carros_populares(tipo_de_carro,quantos_Dias_aluguel,quantos_km_pecorrido)

elif tipo_de_carro =="luxo":

    carros_luxos(tipo_de_carro,quantos_Dias_aluguel,quantos_km_pecorrido)









