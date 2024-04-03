from utils.class_product import Product
from utils.mixin import ReprMixin

class Category(ReprMixin):
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list = None):
        self.name = name                                #название
        self.description = description                  #описание
        self.__products = products                      #список товаров
        Category.category_count += 1                    #общее количество категорий
        Category.product_count += len(self.__products)  #количество уникальных продуктов
        super().__repr__()


    def add_product(self, product):
        if isinstance(product, Product):
            self.__products.append(product)


    @property
    def products(self):
        list_products = []
        for j in self.__products:
            list_products.append(str(j))


    def __str__(self):
        return f'{self.name}, количество продуктов: {len(self)} шт'

    def __len__(self):
        num_products = 0
        for i in self.__products:
            num_products += i.quantity
        return num_products

    def average_price_tag(self):
        average_price = []
        for goods in self.__products:
            try:
                if goods.quantity == 0:
                    raise ZeroDivisionError
                average_price.append(goods.price)
            except ZeroDivisionError:
                return 0
        return sum(average_price) / len(average_price)


