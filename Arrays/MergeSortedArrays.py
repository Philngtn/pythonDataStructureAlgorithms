# # # # # # # # # # # # # # # # # # # # # # # # 
# Python 3 data structure practice 
# Chap 1: Merge sort arrays
# Author : Phuc Nguyen (Philngtn)
# # # # # # # # # # # # # # # # # # # # # # # #

# mergign 2 sorted arrays, which is also sort

# [0,3,4,31], [4,6,30] => [0,3,4,4,6,30,31] 

# Easy implementation 
def merge_sorted_arrays(array1, array2):
    merged_array = []

    # Check input
    if (type(array1) is not list or type(array2) is not list):
        return "hummmm"

    if (len(array1) == 0 or len(array2) == 0):
        return  array1 + array2

    merged_array = array1 + array2
    # Need to be stand alone, cant return the *.sort() directly
    merged_array.sort()
    return merged_array
    
result_easy =  merge_sorted_arrays([0,3,4,31], [4,6,30])
print("Using build-in functions: " + result_easy)



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# In the Interview, we should anwser like this
# Raw processing 
def merge_sorted_arrays_2(array1, array2):
    merged_array = []
    i = 0
    j = 0
    
    # Check input
    if (type(array1) is not list or type(array2) is not list):
        return "hummmm"

    if (len(array1) == 0 or len(array2) == 0):
        return  array1 + array2


    # Use and, because one of two array will have an indicator (i,j) go 
    # beyond its existing value (END FIRST)
    while ( i < len(array1) and j < len(array2)):
        if (array1[i] <= array2[j]):
            merged_array.append(array1[i])
            i +=1
        else:
            merged_array.append(array2[j])
            j +=1
    #  Use [i:] or [j:] since the remain items, which are sorted, just append to the merged array
    return merged_array + array1[i:] + array2[j:]

result =  merge_sorted_arrays_2([0,3,4,31,32 ], [4,6,30])
print(result)
