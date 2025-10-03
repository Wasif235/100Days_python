logo = '''  
  _______           _______  _______  _______  _______  _______  _______  _______ 
(  ____ \|\     /|(  ____ \(  ____ \(  ____ \(  ____ \(  ___  )(       )(  ____ \\
| (    \/| )   ( || (    \/| (    \/| (    \/| (    \/| (   ) || () () || (    \/
| |      | |   | || (__    | (_____ | (_____ | |      | (___) || || || || (__    
| | ____ | |   | ||  __)   (_____  )(_____  )| | ____ |  ___  || |(_)| ||  __)   
| | \_  )| |   | || (            ) |      ) || | \_  )| (   ) || |   | || (      
| (___) || (___) || (____/\/\____) |/\____) || (___) || )   ( || )   ( || (____/\\
(_______)(_______)(_______/\_______)\_______)(_______)|/     \||/     \|(_______/
                                                                                 
'''

print(logo)

import random

EASY = 10
HARD = 5

def level():
    difficulty = input("Choose your level 'easy' or 'hard': \n")
    if difficulty.lower() == 'easy':
        return EASY
    else:
        return HARD

def check_answer(user_guess, actual_answer):
    if user_guess == actual_answer:
        print("🎉 You win!")
        return True
    elif user_guess < actual_answer:
        print("📉 Too low.")
    else:
        print("📈 Too high.")
    return False

print("Welcome to the guessing game")
print("I'm thinking of a number between 1 and 100")

random_number = random.randint(1, 100)
turns = level()
print(f"You have {turns} attempts.")

while turns > 0:
    guess = int(input("Make a guess: "))
    if check_answer(guess, random_number):
        break
    turns -= 1
    if turns > 0:
        print(f"You have {turns} attempts remaining.\n")
    else:
        print(f"😢 You've run out of attempts. The number was {random_number}.")
