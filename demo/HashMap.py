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
    return len(nums) == len(set(nums))


def valid_anagram(t, s):
    if len(t) != len(s):
        return False

    dict_let = {}

    for i in t:
        if i not in dict_let:
            dict_let[i] = 1
        else:
            dict_let[i] += 1

    for i in s:
        if i not in dict_let:
            return False
        dict_let[i] -= 1

        if dict_let[i] < 0:
            return False

    return True

def first_unique_char(s):
    count = {}
    for char in s:
        if char not in count:
            count[char] = 1
        else:
            count[char] += 1
    for index, char in enumerate(s):
        if count[char] == 1:
            return index

    return -1

def maj_elem(nums):
    m = len(nums)
    count = {}
    for char in nums:
        if char not in count:
            count[char] = 1
        else:
            count[char] += 1
    for num, freq in count.items():
        if freq > m/2:
            return num

    return -1

