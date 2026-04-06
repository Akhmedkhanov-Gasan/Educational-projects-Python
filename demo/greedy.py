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


def max_profit(prices: list[int]) -> int:
    min_price = float("inf")
    max_profit = 0
    for i in prices:
        current = i - min_price
        max_profit = max(max_profit, current)
        if i < min_price:
            min_price = i
    return max_profit

print(max_profit([7,1,5,3,6,4]))
