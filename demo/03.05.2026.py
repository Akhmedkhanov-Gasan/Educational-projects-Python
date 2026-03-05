def two_sum_dumb(nums, target):
    for i in nums:
        for j in nums:
            if i + j == target:
                return i, j
    return None


def two_sum(nums, target):
    dict_sum = {}
    for index, value in enumerate(nums):
        if target - value in dict_sum:
            return dict_sum[target - value], index
        dict_sum[value] = index
    return None


def con_dup(nums):
    if len(nums) == len(set(nums)):
        return False
    return True

print(con_dup([1,2,3,1]))
