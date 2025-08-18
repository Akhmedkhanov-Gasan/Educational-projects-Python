with open("secret.txt", "r", encoding="utf-8") as f:
    data = f.read()

result = ""
for ch in data:
    code = ord(ch)
    if code < 128:
        result += ch
    else:
        new_code = code % 256
        result += chr(new_code)
print(result)
