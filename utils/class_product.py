from abc import ABC, abstractmethod
from utils.mixin import ReprMixin

class Commodity(ABC):

    @abstractmethod
    def from_dictionary(self, dictionary):
        pass


class Product(Commodity, ReprMixin):

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name                              #название
        self.description = description                #описание
        self.__price = float(price)                   #цена
        self.quantity = quantity                      #количество в наличии
        super().__repr__()

    @classmethod
    def from_dictionary(cls, dictionary):
        """расспаковывоет продукты из словаря"""
        instance = cls(**dictionary)
        return instance

    @property
    def price(self):
        """выводит цену продукта"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """меняет цену продукта"""
        if new_price <= 0:
            print('Цена введена некорректная')
        else:
            self.__price = new_price

    @price.deleter
    def price(self):
        self.__price = None

    def __str__(self):
        """выводит информауию о продукте"""
        return f'{self.name}, {self.__price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        """высчитывает цену 2 продуктов на складе"""
        if isinstance(other, self.__class__):
            return self.__price * self.quantity + other.__price * other.quantity
        raise TypeError
