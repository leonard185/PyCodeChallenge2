class Customer:
    def __init__(self, name):
        self._name = None
        self.name = name  # Use the property setter to validate initial name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not (1 <= len(value) <= 15):
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = value

# Example usage:
try:
    customer = Customer("Alice")
    print(customer.name)  # Output: Alice

    customer.name = "Bob"  # Update the name
    print(customer.name)  # Output: Bob

    # The following will raise exceptions:
    # customer.name = 123  # TypeError: Name must be a string
    # customer.name = ""  # ValueError: Name must be between 1 and 15 characters
    # customer.name = "This name is way too long"  # ValueError: Name must be between 1 and 15 characters
except (TypeError, ValueError) as e:
    print(e)
