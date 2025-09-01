from itertools import product


def find_mountains(data):
    n = len(data)
    m = len(data[0]) if n else 0
    if n < 3 or m < 3:
        return tuple()

    result = []
    for i, j in product(range(1, n - 1), range(1, m - 1)):
        h = data[i][j]
        if all(
            (k == i and t == j) or h > data[k][t]
            for k, t in product(range(i - 1, i + 2), range(j - 1, j + 2))
        ):
            result.append((i + 1, j + 1))
    return tuple(result)
