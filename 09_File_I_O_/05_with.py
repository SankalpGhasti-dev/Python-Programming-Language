# f = open("myfile.txt")
# print(f.read())
# f.close()

# The same can be written using with statement like this 

with open("09_File_I_O_/file.txt") as txt:
    print(txt.read())

# You don't have to explicitly close the file when using with statement. It automatically takes care of closing the file after the nested block of code.
