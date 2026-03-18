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


def move_zeros(nums):
    insert_pos = 0
    for i in nums:
        if i != 0:
            nums[insert_pos] = i
            insert_pos += 1

    for i in range(insert_pos, len(nums)):
        nums[i] = 0
    return nums


def two_sum_II(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        current_sum = nums[right] + nums[left]

        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return -1


def remove_duplicates(nums):
    if not nums:
        return 0

    slow = 0

    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]

    return slow + 1


def is_anagram(s, t):
    if len(s) != len(t):
        return False

    letters = {}

    for i in s:
        if i not in letters:
            letters[i] = 1
        else:
            letters[i] += 1

    for i in t:
        if i not in letters:
            return False
        letters[i] -=1

        if letters[i] < 0:
            return False

    return True


def first_non_repeating_word(text):
    words = text.split()
    count = {}
    for i in words:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1
    for i in words:
        if count[i] == 1:
            return i
    return None


def has_duplicates(nums):

    seen = {}
    for i in nums:
        if i in seen:
            return True
        else:
            seen[i] = 1
    return False


def group_anagram(words):
    sorted_words = {}

    for i in words:
        if tuple(sorted(i)) not in sorted_words:
            sorted_words[tuple(sorted(i))] = []
            sorted_words[tuple(sorted(i))].append(i)
        else:
            sorted_words[tuple(sorted(i))].append(i)
    return list(sorted_words.values())


def create_dict(x):
    outer = {}
    for i in x:
        if i.isalpha() and i.lower() in outer:
            outer[i.lower()] += 1
        elif i.isalpha() and i.lower() not in outer:
            outer[i.lower()] = 1
    return outer
