from sys import stdin

lines = [line.rstrip('\n') for line in stdin]

find_item = lines[-1].lower()

lines = lines[:-1]

for s in lines:
    if find_item in s.lower():
        print(s)
