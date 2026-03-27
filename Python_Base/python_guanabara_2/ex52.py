#Programa que lê o primeiro termo e a razão de uma progressão aritmética
#mostrar os 10 primeiros termos da progressão

p_termo = int(input('Termo da PA: '))
p_razao = int(input('Razão da PA: '))
decimo = p_termo + (10-1) *p_razao

print('Os 10 primeiros termos da PA:')

for n in range(p_termo, decimo + p_razao, p_razao):
    print(n, end=' -> ')
print('FIM!')