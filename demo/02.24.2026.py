def max_consecutive_ones(nums):
    max_ones = 0
    current_count = 0
    for i in nums:
        if i == 1:
            current_count += 1
            max_ones = max(max_ones, current_count)
        else:
            current_count = 0
    return max_ones

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
print(longest_unique_substring("abba"))
