def merge_sort(array):
    if len(array) == 1:
        return array
    
    mid_point = len(array)//2
    left = array[0:mid_point]
    right = array[mid_point:]
    
    return merge(merge_sort(left), merge_sort(right))


def merge(left, right):
    merge_array = []

    i = j = 0

    # AND condition means loop stop when an array reaches it end
    while(i < len(left) and j < len(right)):
        if (left[i] > right[j]):
            merge_array.append(right[j])
            j += 1
        elif (left[i] < right[j]):
            merge_array.append(left[i])
            i +=1
    # Add the remainding of the LEFT or RIGHT array (1 array has nothing since we reaches it end)
    merge_array.extend(left[i:])
    merge_array.extend(right[j:])

    return merge_array
   

a = [6,5,3,1,8,7,2,4,9]
b = merge_sort(a)
print(b)