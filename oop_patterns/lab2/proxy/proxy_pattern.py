"""
Task1. Proxy pattern. Deanery system
"""
from proxy.user import *
from proxy.mark_list import *
from proxy.mark_data import *

PATH = 'data.txt'

NOT_IMPLEMENTED = "You should implement this."


def main():
    role = ''
    while role != 'y' or role != 'n':
        role = input("Are you teacher? (y/n)\n")
        if role == 'y':
            role = Role.ADMIN
            break
        elif role == 'n':
            role = Role.USER
            break
        else:
            print("Invalid input")

    name = ""
    mark_int = -1

    while mark_int < 0 and len(name) == 0:
        name = input("Enter name of student:\n")
        mark_int = int(input("Enter mark of student:\n"))

    user = User(role)
    proxy_list = ProxyMarkList(user)
    proxy_list.put_mark(PATH, [name, mark_int])

    print(read_file(PATH))


if __name__ == "__main__":
    main()

