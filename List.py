# # # # # # # # # # # # # # # # # # # # # # # # 
# Python 3 data structure practice 
# Chap 1: Collections of data
# Author : Phuc Nguyen (Philngtn)
# # # # # # # # # # # # # # # # # # # # # # # #

# Python Collections (Arrays)
# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered and unindexed. No duplicate members.
# Dictionary is a collection which is unordered (<3.6) and changeable. No duplicate members.

##################### List ######################
thislist = ["apple", "banana", "cherry"]
print(thislist)

# A list can contain one or different data type(s):
list1 = ["apple", "banana", "cherry"]
list2 = ["abc", 34, True, 40, "male"]
list3 = [True, False, False]

# Add List Items
# To add an item to the end of the list, use the append() method:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# To insert a list item at a specified index, use the insert() method.
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# To append elements from another list to the current list, use the extend() method.
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# Remove List Items
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# Remove Specified Index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# If you do not specify the index, the pop() method removes the last item.
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# The del keyword can also delete the list completely.
thislist = ["apple", "banana", "cherry"]
del thislist

# The clear() method empties the list.
# The list still remains, but it has no content.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
