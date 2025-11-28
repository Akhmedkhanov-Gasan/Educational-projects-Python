class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def  move(self, dx, dy):
        self.x += dx
        self.y += dy

    def length(self, other):
        x1 = self.x
        y1 = self.y
        x2 = other.x
        y2 = other.y
        return round((((x1 - x2) ** 2) + ((y1 - y2)) ** 2) ** (0.5), 2)

# point = Point(3, 5)
# print(point.x, point.y)
# point.move(2, -3)
# print(point.x, point.y)

first_point = Point(2, -7)
second_point = Point(7, 9)
print(first_point.length(second_point))
print(second_point.length(first_point))