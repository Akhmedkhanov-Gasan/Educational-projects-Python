print(dict(map(
    lambda x: (
        ''.join(c for c in x[0] if c.isalpha()).lower(),
        sum(x[1]) if isinstance(x[1], (list, tuple))
                     and all(isinstance(n, (int, float)) for n in x[1])
        else x[1]
    ),{'First 1': 2, 'second:': (2, 1, 1), 'THIRD': [1, 2, 3]}.items()
)))