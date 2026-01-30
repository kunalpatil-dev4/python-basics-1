
# Dictionaries are used to store data in key : value pairs

# Example 1: Simple dictionary
student = {
    "name": "avinash",
    "course": "MCA",
    "age": 23
}

print(student)


# Example 2: Accessing values using keys
print(student["name"])
print(student["course"])


# Example 3: Adding new key-value pair
student["college"] = "GESCOE"
print(student)


# Example 4: Updating value
student["age"] = 23

print(student)


# Example 5: Loop through dictionary keys and values
for key, value in student.items():
    print(key, ":", value)


# Example 6: Dictionary with list as value
portfolio = {
    "name": "kunal",
    "skills": ["HTML", "CSS", "Python", "Bootstrap"]
}

for skill in portfolio["skills"]:
    print(skill)
