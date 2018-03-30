# coding: utf-8

"""
Task 2. Template method. Cheesecake production
"""
from enum import Enum


class Packing(Enum):
    FOIL = 0
    PAPER = 1

class Production(object):
    def template_method(self, mass, toping, chocolate, package):
        self.loading_products()
        self.select_parameters(mass, toping, chocolate)
        self.production()
        self.packaging(package)
        self.forming_packages()

    def loading_products(self):
        raise NotImplementedError()

    def select_parameters(self, mass, toping, chocolate):
        raise NotImplementedError()

    def production(self):
        raise NotImplementedError()

    def packaging(self, package):
        raise NotImplementedError()

    def forming_packages(self):
        raise NotImplementedError()


class CheesecakeProductsProd(Production):
    def loading_products(self):
        print("1) Loading products")

    def select_parameters(self, mass, toping, chocolate):
        if chocolate :
            print("2) Cheesecake " + str(mass) + "g with " + str(toping) + ", with chocolate")
        else:
            print("2) Cheesecake " + str(mass) + "g with " + str(toping) + ", without chocolate")
    def production(self):
        print("3) We are doing cheesecake :)")

    def packaging(self, package):
        if Packing.FOIL == package:
            print("4) Packing into foil")
        else:
            print("4) Packing into paper")

    def forming_packages(self):
        print("5) We are forming package with cakes")

if __name__ == "__main__":
    CheesecakeProductsProd = CheesecakeProductsProd()
    CheesecakeProductsProd.template_method(1.2, "banana", True, Packing.FOIL)

