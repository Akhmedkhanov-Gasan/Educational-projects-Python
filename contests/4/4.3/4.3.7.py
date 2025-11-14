def same_type(f):
    def wrapper(*args):
        main_type = type(args[0])
        for arg in args:
            if type(arg) is not main_type:
                print('Обнаружены различные типы данных')
                return False
        return f(*args)
    return wrapper


@same_type
def combine_text(*words):
    return ' '.join(words)


print(combine_text('Hello,', 'world!') or 'Fail')
print(combine_text(2, '+', 2, '=', 4) or 'Fail')
print(combine_text('Список из 30', 0, 'можно получить так', [0] * 30) or 'Fail')