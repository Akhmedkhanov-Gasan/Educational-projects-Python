def majority_element(nums: list[int]) -> int:
    current = 0
    count = 0
    for i in nums:
        if count == 0:
            current = i
        if i == current:
            count += 1
        else:
            count -= 1

    return current

print(majority_element([0,1,1]))
