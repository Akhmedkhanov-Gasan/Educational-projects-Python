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

def valid_parentheses(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for char in s:

        if char not in pairs:
            stack.append(char)
        else:
            if stack == []:
                return False
            if stack[-1] != pairs[char]:
                return False
            stack.pop()

    return not stack

def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return - 1

print(binary_search([-1,0,3,5,9,12], 9))
