# # # # # # # # # # # # # # # # # # # # # # # # 
# Python 3 data structure practice 
# Chap 1: Dictionaries
# Author : Phuc Nguyen (Philngtn)
# # # # # # # # # # # # # # # # # # # # # # # #

# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered (>3.7), changeable and does not allow duplicates.

# Dictionaries are written with curly brackets, and have keys and values:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# To determine how many items a dictionary has, use the len() function:
print(len(thisdict))

# Accessing Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
# Get the value of the "model" key:
x = thisdict.get("model")

# The keys() method will return a list of all the keys in the dictionary.
x = thisdict.keys()
# The values() method will return a list of all the values in the dictionary.
x = thisdict.values()
# The items() method will return each item in a dictionary, as tuples in a list.
x = thisdict.items()
# To determine if a specified key is present in a dictionary use the in keyword:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

# Change Values
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

# Add Dictionary Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

# Update the "year" of the car by using the update() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

# Print all key names in the dictionary, one by one:
for x in thisdict:
  print(x)

# Print all values in the dictionary, one by one:
for x in thisdict:
  print(thisdict[x])
  

