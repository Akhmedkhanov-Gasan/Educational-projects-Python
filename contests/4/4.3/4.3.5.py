def result_accumulator(f):
    results = []

    def wrapper(*args, **kwargs):
        nonlocal results
        method = kwargs.get('method', 'accumulate')
        if method == 'accumulate':
            results.append(f(*args))
        elif method == 'drop':
            results.append(f(*args))
            accumulated = results[:]
            results = []
            return accumulated
        else:
            results.append(f(*args))

    return wrapper

@result_accumulator
def a_plus_b(a, b):
    return a + b


print(a_plus_b(3, 5, method="accumulate"))
print(a_plus_b(7, 9))
print(a_plus_b(-3, 5, method="drop"))
print(a_plus_b(1, -7))
print(a_plus_b(10, 35, method="drop"))

