
def greet(name, ending):
    print("Good Day," + name)
    print(ending)
    return "Glad to meet you!"

a = greet("Sankalp", "Thank you...")
print(a)
b = greet("Soham", "Thanks...")
print(b)
c = greet("Akhilesh", "Thank you...")  
print(c)

# Here, the greet function returns a string "Glad to meet you!" which is then printed after each function call.
# if we do not use return statement, the fun will return None by default. and if we want return value then we have to call function in another variable and then print that variable.
