def fragments(numbers):
    result = []
    cur = [numbers[0]]

    for x in numbers[1:]:
        if x > cur[-1]:
            cur.append(x)
        else:
            result.append(cur)
            cur = [x]
    result.append(cur)
    return result


result = fragments([-4, -2, 5, 0, 3, 7, -8, -2, 6, 7, 6, 8, 10, 5, 7, 8])
print(result)