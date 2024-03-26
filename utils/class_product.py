class Product:

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name                              #название
        self.description = description                #описание
        self.__price = float(price)                   #цена
        self.quantity = quantity                      #количество в наличии

    @classmethod
    def from_dictionary(cls, dictionary):
        instance = cls(**dictionary)
        return instance

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print('Цена введена некорректная')
        else:
            self.__price = new_price

    @price.deleter
    def price(self):
        self.__price = None

    def __str__(self):
        return f'{self.name}, {self.__price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        if type(self) == type(other):
            return self.__price * self.quantity + other.__price * other.quantity
        raise TypeError
