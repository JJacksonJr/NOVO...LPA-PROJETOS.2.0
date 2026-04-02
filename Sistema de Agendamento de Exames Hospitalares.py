import os 

os.system("cls")

preco_total=0 # A acumular o preço dos exames escolhido pela pessoa 

qtd_de_exames=0 # ver a quantidade de exames escolhido pela pessoa

lista_De_nomes_exames=[] # um vetor que armazena os nomes dos exames escolhido pela pessoa

lista_De_precos_dos_exames=[] # um vetor que armazena os preços dos exames escolhido pela pessoa

lista_do_codigo_do_exame=[] # um vetor que armazena os códigos  dos exames escolhido pela pessoa




while True:# usamos while para repetir varias vezes até a pessoa encerrar

    print("===EXAMES==") # Listas dos exames 

    print("""
1 - Hemograma Completo 40 R$
          
2 - Raio-X 100 R$
          
3 - Ultrassonografia 250 R$
          
4 - Eletrocardiograma 60 R$
          
5 - Tomografia 800 R$
          
6 - Ressonância Magnética 1800 R$
          
7 - Exame de Glicose 20 R$
          """)
    
    opcao=int(input(" Digite a opcao de exame que vc quer, de 1 a 7 "))#usamos eessa opção para a pessoa escolher o tipo de exame

    match opcao:# usamos um swith para a pessoa escolher os exames 

        case 1:
            print("")

            print(" === Hemograma completo ===")

            print("")

            lista_De_nomes_exames.append(" Hemograma completo ")# a gente pega esses 3 vetores e armazena o valor neles: Nome do exame, preço do exame e o código do excame

            lista_De_precos_dos_exames.append(40.0)

            lista_do_codigo_do_exame.append(1)

            preco_total+=40 # usamos essa variavel pra somar os precos

            qtd_de_exames+=1# usamos essa variavel pra ver a quantidade de exames escolhido pela pessoa 

            print("")

            repsota=str(input(" Deseja adicionar outro exame ? S ou N ?")).strip().lower()# criamos essa variavel pra poder prosseguir ou parar

            print("")

            if repsota == "n":
                break

            #Todo comentário que digitei, serve para os demais casos(case)

        case 2:
            print("")

            print("  === Raio-X ===")

            lista_De_nomes_exames.append("Raio-X")

            lista_De_precos_dos_exames.append(100.0)

            lista_do_codigo_do_exame.append(2)

            preco_total+=100

            qtd_de_exames+=1

            print("")

            repsota=str(input(" Deseja adicionar outro exame ? S ou N ?")).strip().lower()

            print("")

            if repsota == "n":
                break

        case 3:
            print("")

            print(" === Ultrassonografia ===")

            print("")

            lista_De_nomes_exames.append(" Ultrassonografia ")

            lista_De_precos_dos_exames.append(250.0)

            lista_do_codigo_do_exame.append(3)

            preco_total+=250

            qtd_de_exames+=1

            print("")

            repsota=str(input(" Deseja adicionar outro exame ? S ou N ?")).strip().lower()

            print("")

            if repsota == "n":
                break

        case 4:
            print("")

            print(" === Eletrocardiograma === ")

            print("")

            lista_De_nomes_exames.append("Eletrocardiograma")

            lista_De_precos_dos_exames.append(60)

            lista_do_codigo_do_exame.append(4)

            preco_total+=60

            qtd_de_exames+=1

            print

            repsota=str(input(" Deseja adicionar outro exame ? S ou N ?")).strip().lower()

            if repsota == "n":
                break

        case 5:
            print("")

            print(" === Tomografia ===")

            print("")

            lista_De_nomes_exames.append("Tomografia")

            lista_De_precos_dos_exames.append(800)

            lista_do_codigo_do_exame.append(5)

            preco_total+=800

            qtd_de_exames+=1

            repsota=str(input(" Deseja adicionar outro exame ? S ou N ?")).strip().lower()

            if repsota == "n":
                break

        case 6:
            print("")

            print(" === Ressonância Magnética ===")

            print("")

            lista_De_nomes_exames.append("=== Ressonância Magnética ===")

            lista_De_precos_dos_exames.append(1800)

            lista_do_codigo_do_exame.append(6)

            preco_total+=1800

            qtd_de_exames+=1

            repsota=str(input(" Deseja adicionar outro exame ? S ou N ?")).strip().lower()

            if repsota == "n":
                break

        case 7:
            print("")

            print(" === Exame de Glicose === ")

            print("")

            lista_De_nomes_exames.append(" Exame de Glicose ")

            lista_De_precos_dos_exames.append(20)

            lista_do_codigo_do_exame.append(7)

            preco_total+=20

            qtd_de_exames+=1

            print("")

            repsota=str(input(" Deseja adicionar outro exame ? S ou N ?")).strip().lower()

            print("")

            if repsota == "n":
                break

        case _:
            print("")

            print(" Digite Novamente um codigo válido ")

            print("")



print("")

print("")

for i in range(qtd_de_exames):# usamos esse for pra ver  a quantidade de exames escolhido pela pessoa
    print(f" os exames escolhidos e os preços  são: {lista_De_nomes_exames[i]} --- {lista_De_precos_dos_exames[i]}")# Aqui mostra os valores de cada indíce// vetor nomes e preço

print("")

print(f" O preço total é de: {preco_total}")

print("")


while True:# Usamos esse while para repetir a varias vezes a forma de pagamento até a pessoa encerrar

    pagamento=int(input(" Qual é a formar de pagamento ?  1=convênio 15% , 2=Particular, 3=Cartão de credito acrécimo de 8% ="))# criamos essa variavel para escolher a formar de pagamento de 1 a 3

    match pagamento:# quando o usuario digitar o numero de 1 a 3, vai entrar no caso(case), cada caso(case) executa algo.

        case 1:# Mostra o preço total com o plano do convenio
            print("")

            print("convênio")

            print("")

            valor_com_desconto= preco_total * 0.15

            preco_final= preco_total - valor_com_desconto

            print("")

            print(f" O valor do desconto é de: {valor_com_desconto}")

            print("")

            print(f" O valor a ser pago é de: {preco_final}")

            break

        case 2:#Mostra o preço total com plano particular
            print("")

            print("Particular")

            print("")

            print(f" O valor a ser pago é de: {preco_total}")

            break

        case 3:# Mostra o preço total e o acrécimo do cartão de credito
            print("")

            print(" Cartão de credito")

            print("")

            valor_com_acrecimo= preco_total * 0.08

            preco_final= preco_total + valor_com_acrecimo

            print("")

            print(f" O valor a ser pago é de: {preco_final}")

            break

        case _:

            print("")
            print(" Digite a forma  de pagamento Novamente ")
            print("")

        







            



            
