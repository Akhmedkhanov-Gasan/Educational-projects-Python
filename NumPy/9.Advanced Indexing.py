import numpy as np

# row_1 = [1, 2, 3, 4, 5]
# row_2 = [6, 7, 8, 9, 10]
# row_3 = [11, 12, 13, 14, 15]
# row_4 = [16, 17, 18, 19, 20]
# row_5 = [21, 22, 23, 24, 25]

# test_data = np.array([row_1, row_2, row_3, row_4, row_5])
# # print(test_data)
#
# print(test_data[:, 2:4:1])

# print(test_data[:, -2:-4:-1])

# greater_than_five = test_data > 5
# print(greater_than_five)
# print(test_data[greater_than_five])

# drop_under_5_array = np.where(test_data > 5, test_data, 0)
# print(drop_under_5_array)


# drop_under_5_and_over_20 = np.logical_and(test_data>5, test_data<20)
# print(drop_under_5_and_over_20)
# print(test_data[drop_under_5_and_over_20])



array_a = np.arange(0, 100, 5)
# print(array_a)
# print(array_a.size)
array_a_reshape = array_a.reshape(4,5)
print(array_a_reshape)
#
# print(array_a_reshape[:,-1])
#
# array_a_above_50 = array_a_reshape[array_a_reshape > 50]
# print(array_a_above_50)
#
# print(array_a_above_50[0:len(array_a_above_50):2])
#
# print(array_a_reshape[:, 0:5:2])
#
# print(np.where(array_a_reshape>50, array_a_reshape, -1))

# print(array_a_reshape[:,-1:-4:-1])
print(np.where((array_a_reshape > 20)&(array_a_reshape < 70), array_a_reshape, 0))
