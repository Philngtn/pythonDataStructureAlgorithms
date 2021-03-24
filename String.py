# # # # # # # # # # # # # # # # # # # # # # # # 
# Python 3 data structure practice 
# Chap 0: String
# Author : Phuc Nguyen (Philngtn)
# # # # # # # # # # # # # # # # # # # # # # # #

# Strings in python are surrounded by either single quotation marks, or double quotation marks.

print("Hello World")
print('Hello World 2')

# You can assign a multiline string to a variable by using three quotes:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''

print(a)

##################### Strings are Arrays ######################

a = "Hello, World" 
print(a[1]) 
#  Output: e

# Looping Through a String
for x in "philngtn":
    print(x)
# Output: philngtn

# String Length
print(len(a))

# Check String
txt = "The best things in life are free!"
print("free" in txt)

# Check NOT in String
txt = "The best things in life are free!"
print("expensive" not in txt)

##################### Slicing Strings ######################

b = "Hello, World2"
print(b[2:5])
# Output: llo,

# Slice From the Start
b = "Hello, World3"
print(b[:5])
# Output: Hello,

# Slice To the End
b = "Hello, World!"
print(b[2:])

# Negative Indexing
# Use negative indexes to start the slice from the end of the string:
b = "Hello, World!"
print(b[-5:-2])
# From: "o" in "World!" (position -5) to, but not included: "d" in "World!" (position -2):

##################### Modify Strings ######################
# The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())

# Lower Case
a = "Hello, World!"
print(a.lower())

# Remove Whitespace
# The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

# Replace String
a = "Hello, World!"
print(a.replace("H", "J"))

# Split String
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

##################### String Concatenation ######################
a = "Hello"
b = "World"
c = a + b 
print(c)

##################### String Format  ######################
# The format() method takes the passed arguments, formats them, 
# and places them in the string where the placeholders {} are:
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

##################### Escape Characters  ######################
# To insert characters that are illegal in a string, use an escape character.
txt = "We are the so-called \"Vikings\" from the north."
# \'	Single Quote	
# \\	Backslash	
# \n	New Line	
# \r	Carriage Return	
# \t	Tab	
# \b	Backspace	
# \f	Form Feed	
# \ooo	Octal value	
# \xhh	Hex value

