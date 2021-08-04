class Snake:
    def __init__(self):
        self.snake_body = CoordinateRow()
        self.direction = 'r'

    def add_body(self, part):
        self.snake_body.add_coordinate(part)

    def remove_body(self, part):
        self.snake_body.remove_coordinate(part)

    def get_head(self):
        return self.snake_body.coordinaterow[-1]

    def get_tail(self):
        return self.snake_body.coordinaterow[0]

    def snake_grow(self):
        self.snake_body.coordinaterow.insert(0, self.get_tail())

    def hit_something(self, coordinate):
        return self.snake_body.contains(coordinate)


class CoordinateRow:
    def __init__(self):
        self.coordinaterow = []

    def add_coordinate(self, coordinate):
        self.coordinaterow.append(coordinate)

    def remove_coordinate(self, coordinate):
        self.coordinaterow.remove(coordinate)

    def contains(self, coordinate):
        for part in self.coordinaterow:
            if part.is_equal(coordinate):
                return True
        return False
