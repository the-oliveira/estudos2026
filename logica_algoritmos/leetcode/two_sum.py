#Praticando algoritmos no Leetcode

nums = [2,7,11,15]
target = 9
magic_number = 0
final_resp = []
dict_values = {}

for p, n in enumerate(nums):
    magic_number = target - n
    if magic_number in dict_values.keys():
        final_resp = [dict_values[magic_number], p]
        print(final_resp)
    else:
        dict_values[n] = p
        
