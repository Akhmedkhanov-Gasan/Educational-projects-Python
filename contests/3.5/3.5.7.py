with open(input(), 'r', encoding='utf-8') as f:
    numbers = [int(tok) for tok in f.read().split()]

total_count = len(numbers)
positive_count = sum(1 for x in numbers if x > 0)
min_value = min(numbers)
max_value = max(numbers)
total_sum = sum(numbers)
average = total_sum / total_count

print(total_count)
print(positive_count)
print(min_value)
print(max_value)
print(total_sum)
print(f"{average:.2f}")
