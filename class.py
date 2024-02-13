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

# class pokemon
class Pokemon:
    def __init__(self, name, type, rarity="Legendary"):
        self.name = name
        self.type = type
        self.rarity = rarity

    def get pokemon_info(self):
        return(f"name: {self.type} | Type: {self.type} |Rarity: {self.rarity}")

# Create an instance of the Pokemon class
my_pokemon = Pokemon("Pikachu", "Rare")

# Call the method pokemon_info
print(my_pokemon.pokemon_info())