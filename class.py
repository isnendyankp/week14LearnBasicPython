class Car:
    # initialize with attributes
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    # method to display car information
    def display_info(self):
        return f"this car is a {self.brand} {self.model}"

# Create an instance of the Car class
my_car = Car("Toyota", "Corolla")

# Call the method display_info
print(my_car.display_info())
