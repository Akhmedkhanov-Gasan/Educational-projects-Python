def to_rim(x):
    rim = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I',
    }
    result = []
    for k, v in rim.items():
        while x >= k:
            result.append(v)
            x -= k
    return ''.join(result)

def roman(x, y):
    result = x + y
    return f'{to_rim(x)} + {to_rim(y)} = {to_rim(result)}'
result = roman(1499, 2500)
print(result)