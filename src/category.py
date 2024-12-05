from src.product import Product


class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self.__products)} шт."

    @property
    def products(self):
        return self.__products

    def add_product(self, new_product: Product):
        if isinstance(new_product, Product):
            self.__products.append(new_product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def product_list(self):
        product_str = ""
        for product in self.products:
            product_str += f"{str(product)}\n"
        return product_str

    def middle_price(self):
        """Подсчитывает средний ценник всех товаров"""
        try:
            avg_price = sum([product.price for product in self.__products]) / len(self.__products)
        except ZeroDivisionError:
            avg_price = 0

        return avg_price
