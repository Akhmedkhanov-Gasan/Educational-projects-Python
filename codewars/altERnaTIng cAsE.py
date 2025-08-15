def to_alternating_case(string):
    new_string = ""
    for i in string:
        if i.islower():
            new_string += i.upper()
        elif i.isupper():
            new_string += i.lower()
        else:
            new_string += i
    return new_string

print(to_alternating_case("hello world"))
