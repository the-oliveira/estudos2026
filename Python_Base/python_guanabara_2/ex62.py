#lê o primeiro termo e a razão de uma PA com os 10 primeiros termos
c = 10
primeiro_termo = int(input('Primeiro T1ermo da PA: '))
razao = int(input('Razao da PA: '))
termo = primeiro_termo

while c > 0:
    if c == 10:
        print(termo, end=' ')
    else:
        termo += razao
        print(termo, end=' ')

    c -= 1