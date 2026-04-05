import os 

os.system("cls")


lista_De_10_notas_da_turma=[]

media=0

qtd_de_aluno_acima_da_media=0

posicao_da_maior_nota=[]

soma=0

for i in range(0,10):
    notas=int(input(" Digite uma nota "))

    lista_De_10_notas_da_turma.append(notas)

maior=max(lista_De_10_notas_da_turma)

soma=sum(lista_De_10_notas_da_turma)

media= soma / 10



for i in range(len(lista_De_10_notas_da_turma)):

    if lista_De_10_notas_da_turma[i] == maior:
        posicao_da_maior_nota.append(i)


    if lista_De_10_notas_da_turma[i] > media:
        qtd_de_aluno_acima_da_media+=1


print(f" A Soma total das notas é de: {soma}")
print(f" A média da turma é de : {media}")
print(f" A quantidade de alunos acima da média é de: {qtd_de_aluno_acima_da_media}")
print(f" A maior nota digitada foi de : {maior}")
print(f" A posição da maior nota é de {posicao_da_maior_nota}")