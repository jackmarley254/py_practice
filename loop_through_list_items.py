thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#Print all items by referring to their index number:
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
  
#while loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
  
#list comprehsion
thislist = ["mango", "pawpaw", "orange"]
[print(x) for x in thislist]