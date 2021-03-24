# # # # # # # # # # # # # # # # # # # # # # # # 
# Python 3 data structure practice 
# Chap 1: Array Manipulation
# Author : Phuc Nguyen (Philngtn)
# # # # # # # # # # # # # # # # # # # # # # # #

# Reverse string
# 'Hi my name is Phil' -> 'lihP si eman ym iH'

import math


# Space O(2)
# Complexity O(n)

def reverse(str):
    # Check input
    temp_value = "" 
    str_length = len(str)

    if (str_length < 2):
        return str

    # Odd case
    if (str_length % 2 != 0):
        middle_index = math.ceil(str_length/2)
        for i in range(0, middle_index - 1):
            temp_value = str[i]
            str[str_length - i - 1] = temp_value
        return str
    # Even case
    else:
        middle_index = int(str_length/2)
        for i in range(0, middle_index):
            temp_value = str[i] 
            str[i] = str[str_length - i - 1]
            str[str_length - i - 1] = temp_value 
        return str

vowel = ['h']
vowels = ['e', 'a', 'u', 'o', 'i','2']
tuples = {1,2,3}
# print(reverse(tuples))


# Faster one 

def reverse2(string):
    if type(string) is not str:
        return 'Not a string'
    if (len(string) < 2):
        return string
    
    reverse_string = []

    for i in range(1, len(string) + 1):
        # Read the array from the back to front -1 -> -n
        reverse_string.append(string[-i])
    return ''.join(reverse_string)

print(reverse2(vowels))
print(reverse2('Hi my name is Phil'))