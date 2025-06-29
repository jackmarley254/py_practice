# Object-Oriented Programming (OOP)in Python
# Define a class called Animal
class Animal:
    # Constructor method to initialize the object
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    # Method to make the animal speak
    def speak(self):
        print(f"{self.name} says {self.sound}")

# Inheritance: Dog is a subclass of Animal


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Woof!")
        self.breed = breed

    def show_breed(self):
        print(f"{self.name} is a {self.breed}")

# Polymorphism: Cat has its own speak method


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Meow!")

    def speak(self):
        print(f"{self.name} softly says {self.sound}")


class Hen(Animal):
    def __init__(self, name):
        super().__init__(name, "Kuku!")

    def sing(self):
        print(f"{self.name} softly says {self.sound}")

# Create objects (instances)


dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers")
hen = Hen("Clara")

# Use the objects
dog.speak()         # Output: Buddy says Woof!
dog.show_breed()    # Output: Buddy is a Golden Retriever
cat.speak()         # Output: Whiskers softly says Meow!
hen.sing()         # Output: Clara softly says Kuku!
