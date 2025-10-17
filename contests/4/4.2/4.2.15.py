def get_repeater(func, count):
    def repeater(x):
        res = x
        for _ in range(count):
            res = func(res)
        return res
    return repeater



repeater = get_repeater(lambda x: x + 1, 5)
print(repeater(2))

repeater = get_repeater(lambda x: x * 2, 10)
print(repeater(1))