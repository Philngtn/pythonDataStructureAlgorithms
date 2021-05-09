def qs(array, left, right):

    pivot = partition(array, left, right)
    if left < pivot - 1:
        qs(array,left, pivot-1) 
    if right > pivot: 
        qs(array,pivot, right)
    
def partition(array, left, right):
    pivot = array[(left + right)//2]

    i = left
    j = right

    while (i <= j):
        while (array[i] < pivot):
            i += 1
        while (array[j] > pivot):
            j -= 1
        if (i <= j):
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
            i += 1
            j -= 1
    return i


numbers = [0,0,1,2,2,1,0,1,2,2,1,0,1,1]

print(numbers)
qs(numbers,0, len(numbers) - 1)
print(numbers)