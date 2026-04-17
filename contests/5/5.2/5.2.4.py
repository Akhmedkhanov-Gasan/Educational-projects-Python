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

