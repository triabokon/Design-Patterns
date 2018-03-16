"""
Task 2. Composite pattern. Children's health camp.
"""

from abc import ABCMeta, abstractmethod


class Unit(metaclass=ABCMeta):
    """
    An abstract component, in this case it is a unit (a unit can
    consist of one child or more)
    """
    @abstractmethod
    def print(self) -> None:
        """
        Print data of component
        """
        pass

    @abstractmethod
    def add(self, unit) -> None:
        """
        Add new child
        """
        pass

    @abstractmethod
    def remove(self, unit) -> None:
        """
        Remove new child
        """
        pass

    def sleep(self) -> None:
        print("is sleeping")

    def wake_up(self) -> None:
        print("woke up")


class Child(Unit):
    """
    Child (Leaf)
    """
    def __init__(self, name):
        self.name = name

    def print(self) -> None:
        print('\t\tChild {}'.format(self.name), end=" ")

    def add(self, unit):
        pass

    def remove(self, unit):
        pass


class Composer(Unit):
    """
    Squad -> Room -> Child
    """
    def __init__(self, name):
        self._units = []
        self.name = name

    def print(self) -> None:
        print("{0} (".format(self.name), end=" ")
        for u in self._units:
            u.print()
        print('\t\t)', end=" ")

    def add(self, unit: Unit) -> None:
        """
        Add new child/room

        :param unit: unit (may be a child or room)
        """
        self._units.append(unit)

    def remove(self, unit: Unit) -> None:
        """
        Remove child/room

        :param unit: child/room object
        """
        for u in self._units:
            if u == unit:
                self._units.remove(u)
                break
        else:
            unit.print()
            print('not found {}'.format(unit.name), end="")
            print()

    def get_child(self):
        return self._units


if __name__ == '__main__':

    camp = Composer("Camp")

    # Room 1
    room = Composer("Room 1")
    childAnn = Child("Ann")
    childEmily = Child("Emily")
    room.add(childAnn)
    room.add(childEmily)
    squad = Composer("Squad 1")
    squad.add(room)

    # Room 2
    room1 = Composer("Room 2")
    childEd = Child("Ed")
    childAlex = Child("Alex")
    room1.add(childEd)
    room1.add(childAlex)
    squad.add(room1)

    camp.add(squad)

    print('Night:')

    for s in camp.get_child():
        for r in s.get_child():
            for c in r.get_child():
                c.print()
                c.sleep()
            r.print()
            r.sleep()
        s.print()
        s.sleep()

    print("Morning:")

    for s in camp.get_child():
        for r in s.get_child():
            for c in r.get_child():
                c.print()
                c.wake_up()
            r.print()
            r.wake_up()
        s.print()
        s.wake_up()



