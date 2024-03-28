from utils.class_product import Product
from utils.class_product import Commodity

class Smartphone(Product, Commodity):

    def __init__(self, name, description, price, quantity, performance, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.performance = performance    #производительность
        self.model = model                #модель
        self.memory = memory              #объем встроенной памяти
        self.color = color                #цвет
        super().__repr__()

    @classmethod
    def from_dictionary(cls, dictionary):
        """расспаковывоет продукты из словаря"""
        instance = cls(**dictionary)
        return instance
