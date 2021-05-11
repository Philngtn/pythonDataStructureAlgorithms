import timeit

# Global variable
cache = {}


def memorized_add_to_80(number):
    if number in cache:
        print("Remember")
        return cache[number]
    else:
        print("Calculated")
        cache[number] = (number + 80)
        return cache[number]
        

starttime = timeit.default_timer()

print(memorized_add_to_80(5))
print("The time difference is :", timeit.default_timer() - starttime)


starttime_1 = timeit.default_timer()
print(memorized_add_to_80(5))
print("The time difference is :", timeit.default_timer() - starttime_1)
