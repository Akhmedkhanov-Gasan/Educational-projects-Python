def possible_triangulations(n):
    if n < 4:
        return "Not a valid polygon."

    def fact(x):
        res = 1
        for i in range(2, x + 1):
            res *= i
        return res

    return fact(2 * n - 4) // (fact(n - 2) * fact(n - 2)) // (n - 1)
