# This program will assign a random signed number to the variable number 
# each time it is executed.
#!/usr/bin/python3
import random
number = random.randint(-10, 10)

if number > 0:
    print(f" {number} is Positive")
elif number < 0:
    print(f" {number} is Negative")
else:
    print(f" {number} is Zero")
