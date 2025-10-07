def grow(*numbers, **kwargs):
    base = list(numbers)
    inc = [0] * len(base)

    for key, val in kwargs.items():
        k = len(key)
        if k == 0:
            continue
        for idx, num in enumerate(base):
            if num % k == 0:
                inc[idx] += val

    return tuple(num + add for num, add in zip(base, inc))

result = grow(1, 2, 3, 4, 5, ab=7, dad=10)
print(result)
