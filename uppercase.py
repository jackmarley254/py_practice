#!/usr/bin/python3
def to_uper(character):
    if ord(character) >= 97 and ord(character) <= 122:
        return (ord(character) - 32)
    else:
        return ord(character)


def uppercase(str):
    new = ""
    for character in str:
        new += "%c" % to_uper(character)
    print("{:s}".format(new))
    
if __name__ == "__main__":
    uppercase("best")
uppercase("Best School 98 Battery street")