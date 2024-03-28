from utils.class_product import Product
from utils.class_product import Commodity

class Lawn_grass(Product, Commodity):

    def __init__(self, name, description, price, quantity, manufacturer_country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.manufacturer_country = manufacturer_country    #страна-производитель
        self.germination_period = germination_period        #срок прорастания
        self.color = color                                  #цвет
        super().__repr__()

    @classmethod
    def from_dictionary(cls, dictionary):
        """расспаковывоет продукты из словаря"""
        instance = cls(**dictionary)
        return instance

