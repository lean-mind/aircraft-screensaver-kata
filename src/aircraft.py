from typing import Union

from src.direction import Direction
from src.position import Position
from src.territory import Territory
from src.validation_error import ValidationError


class Aircraft:
    def __init__(self, position: Position, territory: Territory, direction: Direction = Direction.North):
        self.position = position
        self.territory = territory
        self.direction = direction

    def current_position(self) -> Position:
        return self.position.copy()

    def move(self, direction: Direction = None) -> None:
        if direction is None:
            direction = self.direction
        else:
            self.direction = direction
        new_position: Position = self.position
        match direction:
            case direction.NorthEast:
                if self.position.is_reaching_north_limit():
                    new_position = Position(self.position.x + 1, self.position.y + 1)
                elif self.position.is_reaching_east_limit(self.territory):
                    new_position = Position(self.position.x, self.position.y - 1)
                else:
                    new_position = Position(self.position.x + 1, self.position.y - 1)
            case direction.NorthWest:
                new_position = Position(self.position.x - 1, self.position.y - 1)
            case direction.SouthEast:
                new_position = Position(self.position.x + 1, self.position.y + 1)
            case direction.SouthWest:
                new_position = Position(self.position.x - 1, self.position.y + 1)
            case direction.North:
                new_position = Position(self.position.x, self.position.y - 1)
            case direction.South:
                new_position = Position(self.position.x, self.position.y + 1)
            case direction.East:
                new_position = Position(self.position.x + 1, self.position.y)
            case direction.West:
                new_position = Position(self.position.x - 1, self.position.y)
        self.position = new_position


def create(position: Position, territory: Territory, direction: Direction = None) -> Union[Aircraft, ValidationError]:
    if position.x >= territory.width or position.y >= territory.height:
        return ValidationError("The position cant be out of the territory")
    return Aircraft(position, territory, direction)

