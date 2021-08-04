class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_equal(self, other):
        return self.x == other.x and self.y == other.y
