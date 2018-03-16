# coding: utf-8

"""
Task2. Cocktail machine. Abstract factory pattern. Singleton.
"""


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


class Drinks(object):
    """
    Singleton
    """
    __metaclass__ = SingletonMeta

    def __init__(self, drinks):
        self._drinks = drinks

    def get_type(self):
        return self._drinks


class CocktailMachine(object):
    """
    Abstract factory
    """
    def get_drink(self, drink):
        raise NotImplementedError()


class AlcoholDrink(object):
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class NonAlcoholDrink(object):
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class AlcoholDrinkMachine(CocktailMachine):
    def get_drink(self, drink):
        return AlcoholDrink("Alcoholic " + drink)


class NonAlcoholicDrinkMachine(CocktailMachine):
    def get_drink(self, drink):
        return NonAlcoholDrink("Non-Alcoholic " + drink)


def get_factory(ident):
    if ident == 0:
        return AlcoholDrinkMachine()
    elif ident == 1:
        return NonAlcoholicDrinkMachine()


def choose_drinks():
    drinks = -1
    while int(drinks) not in range(1, 6):
        try:
            drinks = int(input("Please, select cocktail:\n\n1)Mojito\n2)Blue Curacao\n3)Mulled wine\n\
4)Grog\n5)Punch\n\n> "))
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
    drinks = Drinks(["Mojito", "Blue Curacao", "Mulled wine", "Grog", "Punch"])
    print(factory.get_drink(drinks.get_type()[drink - 1]))


if __name__ == "__main__":
    main()
