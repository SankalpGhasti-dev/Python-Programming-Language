
def inch_to_cms(inch):
    if(inch==0):
        return 0
    else:
        return inch * 2.54 
    
inch = int(input("Enter iches: "))

inch_to_cms(inch)

print(f"{inch} iches is equal to {inch_to_cms(inch)} cm.")
