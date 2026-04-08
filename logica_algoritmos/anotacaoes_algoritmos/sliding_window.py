#Anotações do Algoritmo Sliding Window
'''
Semelhante ao Two Pointers, porém ao invés de 2 ponteiros, ele verifica um "range de valores" da lista

Resolve problemas de segmentos de texto (substrings), arrays (subarray), grupo de elementos consecutivos

Você move essa "janela" e deixa dentro dela apenas o trecho do código de x a y, podendo aumentar a range e ir deslizando para o lado como uma janela
Ou seja, você vê um trecho do input

Tempo de execução O(n)

Tem 2 tipos:

-> Fixed Window = O tamanho do range da janela mantém o mesmo enquanto percorre o input

    -Titulos de possiveis soluções: (Problemas onde o tamanho da janela, no caso K mantém o mesmo, você valida o que está nela e passa pra frente)
        Maximum avarage of any subarray of size K
        Sum of every k-length block
        subarray of length k with the largest/smallest X


-> Dynamic window = O Tamanho do range da janela vai aumentando ou diminuindo enquanto você verifica o input
    
    -Titulos de possiveis soluções:
        length of the longest substring with at most k unique characters
        smallest subarray with a sum greater than a target
        longest window where a certain rule is valid

'''

#Exemplo de Fixed window:

def findMaxAverage(self, nums: List[int], k: int) -> float:
    if not nums:
        return 0
    elif len(nums) == 1:
        return nums[0]

    n_sum = 0
    current_max_avg = 0
    left = 0
    
    for n in range(0, k):
        n_sum += nums[n]
    current_max_avg = n_sum / k

    for right in range(k, len(nums)):
        n_sum -= nums[left]
        n_sum += nums[right]
        left += 1

        current_max_avg = max(current_max_avg, (n_sum/k))
    
    return current_max_avg


#Exemplo de Flexible Window

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        
        ini_window = 0
        end_window = 0
        curr_sequence = list()
        max_sequence = 0

        while end_window < len(s):
            if s[end_window] not in curr_sequence:
                curr_sequence.append(s[end_window])
                end_window += 1

            else:
                max_sequence = max(max_sequence, len(curr_sequence))
                while s[end_window] in curr_sequence:
                    ini_window += 1
                    curr_sequence.remove(curr_sequence[0])
        
        max_sequence = max(max_sequence, len(curr_sequence))
        return max_sequence
