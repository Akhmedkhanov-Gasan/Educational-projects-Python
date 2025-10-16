DATA = []

def enter_results(*args):
    global DATA
    DATA += tuple(zip(args[::2], args[1::2]))

def get_sum():
    if not DATA:
        return 0.0, 0.0
    first = 0
    second = 0
    for x in DATA:
        first += x[0]
        second += x[1]
    return round(first, 2), round(second, 2)

def get_average():
    if not DATA:
        return 0.0, 0.0
    data_len = len(DATA)
    total_first, total_second = get_sum()
    avg_first = total_first / data_len
    avg_second = total_second / data_len
    return round(avg_first, 2), round(avg_second, 2)


enter_results(1, 2, 3, 4, 5, 6)
print(get_sum(), get_average())
enter_results(1, 2)
print(get_sum(), get_average())
