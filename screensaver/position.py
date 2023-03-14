
class Position:
    def __init__(self, longitude: int = 0, latitude: int = 0):
        self.longitude = longitude
        self.latitude = latitude

    def copy(self):
        return Position(self.longitude, self.latitude)

    def __eq__(self, other) -> bool:
        return other.longitude == self.longitude and other.latitude == self.latitude

    def __str__(self):
        return f"Position({self.longitude},{self.latitude})"


