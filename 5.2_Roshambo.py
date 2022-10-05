import random
'''
ROSHAMBO PROGRAM
----------------

Create a program that randomly chooses a 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.(1 for rock, 2 for paper, 3 for scissors and 4 for quit)
I don't want to be asked to quit each time. I will enter a 4 if I want to quit.
Add conditional statements to figure out who wins and keep the records
Each round tell me what the computer chose, what I chose and also if I won, lost or tied.
When the user quits print an end game message and their win/loss/tie record

'''
losses = 0
wins = 0
ties = 0
done = False
while not done:
    computer = random.randrange(1,4)
    human = str(input("Rock, Paper, Scissors, SHOOT!(4 to end) "))
    if human.lower() == "rock" or human.lower() == "r" and computer == 1:
        print("Computer: Rock")
        print("Human: Rock")
        print("You tied the computer")
        ties += 1
    elif human.lower() == "rock" or human.lower() == "r" and computer == 2:
        print("Computer: Paper")
        print("Human: Rock")
        print("You Lost to the computer")
        losses += 1
    elif human.lower() == "rock" or human.lower() == "r" and computer == 3:
        print("Computer: Scissors")
        print("Human: Rock")
        print("You Won against the computer")
        wins += 1
    elif human.lower() == "paper" or human.lower() == "p" and computer == 1:
        print("Computer: Rock")
        print("Human: Paper")
        print("You Won against the computer")
        wins += 1
    elif human.lower() == "paper" or human.lower() == "p" and computer == 2:
        print("Computer: Paper")
        print("Human: Paper")
        print("You tied the computer")
        ties += 1
    elif human.lower() == "paper" or human.lower() == "p" and computer == 3:
        print("Computer: Scissors")
        print("Human: Paper")
        print("You Lost to the computer")
        losses += 1
    elif human.lower() == "scissors" or human.lower() == "s" and computer == 1:
        print("Computer: Rock")
        print("Human: Scissors")
        print("You Lost against the computer")
        losses += 1
    elif human.lower() == "scissors" or human.lower() == "s" and computer == 2:
        print("Computer: Paper")
        print("Human: Scissors")
        print("You Won against the computer")
        wins += 1
    elif human.lower() == "scissors" or human.lower() == "s" and computer == 3:
        print("Computer: Scissors")
        print("Human: Scissors")
        print("You Tied the computer")
        ties += 1
    elif human == "4":
        print("Your record was",wins,"/",losses,"/",ties)
        done = True
    else:
        print("That was not a choice")









