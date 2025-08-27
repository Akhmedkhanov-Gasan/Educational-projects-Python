result  = 0


def max2D(x):
    global result
    for i in x:
        if max(i) > result:
            result = max(i)
    return result


result = max2D([[-5, -43, 72, 89], [-40, 92, -1, -73], [30, -75, 23, 94]])

print(f'result = {result}')