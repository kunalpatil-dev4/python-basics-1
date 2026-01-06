
# IF–ELSE – DIFFERENT EXAMPLES

# Example 1: Simple if-else
age = 20

if age >= 18:
    print("Eligible for voting")
else:
    print("Not eligible for voting")



# Example 2: if-elif-else

marks = 67

if marks >= 75:
    print("Distinction")
elif marks >= 60:
    print("First Class")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")


# Example 3: Even or Odd

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")



# Example 4: Check positive, negative or zero

num = int(input("Enter number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")


# Example 5: Login validation

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Credentials")


# Example 6: Nested if

age = int(input("Enter age: "))

if age >= 18:
    if age >= 60:
        print("Senior Citizen")
    else:
        print("Adult")
else:
    print("Minor")


# Example 7: Largest of two numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("First number is greater")
elif b > a:
    print("Second number is greater")
else:
    print("Both numbers are equal")



# Example 8: Check eligibility for exam

attendance = int(input("Enter attendance percentage: "))

if attendance >= 75:
    print("Allowed for exam")
else:
    print("Not allowed for exam")


# Example 9: Grade system

score = int(input("Enter score: "))

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
elif score >= 60:
    print("Grade D")
else:
    print("Fail")



# Example 10: Discount calculation
amount = int(input("Enter purchase amount: "))

if amount >= 5000:
    discount = amount * 0.20
elif amount >= 3000:
    discount = amount * 0.10
else:
    discount = 0

print("Discount:", discount)
print("Final Amount:", amount - discount)

