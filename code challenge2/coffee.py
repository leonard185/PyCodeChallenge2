class Coffee:
    def __init__(self, name):
        # Use the property setter to validate the initial name
        self._name = None
        self.name = name

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

# Example usage:
try:
    coffee = Coffee("Latte")
    print(coffee.name)  # Output: Latte

    # The following line will raise an exception:
    # coffee.name = "Espresso"  # AttributeError: Name cannot be changed once set

    # The following will raise exceptions:
    # coffee = Coffee(123)  # TypeError: Name must be a string
    # coffee = Coffee("No")  # ValueError: Name must be at least 3 characters long
except (TypeError, ValueError, AttributeError) as e:
    print(e)
