# membuat fungsi dengan nama animal yang berisi list hewan
def animal():
    print("list of animals")
    butterfly = "🦋"
    # membuat kondisi jika butterfly adalah 🦋 maka print butterfly
    if butterfly == "🦋":
        print("butterfly")
    # membuat list hewan
    my_list = ["🐹", "🐶", "🐼"]
    for item in my_list:
        print(item)

# memanggil fungsi
animal()

# membuat fungsi dengan nama feed yang berisi 3 parameter yaitu animal, food, total
def feed(animal, food, total):
    print(animal + " eats " + food + " " + str(total) + " times.")

# memanggil fungsi feed dengan 3 parameter
feed("hamster", "seeds", 5)