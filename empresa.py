import os 

os.system("cls")




def reajuste_homem(anos_h,salario_h):

    if anos_h < 20:
        
        aumento= salario_h * 0.03

        salario_final= salario_h + aumento

    elif anos_h >=20 and anos_h <=30:

        aumento = salario_h * 0.13

        salario_final= salario_h + aumento

    elif anos_h > 30:

        aumento= salario_h  * 0.25

        salario_final = salario_h + aumento
    
    print(f"Homem: O aumento no salário é de: {aumento} é o salário final é de: {salario_final}")



    

def reajuste_mulher(anos_m,salario_m):

    if anos_m < 15:

        aumento= salario_m * 0.05

        salario_final= salario_m + aumento

    elif anos_m >=15 and anos_m <=20:

        aumento= salario_m * 0.12

        salario_final= salario_m + aumento

    elif anos_m > 20:

        aumento= salario_m * 0.23

        salario_final= salario_m + aumento

    print(f"Mulher: O aumento no salário é de: {aumento} é o salário final é de: {salario_final}")








tipo_genero=str(input("Digite seu gênero M ou F")).strip().lower()

anos=int(input("Digite a quantidade de anos que vc tá na empresa "))

salario=float(input("Digite seu salário "))


if tipo_genero =="m":

    reajuste_homem(anos,salario)

elif tipo_genero =="f":

    reajuste_mulher(anos,salario)

