#Two pointers - anotações

'''
Padrão para solucionar estruturas lineares(array, strings)

Criar 2 ponteiros, um no inicio e outro no final, para evitar loop dentro de loop

- Existem 2 tipos:
    -Ponteiros movendo na mesma direção (começando no inicio)
        Serve para encontrar ciclos de repetição e a metade da lista
        Um ponteiro se move mais rapido que o outro

    -Ponteiros opostos (um no inicio, um no fim)
        Serve para encontrar palindromos, encontrar pares e listas ordenadas

        Os ponteiros se movem baseado em condicionais(comparações)


Problemas mais comuns que da para usar Two Pointers:
    Palindromos
    Reversals
    Merging sorted data
    "K" sized comparisons

Se existe uma lógica em ler uma array apenas uma vez e apontar para o inicio e fim
Então o algoritmo de Two Pointers pode ser usado para resolver o problema.







'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        start_pointer = 0
        end_pointer = len(s) - 1
        s = s.lower()

        while start_pointer < end_pointer:
            if s[start_pointer] == ' ' or s[start_pointer].isalnum() == False:
                start_pointer += 1
            elif s[end_pointer] == ' ' or s[end_pointer].isalnum() == False:
                end_pointer -= 1
            elif s[start_pointer] != s[end_pointer]:
                return False
            else:
                start_pointer += 1
                end_pointer -= 1
    
        return True
    
#Linked lists:

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast and  fast.next:
            fast = fast.next.next
            slow = slow.next
            
        return slow

