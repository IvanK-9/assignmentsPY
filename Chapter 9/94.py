def __init__(self, restaurant_name, cuisine_type):
    """Initialize attributes for restaurant name and cuisine type"""
    self.restaurant_name = restaurant_name
    self.cuisine_type = cuisine_type
    # Add a new attribute with default value 0
    self.number_served = 0  # Number of customers served

def describe_restaurant(self):
    """Prints information about the restaurant"""
    print(f"Restaurant '{self.restaurant_name}' offers {self.cuisine_type} cuisine")

def open_restaurant(self):
    """Prints a message that the restaurant is open"""
    print(f"Restaurant '{self.restaurant_name}' is now open!")

def set_number_served(self, number):
    """Sets the number of customers served"""
    self.number_served = number

def increment_number_served(self, additional_customers):
    """Increases the number of customers served"""
    self.number_served += additional_customers