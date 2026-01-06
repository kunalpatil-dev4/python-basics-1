# ===============================
# WHILE LOOP – DIFFERENT EXAMPLES
# ===============================

# --------------------------------
# Example 1: Simple while loop
# --------------------------------
count = 1
while count <= 5:
    print("Count:", count)
    count += 1


# --------------------------------
# Example 2: Print even numbers
# --------------------------------
num = 2
while num <= 20:
    print(num)
    num += 2


# --------------------------------
# Example 3: Sum of numbers
# --------------------------------
total = 0
number = 1

while number <= 10:
    total += number
    number += 1

print("Sum of numbers from 1 to 10:", total)


# --------------------------------
# Example 4: User input with while loop
# --------------------------------
password = ""
while password != "python":
    password = input("Enter password: ")

print("Access Granted")


# --------------------------------
# Example 5: Using break in while loop
# --------------------------------
num = 1
while True:
    print(num)
    if num == 5:
        break
    num += 1


# --------------------------------
# Example 6: Using continue in while loop
# --------------------------------
num = 0
while num < 10:
    num += 1
    if num == 6:
        continue
    print(num)


# --------------------------------
# Example 7: Reverse counting
# --------------------------------
count = 10
while count >= 1:
    print(count)
    count -= 1


# --------------------------------
# Example 8: Find factorial of a number
# --------------------------------
n = int(input("Enter a number: "))
fact = 1

while n > 0:
    fact *= n
    n -= 1

print("Factorial:", fact)


# --------------------------------
# Example 9: Check number is palindrome
# --------------------------------
num = int(input("Enter number: "))
original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

if original == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome")


# --------------------------------
# Example 10: Multiplication table
# --------------------------------
num = int(input("Enter number: "))
i = 1

while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1


# --------------------------------
# Example 11: Count digits in a number
# --------------------------------
num = int(input("Enter number: "))
count = 0

while num > 0:
    count += 1
    num //= 10

print("Total digits:", count)


# --------------------------------
# Example 12: Menu-driven program
# --------------------------------
choice = 0

while choice != 4:
    print("\n1. Add\n2. Subtract\n3. Multiply\n4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        print("Result:", a + b)

    elif choice == 2:
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        print("Result:", a - b)

    elif choice == 3:
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        print("Result:", a * b)

    elif choice == 4:
        print("Program Ended")

    else:
        print("Invalid Choice")