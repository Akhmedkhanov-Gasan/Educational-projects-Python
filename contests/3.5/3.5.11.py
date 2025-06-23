import json

with open(input(), 'r', encoding='utf-8') as f:
    numbers = [int(tok) for tok in f.read().split()]

total_count = len(numbers)
positive_count = sum(1 for x in numbers if x > 0)
min_value = min(numbers)
max_value = max(numbers)
total_sum = sum(numbers)
average = total_sum / total_count

out_records = {
    "count": total_count,
    "positive_count": positive_count,
    "min": min_value,
    "max": max_value,
    "sum": total_sum,
    "average": f"{average:.2f}"
}

with open(input(), "w", encoding="UTF-8") as file_out:
    json.dump(out_records, file_out, ensure_ascii=False, indent=2)
