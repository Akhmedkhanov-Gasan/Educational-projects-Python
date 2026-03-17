def clone_matrix(matrix: list[list[int]]) -> list[list[int]]:
    x = []
    for row in matrix:
        x.append(row[:])
    return x

m1 = [[1, 2], [3, 4]]
m2 = clone_matrix(m1)

m2[0].append(99)

def max_consecutive_ones(nums):
    max_ones = 0
    current_count = 0
    for i in nums:
        if i == 1:
            current_count += 1
            max_ones = max(max_ones, current_count)
        else:
            current_count = 0
    return max_ones

def counter():
    count = 0

    def inner():
        nonlocal count
        count += 1
        return count

    return inner


def log_calls(func):

    def inner(*args, **kwargs):
        print(func.__name__)
        return func(*args, **kwargs)
    return inner


@log_calls
def add(a, b):
    return a + b

@log_calls
def greet(name):
    print("Hello", name)

print(add(2, 3))
greet('fuck')


