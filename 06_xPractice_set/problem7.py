post = input("Enter the post:")

if("harry".lower() in post.lower()):
    print("Post is talking about harry.")

else:
    print("Post is not talking about harry.")

# The lower() function is used to convert the string to lowercase, making the check case-insensitive. as "Harry", "HARRY", "HaRrY" will treated the same as "harry". and the if condition will return true if any variation of "harry" is found in the post.

#we can write as "harry" instead of "harry".lower() in if condition. 