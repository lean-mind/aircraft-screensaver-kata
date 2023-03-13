import unittest

from src import aircraft
from src.direction import Direction
from src.validation_error import ValidationError
from src.position import Position
from src.territory import Territory


class TestAircraft(unittest.TestCase):

    def test_aircraft_cant_be_positioned_out_of_the_territory(self):
        territory = Territory(width=200, height=200)
        position = Position(x=5000, y=5000)

        an_aircraft = aircraft.create(position, territory)

        self.assertIsInstance(an_aircraft, ValidationError)

    def test_aircraft_changes_position_when_moving(self):
        territory = Territory(width=200, height=200)
        position = Position(x=5, y=5)
        an_aircraft = aircraft.create(position, territory)

        an_aircraft.move(Direction.NorthEast)

        self.assertEqual(vars(Position(x=6, y=4)), vars(an_aircraft.current_position()))

    def test_aircraft_keeps_the_direction(self):
        territory = Territory(width=200, height=200)
        position = Position(x=5, y=5)
        an_aircraft = aircraft.create(position, territory, Direction.North)

        an_aircraft.move()
        an_aircraft.move()

        self.assertEqual(vars(Position(x=5, y=3)), vars(an_aircraft.current_position()))

    def test_aircraft_bounces_at_the_territory_borders(self):
        territory = Territory(width=6, height=6)
        position = Position(x=3, y=0)
        an_aircraft = aircraft.create(position, territory)

        an_aircraft.move(Direction.NorthEast)

        self.assertEqual(vars(Position(x=4, y=1)), vars(an_aircraft.current_position()))
