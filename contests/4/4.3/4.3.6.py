def merge(a, b):
    result = []
    i = j = 0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    result.extend(a[i:])
    result.extend(b[j:])
    return result


def merge_sort(x):
    if len(x) <= 1:
        return x

    mid = len(x) // 2
    left = merge_sort(x[:mid])
    right = merge_sort(x[mid:])
    return merge(left, right)

result = merge_sort([3, 2, 1])
print(result)