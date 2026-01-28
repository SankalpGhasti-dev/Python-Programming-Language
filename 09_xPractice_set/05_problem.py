
list = [ "dockey", "like", "are"]

with open ("09_xPractice_set/05_xproblem.txt" , "r") as f:
    content = f.read()
    
for word in list:
        content = content.replace( word , "#" * len(word))    

with open ("09_xPractice_set/05_xproblem.txt" , "w") as f:
    f.write(content)

