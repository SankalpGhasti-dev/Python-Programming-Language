'''   
n = 3

***
**
*

'''

def star_pattern(n):
    if(n==0):
        return
    print("*" * n)
    star_pattern(n-1)
     

n = int(input("Enter n: "))

star_pattern(n)

    