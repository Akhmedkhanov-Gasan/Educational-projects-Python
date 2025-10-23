print(dict(filter(
    lambda x: isinstance(x[1], list) and any(isinstance(n, int) and n % 2 == 0 for n in x[1]),
    {'first': 2, 'second': '2 + 2 = 4', 'third': [1, 2, 3]}.items()
)))