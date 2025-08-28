NAMES = [
    {'ru': 'Январь', 'en': 'January'},
    {'ru': 'Февраль', 'en': 'February'},
    {'ru': 'Март', 'en': 'March'},
    {'ru': 'Апрель', 'en': 'April'},
    {'ru': 'Май', 'en': 'May'},
    {'ru': 'Июнь', 'en': 'June'},
    {'ru': 'Июль', 'en': 'July'},
    {'ru': 'Август', 'en': 'August'},
    {'ru': 'Сентябрь', 'en': 'September'},
    {'ru': 'Октябрь', 'en': 'October'},
    {'ru': 'Ноябрь', 'en': 'November'},
    {'ru': 'Декабрь', 'en': 'December'},
]


def month(number, language):
    if language == 'ru':
        return NAMES[number - 1]['ru']
    elif language == 'en':
        return NAMES[number - 1]['en']

result = month(1, "en")
print(result)