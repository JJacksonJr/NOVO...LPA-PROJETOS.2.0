import os 


os.system("cls")


def voto(Ano_nascimento):

    idade= 2026 - Ano_nascimento

    

    if idade >=18 and idade <=75:

        print(f" Com {idade} anos :  pode votar ")

    elif idade >75:

        print(f" Com {idade} anos Voto opcional")

    else:

        print(f" Com {idade} anos :  Não pode votar ")

        


        





#Programa principal
idade_sua=int(input(" Digite seu ano de nascimento  "))

voto(idade_sua)#ParÂmetro global que vai entar no local





