'''
factorial(0) = 1
factorial(1) = 1
factorial(2) = 2 X 1
factorial(3) = 3 X 2 X 1
factorial(4) = 4 X 3 X 2 X 1
factorial(5) = 5 X 4 X 3 X 2 X 1

factorial n = n X n-1 X n-2 X ... X 3 X 2 X 1
factorial (n-1) = (n-1) X (n-2) X ... X 3 X 2 X 1

so i can say that:
factorial n = n X factorial (n-1)

'''

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
    
n = int(input("Enter number n: "))

print(f"Factorial of number {n} is {factorial(n)}.")

# Differance between recursion fun and normal fun is that normal fun works on the basis of iteration but recursion fun works on the basis of function calling itself again and again until base condition is met. recursion fun make the code size reduced and easy to read compared to normal fun.
# But recursion fun uses more memory as compared to normal fun because each function call is stored in the call stack until base condition is met.

