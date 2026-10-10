class MyClass:

    def addition(self, x, y):
        return x + y

    def subtraction(self, x, y):
        return x - y

    def divide(self, x, y):
        if y == 0:
            raise ZeroDivisionError("Can't divide with zero")
        return x / y
    