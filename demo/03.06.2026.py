def maj_elem(nums):
    count = {}
    n = len(nums)
    for i in nums:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1
        if count[i] > n // 2:
            return i
    return None

print(maj_elem(nums = [2,2,1,1,1,2,2]))