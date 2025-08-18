shift = int(input())

with open("files/1.txt", "r", encoding="utf-8") as f:
    data = f.read()

private = []

for i in data:
    if i == "\n":
        continue
    elif i.isupper():
        private.append(chr((ord(i) - ord('A') + shift) % 26 + ord('A')))
    elif i.islower():
        private.append(chr((ord(i) - ord('a') + shift) % 26 + ord('a')))
    else:
        private.append(i)

with open("files/private.txt", "w", encoding="utf-8") as file_out:
    file_out.writelines(private)
