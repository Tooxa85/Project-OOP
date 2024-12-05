from src.product import LawnGrass, Product, Smartphone


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


def test_init_smartphone(smartphone1):
    assert smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone1.price == 180000.0
    assert smartphone1.quantity == 5
    assert smartphone1.efficiency == 95.5
    assert smartphone1.model == "S23 Ultra"
    assert smartphone1.memory == 256
    assert smartphone1.color == "Серый"


def test_add_smartphone(smartphone1, smartphone2):
    assert smartphone1 + smartphone2 == 2580000


def test_smartphone_init(grass1):
    assert grass1.name == "Газонная трава"
    assert grass1.description == "Элитная трава для газона"
    assert grass1.price == 500.0
    assert grass1.quantity == 20
    assert grass1.country == "Россия"
    assert grass1.germination_period == "7 дней"
    assert grass1.color == "Зеленый"


def test_lawn_grass_add(grass1, grass2):
    assert grass1 + grass2 == 16750


def test_mixin_product(capsys):
    Product("apples", "Fresh apples", 7.5, 15)

    message = capsys.readouterr()
    assert message.out.strip() == "Product('apples', 'Fresh apples', 7.5, 15)"
