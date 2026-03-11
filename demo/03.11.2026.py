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
        best = max(best, right - left + 1)
    return best

print(max_ones([1,1,0,1,1,1]))
