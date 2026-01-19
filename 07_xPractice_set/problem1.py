# Write a program to print multiplication table of a given number using for loop

a = int(input("Enter No:"))

for i in range(1, 11):
    print(f"{a} X {i} = {a * i}")
    i +=1

# In this code, we use f strings to format the output for better readability.
