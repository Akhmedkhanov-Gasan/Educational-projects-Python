FIRSTFILE = input()
n = int(input())

records = []
with open(FIRSTFILE, encoding='utf-8') as f:
    for raw in f:
        idx = int(raw.split(maxsplit=1)[0])
        val = raw.split(maxsplit=1)[1].rstrip('\n')
        records.append((idx, val))

tail = records[-n:]

for idx, val in tail:
    print(f"{idx} {val}")
