"""
User that changes marks
"""
from enum import Enum


class Role(Enum):
    USER = 0
    ADMIN = 1


class User(object):
    def __init__(self, role):
        self.role = role
