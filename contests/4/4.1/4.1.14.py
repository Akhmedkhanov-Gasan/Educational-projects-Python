def can_eat(horse, other):
    (hx, hy), (ox, oy) = horse, other
    if (abs(hx - ox) == 1 and abs(hy - oy) == 2) or (abs(hx - ox) == 2 and abs(hy - oy) == 1):
        return True
    else:
        return False

result = can_eat((2, 1), (4, 2))
print(result)