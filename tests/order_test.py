import pytest
from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder:
    def test_init(self):
        customer = Customer("Steve")
        coffee = Coffee("Mocha")
        order = Order(customer, coffee, 2.5)
        assert order.customer == customer
        assert order.coffee == coffee
        assert order.price == 2.5
        
    def test_price(self):
        customer = Customer("Steve")
        coffee = Coffee("Mocha")
        with pytest.raises(TypeError):
            Order(customer, coffee, "2.5")
            
        with pytest.raises(ValueError):
            Order(customer, coffee, 0.5)
            
        order = Order(customer, coffee, 2.5)
        with pytest.raises(AttributeError):
            order.price = 3.5
            
    def test_customer(self):
        coffee = Coffee("Mocha")
        with pytest.raises(TypeError):
            Order("Steve", coffee, 2.5)
            
    def test_coffee(self):
        customer = Customer("Steve")
        with pytest.raises(TypeError):
            Order(customer, "Mocha", 2.5)