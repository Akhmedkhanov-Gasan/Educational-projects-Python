recipes = {
    "Эспрессо": {"coffee": 1},
    "Капучино": {"coffee": 1, "milk": 3},
    "Макиато": {"coffee": 2, "milk": 1},
    "Кофе по-венски": {"coffee": 1, "cream": 2},
    "Латте Макиато": {"coffee": 1, "milk": 2, "cream": 1},
    "Кон Панна": {"coffee": 1, "cream": 1}
}


def order(*args):
    for drink in args:
        if drink not in recipes:
            continue
        recipe = recipes[drink]
        if all(in_stock.get(k, 0) >= v for k, v in recipe.items()):
            for k, v in recipe.items():
                in_stock[k] -= v
            return drink
    return "К сожалению, не можем предложить Вам напиток"
Нач


in_stock = {"coffee": 4, "milk": 4, "cream": 0}
print(order("Капучино", "Макиато", "Эспрессо"))
print(order("Капучино", "Макиато", "Эспрессо"))
print(order("Капучино", "Макиато", "Эспрессо"))