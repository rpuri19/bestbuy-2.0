from abc import abstractmethod


class Promotion:
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity) -> float:
        pass

class PercentDiscount(Promotion):
    def __init__(self, discount_name, percent):
        super().__init__(discount_name)
        self.percent = percent

    def apply_promotion(self, product, quantity) -> float:
        new_price = product.price * quantity * (1 - product.discount / 100)
        return new_price

class SecondHalfPrice(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity) -> float:
        if quantity < 2:
            total_price = product.price * quantity
            return total_price
        full_price_items = quantity // 2
        half_price_items = quantity - full_price_items

        total_price = full_price_items * product.price + half_price_items * (0.5 * product.price)
        return total_price

class ThirdOneFree(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity) -> float:
        if quantity < 3:
            total_price = product.price * quantity
            return total_price
        free_items = quantity // 3
        priced_items = quantity - free_items
        total_price = product.price * priced_items
        return int(total_price)


