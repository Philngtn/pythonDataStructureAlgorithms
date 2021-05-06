a = [2,54,213,24,42,1,7]



def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp


print(a)
swap(a, 1,2)
print(a)