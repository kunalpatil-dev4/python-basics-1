
# PYTHON SETS – DIFFERENT TYPES EXAMPLES

# 1. Creating a simple set

colors = {"Red", "Green", "Blue", "Red"}
print("Colors Set:", colors)


# 2. Creating an empty set
# ({} creates a dictionary, so use set())

empty_set = set()
empty_set.add("Python")
empty_set.add("Java")
print("Empty Set after adding values:", empty_set)


# 3. Set with different data types

mixed_set = {10, "Apple", 5.5, True}
print("Mixed Data Type Set:", mixed_set)


# 4. Adding and removing elements

numbers = {1, 2, 3, 4}
numbers.add(5)
numbers.remove(2)
print("Updated Numbers Set:", numbers)



# 5. Using discard() (no error if element not found)

numbers.discard(10)
print("After discard:", numbers)

# 6. Iterating through a set

fruits = {"Apple", "Banana", "Mango"}

print("Fruits in set:")
for fruit in fruits:
    print(fruit)
