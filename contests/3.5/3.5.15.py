import json
import sys


with open('scoring.json', encoding='utf-8') as f:
    groups = json.load(f)

answers = iter(line.strip() for line in sys.stdin)

total_score = 0

for group in groups:
    points = group['points']
    tests = group['tests']
    n = len(tests)
    per_test = points // n

    passed = 0
    for test in tests:
        expected = test['pattern']
        try:
            got = next(answers)
        except StopIteration:
            got = ''
        if got == expected:
            passed += 1

    total_score += per_test * passed

print(total_score)

