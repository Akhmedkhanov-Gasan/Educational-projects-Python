def longest_unique_substring(s: str):
    last_pos = {}
    left = 0
    best = 0
    for right, ch in enumerate(s):
        if ch in last_pos and last_pos[ch] >= left:
            left = last_pos[ch] + 1
        last_pos[ch] = right
        best = max(best, right - left + 1)
    return best

def min_subarray_len(nums, target):
    left = 0
    current_sum = 0
    best = float("inf")

    for right in range(len(nums)):
        current_sum += nums[right]
        while current_sum >= target:
            best = min(best, right - left + 1)
            current_sum -= nums[left]
            left += 1

    return 0 if best == float("inf") else best

def sub_with_most(s: str) -> int:
    left = 0
    best = 0
    counts = {}

    for right, ch in enumerate(s):
        counts[ch] = counts.get(ch, 0) + 1

        while len(counts) > 2:
            left_ch = s[left]
            counts[left_ch] -= 1
            if counts[left_ch] == 0:
                del counts[left_ch]
            left += 1

        best = max(best, right - left + 1)

    return best

def long_sub(s):
    left = 0
    window = set()
    max_len = 0
    for right in s:
        while right in window:
            window.remove(s[left])
            left += 1
        window.add(right)
        max_len = max(max_len, len(window))
    return max_len



def long_rep(s, k):
    left = 0
    counts = {}
    max_freq = 0
    best = 0

    for right in range(len(s)):
        char = s[right]
        if char not in counts:
            counts[char] = 1
        else:
            counts[char] += 1
        max_freq = max(max_freq, counts[char])

        while (right - left + 1) - max_freq > k:
            counts[s[left]] -= 1
            left += 1

        best = max(best, right - left +1)
    return best

def max_ones(nums):
    left = 0
    best = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            left = right + 1
        print(left)
        best = max(best, right - left + 1)
    return best


def max_sum_subarray(nums, k):
    left = 0
    current_sum = 0
    best = 0

    for right in range(len(nums)):
        current_sum += nums[right]
        if right - left + 1 > k:
            current_sum -= nums[left]
            left += 1
        if right - left + 1 == k:
            best = max(best, current_sum)
    return best


def find_vowel(letters, k):
    vowels = ['a','e','i','o','u']
    best = 0
    left = 0
    current_best = 0

    for right in range(len(letters)):
        if letters[right] in vowels:
            current_best += 1
        if right - left + 1 > k:
            best = max(best, current_best)
            if letters[left] in vowels:
                current_best -= 1
            left += 1
        if right - left + 1 == k:
            best = max(best, current_best)
    return best


