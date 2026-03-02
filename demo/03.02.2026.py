def sub_with_most(s: str) -> int:
    left = 0
    best = 0
    counts = {}

    for right, ch in enumerate(s):
        counts[ch] = counts.get(ch, 0) + 1

        while len(counts) > 2:
            left_ch = s[left]
            counts[left_ch] -= 1
            if counts[left_ch] == 0:
                del counts[left_ch]
            left += 1

        best = max(best, right - left + 1)

    return best

print(sub_with_most('ccaabbb'))
