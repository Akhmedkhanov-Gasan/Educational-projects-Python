import numpy as np

# a = np.array([1, 2, 3])
# print(a)
# print(type(a))
#
# zeros = np.zeros(5)
# print(zeros)
#
# ones = np.ones((2, 3))
# print(ones)
#
# full = np.full((2, 2), 7)
# print(full)
#
# ar = np.arange(0, 10, 2)
# print(ar)
#
# lin = np.linspace(0,10, 5)
# print(lin)

# test = np.linspace(0, 1, 5, endpoint=False)
# print(test)

# test_2 = np.linspace(10, 20, 7)
# print(test_2)
#
# test_3 = np.arange(0, 1, 0.1)
# print(test_3)
#
# test_4 = np.full((2, 4), -5)
# print(test_4)

# arr = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr.shape)
# print(arr.ndim)
# print(arr.size)
# print(arr.dtype)

# arr = np.array([10, 20, 30, 40, 50])
# print(arr[0])
# print(arr[-1])
# print(arr[1:4])

mat = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]])
# print(mat[:,1])
# print(mat[0:2, :-1])
# print(mat[0:2, 0:2])
# print(mat[:, 0])
# print(mat[::-1])
# print(mat[:-1:])
# print(mat[range(3), range(3)])
# print(mat[[0, 2], [1, 0]] )
# print(mat[[0,1,2], [2,1,0]])
print(mat[0:3:2, 0:3:2])
