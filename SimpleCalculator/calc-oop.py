class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sum(self):
        return (self.num1 + self.num2)
    
calc1 = Calculator(23,9)
print(calc1.sum())