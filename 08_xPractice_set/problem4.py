'''

sum 1 = 1
sum 2 = 1 + 2
sum 3 = 1 + 2 + 3

sum n = 1 + 2 + ... + (n-1) + n
sum n = sum(n-1) + n

'''

def sum(n):
    if(n==0):
        return 0
    else:
        return sum(n-1) + n
    
n = int(input("Enter n: "))

sum(n)

print(f"Sum of no. 1 to {n} is {sum(n)}.")
