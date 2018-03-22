# coding: utf-8

"""
Task2. Cocktail machine. Abstract factory pattern. Singleton.
"""
from abstract_factory_pattern.drinks import *
import abc


class SingletonMeta(type):
    def __init__(cls, *args, **kwargs):
        cls._instance = None
        # глобальная точка доступа `Singleton.get_instance()`
        cls.get_instance = classmethod(lambda c: c._instance)
        super(SingletonMeta, cls).__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instance


class CocktailMachine(metaclass=abc.ABCMeta):
    """
    Abstract factory
    """
    def get_grog(self):
        raise NotImplemented()

    def get_mojito(self):
        raise NotImplemented()

    def get_curacao(self):
        raise NotImplemented()


class AlcoholDrinkMachine(CocktailMachine):
    __metaclass__ = SingletonMeta

    def get_grog(self):
        return AlcoholGrog()

    def get_mojito(self):
        return AlcoholMojito()

    def get_curacao(self):
        return AlcoholBlueCuracao()


class NonAlcoholicDrinkMachine(CocktailMachine):
    __metaclass__ = SingletonMeta

    def get_grog(self):
        return NonAlcoholGrog()

    def get_mojito(self):
        return NonAlcoholMojito()

    def get_curacao(self):
        return NonAlcoholBlueCuracao()


def get_factory(ident):
    if ident == 0:
        return AlcoholDrinkMachine()
    elif ident == 1:
        return NonAlcoholicDrinkMachine()


def choose_drinks():
    drinks = -1
    while int(drinks) not in range(1, 4):
        try:
            drinks = int(input("Please, select cocktail:\n\n1)Mojito\n2)Blue Curacao\n\
3)Grog\n\n> "))
        except ValueError:
            print("That's not an int!")
            drinks = 0
    return drinks


def ask_age():
    age = 0
    while int(age) not in range(1, 100):
        try:
            age = int(input("Please, input your age:\n"))
        except ValueError:
            print("That's not an int!")
            age = 0
    return age


def main():
    drink = choose_drinks()
    age = ask_age()
    if age > 18:
        factory = get_factory(0)
    else:
        factory = get_factory(1)

    if drink == 1:
        drink = factory.get_mojito()
    elif drink == 2:
        drink = factory.get_curacao()
    else:
        drink = factory.get_grog()

    print("\nGet: " + drink.get_type())


if __name__ == "__main__":
    main()
