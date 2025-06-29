#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# This program prints the last digit of a number and describes its value.

def print_last_digit(number):
    # Convert the number to string to handle negatives easily
    num_str = str(number)
    last_char = num_str[-1]  # last character of the string

    # For negative numbers, the last digit could be negative if we slice differently,
    # but here we'll just take the last digit normally
    last_digit = int(last_char)

    # Print the base message first
    print(f"Last digit of {number} is {last_char} ", end='')

    # Determine the phrase based on last digit value
    if last_digit == 0:
        print("and is 0")
    elif last_digit > 5:
        print("and is greater than 5")
    else:
        print("and is less than 6 and not 0")

if __name__ == "__main__":
    print_last_digit(number)