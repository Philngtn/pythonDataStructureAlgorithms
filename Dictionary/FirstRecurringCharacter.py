def first_recurring_char(arr):
    # Declare an empty dictionary 
    map = {}
    
    # Set a counter for each unique value in the array  
    for i in arr:
        map[i] = 0
    # print(map)  
          
    # Start to count until the first one get count = 2
    for i in arr:
        map[i] = map[i] + 1
        # print(map)
        if (map[i] > 1):
            return i

    # Time complexity O(2n)
    # Space complexity O(n)
    
    return None

array1 = [2,5,1,2,3,5,1,2,4]
array2 = [2,1,1,2,3,4,2,6,4]
array3 = [2,3,4,5]
print(first_recurring_char(array1))

