#Programa que leia um número inteiro e mostra na tela o seu sucessor e seu antecessor
numero = int(input('Digite um número: '))
antecessor = numero - 1
sucessor = numero + 1

print(f'O número {numero} vem depois do {antecessor} e antes do {sucessor}')