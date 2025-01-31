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

    def __str__(self):
        return f"Name: {self.name}, Price: ${self.price:.2f}, Quantity: {self.quantity}, Active: {self.active}"

    def get_quantity(self):
        return float(self.quantity)

    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity can not be less than 0 ")
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

    def show(self):
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        """Buys a given quantity of the product.
            Returns the total price (float) of the purchase.
            Updates the quantity of the product.
            In case of a problem (when? think about it), raises an Exception.
        """
        if quantity <= 0:
            raise ValueError ("Quantity to buy must be greater than 0")
        if quantity > self.quantity:
            raise ValueError ("Not enough quantity available")
        total_price = self.price * quantity
        new_quantity = self.quantity - quantity
        self.set_quantity(new_quantity)
        return total_price
