import pytest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer:
    def test_name(self):
        customer = Customer("Steve")
        assert customer.name == "Steve"
        
        with pytest.raises(TypeError):
            Customer(123)
            
        with pytest.raises(ValueError):
            Customer("")
            
    def test_orders(self):
        customer = Customer("Steve")
        coffee = Coffee("Mocha")
        order = Order(customer, coffee, 2.5)
        assert order in customer.orders()
        
    def test_coffees(self):
        customer = Customer("Steve")
        coffee1 = Coffee("Mocha")
        coffee2 = Coffee("Latte")
        Order(customer, coffee1, 2.5)
        Order(customer, coffee2, 3.5)
        assert coffee1 in customer.coffees()
        assert coffee2 in customer.coffees()