import math

class Racional:
    def __init__(self, numerador, denominador):
        g = math.gcd(numerador, denominador)
        self.numerador = numerador // g
        self.denominador = denominador // g

    def __str__(self):
        return "{} / {}".format(self.numerador, self.denominador)

    def calc(self):
        return self.numerador / self.denominador

    def __add__(self, other):
        if type(other) == Racional:
            return Racional(self.numerador * other.denominador + other.numerador * self.denominador, self.denominador * other.denominador)
        elif type(other) == int:
            return self + Racional(other, 1)

    def __sub__(self, other):
        if type(other) == Racional:
            return Racional(self.numerador * other.denominador - other.numerador * self.denominador, self.denominador * other.denominador)
        elif type(other) == int:
            return self - Racional(other, 1)

    def __mul__(self, other):
        if type(other) == Racional:
            return Racional(self.numerador * other.numerador, self.denominador * other.denominador)
        elif type(other) == int:
            return self * Racional(other, 1)

    def __truediv__(self, other):
        if type(other) == Racional:
            return self * Racional(other.denominador, other.numerador)
        elif type(other) == int:
            return Racional(self.numerador, self.denominador * other)


    def __eq__(self, other):
        if type(other) == Racional:
            return self.numerador == other.numerador and self.denominador == other.denominador
        elif type(other) == int:
            if self.denominador != 1:
                return False
            else:
                return self.numerador == other