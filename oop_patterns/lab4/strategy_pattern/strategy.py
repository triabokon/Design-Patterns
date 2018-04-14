# coding: utf-8

"""
Task 1. Strategy. Conference invitation
"""


class Status(object):
    conf_parts = ["Open ceremony", "Close ceremony", "Lectures", "Workshop", "Special guests", "Hackaton"]

    @staticmethod
    def access():
        raise NotImplementedError()


class AverageStatus(Status):
    @staticmethod
    def access():
        str = ""
        for i in range(2):
            str += Status.conf_parts[i] + ", "
        return str[:-2]


class RegularStatus(Status):
    @staticmethod
    def access():
        str = "You are our Regular visitor and for you available these parts:\n"
        for i in range(3):
            str += Status.conf_parts[i] + ", "
        return str[:-2]


class SuperRegularStatus(Status):
    @staticmethod
    def access():
        str = "You are our Super Regular visitor and for you available these parts:\n"
        for i in range(4):
            str += Status.conf_parts[i] + ", "
        return str[:-2]


class HonorableStatus(Status):
    @staticmethod
    def access():
        str = "You are our Honorable visitor and for you available these parts:\n"
        for i in range(5):
            str += Status.conf_parts[i] + ", "
        return str[:-2]


class Customer(object):

    def visit(self):
        invitation = None
        if self._visits in range(1, 3):
            invitation = AverageStatus
        elif self._visits in range(3, 5):
            invitation = RegularStatus
        elif self._visits in range(5, 7):
            invitation = SuperRegularStatus
        elif self._visits > 7:
            invitation = HonorableStatus
        else:
            raise ValueError('Invalid number of visits')
        self._visits += 1
        conf_parts = invitation.access()
        print(
            "Hello, " + self._name + "\nWe are glad to invite you to " + self._conf_name + " conference!\n" + conf_parts)

    def __init__(self, name, conf_name, visits):
        self._name = name
        self._conf_name = conf_name
        self._visits = visits


if __name__ == "__main__":
    tanya = Customer("Tanya", "Python days", 4)
    tanya.visit()
