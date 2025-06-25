import json
from sys import stdin
JSONFILE = input()
with open(JSONFILE, encoding="UTF-8") as file_in:
    old_dir = json.load(file_in)

lines = []
for line in stdin:
    lines.append(line.rstrip("\n"))

new_dir = {}

for line in lines:
    part = line.split('==')
    key = part[0].strip()
    value = part[1].strip()
    new_dir[key] = value

old_dir.update(new_dir)

with open(JSONFILE, "w", encoding="UTF-8") as file_out:
    json.dump(old_dir, file_out, ensure_ascii=False, indent=2)
