def move_zeros_my(nums):
    current_dict = []
    nulls = []
    for index, number in enumerate(nums):
        if number == 0:
            nulls.append(0)
        else:
            current_dict.append(number)
    return current_dict + nulls


def counter():
    count = 0

    def inner():
        nonlocal count
        count += 1
        return count

    return inner

def is_palindrome(s):
    text = [ch.lower() for ch in s if ch.isalpha()]
    left = 0
    right = len(text) - 1

    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1

    return True


print(is_palindrome('Race car'))