# using Noraml Method

# f = open("09_xPractice_set/poem.txt")

# content = f.read()
# if("Twinkle" in content):
#     print("The word Twinkle is present in the content.")
# else:
#     print("The word Twinkle is present in the content.")

# f.close()

# using with statement

with open("09_xPractice_set/xPoem.txt") as f:
    content = f.read()
    if("Twinkle" in content):
        print("The word Twinkle is present in the content.")
    else:
        print("The word Twinkle is present in the content.")

    