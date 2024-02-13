class Car:
    # initialize with attributes
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    # method to display car information
    def display_info(self):
        return f"this car is a {self.brand} {self.model}"

# Create an instance of the Car class
class Pokemon:
    def __init__(self, name, type, rarity="Legendary"):
        self.name = name
        self.type = type
        self.rarity = rarity

    def get_pokemon_info(self):
        print (f"name: {self.name} | Type: {self.type} | Rarity: {self.rarity}")

# Create an instance of the Pokemon class
my_pokemon = Pokemon("Pikachu", "Rare")

# Call the method pokemon_info
print(my_pokemon.get_pokemon_info())