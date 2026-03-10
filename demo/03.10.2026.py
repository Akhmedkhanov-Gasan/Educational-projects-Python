def move_zeros(nums):
    slow = 0
    for fast in nums:
        if fast != 0:
            nums[slow] = fast
            slow += 1

    for i in range(slow, len(nums)):
        nums[i] = 0

    return nums

def rem_dup(nums):
    slow = 0
    if not nums:
        return 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return slow


print(rem_dup([0,0,1,1,1,2,2,3,3,4]))