def concatenate_strings(*args):
    """
    Concatenates multiple string arguments into a single string.

    Args:
        *args: Variable length string arguments.

    Returns:
        str: The concatenated string.
    """
    return ''.join(args)

if __name__ == "__main__":
    result = concatenate_strings("Hello, ", "world", "!")
    print(result)  # Output: Hello, world!
    
#!/usr/bin/python3
def islower(c):
    if ord(c) > 96:
        return True
    else:
        return False
    
if __name__ == "__main__":
    print("Testing islower function:")
    test_chars = ['a', 'H', 'A', '3', 'g']
    for char in test_chars:
        print(f"{char} is {'lower' if islower(char) else 'upper'}")

print("a is {}".format("lower" if islower("a") else "upper"))
print("H is {}".format("lower" if islower("H") else "upper"))
print("A is {}".format("lower" if islower("A") else "upper"))
print("3 is {}".format("lower" if islower("3") else "upper"))
print("g is {}".format("lower" if islower("g") else "upper"))

a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)