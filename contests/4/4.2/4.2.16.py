def login(username, password, on_login, on_fail):
    sum_all_username = 0
    for i in username:
        sum_all_username += ord(i)
    len_of_username = sum_all_username * len(username)
    sixteen = f'{len_of_username:x}'

    if sixteen[::-1].lower() == password.lower():
        on_login(username)
    else:
        on_fail(username)

def on_login(username):
    print(f'Hello, {username}!')


def on_fail(username):
    print(f'Nice try... You are not {username}!')


login('NoobMaster', '4C72', on_login, on_fail)