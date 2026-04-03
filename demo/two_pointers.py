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


def reverse(nums, left, right):
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return nums


def rotate(nums: list[int], k: int) -> None:
    k = k % len(nums)
    n = len(nums)
    reverse(nums, 0, n - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, n - 1)

nums = ([1,2,3,4,5,6,7])
rotate(nums, 3)
print(nums)
