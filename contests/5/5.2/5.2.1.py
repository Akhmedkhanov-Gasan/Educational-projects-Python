class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def length(self, other):
        x1 = self.x
        y1 = self.y
        x2 = other.x
        y2 = other.y
        return round((((x1 - x2) ** 2) + ((y1 - y2)) ** 2) ** (0.5), 2)


class PatchedPoint(Point):

    def __init__(self, *args):
        if len(args) == 0:
            x = 0
            y = 0
        elif len(args) == 1:
            x, y = args[0]
        elif len(args) == 2:
            x = args[0]
            y = args[1]
        super().__init__(x, y)

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'{self.__class__.__name__}{self.__str__()}'

    def __add__(self, other):
        dx, dy = other
        return PatchedPoint(self.x + dx, self.y + dy)

    def __iadd__(self, other):
        dx, dy = other
        self.x += dx
        self.y += dy
        return self

point = PatchedPoint()
print(point)
new_point = point + (2, -3)
print(point, new_point, point is new_point)