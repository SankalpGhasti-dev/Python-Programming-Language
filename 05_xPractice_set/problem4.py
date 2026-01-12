s = set()

s.add(20)
s.add(20.0)
s.add('20') # length of s after theses operations?

print(s)
print(len(s))

# Answer: The leangth of s will be 2 because 20 and 20.0 are considered equal in Python sets, while '20' is a different string type. In python 1 == 1.0 consided as a equal.
