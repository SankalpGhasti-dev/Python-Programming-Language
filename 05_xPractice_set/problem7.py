s = set()
s.add(0)
s.add(False)

print(len(s))

# The length of s will be 1 because in Python, 0 is considered equal to False. Therefore, when both are added to the set, only one unique value is stored.
