import os 

os.system("cls")

lista_de_nome=[]

lista_de_genero=[]

lista_de_salario=[]

qtd_de_mulheres=0

qtd_pessoas=0

for i in range (0,5):
    
    nome=str(input("Digite seu Nome ")).strip()

    sexo=str(input(" Digite seu Gênero m ou f ")).strip().lower()

    salario=float(input(" Digite seu salario "))

    qtd_pessoas+=1

    

    if sexo == "f" and  salario > 5000:

        lista_de_nome.append(nome)

        lista_de_genero.append(sexo)

        lista_de_salario.append(salario)

        qtd_de_mulheres+=1

for i in range(qtd_de_mulheres):
    print(f" mulheres que ganham mais de 5000: {lista_de_nome[i]} ---- R$ {lista_de_salario[i]}")

