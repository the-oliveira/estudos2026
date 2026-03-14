#Sortear a ordem de apresentação dos 4 alunos.
from random import randint

alunos = []
ordem_alunos = {}
posicao = 0

for aluno in range(0, 4):
    aluno = input('Digite o nome do aluno: ')
    alunos.append(aluno)

for a in alunos:
    if a not in ordem_alunos.values():
        posicao = randint(1, 4)
        while posicao in ordem_alunos.keys():
            posicao = randint(1, 4)
        ordem_alunos[posicao] = a

print(f'A ordem de apresentação é: {ordem_alunos[1]}, {ordem_alunos[2]}, {ordem_alunos[3]}, {ordem_alunos[4]}')