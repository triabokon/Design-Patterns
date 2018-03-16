"""
Task1. Bridge pattern. International internet market.
"""

from abc import ABCMeta, abstractmethod
import locale
import time

NOT_IMPLEMENTED = "It's not implemented yet."
ENG = 0
UKR = 1
CHN = 2
COST = 3

base_of_products = [["Laptop Apple Macbook", "Ноутбук Apple Macbook", "笔记本电脑 Apple Macbook", 1000],
                    ["Laptop Lenovo Z580", "Ноутбук Lenovo Z580", "笔记本电脑 Lenovo Z580", 800],
                    ["Smartphone Apple iPhone 6", "Телефон Apple iPhone 6", "电话 Apple iPhone 6", 600],
                    ["Headphones Apple EarPods", "Навушники Apple EarPods", "头戴耳机 Apple EarPods", 200]]


# Bridge pattern
class Localization:
    """
    Implementor
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def get_bill(self, list_of_products, cost):
        raise NotImplementedError(NOT_IMPLEMENTED)


class EnglishLocalization(Localization):
    """
    ConcreteImplementor 1
    """

    def get_bill(self, list_of_products, cost):
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
        str_list = ""
        for item in list_of_products:
            str_list += item + "\n"
        return "\nInternet market bill\n===================\n\nItems:\n{0}\nTime:\
 {1}\n\nCost: {2}\n".format(str_list, time.strftime("%b %d %Y %H:%M:%S"), locale.currency(cost, grouping=True))


class ChinaLocalization(Localization):
    """
    ConcreteImplementor 2
    """

    def get_bill(self, list_of_products, cost):
        locale.setlocale(locale.LC_ALL, 'zh_CN.UTF-8')
        str_list = ""
        for item in list_of_products:
            str_list += item + "\n"
        return "\n互联网市场法案\n===================\n\n项目:\n{0}\n时间:\
 {1}\n\n成本: {2}\n".format(str_list, time.strftime("%b %d %Y %H:%M:%S"), locale.currency(cost, grouping=True))


class UkrainianLocalization(Localization):
    """
        ConcreteImplementor 3
    """

    def get_bill(self, list_of_products, cost):
        locale.setlocale(locale.LC_ALL, 'uk_UA.UTF-8')
        str_list = ""
        for item in list_of_products:
            str_list += item + "\n"
        return "\nЧек з інтернет-магазину\n===================\n\nТовари:\n{0}\nЧас:\
 {1}\n\nЦіна: {2}\n".format(str_list, time.strftime("%b %d %Y %H:%M:%S"), locale.currency(cost, grouping=True))


class AbstractBill:
    """
    Abstraction
    """

    __metaclass__ = ABCMeta

    loc = None

    def __init__(self, loc):
        self.loc = loc

    # Low-level
    @abstractmethod
    def print_bill(self):
        raise NotImplementedError(NOT_IMPLEMENTED)

    # High-level
    @abstractmethod
    def make_list(self, country):
        raise NotImplementedError(NOT_IMPLEMENTED)


class Bill(AbstractBill):
    """
    Refined Abstraction
    """

    def __init__(self, list_of_products, cost, loc):
        self.list_of_products = list_of_products
        self.cost = cost
        super(Bill, self).__init__(loc)

    # low-level i.e. Implementation specific
    def print_bill(self):
        return self.loc.get_bill(
            self.list_of_products, self.cost
        )

    # high-level i.e. Abstraction specific
    def make_list(self, country):
        country_list = []
        for i in self.list_of_products:
            country_list.append(base_of_products[i][country - 1])
        self.list_of_products = country_list


# Utils
def choose_country():
    country = -1
    while int(country) not in range(1, 4):
        try:
            country = int(input("Please, input your country:\n\n1)USA\n2)Ukraine\n3)China\n\n> "))
        except ValueError:
            print("That's not an int!")
            country = 0
    return country


def main():

    list_of_products = []
    cost = 0
    country = choose_country()
    product = -1

    while product != 0:

        print("\nSelect products:\n")

        for i in range(len(base_of_products)):
            print("{0}) {1}".format(str(i + 1), base_of_products[i][int(country) - 1]))

        print("0) Buy!\n")
        try:
            product = int(input("> "))
        except ValueError:
            print("That's not an int!")
            product = 1
            continue

        if product in range(1, len(base_of_products) + 1):
            list_of_products.append(product - 1)
            cost += base_of_products[product - 1][COST]
        elif product == 0:
            print("Thank you!")
        else:
            print("There is no such products")

    if country == ENG + 1:
        bill = Bill(list_of_products, cost, EnglishLocalization())
    elif country == UKR + 1:
        bill = Bill(list_of_products, cost, UkrainianLocalization())
    else:
        bill = Bill(list_of_products, cost, ChinaLocalization())

    bill.make_list(int(country))
    print(bill.print_bill())


if __name__ == "__main__":
    main()
