

# Functions – Diffenrent Examples


# Example 1: Simple function without parameters
def show_message():
    print("Python functions help in code reusability")
    print("They make programs easy to read and manage")

show_message()


# Example 2: Function with parameters
def student_info(name, course):
    print("Student Name:", name)
    print("Course:", course)

student_info("Janhavi", "MCA")
student_info("Anamika", "BCA")


# Example 3: Function with return value
def add_numbers(a, b):
    total = a + b
    return total

result = add_numbers(15, 25)
print("Addition Result:", result)


# Example 4: Function using if-else (decision making)
def check_result(marks):
    if marks >= 40:
        return "Pass"
    else:
        return "Fail"

print("Result:", check_result(65))
print("Result:", check_result(32))


# Example 5: Function with default argument
def greet(name="Guest"):
    print("Welcome,", name)

greet()
greet("Janhavi")


# Example 6: Function working with list
def print_skills(skill_list):
    print("Skills are:")
    for skill in skill_list:
        print("-", skill)

skills = ["HTML", "CSS", "Python", "Bootstrap"]
print_skills(skills)


# Example 7: Function working with dictionary
def show_profile(profile):
    print("Profile Details:")
    for key, value in profile.items():
        print(key, ":", value)

profile_data = {
    "Name": "Janhavi",
    "Course": "MCA",
    "College": "GESCOE"
}

show_profile(profile_data)


# Example 8: Function to calculate average
def calculate_average(marks):
    total = sum(marks)
    avg = total / len(marks)
    return avg

marks_list = [70, 65, 80, 75]
print("Average Marks:", calculate_average(marks_list))


# Example 9: Function with loop and condition
def count_pass_students(marks):
    count = 0
    for m in marks:
        if m >= 40:
            count += 1
    return count

student_marks = [45, 67, 30, 55, 80]
print("Passed Students:", count_pass_students(student_marks))


# Example 10: Function calling another function
def square(num):
    return num * num

def show_square(number):
    result = square(number)
    print("Square of", number, "is", result)

show_square(6)
show_square(9)


# Example 11: Function with multiple return values
def calculate_operations(a, b):
    return a + b, a - b, a * b

add, sub, mul = calculate_operations(10, 5)
print("Addition:", add)
print("Subtraction:", sub)
print("Multiplication:", mul)


# Example 12: Real-life style function example
def bank_account(balance, withdraw_amount):
    if withdraw_amount <= balance:
        balance -= withdraw_amount
        print("Withdrawal Successful")
    else:
        print("Insufficient Balance")
    return balance

current_balance = 5000
current_balance = bank_account(current_balance, 1200)
print("Current Balance:", current_balance)
current_balance = bank_account(current_balance, 6000)
print("Current Balance:", current_balance)
