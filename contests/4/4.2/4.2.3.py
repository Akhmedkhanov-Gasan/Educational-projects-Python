def euclid(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def gcd(*numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result = euclid(result, num)
    return result

result = gcd(3)
print(result)
