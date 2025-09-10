import numpy as np

array_a = np.array([[1,2,3],[4,5,6],[7,8,9]])
array_b = np.array([[2,2,2],[3,4,5],[6,7,8]])

# single array operations
# print(array_a.sum(axis=1))
# print(array_a.cumsum())
# print(array_a.prod())
# print(array_a.cumprod())

# two array math
# print(array_a + array_b)
# print(array_a - array_b)
# print(array_a * array_b)
# print(array_a / array_b)

# print(np.dot(array_a, array_b))

print(array_a)
print(array_b)

print(array_a.sum(axis=0))

print(np.ptp(array_a, axis=1))

print(array_a.mean())

#power
print(np.power(array_a, array_b))
