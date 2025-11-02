
friends = ["Apple", "Orange" , 4 , 34.543 , False , "Akash", "Sankalp"]

print(friends[0])

friends[4] = "Sankalp"

print(friends[4])

# Unlike Strings, Lists are Mutable.

print(friends[0:4])
# list slicing works the same way as string slicing.

friends.append("Yash")
print(friends)

l1 = [ 23, 4, 64, 67, 27]
l1.sort()

print(l1)

# l1.reverse()
# print(l1)

# l1.insert(4,22222)
# insert 22222 such that it's index in the list is 4
# print(l1)

l1.pop(2)
print(l1)
