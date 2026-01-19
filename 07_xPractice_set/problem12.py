
n = int(input("Enter n:"))

for i in range(1,11):
    print(f"{n} X {11 - i} = {n * (11 - i)}")

# In this code, we have to print multiplication table of a given number in reverse order from 10 to 1. so we use (11 - i) to achieve that. 

# logic behind like this if we have to print normal multiplication table we use 1 and in reverse 10 .. then same for 2 and 9 .. then 3 and 8 . then 4 and 7 .. then 5 and 6 .. then 6 and 5 .. then 7 and 4 .. then 8 and 3 .. then 9 and 2 .. then 10 and 1 .. so we can see that the sum of both the numbers is always 11 . so we use (11 - i) instead of i to get the reverse order of multiplication table.
