def first_unique_char(s: str) -> int:
    letters = {}
    for i in s:
        if i not in letters:
            letters[i] = 1
        else:
            letters[i] += 1
    for index, value in enumerate(s):
        if letters[value] == 1:
            return index
    return -1

print(first_unique_char('leetcode'))
