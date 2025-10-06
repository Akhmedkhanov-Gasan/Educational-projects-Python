def make_matrix(size, value=0):
    if isinstance(size, tuple):
        m, n = size
    else:
        m = n = size
    return [
        [value for _ in range(m)]
        for _ in range(n)]


result = make_matrix((4, 2), 1)
print(result)