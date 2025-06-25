import json

FIRST_JSON_FILE = input()
SECOND_JSON_FILE = input()

with open(FIRST_JSON_FILE, encoding="UTF-8") as file_in:
    users = json.load(file_in)

with open(SECOND_JSON_FILE, encoding="UTF-8") as file_in:
    updates = json.load(file_in)

old_dir = {}
for user in users:
    name = user['name']
    old_dir[name] = {}
    for key, value in user.items():
        if key != 'name':
            old_dir[name][key] = value

update_dir = {}

for user in updates:
    name = user['name']
    update_dir[name] = {}
    for key, value in user.items():
        if key != 'name':
            update_dir[name][key] = value

for name, upd_fields in update_dir.items():
    if name in old_dir:
        for key, new_val in upd_fields.items():
            if key in old_dir[name]:
                old_val = old_dir[name][key]
                old_dir[name][key] = max(old_val, new_val)
            else:
                old_dir[name][key] = new_val
    else:
        old_dir[name] = upd_fields

with open(FIRST_JSON_FILE, "w", encoding="UTF-8") as file_out:
    json.dump(old_dir, file_out, ensure_ascii=False, indent=2)
