money = [1, 5, 200, 0.5, 0.05, 10, 25, 1000, 5000, 1, 2, 100, 0.1, 5, 2000, 0.01]

def take_small(x):
    y = []
    for i in x:
        if i < 100:
            y.append(i)
    return y

print(take_small(money))