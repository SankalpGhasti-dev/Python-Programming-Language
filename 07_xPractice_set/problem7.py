n = int(input("Enter no:"))
product = 1
i = 1

for i in range (1, n+1):
    product = product * i 
    i += 1 

print(f"factorial of no. {n} is {product}.")
    