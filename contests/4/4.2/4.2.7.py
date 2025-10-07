def get_formatter(sep=' ', end=''):
    return lambda *args : sep.join(map(str, args)) + end


formatter = get_formatter(end="!", sep=", ")
print(formatter("Hello", "world"))