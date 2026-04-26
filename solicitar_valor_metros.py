import os 

os.system("cls")



def retornando_em_cm(em_metros):

    cm= em_metros * 100

    return cm











valor_em_metros=float(input("Digite um valor em metros "))

cm=retornando_em_cm(valor_em_metros)

print(f"O valor de metros para cm é de: {cm}")