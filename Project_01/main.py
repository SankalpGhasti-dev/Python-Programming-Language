# We all have played snake, water gun game in our childhood. If you haven’t, google the rules of this game and write a python program capable of playing this game with the user.

'''   
1 for snake 
-1 for water 
0 for gun

'''

computer = 1
yourstr = input("Enter your Choice: ")
youDict = {"s": 1 , "w": -1 , "g": 0}
reverseDict  = { 1:"snake", -1: "water", 0: "gun"}

you = youDict[yourstr]

print(f"You chose {reverseDict[you]}\nComputer Chose {reverseDict[computer]}.")

if(computer == you):
    print("Its a draw..")

else:
    if(computer == 1 and you == -1):
        print("You Lose !!")

    elif(computer == 1 and you == 0 ):
        print("You Win !!")
 
    elif(computer == -1 and you == 1):
        print("You win !!")
 
    elif(computer == 1 and you == 0):
        print("You Lose !!")
 
    elif(computer == 0 and you == -1):
        print("You Win !!")
 
    elif(computer == 0 and you == 1):
        print("You Lose !!")