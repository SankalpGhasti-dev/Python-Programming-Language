''' Write a program to calculate the grade of a student from his marks from the
following scheme:
90 = 100 => Ex
80 = 90 => A
70 = 80 => B
60 = 70 =>C
50 = 60 => D
<50 => F  
'''

marks = int(input("Enter your marks:"))

if(marks<=100 and marks>=90):
    print(f"You pass the exam with {marks} marks and Ex Grade.")

elif(marks<90 and marks>=80):
    print(f"Your pass the exam with {marks} marks and A Grade.")

elif(marks<80 and marks>=70):
    print(f"Your pass the exam with {marks} marks and B Grade.")

elif(marks<70 and marks>=60):
    print(f"Your pass the exam with {marks} marks and C Grade.")

elif(marks<60 and marks>=50):
    print(f"Your pass the exam with {marks} marks and D Grade.")

elif(marks<50):
    print(f"You failed the exam with {marks} marks and F Grade.")

