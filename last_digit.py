#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        l_digit = number % 10
    else:
        l_digit = number % -10
        l_digit *= -1

    print("{:d}".format(l_digit), end="")
    return (l_digit)

if __name__ == "__main__":
    print_last_digit(98)
    print_last_digit(0)
    print_last_digit(-1024)
    print_last_digit(1000)
    print_last_digit(-1)
    print_last_digit(1234567890)
    print_last_digit(-9876543210)
    r = print_last_digit(-1028)
print(r)