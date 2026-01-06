
# ===============================
# TUPLES –  DIFFERENT EXAMPLES
# ===============================

# --------------------------------
# 1. Simple Tuple (same data type)
# --------------------------------
numbers = (10, 20, 30, 40, 50)
print("Numbers Tuple:", numbers)

print(numbers[0])
print(numbers[-1])


# --------------------------------
# 2. Tuple with mixed data types
# --------------------------------
mixed_tuple = ("Python", 3, 4.5, True)
print("Mixed Tuple:", mixed_tuple)


# --------------------------------
# 3. Nested Tuple
# --------------------------------
students = (
    ("Asha", 21),
    ("Rahul", 23),
    ("Neha", 22)
)

print("Student Details:")
for student in students:
    print("Name:", student[0], "Age:", student[1])


# --------------------------------
# 4. Tuple unpacking
# --------------------------------
person = ("Janhavi", 23, "MCA")

name, age, course = person
print("Name:", name)
print("Age:", age)
print("Course:", course)


# --------------------------------
# 5. Tuple methods (count & index)
# --------------------------------
colors = ("red", "blue", "green", "red", "yellow")

print("Count of 'red':", colors.count("red"))
print("Index of 'green':", colors.index("green"))

