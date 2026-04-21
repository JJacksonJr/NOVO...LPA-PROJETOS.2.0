import os 

os.system("cls")



def Reajuste(anos,salario):

    if anos <3:

        aumento= salario *0.03

    elif anos >=3 and anos <=10:

        aumento = salario * 0.125

    elif anos >10:

        aumento= salario * 0.2


    return aumento



def Novo_salario(salario_novo,salario_):

    novo= salario_novo + salario_

    return novo




nome=str(input("Digite seu nome ")).strip()

ano=int(input("Digite Quantos anos vc trabalhou na empresa "))

salarioo=float(input("Digite seu salario "))

aumento=Reajuste(ano,salarioo)

Novo_salari=Novo_salario(aumento,salarioo)


print(f"{nome} ")
print(f" Seu salario: {salarioo}")
print(f"Seu Aumento é de: {aumento}")
print(f"Novo salario: {Novo_salari}")


