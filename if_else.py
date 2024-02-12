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