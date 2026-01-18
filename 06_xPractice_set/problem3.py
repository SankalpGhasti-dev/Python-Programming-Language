p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

meassage = input("Enter your comment:")

if((p1 in meassage) or (p2 in meassage) or (p3 in meassage) or (p4 in meassage)):
    print("This comment is a spam.")

else:
    print("This comment is not a spam.")