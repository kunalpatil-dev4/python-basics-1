
# Class and Object – Different examples

# Example 1: Simple class with attributes
class Book:
    title = "Python Basics"
    price = 299

book1 = Book()
print(book1.title)
print(book1.price)


# Example 2: Class with a method
class Mobile:
    brand = "Samsung"

    def show_brand(self):
        print("Mobile Brand:", self.brand)

m1 = Mobile()
m1.show_brand()


# Example 3: Constructor (__init__)
class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def details(self):
        print("Teacher Name:", self.name)
        print("Subject:", self.subject)

t1 = Teacher("Anita", "Maths")
t2 = Teacher("Rahul", "Science")

t1.details()
t2.details()


# Example 4: Updating object data
class Account:
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    def show_balance(self):
        print("Account Holder:", self.holder)
        print("Balance:", self.balance)

    def deposit(self, amount):
        self.balance += amount

acc = Account("kunal patil", 5000)
acc.show_balance()
acc.deposit(2000)
acc.show_balance()


# Example 5: Using return value
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

c1 = Circle(7)
print("Circle Area:", c1.area())


# Example 6: Another real-life example
class Laptop:
    def __init__(self, brand, ram, storage):
        self.brand = brand
        self.ram = ram
        self.storage = storage

    def specs(self):
        print("Brand:", self.brand)
        print("RAM:", self.ram)
        print("Storage:", self.storage)

lap1 = Laptop("HP", "8GB", "512GB")
lap1.specs()
