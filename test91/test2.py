# Dice rolling game
import random

test = True
while test:
    dice = input("Roll the dice? (y/n): ").lower()
    count=0
    if dice == 'y':
        times = int(input("How many times do you want to roll? "))
        for i in range(times):
            die1 = random.randint(1, 6)
            die2 = random.randint(1, 6)
            print(f'({die1},{die2})')
            count+=1
        print("This user has rolled a dice",count,"times.")
    elif dice == 'n':
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice!")
        test = False