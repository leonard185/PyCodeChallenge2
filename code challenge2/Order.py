class Order:
    def __init__(self, customer, coffee, price):
        # Use the property setter to validate the initial price
        self._price = None
        self.customer = customer
        self.coffee = coffee
        self.price = price  # Validate and set the price using the property setter

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
class Customer:
    def __init__(self, name):
        self.name = name

class Coffee:
    def __init__(self, name):
        self.name = name

try:
    customer = Customer("Alice")
    coffee = Coffee("Latte")
    order = Order(customer, coffee, 5.0)
    print(order.price)  # Output: 5.0

    # The following line will raise an exception:
    # order.price = 6.0  # AttributeError: Price cannot be changed once set

    # The following will raise exceptions:
    # order = Order(customer, coffee, "five")  # TypeError: Price must be a float
    # order = Order(customer, coffee, 11.0)  # ValueError: Price must be between 1.0 and 10.0, inclusive
except (TypeError, ValueError, AttributeError) as e:
    print(e)
