

# LISTS – WITH DIFFERENT TYPES


# --------------------------------
# 1. Simple List (same data type)
# --------------------------------
numbers = [10, 20, 30, 40, 50]
print("Numbers List:", numbers)

numbers.append(60)
numbers.remove(20)

print("Updated Numbers:", numbers)


# --------------------------------
# 2. Mixed Data Type List
# --------------------------------
mixed_list = ["Python", 3, 4.5, True]
print("Mixed List:", mixed_list)


# --------------------------------
# 3. Nested List
# --------------------------------
student_data = [
    ["Asha", 21],
    ["Rahul", 23],
    ["Neha", 22]
]

print("Student Data:")
for student in student_data:
    print("Name:", student[0], "Age:", student[1])


# --------------------------------
# 4. List using User Input
# --------------------------------
items = []
n = int(input("Enter number of items: "))

for i in range(n):
    value = input("Enter item: ")
    items.append(value)

print("Items List:", items)


# --------------------------------
# 5. List Comprehension
# --------------------------------
squares = [x * x for x in range(1, 11)]
print("Squares List:", squares)
