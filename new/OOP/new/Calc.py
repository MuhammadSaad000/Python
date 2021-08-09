from cmath import *


class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        return self.a / self.b

    def mod(self):
        return self.a % self.b

    def TakePower(self):
        return pow(self.a, self.b)

    def takeSquareRoot(self):
        return sqrt(self.a)

    def takeSin(self):
        return sin(self.a)

    def takeCos(self):
        return cos(self.a)

    def takeTan(self):
        return tan(self.a)
