import os 


os.system("cls")


def exibir_menu():

    print("""
\n1.Solicite matrícula e senha do funcionário para ter acesso aos seus dados.
\n2.Solicite o salário base do funcionário.
\n3.Pergunte se o funcionário deseja receber vale transporte (s/n).
\n4.Consulte o valor do vale refeição fornecido pela empresa.
\n5.Pergunte ao usuário a quantidade de dependentes.
\n6.Calcule os descontos e acréscimos na folha de pagamento do funcionário.
\n7.Mostre o salário líquido do funcionário após os descontos e acréscimos.
          """)

    

def vale_transporte_calculo(vale_t):

    vale_transporte_= vale_t * 0.06

    return vale_transporte_



def vale_reifeicao_calculo(vale_rei):

    vale_reifeicao= vale_rei * 0.20

    return vale_reifeicao


def plano_de_saude_calculo(saude_dependentes):

    plano= saude_dependentes * 150

    return plano


def calculando_inns(salario):
    Inns=0

    if salario < 1518.00:

        Inns = salario * 0.075

    elif salario >1518.01 and salario <= 2793.88:

        Inns= salario * 0.09

    elif salario > 2793.89 and salario <= 4190.83:

        Inns= salario * 0.12

    elif salario > 4190.84 and salario <= 8157.41:

        Inns= salario * 0.14
    
    elif salario > 8157.42:

        Inns = 951.62

    

    return Inns




def calculando_imposto(salario_base,inns):

    base= salario_base - inns

    irrf=0

    if base < 2428.80:

        irrf= 0
    
    elif base > 2428.81 and base <= 2826.65:

        irrf= base * 0.075

    elif base > 2826.66 and base <= 3751.05:

        irrf = base * 0.15

    elif base  > 3751.06 and base <= 4664.68:

        irrf= base * 0.225

    elif base > 4664.68:

        irrf = base * 0.275

    return irrf




matricula_do_usuario=0

senha_do_usuario=0

salario_base_do_funcionario=0

vale_transporte=""

vale=0

vale_reifeicao_pedido=0

dependentes=0

plano_de_saude=0

inns=0
imposto=0

salario_final=0

while True:

    exibir_menu()

    opcao=int(input("Escolha as opções acima = "))

    match opcao:

        case 1:

            print("")
            matricula_do_usuario=int(input("Digite sua matrícula Ex: números ="))
            print("")
            senha_do_usuario=int(input("Digite a sua senha= "))

            print("===Cadastro Concluído===")

        case 2:
            print("")

            salario_base_do_funcionario=float(input("Digite seu salário base ="))
            print("")
            print("===salário solicitado concluído===")

        case 3:
            print("")

            vale_transporte=str(input("Deseja solicitar o vale transporte ? S / N =")).strip().lower()

            print("Concluído")

            if vale_transporte == "s":
                
                vale=vale_transporte_calculo(salario_base_do_funcionario)

            

        case 4:
            print("")
            vale_reifeicao_pedido=int(input("Digite um valor do vale reifeição da empresa = "))

            vale_reifeicao=vale_reifeicao_calculo(vale_reifeicao_pedido)

            print("calculo concluído")

        case 5:
            print("")

            dependentes=int(input("Digite a Quantidade de Dependentes ="))

            plano_de_saude=plano_de_saude_calculo(dependentes)

            print("Concluído")

        case 6:
            print("CALCULANDO DESCONTOS: INNS E IMPOSTO ")
            print("")
            print("Concluído")

            inns=calculando_inns(salario_base_do_funcionario)
            imposto=calculando_imposto(salario_base_do_funcionario,inns)
        
        case 7:
            print("")

            print("Mostrando o salário líquido do funcionário após os descontos e acréscimos")

            salario_final= salario_base_do_funcionario - (inns + imposto + vale + vale_reifeicao + plano_de_saude)

            print(f"Salario_base: {salario_base_do_funcionario}")
            print(f"INNS: {inns}")
            print(f"Imposto: {imposto}")
            print(f"Vale_transporte: {vale}")
            print(f"Vale_reifeição: {vale_reifeicao}")
            print(f"Plano_de_saúde: {plano_de_saude}")
            print("")

            print(f"Salario Final : {salario_final}")

        case _:

            print("Escolha as opções de 1 a 7")















    




