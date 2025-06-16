from sys import stdin

endline = []
for line in stdin:
    lines = []
    parts = line.strip().split()
    for part in parts:
        if part.isdigit():
            lines.append(int(part))
    endline.append(lines[1] - lines[0])

mean = sum(endline) / len(endline)
round_mean = round(mean)
print(round_mean)
