#Programa que leia 3 números e dirá o maior e o menor
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
maior = n2 if n2 > n3 and n2 > n1 else n3 or n3 if n3 > n2 and n3 > n1 else n1
menor = n2 if n2 < n3 and n2 < n1 else n3 or n3 if n3 < n2 and n3 < n1 else n1

print(f'''
    O maior número é o {maior}
    O menor número é o {menor}
''')
