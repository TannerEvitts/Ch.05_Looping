import random
'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''
nativesTraveledRandomizer = random.randrange(7,15)
print("Instructions")
done = False
dead = False
camelDead = False
diedOfThirst = False
caughtByNatives = False
milesTraveled = 0
thirst = 0
camelTiredness = 0
nativesTraveled = -20
canteenDrinks = 3
while not done:
    if milesTraveled <= nativesTraveled:
        print("You were caught by the natives")
        done = True
        dead = True
        caughtByNatives = True
    if milesTraveled - nativesTraveled <= 15 and caughtByNatives == False:
        print("The natives are getting close")
    if camelTiredness >= 8:
        camelDead = True
    if thirst >= 6:
        diedOfThirst = True
    if thirst >= 4 and thirst < 6 and camelDead == False and milesTraveled < 200:
        print("You are Thirsty!")
    if thirst >= 6 and camelDead == False:
        print("You died of thirst!")
        done = True
        dead = True
    if camelTiredness >= 5 and camelTiredness < 8 and diedOfThirst == False and milesTraveled < 200:
        print("Your camel is getting tired")
    if camelTiredness >= 8 and diedOfThirst == False:
        print("Your camel is dead.")
        done = True
        dead = True
    if milesTraveled >= 200 and caughtByNatives == False and diedOfThirst == False and camelDead == False:
        print("You got away from the natives and escaped the desert!")
        done = True
        dead = True
    if not dead:
        oasis = random.randrange(1,21)
        if oasis == 1:
            print("You found an oasis!")
            canteenDrinks = 3
            thirst = 0
            camelTiredness = 0
        print("A. Drink from your canteen")
        print("B. Ahead moderate speed")
        print("C. Ahead full speed")
        print("D. Stop for the night")
        print("E. Status check")
        print("Q. Quit")
        choice = input("What would you like to do ")
        if choice.lower() == "q":
            done = True
        elif choice.lower() == "e":
            print("- Miles traveled:",milesTraveled)
            print("- Drinks in canteen:",canteenDrinks)
            print("- The natives are",milesTraveled - nativesTraveled,"miles behind you")
        elif choice.lower() == "d":
            camelTiredness = 0
            print("The camel is happy")
            nativesTraveledRandomizer = random.randrange(7, 15)
            nativesTraveled = nativesTraveled + nativesTraveledRandomizer
        elif choice.lower() == "c":
            distanceTraveledRandomizer = random.randrange(10,20)
            camelTirednessRandomizer = random.randrange(1,4)
            nativesTraveledRandomizer = random.randrange(7,15)
            print("You traveled",distanceTraveledRandomizer,"miles")
            thirst += 1
            nativesTraveled = nativesTraveled + nativesTraveledRandomizer
            camelTiredness = camelTiredness + camelTirednessRandomizer
            milesTraveled = milesTraveled + distanceTraveledRandomizer
        elif choice.lower() == "b":
            distanceTraveledRandomizer = random.randrange(5,12)
            nativesTraveledRandomizer = random.randrange(7,15)
            print("You traveled",distanceTraveledRandomizer,"miles")
            thirst += 1
            camelTiredness += 1
            nativesTraveled = nativesTraveled + nativesTraveledRandomizer
            milesTraveled = milesTraveled + distanceTraveledRandomizer
        elif choice.lower() == "a" and canteenDrinks > 0:
            canteenDrinks -= 1
            thirst = 0
        elif choice.lower() == "a" and canteenDrinks <= 0:
            print("Error, no drinks left in canteen")