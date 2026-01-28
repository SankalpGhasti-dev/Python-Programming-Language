import random

def game():
    print("You are playing the game...")
    score = random.randint(1, 100)
    # Fetch the hi-score
    with open("09_xPractice_set/02_xHiscore.txt") as f:
        hiscore = f.read()
        if(score != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0 
            
    

    print(f"Your Score {score}")
    if(score>hiscore):
        with open("09_xPractice_set/02_xHiscore.txt", "w") as f:
            f.write(str(score))

    return score 


game()


            