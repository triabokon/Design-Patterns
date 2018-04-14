# coding: utf-8

"""
Task1. Chain of Responsibility. ATM
"""


class NoteHandler(object):
    """Абстрактный класс обработчика"""
    def handle(self, money):
        raise NotImplementedError()


class Note200Handler(NoteHandler):
    """Handler for Note 200"""
    def handle(self, money):
        if not money % 200:
            print("Note 200")
            return 200


class Note100Handler(NoteHandler):
    """Handler for Note 100"""
    def handle(self, money):
        if not money % 100:
            print("Note 100")
            return 100


class Note50Handler(NoteHandler):
    """Handler for Note 50"""
    def handle(self, money):
        if not money % 50:
            print("Note 50")
            return 50


class NoteNoneHandler(NoteHandler):
    """Handler for none Note"""
    def handle(self, money):
        if money < 50:
            return -1


class Client(object):
    def __init__(self):
        self._handlers = []

    def add_handler(self, h):
        self._handlers.append(h)

    def response(self, code):
        for h in self._handlers:
            msg = h.handle(code)
            if msg:
                return msg
        else:
            print('Error')


def main():

    client = Client()
    client.add_handler(Note200Handler())
    client.add_handler(Note100Handler())
    client.add_handler(Note50Handler())
    client.add_handler(NoteNoneHandler())

    while 1:
        money = int(input("Sum: "))
        while money > 0:
            res = client.response(money)
            if res == -1:
                print("Enter another sum")
                break
            money -= res
        else:
            break


if __name__ == "__main__":
    main()
