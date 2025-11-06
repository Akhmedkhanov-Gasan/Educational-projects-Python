import re
from datetime import datetime

USERS = []

def insert(*args):
    USERS.extend(args)


def select(condition: str | None = None):
    if not condition:
        return sorted(USERS, key=lambda u: u["id"])

    field, op, raw_value = _parse_condition(condition)
    typed_value = _convert_value(field, raw_value)

    def predicate(user):
        left = user[field]
        if field == "id":
            left = int(left)
        elif field == "birth":
            left = _to_date(left)  # datetime.date
        else:
            left = str(left)

        return _compare(left, op, typed_value)

    result = [u for u in USERS if predicate(u)]
    result.sort(key=lambda u: u["id"])
    return result


_COND_RE = re.compile(
    r"^\s*(id|name|birth)\s*(<=|>=|!=|=|<|>)\s*(.+?)\s*$",
    re.IGNORECASE
)

def _parse_condition(cond: str):
    m = _COND_RE.match(cond)
    if not m:
        raise ValueError(
            "Некорректное условие. Ожидается '<поле> <оператор> <значение>'. "
            "Поля: id|name|birth. Операторы: <, <=, =, !=, >=, >."
        )
    field, op, value = m.groups()
    field = field.lower()
    return field, op, value


def _convert_value(field: str, value: str):
    value = value.strip()
    if field == "id":
        try:
            return int(value)
        except ValueError:
            raise ValueError("Значение для id должно быть целым числом.")
    if field == "birth":
        try:
            return _to_date(value)
        except ValueError:
            raise ValueError("Дата должна быть в формате DD.MM.YYYY.")
    if (value.startswith("'") and value.endswith("'")) or (value.startswith('"') and value.endswith('"')):
        value = value[1:-1]
    return value


def _to_date(s: str):
    return datetime.strptime(s, "%d.%m.%Y").date()


def _compare(left, op: str, right):
    if op == "<":
        return left < right
    if op == "<=":
        return left <= right
    if op == "=":
        return left == right
    if op == "!=":
        return left != right
    if op == ">=":
        return left >= right
    if op == ">":
        return left > right
    raise ValueError(f"Неизвестный оператор сравнения: {op}")

insert({'id': 1, 'name': 'Ann', 'birth': '01.03.2001'})
insert(
    {'id': 3, 'name': 'Bob', 'birth': '05.03.2002'},
    {'id': 4, 'name': 'Chuck', 'birth': '07.06.2001'}
)
print([user['name'] for user in select()])
print([user['name'] for user in select("name > B")])
insert({'id': 2, 'name': 'Den', 'birth': '29.02.2000'})
print([user['name'] for user in select("name > B")])
print([user['name'] for user in select("id <= 2")])
print(*select("birth >= 12.04.2001"), sep="\n")