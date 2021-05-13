import timeit

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




refFibo = fibonacciDynamic()

# print(count)

starttime = timeit.default_timer()
print(fibonacci(30))
print("The time of normal Fibo is :", timeit.default_timer() - starttime)

starttime = timeit.default_timer()
print(refFibo(30))
print("The time of dynamic Fibo is :", timeit.default_timer() - starttime)


