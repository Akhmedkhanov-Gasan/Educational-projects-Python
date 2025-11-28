def cycle(x):
    while True:
        for i in x:
            yield i

print(*(x for _, x in zip(range(5), cycle([1, 2, 3]))))