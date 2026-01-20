class Cell:
    def __init__(self, state: str):
        self._state = state

    def status(self) -> str:
        return 'X' if self._state == '*' else self._state


class Checkers:
    def __init__(self):
        self._cells = {}

        cols = "ABCDEFGH"
        rows = "12345678"

        for r in rows:
            for c in cols:
                is_dark = ((ord(c) - ord('A') + int(r)) % 2 == 1)

                if not is_dark:
                    state = '*'
                else:
                    if r in "123":
                        state = 'W'
                    elif r in "678":
                        state = 'B'
                    else:
                        state = '*'

                self._cells[c + r] = Cell(state)

    def get_cell(self, p: str) -> Cell:
        return self._cells[p]

    def move(self, f: str, t: str) -> None:
        self._cells[t]._state = self._cells[f]._state
        self._cells[f]._state = '*'

checkers = Checkers()
for row in '87654321':
    for col in 'ABCDEFGH':
        print(checkers.get_cell(col + row).status(), end='')
    print()