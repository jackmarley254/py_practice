txt = "We are the so-called \"Vikings\" from the north."
print(txt)


txt = 'It\'s alright.'
print(txt) 

txt = "This will insert one \\ (backslash)."
print(txt) 

txt = "Hello\nWorld!"
print(txt) 

txt = "Hello\rWorld!"
print(txt) 

txt = "Hello\tWorld!"
print(txt) 

#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt)
 
txt = "\x48\x65\x6c\x6c\x6f"
print(txt)

#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt) 