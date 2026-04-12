import os
os.system("cls")

def jogador(nome, gol):
    return f"O jogador {nome} fez {gol} gols no campeonato"

r1 = input("Digite seu nome jogador: ").strip()
r2 = int(input("Digite a quantidade de gols: "))

print(jogador(r1, r2))


