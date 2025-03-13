class Calculator:
    def _init_(self):
        self.operations = {
            '+': self.add,
            '-': self.subtract,
            '*': self.multiply,
            '/': self.divide
        }

    def add(self, x, y):
            return x + y 

    def subtract(self, x, y):
             return x - y

    def multiply(self, x, y):
            return x * y

    def divide(self, x, y):
             return x / y if y != 0 else 'Error: Division by zero'

        ## Test case

if __name__ == '__main__':
        Calculator = Calculator()
        ## Let add two numbers
        x, y = 10, 12
        print(f"The addition of {x} + {y} = {Calculator.add(x, y)}")
        print(f"The subtraction of {x} - {y} = {Calculator.subtract(x, y)}")
        print(f"The multiplication of {x} * {y} = {Calculator.multiply(x, y)}")
        print(f"The division of {x} / {y} = {Calculator.divide(x, y)}")