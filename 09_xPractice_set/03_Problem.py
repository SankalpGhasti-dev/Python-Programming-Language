
def generateTable(n):
    Table = ""
    Table += (f"----Table of {n}----\n")
    for i in range(1,11):
        Table += f"{n} X {i} = {n* i}\n"
    
    with open(f"09_xPractice_set/03_Table/table_of_{n}.txt", "w") as f:
        f.write(Table)
        


for i in range(2, 21):
    generateTable(i)

