import os
import math

file_path = 'files/test1.txt'

size_bytes = os.path.getsize(file_path)

def human_readable_size(size):
    units = ["Б", "КБ", "МБ", "ГБ"]
    i = 0
    while size > 1024 and i < len(units) - 1:
        size = math.ceil(size / 1024)
        i += 1
    return f"{size}{units[i]}"

print(human_readable_size(size_bytes))
