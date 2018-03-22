"""
Drinks types
"""
import abc


class Drinks(metaclass=abc.ABCMeta):
    """
    Abstract drink
    """

    @abc.abstractmethod
    def get_type(self):
        pass


class AlcoholMojito(Drinks):
    """
    Define a product object to be created by the corresponding concrete
    factory.
    Implement the AbstractProduct interface.
    """

    def get_type(self):
        return "Alcohol Mojito"


class NonAlcoholMojito(Drinks):

    def get_type(self):
        return "Non-alcohol Mojito"


class AlcoholBlueCuracao(Drinks):

    def get_type(self):
        return "Alcohol Blue Curacao"


class NonAlcoholBlueCuracao(Drinks):

    def get_type(self):
        return "Non-alcohol Blue Curacao"


class AlcoholGrog(Drinks):

    def get_type(self):
        return "Alcohol Grog"


class NonAlcoholGrog(Drinks):

    def get_type(self):
        return "Non-alcohol Grog"

