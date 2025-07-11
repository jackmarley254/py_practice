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