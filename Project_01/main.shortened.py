# We all have played snake, water gun game in our childhood. If you haven’t, google the rules of this game and write a python program capable of playing this game with the user.

'''   
1 for snake 
-1 for water 
0 for gun

'''
import random

computer = random.choice([1,-1,0])
yourstr = input("Enter your Choice: ")
youDict = {"s": 1 , "w": -1 , "g": 0}
reverseDict  = { 1:"snake", -1: "water", 0: "gun"}

you = youDict[yourstr]

# By now we havve 2 numbers (variables), you and computer

print(f"You chose {reverseDict[you]}\nComputer Chose {reverseDict[computer]}.")

if((computer - you == -1) or (computer - you == 2) ):
    print("You Lose !!")
else:
    print("You win !!")
