# # # # # # # # # # # # # # # # # # # # # # # # 
# Python 3 data structure practice 
# Chap 1: Merge sort arrays
# Author : Phuc Nguyen (Philngtn)
# # # # # # # # # # # # # # # # # # # # # # # #

# mergign 2 sorted arrays, which is also sort
# [0,3,4,31], [4,6,30] => [0,3,4,4,6,30,31] 

def merge_sorted_arrays(array1, array2):
    merged_array = []

    # Check input
    if (type(array1) is not list or type(array2) is not list):
        return "hummmm"

    if (len(array1) == 0):
        return array2
    if (len(array2) == 0):
        return array1
    if (len(array1) and len(array2) == 0):
        return merged_array

    merged_array = array1 + array2
    merged_array.sort()
    return merged_array
    

    

result =  merge_sorted_arrays([0,3,4,31], [4,6,30])
print(result)