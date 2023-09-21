import data
import random
print(data.logo)
StillInGame = True #start game
score = 0
itemA = None
itemB = None
answer = None

def DrawAandB(itemA,itemB,answer):
    if itemA is None and itemB is None:
        itemA = random.choice(data.data)
        itemB = random.choice(data.data)
    elif answer == 'a':
        itemB = random.choice(data.data)
    elif answer == 'b':
        itemA = itemB
        itemB = random.choice(data.data)
    return itemA, itemB

def calculateAnswer(answer,score):
    if answer == 'a':
        if valueA > valueB:
            win = True
            score += 1
        else:
            win = False
    elif answer == 'b':
        if valueA < valueB:
            win = True
            score += 1
        else:
            win = False
    else:
        print(f"Wrong input. You lost the game. Your score is {score}")
        exit()
    return score, win

while StillInGame == True:
    itemA, itemB = DrawAandB(itemA,itemB,answer)
    valueA = itemA['follower_count']
    valueB = itemB['follower_count']
    print(f"Compare A: {itemA['name']}, a {itemA['description']} from {itemA['country']}.")
    print(data.vs)
    while itemB == itemA:
        itemB = random.choice(data.data)
    print(f"Against B: {itemB['name']}, a {itemB['description']} from {itemB['country']}.")
    valueB = itemB['follower_count']     
    answer = input("\nWho has more followers? Type 'A' or 'B': ").lower()
    score,win = calculateAnswer(answer,score)
    if win == False:
        print(f"Wrong guess, your final score is {score}")
        StillInGame = False



