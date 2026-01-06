
print("Hello, Welcome to Python Demo Program")

# Variables and Data Types
message = "Learning Python is fun!"
print(message)
print(type(message))

num_int = 10
num_float = 3.75
flag = False

print(type(num_int))
print(type(num_float))
print(type(flag))

print(num_int)
print(num_float)
print(flag)

# String basics
sentence = "Python Programming Language"
print(sentence)

# Length of string
print(len(sentence))

# String indexing and slicing
word = "Hello Python"
print(word[1])
print(word[-2])
print(word[2:7])
print(word[:5])
print(word[6:])
print(word[-3:])

# String methods
print(word.upper())
print(word.lower())
print(word.capitalize())
print(word.count("o"))
print(word.find("P"))
print(word.find("z"))

# Replace string
print(word.replace("Python", "Java"))
print(word)

# Replace characters
text = "goooood morrrning"
print(text.replace("o", "O"))
print(text.replace("x", "X"))

# Strip spaces
data = "   Welcome Home   "
print(data)
print(data.strip())
print(data.count(" "))
print(data.strip().count(" "))

# Split string
details = "101, Rahul Sharma, Pune"
split_data = details.split(",")
print(split_data)
print(type(split_data))

# String concatenation
fname = "Rahul"
lname = "Sharma"

fullname = fname + lname
print(fullname)

fullname = fname + " " + lname
print(fullname)

fullname = "{} {}".format(fname, lname)
print(fullname)

fullname = f"{fname.lower()} {lname.upper()}"
print(fullname)

# Integer and Float operations
x = 8
y = 3
print(x, y)
print(type(x), type(y))

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)
print(x % y)

print(type(x / y))

# Float arithmetic
a = 1.5
b = 2.2
print(a + b)
print(a * b)

# Integer and float together
i = 7
f = 0.5
print(i + f)

# User input
user_name = input("Enter your name: ")
print(user_name)
print(type(user_name))

# Menu driven calculator
n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))

while True:
    print("\n1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Remainder")
    print("6. Exit")

    choice = int(input("Choose option: "))

    if choice == 1:
        print("Addition:", n1 + n2)

    elif choice == 2:
        print("Subtraction:", n1 - n2)

    elif choice == 3:
        print("Multiplication:", n1 * n2)

    elif choice == 4:
        if n2 != 0:
            print("Division:", n1 / n2)
        else:
            print("Error: Division by zero")

    elif choice == 5:
        print("Remainder:", n1 % n2)

    elif choice == 6:
        print("Program Ended")
        break

    else:
        print("Invalid Option")
