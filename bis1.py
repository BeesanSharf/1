# Display numbers from a list using a loop
numbers = [12, 75, 150, 180, 145, 525, 50]
result_num = []
for item in list(numbers):
    if item > 500:
        break

    if item > 150:
        continue

    if item % 5 == 0:
        result_num.append(item)
print(result_num)
# Use else block to display a message “Done” after successful execution of for loop
for i in range(5):
    print(i)
else:
    print("Done!")
    # revere a given integer number
    num = 76542
    reverseNumber = 0
    print(f"Given Number {num} ")
    while num > 0:
        reminder = num % 10
        reverse_number = (reverseNumber * 10) + reminder
        num = num // 10
    print(f"Revere Number {reverse_number} ")
# Convert two lists into a dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
Dict = {}
for key in range(len(keys)):
    Dict.update({keys[key]: values[key]})
print(Dict)
# Delete a list of keys from a dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]

for key in keys:
    sample_dict.pop(key)
print(sample_dict)
# Add a list of elements to a set
sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]
sample_set.update(sample_list)
print(sample_set)
# Return a new set of identical items from two sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.intersection(set2))
# Reverse the tuple
tuple1 = (10, 20, 30, 40, 50)
tuple1 = tuple1[::-1]
print(tuple1)
# Access value 20 from the tuple
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
print(tuple1[1][1])
# Unpack the tuple into 4 variables
tuple1 = (10, 20, 30, 40)
a, b, c, d = tuple1
print(a)
print(b)
print(c)
print(d)
