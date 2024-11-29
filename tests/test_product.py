from src.product import Product


def test_class_product(class_product):
    assert class_product.name == "Samsung Galaxy C23 Ultra"
    assert class_product.description == "256GB, Серый цвет, 200MP камера"
    assert class_product.price == 180000.0
    assert class_product.quantity == 5


def test_new_product(class_new_product):
    class_new_product.price = 0
    assert class_new_product.price == 180000
    class_new_product.price = 12000
    assert class_new_product.price == 12000


def test_product_1():
    product_1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000, 5)
    assert product_1.price * product_1.quantity == 900000


def test_product_2():
    product_2 = Product("Iphone 15", "512GB, Gray space", 210000, 8)
    assert product_2.price * product_2.quantity == 1680000


def test_product_3():
    product_3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    assert product_3.price * product_3.quantity == 434000


def test_str_product():
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000, 5)
    str_data = "Samsung Galaxy S23 Ultra, 180000 руб. Остаток: 5 шт."
    assert str(product) == str_data
