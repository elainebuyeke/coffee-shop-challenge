from customer import Customer
from coffee import Coffee
from order import Order

if __name__ == "__main__":
    c1 = Customer("Steve")
    c2 = Customer("Stacy")
    
    cof1 = Coffee("Mocha")
    cof2 = Coffee("Latte")
    
    o1 = Order(c1, cof1, 2.5)
    o2 = Order(c1, cof2, 3.5)
    o3 = Order(c2, cof1, 4.0)
    
    print("Customer orders:", c1.orders())
    print("Customer coffees:", c1.coffees())
    print("Coffee orders:", cof1.orders())
    print("Coffee customers:", cof1.customers())
    print("Coffee num orders:", cof1.num_orders())
    print("Coffee avg price:", cof1.average_price())