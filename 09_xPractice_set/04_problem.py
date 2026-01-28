
with open ("09_xPractice_set/04_xproblem.txt" , "r") as f:
    content = f.read()
    

contentNew = content.replace("donkey", "####")    

with open ("09_xPractice_set/04_xproblem.txt" , "w") as f:
    f.write(contentNew)

