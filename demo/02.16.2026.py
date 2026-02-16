def is_anagram(s, t):
    if len(s) != len(t):
        return False

    letters = {}

    for i in s:
        if i not in letters:
            letters[i] = 1
        else:
            letters[i] += 1

    for i in t:
        if i not in letters:
            return False
        letters[i] -=1

        if letters[i] < 0:
            return False

    return True


print(is_anagram("listen", "silent"))
