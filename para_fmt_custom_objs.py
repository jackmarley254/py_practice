class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __format__(self, format_spec):
        if format_spec == "short":
            return self.name
        elif format_spec == "detailed":
            return f"{self.name} ({self.age} years old)"
        else:
            return str(self)


p = Person("Alice", 30)
print(f"{p:short}")    # Output: Alice
print(f"{p:detailed}")  # Output: Alice (30 years old)
