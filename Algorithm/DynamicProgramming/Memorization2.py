import timeit

def memorized_add_to_80():
    cache = {}
    def returnFunc(number):
        delay = 1000000

        if number in cache:
            print("Remember")s
            return cache[number]
        else:
            print("Calculate")
            while(delay):
                delay -= 1
            cache[number] = number + 80
            return cache[number]
    
    return returnFunc

memorized = memorized_add_to_80()

starttime = timeit.default_timer()
print(memorized(5))
print("The time difference is :", timeit.default_timer() - starttime)


starttime = timeit.default_timer()
print(memorized(5))
print("The time difference is :", timeit.default_timer() - starttime)