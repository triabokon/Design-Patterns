# coding: utf-8

"""
Task 1. Library ticket machine. Factory method pattern.
"""

from abc import ABC, abstractmethod


"""
Types of ticket
"""


class Ticket(ABC):
    """
    Base ticket
    """
    def __repr__(self):
        return self.__str__()


class SchoolTicket(Ticket):
    def __str__(self):
        return 'Ticket for school student created.'


class StudentTicket(Ticket):
    def __str__(self):
        return 'Ticket for university student created.'


class ScienceTicket(Ticket):
    def __str__(self):
        return 'Ticket for scientist created.'


class AcademicTicket(Ticket):
    def __str__(self):
        return 'Ticket for academic created.'


"""
Ticket machine
"""


class TicketMachine:

    ticket = None

    def __str__(self):
        return self.ticket.__str__()

    def __repr__(self):
        return self.ticket.__repr__()

    @abstractmethod
    def set_ticket_type(self, type_):
        """
        Set type of ticket : Factory method
        """
        raise NotImplementedError('Not Implemented Culture')


"""
Ticket machine in my university
"""


class UniversityTicketMachine(TicketMachine):
    def set_ticket_type(self, type_):
        if type_ == 1:
            self.ticket = SchoolTicket()
        elif type_ == 2:
            self.ticket = StudentTicket()
        elif type_ == 3:
            self.ticket = ScienceTicket()
        elif type_ == 4:
            self.ticket = AcademicTicket()


def choose_ticket_type():
    ticket_type = -1
    while int(ticket_type) not in range(1, 5):
        try:
            ticket_type = int(input("Please, input type of ticket that you need:\n\n1)School\n2)Student\n3)Scientist\n\
4)Academic\n\n> "))
        except ValueError:
            print("That's not an int!")
            ticket_type = 0
    return ticket_type


def main():
    ticket_type = choose_ticket_type()
    ticket_machine = UniversityTicketMachine()
    ticket_machine.set_ticket_type(ticket_type)
    print("\n" + str(ticket_machine))


if __name__ == "__main__":
    main()
