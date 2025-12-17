# Exercise 9-6: Ice Cream Stand
# We will inherit from the Restaurant class from exercise 9-4

class Restaurant:
    """A simple model of a restaurant"""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initializes attributes for restaurant name and cuisine type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        """Prints information about the restaurant"""
        print(f"Restaurant '{self.restaurant_name}' offers {self.cuisine_type} cuisine")
    
    def open_restaurant(self):
        """Prints a message that the restaurant is open"""
        print(f"Restaurant '{self.restaurant_name}' is now open!")


class IceCreamStand(Restaurant):
    """Represents an ice cream stand - a specialized restaurant"""
    
    def __init__(self, restaurant_name, cuisine_type='ice cream'):
        """
        Initializes attributes of the parent class
        and adds attributes specific to an ice cream stand
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'strawberry', 'pistachio']
    
    def display_flavors(self):
        """Displays the list of available ice cream flavors"""
        print(f"Ice cream stand '{self.restaurant_name}' offers the following flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")
    
    def add_flavor(self, flavor):
        """Adds a new ice cream flavor to the list"""
        if flavor not in self.flavors:
            self.flavors.append(flavor)
            print(f"Added new flavor: {flavor}")
        else:
            print(f"Flavor '{flavor}' is already in the list")
    
    def remove_flavor(self, flavor):
        """Removes an ice cream flavor from the list"""
        if flavor in self.flavors:
            self.flavors.remove(flavor)
            print(f"Removed flavor: {flavor}")
        else:
            print(f"Flavor '{flavor}' not found in the list")


# Demonstration of the IceCreamStand class
def main():
    print("=" * 50)
    print("EXERCISE 9-6: ICE CREAM STAND")
    print("=" * 50)
    
    # Create an instance of an ice cream stand
    ice_cream_stand = IceCreamStand("Ice Cream Paradise", "desserts")
    
    # Use methods from the parent class
    print("\n1. Using inherited methods from Restaurant class:")
    print("-" * 40)
    ice_cream_stand.describe_restaurant()
    ice_cream_stand.open_restaurant()
    
    # Use methods from the child class
    print("\n2. Using IceCreamStand specific methods:")
    print("-" * 40)
    print("Initial flavors list:")
    ice_cream_stand.display_flavors()
    
    # Add new flavors
    print("\nAdding new flavors:")
    ice_cream_stand.add_flavor("banana")
    ice_cream_stand.add_flavor("mint chocolate chip")
    ice_cream_stand.add_flavor("vanilla")  # Try adding duplicate
    
    # Display updated list
    print("\nUpdated flavors list:")
    ice_cream_stand.display_flavors()
    
    # Remove a flavor
    print("\nRemoving a flavor:")
    ice_cream_stand.remove_flavor("pistachio")
    ice_cream_stand.remove_flavor("mango")  # Try removing non-existent
    
    # Display final list
    print("\nFinal flavors list:")
    ice_cream_stand.display_flavors()
    
    # Create another ice cream stand with different flavors
    print("\n" + "=" * 50)
    print("CREATING ANOTHER ICE CREAM STAND")
    print("=" * 50)
    
    ice_cream_stand2 = IceCreamStand("Frozen Delights")
    
    print("\nSecond ice cream stand:")
    ice_cream_stand2.describe_restaurant()
    
    print("\nDefault flavors (using inheritance with default cuisine_type):")
    ice_cream_stand2.display_flavors()
    
    # Demonstrate modifying flavors for second stand
    print("\nCustomizing second ice cream stand:")
    ice_cream_stand2.add_flavor("cookies and cream")
    ice_cream_stand2.add_flavor("rocky road")
    ice_cream_stand2.remove_flavor("pistachio")
    
    print("\nCustomized flavors list:")
    ice_cream_stand2.display_flavors()
    
    # Demonstrate that each instance maintains its own state
    print("\n" + "=" * 50)
    print("DEMONSTRATING INSTANCE INDEPENDENCE")
    print("=" * 50)
    print(f"\n'{ice_cream_stand.restaurant_name}' flavors:")
    ice_cream_stand.display_flavors()
    
    print(f"\n'{ice_cream_stand2.restaurant_name}' flavors:")
    ice_cream_stand2.display_flavors()


# Inheritance demonstration
print("\n" + "=" * 50)
print("INHERITANCE DEMONSTRATION")
print("=" * 50)

# Show that IceCreamStand inherits from Restaurant
print(f"\nIceCreamStand inherits from Restaurant: {issubclass(IceCreamStand, Restaurant)}")

# Show method resolution order
print(f"\nMethod Resolution Order for IceCreamStand:")
for i, cls in enumerate(IceCreamStand.__mro__):
    print(f"{i}. {cls.__name__}")

# Test the class directly
if __name__ == "__main__":
    main()


# Additional example: Creating multiple ice cream stands
print("\n" + "=" * 50)
print("ADDITIONAL EXAMPLE: MULTIPLE ICE CREAM STANDS")
print("=" * 50)

# Create multiple ice cream stands
stands = [
    IceCreamStand("Scoops & Smiles", "frozen desserts"),
    IceCreamStand("The Cold Cone"),
    IceCreamStand("Arctic Treats", "artisan ice cream")
]

# Customize each stand
stands[0].add_flavor("salted caramel")
stands[0].add_flavor("coffee")

stands[1].add_flavor("blueberry")
stands[1].remove_flavor("pistachio")

stands[2].add_flavor("lavender honey")
stands[2].add_flavor("matcha green tea")

# Display information for all stands
for i, stand in enumerate(stands, 1):
    print(f"\n{i}. {stand.restaurant_name}:")
    stand.describe_restaurant()
    stand.display_flavors()
    print()