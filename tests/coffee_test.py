import pytest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCoffee:
    def test_name(self):
        coffee = Coffee("Mocha")
        assert coffee.name == "Mocha"
        
        with pytest.raises(TypeError):
            Coffee(123)
            
        with pytest.raises(ValueError):
            Coffee("A")
            
        with pytest.raises(AttributeError):
            coffee.name = "Latte"
            
    def test_orders(self):
        coffee = Coffee("Mocha")
        customer = Customer("Steve")
        order = Order(customer, coffee, 2.5)
        assert order in coffee.orders()
        
    def test_customers(self):
        coffee = Coffee("Mocha")
        customer1 = Customer("Steve")
        customer2 = Customer("Stacy")
        Order(customer1, coffee, 2.5)
        Order(customer2, coffee, 3.5)
        assert customer1 in coffee.customers()
        assert customer2 in coffee.customers()
        
    def test_num_orders(self):
        coffee = Coffee("Mocha")
        assert coffee.num_orders() == 0
        Order(Customer("Steve"), coffee, 2.5)
        assert coffee.num_orders() == 1
        
    def test_average_price(self):
        coffee = Coffee("Mocha")
        assert coffee.average_price() == 0
        Order(Customer("Steve"), coffee, 2.5)
        Order(Customer("Stacy"), coffee, 3.5)
        assert coffee.average_price() == 3.0