

with open ("09_xPractice_set/07_xlog.txt") as f:
    lines = f.readline()

line_no = 1
for line in lines:

    if("python" in line):
        print(f"Yes ! Python is present at line{line_no}.")
        break 
    line_no += 1 

else:
    print("No !")

    