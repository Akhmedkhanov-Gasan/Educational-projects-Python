def create_dict(x):
    outer = {}
    for i in x:
        if i.isalpha() and i.lower() in outer:
            outer[i.lower()] += 1
        elif i.isalpha() and i.lower() not in outer:
            outer[i.lower()] = 1
    return outer

def valid_anagram(s, t):
    first = create_dict(s)
    second = create_dict(t)
    return first == second

def first_unique_char(s):
    target = create_dict(s)
    for i in range(len(s)):
        if target[s[i].lower()] == 1:
            return i
    return -1

print(first_unique_char('Swiss'))
