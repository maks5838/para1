def add(self, x, y):
    return x + y


def subtract(self, x, y):
    return x - y


def multiply(self, x, y):
    return x * y


def divide(self, x, y):
    if y == 0:
        return "Ділення на нуль неможливе"
    else:
        return x / y
    calculator_1 = calculator()
    print("Сума:", calc.add(4+3))
    print("Різниця:", calc.subtract(10-4))
    print("Добуток:", calc.multiply(2*6))
    print("Частка:", calc.divide(8/2))