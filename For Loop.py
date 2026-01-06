
# For Loop – examples

# Iterate through a list
cities = ['Pune', 'Mumbai', 'Nashik', 'Delhi']

for city in cities:
    print(city)


# Iterate through a tuple
animals = ('dog', 'cat', 'horse')

for animal in animals:
    print(animal)


# Iterate through a dictionary (keys and values)
student = {'name': 'Asha', 'roll': 12, 'course': 'MCA'}

for key in student:
    print(key, student[key])


# Iterate through a string
word = "Python"
for ch in word:
    print(ch)


# Using range() – default start from 0
for i in range(6):
    print(i)

print("------")

# Using range(start, stop)
for i in range(5, 10):
    print(i)


# Using enumerate to get index
subjects = ['Math', 'Science', 'English', 'Computer']

for index, subject in enumerate(subjects):
    print(index, subject)


# Getting index using range and len
subjects = ['Math', 'Science', 'English', 'Computer']

for i in range(len(subjects)):
    print(i, subjects[i])


# Using condition inside for loop
numbers = [10, 25, 30, 45]

for num in numbers:
    if num > 30:
        print(num, "is greater than 30")
    else:
        print(num, "is not greater than 30")


# break statement example
numbers = [5, 10, 15, 20, 25]

for n in numbers:
    print(n)
    if n == 15:
        break


# break with print after condition
numbers = [5, 10, 15, 20, 25]

for n in numbers:
    if n == 15:
        break
    print(n)


# continue statement example
numbers = [2, 4, 6, 8, 10]

for n in numbers:
    if n == 6:
        continue
    print(n)


# Loop through user input string
username = input("Enter username: ")
print("Characters in username:")
for ch in username:
    print(ch)


# Function used inside for loop
values = [3, 5, 7, 9]

def cube(num):
    return num * num * num

for v in values:
    print(v, cube(v))


# Sum of elements in a list
nums = [12, 22, 32, 42]
total = 0

for n in nums:
    total += n

print("Total sum:", total)


# Multiplication table using for loop
number = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")


# Nested for loop (combination example)
sizes = ['Small', 'Medium', 'Large']
colors = ['Red', 'Blue']

for s in sizes:
    for c in colors:
        print(s, c)


# Nested loop with numbers
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)


# Star pattern
rows = int(input("Enter rows: "))
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
    print()


# Number pattern
rows = int(input("Enter rows: "))
for i in range(1, rows + 1):
    for j in range(i):
        print(j + 1, end="")
    print()


# Find length of list without len()
items = ['pen', 'book', 'bag', 'bottle']
count = 0

for item in items:
    count += 1

print("Length of list:", count)


# Find index of an element
items = ['pen', 'book', 'bag', 'bottle']
position = 0

for item in items:
    position += 1
    if item == 'bag':
        print("Item found at position:", position)
        break


# Check character and stop loop
chars = ['x', 'y', 'z', 'w']

for ch in chars:
    if ch == 'z':
        print("Character found")
        break
    else:
        print(ch)

