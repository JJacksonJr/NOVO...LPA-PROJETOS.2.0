import os 


os.system("cls")





def media_aluno(nota_do_aluno):

    soma_das_notas=sum(nota_do_aluno)

    tamanho= len(nota_do_aluno)

    media= soma_das_notas / tamanho

    return media,soma_das_notas








lista_3_notas=[]

for i in range(1,4,1):

    nota=int(input(f"Digite sua {i+0} nota "))

    lista_3_notas.append(nota)

media,soma=media_aluno(lista_3_notas)


print(f"soma das notas: {soma} e a média é de: {media}")