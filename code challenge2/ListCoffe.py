class Customer:
    def __init__(self, name):
        if not isinstance(name, str) or not (1 <= len(name) <= 15):
            raise ValueError("Name must be a string between 1 and 15 characters long")
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not (1 <= len(value) <= 15):
            raise ValueError("Name must be between 1 and 15 characters")
        if hasattr(self, '_name') and self._name is not None:
            raise AttributeError("Name cannot be changed once set")
        self._name = value


class Coffee:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) < 3:
            raise ValueError("Name must be a string with at least 3 characters")
        self._name = name
        self._orders = []  # List to store orders related to this coffee

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if len(value) < 3:
            raise ValueError("Name must be at least 3 characters long")
        if hasattr(self, '_name') and self._name is not None:
            raise AttributeError("Name cannot be changed once set")
        self._name = value

    def add_order(self, order):
        if not isinstance(order, Order):
            raise TypeError("Order must be an instance of Order")
        self._orders.append(order)

    def orders(self):
        return self._orders

    def customers(self):
        unique_customers = set()
        for order in self._orders:
            unique_customers.add(order.customer)
        return list(unique_customers)


class Order:
    def __init__(self, customer, coffee, price):
        self._customer = None
        self._coffee = None
        self._price = None
        self.customer = customer
        self.coffee = coffee
        self.price = price
        self.coffee.add_order(self)  # Add this order to the coffee's orders

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        if not isinstance(value, Customer):
            raise TypeError("Customer must be an instance of Customer")
        if hasattr(self, '_customer') and self._customer is not None:
            raise AttributeError("Customer cannot be changed once set")
        self._customer = value

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        if not isinstance(value, Coffee):
            raise TypeError("Coffee must be an instance of Coffee")
        if hasattr(self, '_coffee') and self._coffee is not None:
            raise AttributeError("Coffee cannot be changed once set")
        self._coffee = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, float):
            raise TypeError("Price must be a float")
        if not (1.0 <= value <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0, inclusive")
        if hasattr(self, '_price') and self._price is not None:
            raise AttributeError("Price cannot be changed once set")
        self._price = value


# Example usage:
try:
    customer1 = Customer("Alice")
    customer2 = Customer("Bob")
    coffee1 = Coffee("Latte")
    coffee2 = Coffee("Espresso")

    order1 = Order(customer1, coffee1, 5.0)
    order2 = Order(customer2, coffee1, 6.0)
    order3 = Order(customer1, coffee2, 4.0)

    print(coffee1.orders())  # Output: [<__main__.Order object at ...>, <__main__.Order object at ...>]
    print([order.customer.name for order in coffee1.orders()])  # Output: ['Alice', 'Bob']

    print(coffee1.customers())  # Output: [<__main__.Customer object at ...>, <__main__.Customer object at ...>]
    print([customer.name for customer in coffee1.customers()])  # Output: ['Alice', 'Bob']
except (TypeError, ValueError, AttributeError) as e:
    print(e)
