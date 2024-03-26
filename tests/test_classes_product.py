import pytest

from utils.class_category import Category
from utils.class_product import Product
from utils.product_lawn_grass import Lawn_grass
from utils.product_smartphone import Smartphone

commodity = [
    {
        "name": "Samsung",
        "description": "200MP камера",
        "price": 180000.0,
        "quantity": 5
    },
    {
        "name": "Samsung",
        "description": "200MP камера",
        "price": 180000.0,
        "quantity": 5,
        "performance": "Samsung",
        "model": "s7",
        "memory": "1tb",
        "color": "синий"
    },
    {
        "name": "Трава",
        "description": "зеленая зеленая",
        "price": 1000.0,
        "quantity": 5,
        "manufacturer_country": "Китай",
        "germination_period": "15 дней",
        "color": "ярко зеленая"
    }
]


@pytest.fixture()
def test_products_smartphone():
    return Smartphone(commodity[1]['name'], commodity[1]['description'], commodity[1]['price'], commodity[1]['quantity'], commodity[1]['performance'], commodity[1]['model'], commodity[1]['memory'], commodity[1]['color'])

@pytest.fixture()
def test_products_lawn_grass():
    return Lawn_grass(commodity[2]['name'], commodity[2]['description'], commodity[2]['price'], commodity[2]['quantity'], commodity[2]['manufacturer_country'], commodity[2]['germination_period'], commodity[2]['color'])

@pytest.fixture()
def test_products():
    return Product(commodity[0]['name'], commodity[0]['description'], commodity[0]['price'], commodity[2]['quantity'])

@pytest.fixture()
def test_category():
    return Category('Тестовый', "для тестов", [])

@pytest.fixture()
def test_category_2():
    return Category('Тестовый', "для тестов", [])

def test_class_category_add(test_products_smartphone, test_products_lawn_grass, test_products, test_category, test_category_2):
    assert str(test_category) == 'Тестовый, количество продуктов: 0 шт'
    test_category.add_product(test_products_smartphone)
    test_category.add_product(test_products_lawn_grass)
    test_category.add_product(test_products)
    test_category.add_product(test_category_2)
    assert str(test_category) == 'Тестовый, количество продуктов: 15 шт'


