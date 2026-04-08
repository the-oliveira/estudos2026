#Binary Search

'''
Cortar o problema na metade em cada etapa
Achar valores em uma lista ordenada ou existe uma "direção" nos dados do array

O(log n) tempo de execução


Premissa: 
    Criar um ponteiro no inicio e outro no final,
    Verifica a metade dividindo pela parte inteira (//)
    Se o valor no indice da metade for menor que o target:
        -Move o ponteiro do inicio para metade + 1
    Se o valor no indice da metade for maior que o target:
        -Move o ponteiro do final para metade - 1
    
    Depois divide novamente no meio e faz o mesmo processo até achar o target.
'''
#Exemplo:

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0                #Ponteiro do inicio
        right = len(nums) - 1   #Ponteiro do final

        while left <= right:    
            mid = (left + right) // 2   #Divisão inteira para pegar a metade
            if nums[mid] == target: 
                return mid              #Se for o target retorna o indice
            elif nums[mid] > target:
                right = mid - 1         #Se for maior que o target, transforma o final na metade -1
            else:   
                left = mid + 1          #Se for menor que o target, transforma o inicio na metade +1
        
        return -1       #Se não encontrar retorna -1