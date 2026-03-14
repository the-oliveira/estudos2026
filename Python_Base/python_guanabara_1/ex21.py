#Sortear um dos alunos para apagar o quadro.
from random import randint
alunos = []

for n in range(0, 4):
    n = input('Digite o nome do aluno: ')
    alunos.append(n)
escolha = randint(0, 3)

print(f'O aluno escolhido para apagar a lousa é você, {alunos[escolha]}')
