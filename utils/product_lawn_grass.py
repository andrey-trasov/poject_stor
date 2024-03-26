from utils.class_product import Product


class Lawn_grass(Product):

    def __init__(self, name, description, price, quantity, manufacturer_country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.manufacturer_country = manufacturer_country    #страна-производитель
        self.germination_period = germination_period        #срок прорастания
        self.color = color                                  #цвет



