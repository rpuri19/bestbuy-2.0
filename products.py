class Product:
    def __init__(self, name, price, quantity):

        if not name or not isinstance(name, str):
            raise ValueError ("Please enter a Name")
        if not price > 0:
            raise ValueError ("Price can not be negative")
        if quantity < 0:
            raise ValueError ("Quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        if quantity > 0:
            self.active = True
        self.promotion = None

    def __str__(self):
        return f"Name: {self.name}, Price: ${self.price:.2f}, Quantity: {self.quantity}, Active: {self.active}"

    def get_quantity(self):
        return float(self.quantity)

    def set_quantity(self, quantity):

        self.quantity = quantity

        if self.quantity == 0:
            self.deactivate()
        else:
            self.activate()

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def set_promotion(self, promotion):
        self.promotion = promotion

    def get_promotion(self):
        return self.promotion

    def show(self):
        if self.promotion:
            promotion_name = self.promotion.name
            return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Promotion: {promotion_name}"
        else:
            return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Promotion: No promotion"

    def buy(self, quantity):
        """Buys a given quantity of the product.
            Returns the total price (float) of the purchase.
            Updates the quantity of the product.
        """
        if quantity <= 0:
            raise ValueError ("Quantity to buy must be greater than 0")
        if quantity > self.quantity:
            raise ValueError ("Not enough quantity available")
        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)

        else:
            total_price = self.price * quantity

        new_quantity = self.quantity - quantity
        self.set_quantity(new_quantity)
        return total_price

class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)
        self.active = False

    def show(self):
        return f"{self.name}, Price: {self.price}"


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def show(self):
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Maximum: {self.maximum}"

    def get_maximum(self):
        return self.maximum

    def buy(self, quantity):
        """Buys a given quantity of the product.
            Returns the total price (float) of the purchase.
            Updates the quantity of the product.
            Raises error if the quantity exceeds maximum value allowed
        """
        if quantity <= 0:
            raise ValueError ("Quantity to buy must be greater than 0")
        if quantity > self.quantity:
            raise ValueError ("Not enough quantity available")
        if quantity > self.get_maximum():
            raise ValueError ("Exceeded maximum allowed number for purchase. ")
        total_price = self.price * quantity
        new_quantity = self.quantity - quantity
        self.set_quantity(new_quantity)
        return total_price