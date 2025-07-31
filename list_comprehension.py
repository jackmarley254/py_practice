#new list containing items with 'a'
# This is a more concise way to achieve the same result as the for loop above.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

#With list comprehension you can do all that with only one line of code:
#newlist = [expression for item in iterable if condition == True]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
print(fruits)

#Set the values in the new list to upper case:
newlist = [x.upper() for x in fruits]

print(newlist)

#You can set the outcome to whatever you like:
newlist = ['hello' for x in fruits]
print(newlist)

#Return the item if it is not banana, if it is banana return orange.
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)