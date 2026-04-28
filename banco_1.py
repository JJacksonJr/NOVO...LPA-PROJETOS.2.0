import os

os.system("cls")


def exibir_menu_banco():

    print("""
    BEM - VINDO AO BANCO SENAI DIGITAL 
    
    1. CRIAR USUÁRIO
    2. SALDO
    3. SACAR
    4. DEPOSITAR
    5. SAIR
          """)
    


def criando_usuario():

    global nome,senha,conta_do_usario

    nome=str(input("Digite seu nome ")).strip().lower()

    senha=int(input("Digite sua senha do banco "))

    conta_do_usario=int(input("Digite o número da sua conta "))



def saldo_do_usuario_banco(saldo):

    print(f"SEU SALDO  É DE: {saldo}")




def sacar_dinheiro(saldo,saque):

    saldo-=saque

    return saldo



def deposito_do_usuario(saldo,deposito):

    saldo+=deposito

    return saldo








def mostrando_resultados(usuario,conta,sacar,deposito,saldo):

    print("")
    print(f"USUÁRIO: {usuario}")
    print(f"CONTA: {conta}")
    print(f"SAQUE: {sacar}")
    print(f"DEPOSITO FEITO: {deposito}")
    print(f"SALDO ATUAL: {saldo}")
    
    print("ATÉ A PRÓXIMA ")







nome=""

senha=0

conta_do_usario=0


saldo_do_usuario=0


saque=0



depositar=0


while True:

    exibir_menu_banco()

    opcao=int(input("ESCOLHA UMA OPCÇÂO 1 A 5 ="))


    match opcao:

        case 1:

            print("")

            print("CRIE SEU USUÀRIO=")
            print("")
            criando_usuario()
            print("")
            print("=====USUÁRIO CRIADO=====")
            print("")
            print(f"!!!!!!SEJA BEM VINDO !!!!!! {nome}")

        case 2:
            print("")
            print("=====SALDO=====")
            print("")
            saldo_do_usuario_banco(saldo_do_usuario)
            print("")
            print("PRONTO")
           

        case 3:
            print("")

            print("==== SAQUE =====")
            print("")
            saque=float(input("QUAL É O VALOR DO SAQUE ?="))
            print("")
            if saque not in [100,50,25,10,5]:

                print("VALOR INVÁLIDO (use 100, 50, 25, 10 ou 5)")

            elif saque > saldo_do_usuario:

                print("O SAQUE NÃO PODE SER MAIOR QUE O SALDO ")

            else:

                saldo_do_usuario = sacar_dinheiro(saldo_do_usuario, saque)
                print("SAQUE REALIZADO")
        


            

        case 4:
            print("")

            print("==== DEPOSITAR =====")
            print("")
            depositar=float(input("QUAL VAI SER O VALOR DO DEPOSITO ?="))
            print("")
            saldo_do_usuario=deposito_do_usuario(saldo_do_usuario,depositar)
            print("")
            print("!!!!! DEPOSITO REALIZADO !!!!!")

        case 5:
            print("MOSTRANDO AS EXECUSSÕES !!!!!")
            mostrando_resultados(nome,conta_do_usario,saque,depositar,saldo_do_usuario)
            
        case _:
            print("DIGITE A OPÇÃO CORRETA ")
            