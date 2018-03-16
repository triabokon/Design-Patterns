"""
Task2. Flyweight pattern. Battleship
"""

from abc import ABCMeta, abstractmethod
from enum import Enum
import random


class Sell(Enum):
    EMPTY = '-'
    SHIP = 'X'


class AllShips:
    """
    Create and manage flyweight objects.
    Ensure that flyweights are shared properly. When a client requests a
    flyweight, the FlyweightFactory object supplies an existing instance
    or creates one, if none exists.
    """

    def __init__(self):
        self._flyweights = {}

    def get_ships(self, key):
        try:
            flyweight = self._flyweights[key]
        except KeyError:
            flyweight = ConcreteShip()
            self._flyweights[key] = flyweight
        return flyweight


class Ship:
    """
    Declare an interface through which flyweights can receive and act on
    extrinsic state.
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        self.type = 0
        self.coord = []
        self.intrinsic_state = None

    @abstractmethod
    def set_on_field(self, extrinsic_state, x, y, field):
        pass


class ConcreteShip(Ship):
    """
    Implement the Flyweight interface and add storage for intrinsic
    state, if any. A ConcreteFlyweight object must be sharable. Any
    state it stores must be intrinsic; that is, it must be independent
    of the ConcreteFlyweight object's context.
    """

    def set_on_field(self, extrinsic_state, x, y, field):
        while not validate(field, x, y, extrinsic_state):
            x = random.randint(0, len(field[0])-extrinsic_state-1)
        self.type = extrinsic_state
        for i in range(extrinsic_state):
            y += 1
            if field[x][y] == Sell.EMPTY.value:
                field[x][y] = Sell.SHIP.value


def get_field(m):
    field = []
    for i in range(m):
        line = []
        for j in range(m):
            line.append(Sell.EMPTY.value)
        field.append(line)

    return field


def validate(field, x, y, ship_type):
    for i in range(ship_type):
        if field[x][y] != Sell.EMPTY.value or field[x][y+1] != Sell.EMPTY.value \
                or field[x][y-1] != Sell.EMPTY.value:
            return False
        y += 1
    return True


def draw_field(field):
    n = len(field[0])
    for i in range(n):
        for j in range(n):
            print(field[i][j], end="")
        print()


def main():
    m = 10

    field = get_field(m)
    flyweight_factory = AllShips()
    for t in range(4, 0, -1):
        for i in range(t, 5):
            ship = flyweight_factory.get_ships(t)
            ship.set_on_field(t, random.randint(0, m-t-1), random.randint(0, m-t-1), field)
    draw_field(field)


if __name__ == "__main__":
    main()
