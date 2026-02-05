class demo:
    a = 4

o = demo()

print(o.a)  # printing the class attribute.

o.a = 0     # Creating an instance attribute.

print(o.a)

# In this case Instance attribute will override the class attribute and print instance attribute value. but it will never change the class attribute value.
