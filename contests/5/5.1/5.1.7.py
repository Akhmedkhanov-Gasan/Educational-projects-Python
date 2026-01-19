class Rectangle:

    def __init__(self, first, second):
        (x1, y1), (x2, y2) = first, second
        x1, x2 = sorted((x1, x2))
        y1, y2 = sorted((y1, y2))
        self.x, self.y = x1, y1
        self.width, self.height = x2 - x1, y2 - y1

    def area(self):
        return round(self.width * self.height, 2)

    def perimeter(self):
        return round(2 * (self.width + self.height), 2)

    def get_pos(self):
        return (round(self.x, 2), round(self.y + self.height, 2))

    def get_size(self):
        return (round(self.width,2), round(self.height, 2))

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def resize(self, width, height):
        top_y = self.y + self.height

        self.width = width
        self.height = height

        self.y = top_y - height

    def turn(self):
        cx = self.x + self.width / 2
        cy = self.y + self.height / 2

        self.width, self.height = self.height, self.width

        self.x = cx - self.width / 2
        self.y = cy - self.height / 2

    def scale(self, factor):
        cx = self.x + self.width / 2
        cy = self.y + self.height / 2

        self.width *= factor
        self.height *= factor

        self.x = cx - self.width / 2
        self.y = cy - self.height / 2


rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
print(rect.get_pos(), rect.get_size(), sep='\n')
rect.turn()
print(rect.get_pos(), rect.get_size(), sep='\n')


