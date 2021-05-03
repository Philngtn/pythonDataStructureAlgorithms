def bubble_sort(array):
    count = len(array)

    while(count):
        for i in range(len(array) - 1) :
            if(array[i] < array[i+1]):
                temp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = temp
        count -= 1
        
def selection_sort(array):
    
    for i in range(len(array)):
        smallest = i
        for j in range(i,len(array)):
            if array[j] < array[smallest]:
                smallest = j

        temp = array[i]
        array[i] = array[smallest]
        array[smallest] = temp
        

a = [1,2,4,61,1,2,3]
b = [0,5,2,6,9,3,1,4,8,7]
bubble_sort(a)
print(a)
selection_sort(b)
print(b)