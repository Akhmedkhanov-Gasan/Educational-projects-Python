def get_operator(operator):
    if operator == "+":
        return lambda a, b: a + b
    elif operator == "-":
        return lambda a, b: a - b
    elif operator == "*":
        return lambda a, b: a * b
    elif operator == "/":
        return lambda a, b: a / b
    elif operator == "//":
        return lambda a, b: a // b
    elif operator == "%":
        return lambda a, b: a % b
    elif operator == "**":
        return lambda a, b: a ** b


operator_power = get_operator("**")
print(operator_power(2, 10))