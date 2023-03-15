from typing import Union

from screensaver.direction import Direction
from screensaver.flying_object import FlyingObject
from screensaver.position import Position
from screensaver.territory import Territory
from screensaver.validation_error import ValidationError


class Aircraft(FlyingObject):
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
                if self.territory.at_northern_border(self.position):
                    new_position = Position(self.position.longitude + 1, self.position.latitude + 1)
                elif self.territory.at_eastern_border(self.position):
                    new_position = Position(self.position.longitude - 1, self.position.latitude - 1)
                else:
                    new_position = Position(self.position.longitude + 1, self.position.latitude - 1)
            case direction.NorthWest:
                # Proposal: develop bounces with TDD for all directions
                new_position = Position(self.position.longitude - 1, self.position.latitude - 1)
            case direction.SouthEast:
                new_position = Position(self.position.longitude + 1, self.position.latitude + 1)
            case direction.SouthWest:
                new_position = Position(self.position.longitude - 1, self.position.latitude + 1)
            case direction.North:
                new_position = Position(self.position.longitude, self.position.latitude - 1)
            case direction.South:
                new_position = Position(self.position.longitude, self.position.latitude + 1)
            case direction.East:
                new_position = Position(self.position.longitude + 1, self.position.latitude)
            case direction.West:
                new_position = Position(self.position.longitude - 1, self.position.latitude)
        self.position = new_position
        self.territory.update_position(self)

    def is_colliding_with(self, flying_object: FlyingObject) -> bool:
        return self.position == flying_object.current_position()


def create(position: Position, territory: Territory, direction: Direction = None) -> Union[Aircraft, ValidationError]:
    if position.longitude > territory.max_longitude or position.latitude > territory.max_latitude:
        return ValidationError("The position cant be out of the territory")

    aircraft = Aircraft(position, territory, direction)
    territory.register(aircraft)
    return aircraft

