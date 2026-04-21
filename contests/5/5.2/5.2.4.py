from math import gcd


class Fraction:

    def __init__(self, *args):
        if len(args) == 2:
            num = args[0]
            den = args[1]
        elif len(args) == 1:
            num_str, den_str = args[0].split('/')
            num = int(num_str)
            den = int(den_str)
        else:
            raise ValueError("Invalid arguments")

        self._numerator = num
        self._denominator = den
        self._reduce()

    def __str__(self):
        return f"{self._numerator}/{self._denominator}"

    def __repr__(self):
        return f"Fraction('{self._numerator}/{self._denominator}')"

    def __neg__(self):
        return Fraction(-self._numerator, self._denominator)

    def __add__(self, other):
        new_num = (self._numerator * other._denominator) + (other._numerator * self._denominator)
        new_den = self._denominator * other._denominator
        return Fraction(new_num, new_den)

    def __sub__(self, other):
        new_num = (self._numerator * other._denominator) - (other._numerator * self._denominator)
        new_den = self._denominator * other._denominator
        return Fraction(new_num, new_den)

    def __iadd__(self, other):
        self._numerator = (self._numerator * other._denominator) + (other._numerator * self._denominator)
        self._denominator = self._denominator * other._denominator
        self._reduce()
        return self

    def __isub__(self, other):
        self._numerator = (self._numerator * other._denominator) - (other._numerator * self._denominator)
        self._denominator = self._denominator * other._denominator
        self._reduce()
        return self

    def __mul__(self, other):
        new_num = self._numerator * other._numerator
        new_den = self._denominator * other._denominator
        return Fraction(new_num, new_den)

    def __imul__(self, other):
        self._numerator = self._numerator * other._numerator
        self._denominator = self._denominator * other._denominator
        self._reduce()
        return self

    def __truediv__(self, other):
        new = self * other.reverse()
        return new

    def __itruediv__(self, other):
        new = self * other.reverse()
        self._numerator = new._numerator
        self._denominator = new._denominator
        self._reduce()
        return self

    def reverse(self):
        new_num = self._denominator
        new_den = self._numerator
        return Fraction(new_num, new_den)

    def _reduce(self):
        g = gcd(self._numerator, self._denominator)
        self._numerator //= g
        self._denominator //= g
        if self._denominator < 0:
            self._numerator *= -1
            self._denominator *= -1

    def numerator(self, value=None):
        if value is None:
            return abs(self._numerator)
        else:
            self._numerator = value
            self._reduce()

    def denominator(self, value=None):
        if value is None:
            return abs(self._denominator)
        else:
            self._denominator = value
            self._reduce()


a = Fraction(1, 3)
c = b = Fraction(2, 1).reverse()
b /= a
print(a, b, c, b is c)
