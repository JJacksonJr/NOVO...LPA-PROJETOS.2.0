import os 

os.system("cls")



def calculando_notas(n1,n2):

    soma=n1+n2

    media= soma / 2

    return media,soma




def condicao(situacao):

    if situacao >=7:

        return "Aprovado"
    

    elif situacao >=5 and situacao <=6.9:

        return "Recuperação "
    
    elif situacao <=4.9:

        return "Reprovado"







nota_1=int(input("Digite sua primeira nota "))

nota_2=int(input("Digite sua segunda nota "))

media,soma=calculando_notas(nota_1,nota_2)

print(f"A soma total das notas é de: {soma}")
print(f"Media: {media}")


print(f"{condicao(media)}")