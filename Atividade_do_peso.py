import os

# Função sem retorno.
def logoSenai():
    os.system("cls || clear")
    print("=== SENAI === ")



def calcular_imc(PESO,ALTURA):

    imc= PESO / (ALTURA**2)

    return imc


def condicao(situacao):
      if situacao < 18.5:
        
        return "Abaixo do peso "
      
      elif situacao >=18.5 and situacao <=25:
            
        return "Peso Normal"
      
      elif situacao >25 and situacao <=30:
            
        return "Sobrepeso"
      
      elif situacao > 30 and situacao <=35:
            
        return "Obesidade Grau 1"
      
      elif situacao > 35 and situacao <=40:
        
        return "Obesidade Grau 2"
      
      else:
            
        return "Obesidade Grau 3"




# Definindo listas vazias para armazenar os dados dos usuários
nomes = []
sobrenome=[]
idades = []
alturas = []
pesos = []
imc_do_usuario=[]

# Solicitando os dados dos usuários em um loop
while True:
    logoSenai()
    nome = input("Digite o nome do usuário (ou digite 'sair' para encerrar): ").strip()
    
    # Verificando se o usuário quer sair
    if nome.lower() == 'sair':
        break

    sobre_nome=input("Digite seu Sobrenome").strip()
    idade = int(input("Digite a idade do usuário: "))
    altura = float(input("Digite a altura do usuário (em metros): "))
    peso = float(input("Digite o peso do usuário (em quilogramas): "))

    imc=calcular_imc(peso,altura)

    imc_do_usuario.append(imc)

    meuca=condicao(imc_do_usuario)


    # Adicionando os dados às listas
    nomes.append(nome)
    sobrenome.append(sobre_nome)
    idades.append(idade)
    alturas.append(altura)
    pesos.append(peso)

# Exibindo os dados armazenados
logoSenai()
print("\nDados dos usuários:")
for i in range(len(nomes)):
    print(f"Usuário {i+1}:")
    print("Nome:", nomes[i])
    print("Sobrenome",sobrenome[i])
    print("Idade:", idades[i])
    print("Altura:", alturas[i], "metros")
    print("Peso:", pesos[i], "quilogramas")
    print(f"{nome[i]} {sobrenome[i]} O Seu imc é de: {imc_do_usuario[i]} ")
    print(f"{meuca}")