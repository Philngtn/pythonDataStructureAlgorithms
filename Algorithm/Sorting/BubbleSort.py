def bubble_sort(array):
    count = len(array)

    while(count):
        for i in range(len(array) - 1) :
            if(array[i] < array[i+1]):
                temp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = temp
        count -= 1
        

        

a = [1,2,4,61,1,2,3]
bubble_sort(a)
print(a)
