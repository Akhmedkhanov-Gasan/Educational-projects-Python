def is_palindrome(x):
    if isinstance(x, str):
        t = ''.join(x.lower().split())
        if t == t[::-1]:
            return True
        else:
            return False
    elif isinstance(x, int):
        t = str(x)
        if t == t[::-1]:
            return True
        else:
            return False
    elif isinstance(x, (list, tuple)):
        if x == x[::-1]:
            return True
        else:
            return False


result = is_palindrome([1, 2, 1, 2, 1])
print(result)
