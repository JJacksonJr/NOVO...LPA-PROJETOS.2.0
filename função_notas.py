import os 

os.system("cls")



def notas(*n):

    

    maior=max(n)

    menor=min(n)

    tamanho=len(n)

    media=sum(n)/tamanho

    return maior,menor,tamanho,media


   






res=notas(5.5,2.5,6.7)

print(res)