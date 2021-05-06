def quick_sort(array):
    left = 0
    right = len(array) - 1
    _qs(array, left, right)


def _swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp


def _qs(array, left, right):
    # Where to top the array for sorting
    index = _partition(array, left, right)
    # 
    if (left < index - 1):
        _qs(array, left, index -1 )
    if (index < right):
        _qs(array, index, right)

def _partition(array, left, right):
    i = left
    j = right
    pivot = array[(left + right) // 2]

    # When start crosses end stop (it divides the 2 half where left is smaller and right is bigger than pivot)
    while (i <= j):
        while(array[i] < pivot):
            i+=1
        while(array[j] > pivot):
            j-=1  
        # when array[i] >= pivot >= array[j] -> swap
        # the condition of check in range
        if (i <= j):
            _swap(array, i, j)
            i+=1
            j-=1
    # Return the point to chop the array
    return i


numbers = [0,0,1,2,2,1,0,1,2,2,1,0,1,1]

print(numbers)
quick_sort(numbers)
print(numbers)