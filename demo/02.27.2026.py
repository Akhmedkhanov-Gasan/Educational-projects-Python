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

def log_calls(func):

    def inner(*args, **kwargs):
        print(func.__name__)
        return func(*args, **kwargs)
    return inner


@log_calls
def add(a, b):
    return a + b

@log_calls
def greet(name):
    print("Hello", name)

print(add(2, 3))
greet('fuck')