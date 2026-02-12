def clone_matrix(matrix: list[list[int]]) -> list[list[int]]:
    x = []
    for row in matrix:
        x.append(row[:])
    return x

m1 = [[1, 2], [3, 4]]
m2 = clone_matrix(m1)

m2[0].append(99)

print(m1)
print(m2)
