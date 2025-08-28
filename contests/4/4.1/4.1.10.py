def split_numbers(text):
    out = tuple(int(x) for x in text.split())
    return out

result = split_numbers("1 -2 3 -4 5")
print(result)