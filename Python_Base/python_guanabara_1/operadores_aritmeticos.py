#Operadores Aritiméticos

#   + adição
#   - subtração
#   * multiplicação
#   / divisão
#   ** potencia
#   // divisão initeira
#   %  módulo (resto da divisão)
#   == igualdade


#Ordem de precedência:

#Prioridade 1 = parenteses ()
#Prioridade 2 = exponenciação **
#Prioridade 3 = Multiplicação, divisão, divisão inteira e resto (*, /, //, %) -> Prioriza o que vem primeiro
#Prioridade 4 = Soma e subtração (+ e -)

pessoa = 'Jorge'
print(f'Salve {pessoa:.^20}')

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

print(f'A soma de {n1} + {n2} = {n1+n2}')
print(f'Subtraindo {n1} - {n2} = {n1-n2}')
print(f'Multiplicando temos {n1} x {n2} = {n1 * n2}')
print(f'Dividindo temos {n1} / {n2} = {n1 / n2:.3}')

#   /n no meio da string joga o que vem depois para linha de baixo
#   end = '' para o print abaixo ficar na mesma linha