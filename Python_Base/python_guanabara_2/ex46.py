#Criar um jogo de Jokenpô
from random import randint
from time import sleep

pc_opt = ['pedra', 'papel', 'tesoura']
pc_escolha = pc_opt[randint(0,2)]

print('Vamos jogar Jokenpô!')
sleep(1)

p_escolha = str(input('Faça sua escolha [Pedra, Papel ou Tesoura]: ')).strip().lower()

while p_escolha not in ('pedra papel tesoura'):
    print('Escolha um valor válido...')
    sleep(1)
    p_escolha = str(input('Faça sua escolha [Pedra, Papel ou Tesoura]: ')).strip().lower()


print('Vamos lá!')
sleep(1)
print('Jo')
sleep(1)
print('Ken')
sleep(1)
print('Pô!')
sleep(1)

if p_escolha == 'pedra' and pc_escolha == 'pedra' or p_escolha == 'tesoura' and pc_escolha == 'tesoura' or p_escolha == 'papel' and pc_escolha == 'papel':
    sleep(1)
    print(f'Jogamos {pc_escolha.upper()} e ficamos no empate, bom jogo!')
elif p_escolha == 'pedra' and pc_escolha == 'tesoura' or p_escolha == 'tesoura' and pc_escolha == 'papel' or p_escolha == 'papel' and pc_escolha == 'pedra':
    sleep(1)
    print(f'Joguei {pc_escolha.upper()} e você {p_escolha.upper()}, você ganhou!')
    sleep(1)
    print('Parabéns!')
else:
    sleep(1)
    print(f'Joguei {pc_escolha.upper()} e você {p_escolha.upper()}, parece que ganhei!')
    sleep(1)
    print('Bom jogo!')