# for loop number 1 to 11
for number in range(1, 11):
    print(number)

# for loop with array
array = ["A", "B", "C", "D", "E"]
for data in array:
    print(data)

# Comprehension
# for loop with array
array = ["A", "B", "C", "D", "E"]
for data in array:
    print(data)
# for loop with array using comprehension
array = ["A", "B", "C", "D", "E"]
[print(data) for data in array]

# for loop with array for this case we want to print only "A"
array = ["A", "B", "C", "A"]
array_a = [data for data in array if data == "A"]
print(array_a)

