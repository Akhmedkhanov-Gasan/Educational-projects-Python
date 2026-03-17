def move_zeros_my(nums):
    current_dict = []
    nulls = []
    for index, number in enumerate(nums):
        if number == 0:
            nulls.append(0)
        else:
            current_dict.append(number)
    return current_dict + nulls

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

