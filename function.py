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
def feed(animal = "panda", food = "bamboo", total = 3):

    # menggunakan fungsi print untuk menampilkan hasil dari parameter yang diinputkan
    # print(animal + " eats " + food + " " + str(total) + " times.")

    # menggunakan return untuk mengembalikan nilai dari parameter yang diinputkan
    return animal + " eats " + food + " " + str(total) + " times."

activity, activity2, activity3 = feed("hamster", "seeds", 5), feed("cat", "fish", 3), feed("dog", "bone", 2)

# memanggil fungsi feed dengan 3 parameter
# feed("hamster", "seeds", 5)

# memanggil variabel activity, activity2, activity3 yang berisi fungsi feed
print(activity2)
print(activity3)

# memanggil fungsi feed tanpa parameter atau menggunakan default parameter
print(feed())

# tuple argument

def family(*kids):
    print("The youngest child is " + kids[2])

family("Emil", "Tobias", "Linus")
# hasoutput: The youngest child is Linus karena Linus adalah anak termuda dan berada di index ke-2

