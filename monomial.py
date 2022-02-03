class Monomial:
    def __init__(self, coef, degree):
        self.coef = coef
        self.degree = degree

    def __str__(self):
        if self.coef == 1:
            if self.degree == 0:
                sCoef = str(self.coef)
            else:
                sCoef = ""
        elif self.coef == 0:
            return ""
        else:
            sCoef = str(self.coef)
        if self.degree == 1:
            sDegree = "x"
        elif self.degree == 0:
            sDegree = ""
        else:
            sDegree = "x^{}".format(self.degree)
        return sCoef + sDegree

    def evaluate(self, x):
        return self.coef * x ** self.degree

    def __add__(self, other):
        if isinstance(other, Monomial):
            return Monomial(self.coef + other.coef, self.degree)
        elif isinstance(other, int) and self.degree == 0:
            return Monomial(self.coef + other, 0)
    
    def __radd__(self, other):
        return self + other