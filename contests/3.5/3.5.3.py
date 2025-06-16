from sys import stdin
lines = []
for line in stdin:
    head, sep, tail = line.partition("#")
    if head.strip():
        lines.append(head.rstrip())

for line in lines:
    print(line)
