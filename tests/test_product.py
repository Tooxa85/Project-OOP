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
