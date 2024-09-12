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


class Order:
    def __init__(self, customer, coffee, price):
        # Use the property setters to validate and set attributes
        self._customer = None
        self._coffee = None
        self._price = None
        self.customer = customer  # Validate and set the customer
        self.coffee = coffee  # Validate and set the coffee
        self.price = price  # Validate and set the price

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

    customer = Customer('Ashley')
    coffee = Coffee("Latte")
    coffee = Coffee('Americano')
    order = Order(customer,coffee,  5.0 )

    print(order.customer.name)  # Output: Alice
    print(order.coffee.name)  # Output: Latte
    print(order.price)  # Output: 5.0

    # The following lines will raise exceptions:
    # order.customer = Customer("Bob")  # AttributeError: Customer cannot be changed once set
    # order.coffee = Coffee("Espresso")  # AttributeError: Coffee cannot be changed once set
    # order.price = 6.0  # AttributeError: Price cannot be changed once set

except (TypeError, ValueError, AttributeError) as e:
    print(e)
