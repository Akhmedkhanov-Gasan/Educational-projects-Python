def to_string(*args, sep=' ', end='\n'):
    return sep.join(map(str, args)) + end


# result = to_string(1, 2, 3)
# print(result)


data = [7, 3, 1, "hello", (1, 2, 3)]
result = to_string(*data, sep=", ", end="!")
print(result)