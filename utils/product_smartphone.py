from utils.class_product import Product


class Smartphone(Product):

    def __init__(self, name, description, price, quantity, performance, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.performance = performance    #производительность
        self.model = model                #модель
        self.memory = memory              #объем встроенной памяти
        self.color = color                #цвет

