class Factorial:

    def __init__(self) -> None:
        pass

    def calculate(self, n):
        if (n == 1):
            return 1
        return n*self.calculate(n-1)


factorial = Factorial()
print(factorial.calculate(9))

