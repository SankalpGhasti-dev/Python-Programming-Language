name = "Sankalp"

print(name[0:3])    

print(name[-4:-1])
# it is an negative slicing. to solve this we count from the end of string. 
# index -1 is 'p', -2 is 'l', -3 is 'a', -4 is 'k' and so on.

# To easily solve negative slicing, firstly convert negative indices to positive ones.

print(name[1:4])

# if there is no starting index, it is considered as 0.
print(name[:4])   
print(name[0:4])  

# if there is no ending index, it is considered as length of string. means here 7.
print(name[1:])
print(name[1:7]) 
