import pytest

from src.category import Category
from src.product import LawnGrass, Product, Smartphone


@pytest.fixture
def class_product():
    return Product(
        name="Samsung Galaxy C23 Ultra" or "Iphone 15" or "Xiaomi Redmi Note 11" or '55" QLED 4K',
        description="256GB, Серый цвет, 200MP камера" or "512GB, Gray space" or "1024GB, Синий" or "Фоновая подсветка",
        price=180000.0 or 210000.0 or 31000.0 or 123000.0,
        quantity=5 or 8 or 14 or 7,
    )


@pytest.fixture
def class_category():
    return Category(
        name="Смартфоны" or "Телевизоры",
        description="Смартфоны, как средство не только коммуникации,"
        " но и получение дополнительных функций для удобства жизни"
        or "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        products=[],
    )


@pytest.fixture
def class_new_product():
    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    return new_product


@pytest.fixture
def smartphone1():
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def smartphone2():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def grass1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def grass2():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
