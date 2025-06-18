import re

cleaned_lines = []

for raw in open(input(), encoding='utf-8'):
    s = raw.replace('\t', '')
    s = s.rstrip('\n').strip(' ')
    s = re.sub(r' {2,}', ' ', s)

    if s:
        cleaned_lines.append(s)

# Запись
with open(input(), 'w', encoding='utf-8') as fout:
    fout.write('\n'.join(cleaned_lines))
