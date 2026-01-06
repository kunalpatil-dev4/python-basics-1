
# PYTHON MODULES – PRACTICE CODE


# 1. Built-in Module: math

import math

print("Square Root of 64:", math.sqrt(64))
print("Factorial of 5:", math.factorial(5))
print("Value of PI:", math.pi)
print("Power 2^4:", math.pow(2, 4))


# 2. Built-in Module: random

import random

print("Random Number (1–10):", random.randint(1, 10))
print("Random Choice:", random.choice(["Apple", "Banana", "Mango"]))
print("Random Float:", random.random())

# 3. Built-in Module: datetime

import datetime

today = datetime.date.today()
current_time = datetime.datetime.now()

print("Today's Date:", today)
print("Current Date & Time:", current_time)


# 4. Built-in Module: time

import time

print("Program started")
time.sleep(1)
print("Program paused for 1 second")
time.sleep(1)
print("Program ended")



# 5. Built-in Module: sys

import sys

print("Python Version:", sys.version)
print("Operating System:", sys.platform)


# 6. Import specific functions

from math import sqrt, factorial

print("Square Root of 81:", sqrt(81))
print("Factorial of 6:", factorial(6))



# 7. Import module with alias

import math as m

print("Cos(0):", m.cos(0))
print("Sin(0):", m.sin(0))
