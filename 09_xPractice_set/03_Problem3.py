
def generateTable(n):
    Table = ""
    for i in range(1,11):
        print(f"{n} X {i} = {n* i}")
    
    with open(f"Table/table_of_{n}.txt", "w") as f:
        f.write(Table)
        


for i in range(2, 21):
    generateTable(i)

