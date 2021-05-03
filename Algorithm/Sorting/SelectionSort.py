def selection_sort(array):
    
    for i in range(len(array)):
        smallest = i
        for j in range(i,len(array)):
            if array[j] < array[smallest]:
                smallest = j

        temp = array[i]
        array[i] = array[smallest]
        array[smallest] = temp

b = [0,5,2,6,9,3,1,4,8,7]

selection_sort(b)
print(b)