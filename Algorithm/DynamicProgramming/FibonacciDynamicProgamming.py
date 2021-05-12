

count = 0 

def fibonacci(n): 
    global count 
    count += 1
   
    if (n < 2):
        return n
    return fibonacci(n-1) + fibonacci(n-2)


def fibonacciDynamic():
    cache = {}
    
    def fib(n):
        if n in cache:
            return cache[n]
        else:
            if n < 2:
                return n
            else:
                cache[n] = fib(n-1) + fib(n-2)
                return cache[n]

    return fib




print(fibonacci(7))
print(count)

refFibo = fibonacciDynamic()
print(refFibo(8))