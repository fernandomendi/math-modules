from monomial import Monomial
import math

class Polynomial:
    def __init__(self, l):
        if isinstance(l[0], int):
            self.coefs = l
            self.degree = len(self.coefs) - 1
            self.monomials = []
            for i in range(self.degree + 1):
                self.monomials.append(Monomial(self.coefs[i], i))
        elif isinstance(l[0], Monomial):
            l.sort(key = lambda mon: mon.degree)
            self.monomials = l
            self.degree = len(self.monomials) - 1

    def __str__(self):
        pol = ""
        for mon in self.monomials:
            if str(mon) != "":
                pol += "{} + ".format(mon)
        return pol[:-3]

    def evaluate(self, x):
        eval = 0
        for mon in self.monomials:
            eval += mon.evaluate(x)
        return eval

    def hasDegree(self, n):
        for mon in self.monomials:
            if mon.degree == n:
                return True
        return False

    def __add__(self, other):
        mons = self.monomials[:]
        if isinstance(other, Polynomial):
            for jmon in other.monomials:
                if self.hasDegree(jmon.degree):
                    for imon in self.monomials:
                        if jmon.degree == imon.degree:
                            mons.remove(imon)
                            mons.append(jmon + imon)
                else:
                    mons.append(jmon)
        if isinstance(other, Monomial):
            if self.hasDegree(other.degree):
                for imon in self.monomials:
                    if other.degree == imon.degree:
                        mons.remove(imon)
                        mons.append(other + imon)
            else:
                mons.append(jmon)
        if isinstance(other, int):
            if self.hasDegree(0):
                for imon in self.monomials:
                    if 0 == imon.degree:
                        mons.remove(imon)
                        mons.append(other + imon)
            else:
                mons.append(jmon)
        return Polynomial(mons)
            
    def roots(self):
        if self.degree == 0:
            return []
        elif self.degree == 1:
            a = self.monomials[0].coef
            b = self.monomials[1].coef
            return -b/a
        elif self.degree == 2:
            a = self.monomials[0].coef
            b = self.monomials[1].coef
            c = self.monomials[2].coef
            disc = b**2 - 4*a*c
            if disc > 0:
                return [(-b + math.sqrt(disc))/(2*a), (-b - math.sqrt(disc))/(2*a)]
            elif disc == 0:
                return [-b/2]
            else:
                return []
        else:
            raise Exception("No method to calculate roots of a polynomial of degree {}.".format(self.degree))



p = Polynomial([3,0,-1])
print(p)
print(p.roots())
p1 = Polynomial([Monomial(2,3), Monomial(2,0)])
print(p1)
print(p+p1+Monomial(1,1))

