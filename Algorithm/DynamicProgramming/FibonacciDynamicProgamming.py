

count = 0 

def fibonacci(n): 
    global count 
    count += 1
   
    if (n < 2):
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(7))
print(count)