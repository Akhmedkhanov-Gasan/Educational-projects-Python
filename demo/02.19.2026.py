from typing import Any, Generator


def two_sum(nums, target):
    seen = {}
    for key, value in enumerate(nums):
        need = target - value
        if need in seen:
            return [seen[need], key]
        else:
            seen[value] = key
    return False

def doubled(nums):
    new_list = [x * 2 for x in nums]
    print(nums)
    return new_list
