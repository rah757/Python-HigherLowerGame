import data
import random
# print(data.data)
print(data.logo)

StillInGame = True #start game
score = 0
itemA = None
itemB = None

def DrawAandB(itemA,itemB):
    if itemA is None and itemB is None:
        itemA = random.choice(data.data)
        itemB = random.choice(data.data)

    return itemA, itemB

while StillInGame == True:
    itemA, itemB = DrawAandB(itemA,itemB)
    valueA = itemA['follower_count']
    valueB = itemB['follower_count']
    print(f"Compare A: {itemA['name']}, a {itemA['description']} from {itemA['country']}.")
    print(data.vs)
    while itemB == itemA:
        itemB = random.choice(data.data)
    print(f"Against B: {itemB['name']}, a {itemB['description']} from {itemB['country']}.")
    valueB = itemB['follower_count']     
    


