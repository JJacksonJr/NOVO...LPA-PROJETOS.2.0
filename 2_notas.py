import os 

os.system("cls")


def media(n1,n2):

    media_do_aluno= (n1 + n2 ) / 2

    return media_do_aluno






nota_1=int(input("Digite sua primeira nota"))

nota_2=int(input(" Digite sua segunda nota "))


resultado=media(nota_1,nota_2)


print(f"{resultado}")