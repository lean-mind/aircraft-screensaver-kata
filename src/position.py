from src.territory import Territory


class Position:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def copy(self):
        return Position(self.x, self.y)

    def is_out_of(self, territory: Territory):
        return self.x >= territory.width or self.y >= territory.height

    def is_reaching_north_limit(self):
        return self.y == 0

    def is_reaching_east_limit(self, territory: Territory):
        return self.x == territory.width

    def __eq__(self, other):
        return other.x == self.x and other.y == self.y

    def __str__(self):
        return f"Position({self.x},{self.y})"


