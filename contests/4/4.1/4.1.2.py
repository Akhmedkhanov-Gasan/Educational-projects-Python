def gcd(a, b):
    big = max(a, b)
    small = min(a, b)

    while True:
        prev = big % small
        if big % small == 0:
            return small
        else:
            big = small
            small = prev

print(gcd(144, 96))
