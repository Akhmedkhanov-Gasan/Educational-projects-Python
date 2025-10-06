def make_list(length, value=0):
    list = []
    for i in range(length):
        list.append(value)
    return list

result = make_list(5, 1)
print(result)