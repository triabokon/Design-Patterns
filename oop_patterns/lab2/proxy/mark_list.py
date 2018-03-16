"""
Mark list
"""
from abc import ABCMeta, abstractmethod
from proxy.user import Role
from proxy.mark_data import *

NOT_IMPLEMENTED = "You should implement this."


class AbstractMarkList:
    __metaclass__ = ABCMeta

    @abstractmethod
    def put_mark(self, path, mark):
        raise NotImplementedError(NOT_IMPLEMENTED)


class MarkList(AbstractMarkList):
    def put_mark(self, path, mark):
        mark_list = read_file(path)
        mark_list.append(mark)
        write_file(path, mark_list)


class ProxyMarkList(AbstractMarkList):
    def __init__(self, user):
        self.mlist = MarkList()
        self.user = user

    def put_mark(self, path, mark):
        if self.user.role == Role.USER:
            print("Only teachers can put marks to students")
        else:
            self.mlist.put_mark(path, mark)
