def merge(left, right):
    new_list = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            new_list.append(left[i])
            i += 1
        else:
            new_list.append(right[j])
            j += 1

    new_list.extend(left[i:])
    new_list.extend(right[j:])

    return tuple(new_list)

result = merge((1, 2), (3, 4, 5))
print(result)