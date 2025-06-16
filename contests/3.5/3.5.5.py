from sys import stdin


def is_palindrome(s: str) -> bool:
    cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]


lines = [line.rstrip('\n') for line in stdin]

out_line = []
for line in lines:
    for i in line.split():
        if is_palindrome(i):
            out_line.append(i)

unique = sorted(set(out_line))
print(unique)
