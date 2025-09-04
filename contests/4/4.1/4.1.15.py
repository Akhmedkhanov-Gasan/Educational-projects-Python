def get_dict(text):
    new_dict = {}
    for i in text.split(';'):
        key, value = i.split('=')
        new_dict[key] = value
    return new_dict


result = get_dict('id=3-76;ip=127.0.0.1;phone=+7-(123)-456-78-90')
print(result)



