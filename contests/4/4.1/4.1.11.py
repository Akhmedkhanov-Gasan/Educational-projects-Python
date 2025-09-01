def find_mountains(data):
    is_mountain = []
    for index, (left, middle, right) in enumerate(zip(data, data[1:], data[2:]), 2):
        if left < middle > right:
            is_mountain.append(index)
    return tuple(is_mountain)



result = find_mountains([5, 1, 10, 2, 3, 4, 3, 20])
print(result)