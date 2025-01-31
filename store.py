from products import Product
class Store:
    all_products = []
    def __init__(self, all_products):
        if not all(isinstance(product, Product) for product in all_products):
            raise ValueError("All items in all_products must be Product instances.")
        self.all_products = all_products

    def add_product(self, product):
        self.all_products.append(product)

    def remove_product(self, product):
        if product in self.all_products:
            self.all_products.remove(product)
        else:
            raise ValueError ("Product Not in List")

    def get_total_quantity(self):
        total_quantity = 0
        for product in self.all_products:
            total_quantity += product.get_quantity()
        return total_quantity

    def get_all_products(self) -> list[Product]:
        list_of_products = []
        for product in self.all_products:
            if product.is_active():
                list_of_products.append(product)
        return list_of_products

    def order(self, shopping_list):
        """Gets a list of tuples, where each tuple has 2 items:
        Product (Product class) and quantity (int).
        Buys the products and returns the total price of the order."""
        total_price = 0

        for product_id, quantity in shopping_list:
            if product_id > len(self.all_products):
                raise ValueError ("Not all product # entered valid. Please check ")
            else:
                product = self.all_products[product_id - 1]

            if product not in self.all_products:
                raise ValueError ("Product not in list")
            if not product.is_active():
                raise ValueError ("Product not available.")
            if product.get_quantity() < quantity:
                raise ValueError ("Insufficient stock.")
            total_price += product.buy(quantity)
        return total_price