def test_class_category(class_category):
    assert class_category.name == "Смартфоны"
    assert (
        class_category.description
        == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )
    assert class_category.products == []
    assert class_category.category_count == 1
    assert class_category.product_count == 0


def test_add_product(class_category, class_new_product):
    assert len(class_category.products) == 0
    class_category.add_product(class_new_product)
    assert len(class_category.products) == 1


def test_str_category(class_category):
    assert str(class_category) == "Смартфоны, количество продуктов: 0 шт."
