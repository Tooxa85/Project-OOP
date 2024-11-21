def test_class_category(class_category):
    assert class_category.name == "Смартфоны"
    assert (
        class_category.description
        == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )
    assert class_category.products == []
    assert class_category.category_count == 1
    assert class_category.product_count == 0
