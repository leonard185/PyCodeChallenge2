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

    def num_orders(self):
        # Return the number of orders for this coffee
        return len(self._orders)

    def average_price(self):
        # Calculate the average price of orders for this coffee
        if not self._orders:
            return 0  # No orders, so average price is 0
        total_price = sum(order.price for order in self._orders)
        return total_price / len(self._orders)


class Customer:
    _all_customers = []  # Class-level list to track all customer instances

    def __init__(self, name):
        if not isinstance(name, str) or not (1 <= len(name) <= 15):
            raise ValueError("Name must be a string between 1 and 15 characters long")
        self._name = name
        self._orders = []  # List to store orders related to this customer
        Customer._all_customers.append(self)  # Add the instance to the class-level list

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

    def add_order(self, order):
        if not isinstance(order, Order):
            raise TypeError("Order must be an instance of Order")
        self._orders.append(order)

    def orders(self):
        return self._orders

    def coffees(self):
        unique_coffees = set()
        for order in self._orders:
            unique_coffees.add(order.coffee)
        return list(unique_coffees)

    @classmethod
    def most_aficionado(cls, coffee):
        if not isinstance(coffee, Coffee):
            raise TypeError("Argument must be an instance of Coffee")

        best_customer = None
        max_spent = 0.0

        for customer in cls._all_customers:
            total_spent = sum(order.price for order in customer.orders() if order.coffee == coffee)

            if total_spent > max_spent:
                max_spent = total_spent
                best_customer = customer

        return best_customer

    def create_order(self, coffee, price):
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be an instance of Coffee")
        if not isinstance(price, float) or not (1.0 <= price <= 10.0):
            raise ValueError("Price must be a float between 1.0 and 10.0 inclusive")

        order = Order(self, coffee, price)
        return order


class Order:
    def __init__(self, customer, coffee, price):
        self._customer = None
        self._coffee = None
        self._price = None
        self.customer = customer
        self.coffee = coffee
        self.price = price
        self.customer.add_order(self)  # Add this order to the customer's orders
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
    coffee = Coffee("Latte")
    customer1 = Customer("Alice")
    customer2 = Customer("Bob")

    # Creating orders
    order1 = customer1.create_order(coffee, 5.0)
    order2 = customer2.create_order(coffee, 7.0)

    # Output the number of orders and average price for the coffee
    print(f"Number of orders for {coffee.name}: {coffee.num_orders()}")
    print(f"Average price for {coffee.name}: ${coffee.average_price():.2f}")
except (TypeError, ValueError, AttributeError) as e:
    print(e)
