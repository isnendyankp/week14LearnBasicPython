animal = "🐱"

# # basic if else
# # wolf
# if animal == "🐺":
#     gender = "jantan"
#     print("wolf")
# # cat
# elif animal == "🐱":
#     gender = "betina"
#     print("cat")
# else:
#     print("animal not found")


# inline if else
print("wolf") if animal == "🐺" else print("cat") if animal == "🐱" else print("animal not found")

# membuat if else dengan variabel total
total = 100
if total > 100:
    print("total lebih dari 100")
elif total == 100:
    print("total sama dengan 100")

# membuat if else dengan variabel boolean dan operator logika
a,b,c = True, True, False

if a is b:
    print("a sama dengan b")
if a is not b:
    print("a tidak sama dengan b")
if a or b:
    print("a atau b benar")