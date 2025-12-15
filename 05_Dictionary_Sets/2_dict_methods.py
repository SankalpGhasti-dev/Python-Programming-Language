d = {} # Empty Dictionary 
marks = {
    "Harry" : 100, 
    "Rohan" : 25, 
    "Skill" : 70,
}

# The left one (Harry, Rohan) are keys and the right one (100, 25) are values.

print(marks.items())

print(marks.keys())

print(marks.values())

marks.update({"Harry": 98, "Renuka": 100})
print(marks)

# If the key is already present then its value will be updated else new key:value pair will be added.

# Dictionary are mutable.

print(marks.get("Harry2")) # Prints None
# print(marks["Harry2"])     # Returns an error
