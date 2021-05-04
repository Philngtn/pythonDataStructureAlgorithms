def insertion_sort(array):

    result = []
    result.append(array[0])

    for i in range(1,len(array)):
        for j in range(len(result)):
            if (array[i] < result[j]):
                result.insert(j,array[i])
                break
            elif(array[i] > result[-1]):
                result.append(array[i])
                break

    return result
                         

a = [6,5,3,1,8,7,2,4,4,2,115,14,54,12]
b = insertion_sort(a)
print(b)