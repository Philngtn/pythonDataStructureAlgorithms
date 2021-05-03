class Factorial:

    def __init__(self) -> None:
        pass

    def calculate(self, n):
        if (n == 1):
            return 1
        return n*self.calculate(n-1)


class Fibonacci:

    def __init__(self) -> None:
        pass
    
    def calculate_fibo(self,n):
        if (n == 0):
            return 0
        if (n == 1):
            return 1
        return self.calculate_fibo(n-1) + self.calculate_fibo(n-2) 


factorial = Factorial()
print(factorial.calculate(9))

fibonacci = Fibonacci()
print(fibonacci.calculate_fibo(12))

