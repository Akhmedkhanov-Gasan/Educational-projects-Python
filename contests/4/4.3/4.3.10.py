def make_linear(x):
    result = []
    for i in x:
        if isinstance(i, list):
            result.extend(make_linear(i))
        else:
            result.append(i)
    return result


result = make_linear([1, 2, [3]])
print(result)