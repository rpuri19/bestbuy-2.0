
import pytest
import products

def test_creating_prod():
    product = products.Product("MacBook Air M2", price=1450, quantity=100)
    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.quantity == 100


def test_creating_prod_invalid_details():
    with pytest.raises(ValueError):
        products.Product("", price=1450, quantity=100)

    with pytest.raises(ValueError):
        products.Product("MacBook Air M2", price=-1450, quantity=100)

    with pytest.raises(ValueError):
        products.Product("MacBook Air M2", price=1450, quantity=-100)

def test_prod_becomes_inactive():
    product = products.Product("MacBook Air M2", price=1450, quantity=1)
    product.buy(1)
    assert product.activate() == None
    assert product.deactivate() == None
    assert product.get_quantity() == 0


def test_buy_modifies_quantity():
    product = products.Product("MacBook Air M2", price=1450, quantity=100)
    product.buy(1)
    assert product.get_quantity() == 99


def test_buy_too_much():
    product = products.Product("MacBook Air M2", price=1450, quantity=100)
    with pytest.raises(ValueError):
        product.buy(1000)