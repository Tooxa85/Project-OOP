import pytest
from src.product import Product
from src.category import Category

@pytest.fixture
def class_product():
    return Product(
        name="Samsung Galaxy C23 Ultra" or "Iphone 15" or "Xiaomi Redmi Note 11" or "55\" QLED 4K",
        description="256GB, Серый цвет, 200MP камера" or "512GB, Gray space" or "1024GB, Синий" or "Фоновая подсветка",
        price=180000.0 or 210000.0 or 31000.0 or 123000.0,
        quantity=5 or 8 or 14 or 7
    )


@pytest.fixture
def class_category():
    return Category(
        name="Смартфоны" or "Телевизоры",
        description="Смартфоны, как средство не только коммуникации,"
        " но и получение дополнительных функций для удобства жизни"
        or "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        products=[]
    )
