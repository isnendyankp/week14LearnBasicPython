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

# Arbitrary keyword argument

def my_function(**kid):
    print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
# hasoutput: His last name is Refsnes karena lname adalah keyword argument yang diinputkan pada fungsi my_function
# dan di print menggunakan print(kid["lname"]) yang berarti print nilai dari lname  yang diinputkan pada fungsi my_function yaitu Refsnes

# pass statement
def myfunction():
    pass
# pass statement digunakan untuk menulis kode yang belum diimplementasikan atau kode yang kosong tanpa error atau exception yang dihasilkan oleh python jika kode tersebut kosong

# keyword-only arguments
def myfunction(name, *, age):
    print(name + " is " + age + " years old")

myfunction("John", age = "36")
# hasoutput: John is 36 years old karena age adalah keyword-only arguments yang diinputkan pada fungsi myfunction