class Interval:
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper

    def __str__(self):
        return f"({self.lower}, {self.upper})"
    def __repr__(self):
        return f"({self.lower}, {self.upper})"

    def __lt__(self, other):
        if isinstance(other, Interval):
            if self.lower != other.lower:
                return self.lower < other.lower
            else:
                return self.upper < other.upper
    
    def length(self):
        return self.upper - self.lower

    def contains(self, other):
        if isinstance(other, Interval):
            return self.lower <= other.lower and self.upper >= other.upper

    def __sub__(self, other):
        if isinstance(other, Interval):
            if intersection(self, other) == None:
                return self
            else:
                if self.contains(other):
                    if self.lower == other.lower:
                        return Interval(other.upper, self.upper)
                    elif self.upper == other.upper:
                        return Interval(self.lower, other.lower)
                    else:
                        return [Interval(self.lower, other.lower), Interval(other.upper, self.upper)]
                elif other.contains(self):
                    return None
                else:
                    if self < other:
                        return Interval(self.lower, other.lower)
                    else:
                        return Interval(other.upper, self.upper)

    def __rsub__(self, other):
        if isinstance(other, list):
            newIntv = []
            for intv in other:
                aux = intv - self
                if aux != None:
                    newIntv.append(aux)
            if len(newIntv) == 1:
                return newIntv[0]
            else:
                return newIntv

def intersection(intv1, intv2):
    if isinstance(intv1, Interval) and isinstance(intv2, Interval):
        intv1, intv2 = min(intv1, intv2), max(intv1, intv2)
        if intv1.upper <= intv2.lower:
            return None
        else:
            lower = min(intv1.upper, intv2.lower)
            upper = max(intv1.upper, intv2.lower)
            return Interval(lower, upper)

def union(intv1, intv2):
    if isinstance(intv1, Interval) and isinstance(intv2, Interval):
        if intersection(intv1, intv2) == None:
            lst = [intv1, intv2]
            lst.sort()
            return lst
        else:
            lower = min(intv1.lower, intv2.lower)
            upper = max(intv1.upper, intv2.upper)
            return Interval(lower, upper)
