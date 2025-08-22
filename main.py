import os
import time
import random

tries = 0
user_attempts = 0
game_round = 1
timer = 0
high_score = 0

def easy_mode(tries, user_attempts, game_round, random_number, high_score):
    high_score = 0
    clear()
    print(random_number)
    print(f"Current round {game_round}")
    print("Guess the number from 1 to 100")
    start = time.time()
    while tries > 0:
        user_answer = input("Your guess: ") 
        if user_answer == random_number: # win
            end = time.time()
            elapsed_time = round(end - start, 2)
            print(f"You won! It took you {user_attempts} attempts and {elapsed_time} seconds!\nDo you want to continue playing?\n1 - Yes\n2 - No")
            random_number = str(random.randint(1, 100))
            game_round += 1
            high_score += 1
            print(high_score)
            user_answer = input("Choose option: ")
            if user_answer == "1":
                clear()
                print(f"You have {tries} tries")
                input("Press any key...")
                easy_mode(tries, user_attempts, game_round, random_number, high_score)
                return high_score
            elif user_answer == "2":
                return high_score
            else: 
                print("Invalid option")
                input("Press any key...")
                return high_score
        elif user_answer > random_number:
            print(f"Your guess {user_answer} is HIGHER than selected number")
            input("Press any key...")
            tries -= 1
            user_attempts += 1
        elif user_answer < random_number:
            print(f"Your guess {user_answer} is LESS than selected number")
            input("Press any key...")
            tries -= 1
            user_attempts += 1
        else:
            print("Invalid option")
            input("Press any key...")
    print(f"You have no tries left! Selected number was {random_number}")
    input("Press any key...")
    return high_score

def medium_mode(tries, user_attempts):
    clear()
    print("Guess the number from 1 to 100")
    while tries > 0:
        user_answer = input("Your guess: ")
        if user_answer == random_number:
            print(f"You won! It took you {user_attempts} attempts!")
            input("Press any key...")
            return
        elif user_answer > random_number:
            print(f"Your guess {user_answer} is HIGHER than selected number")
            input("Press any key...")
            tries -= 1
            user_attempts += 1
        elif user_answer < random_number:
            print(f"Your guess {user_answer} is LESS than selected number")
            input("Press any key...")
            tries -= 1
            user_attempts += 1
        else:
            print("Invalid option")
            input("Press any key...")
    print(f"You have no tries left! Selected number was {random_number}")
    input("Press any key...")

def hard_mode(tries, user_attempts):
    clear()
    print("Guess the number from 1 to 100")
    while tries > 0:
        user_answer = input("Your guess: ")
        if user_answer == random_number:
            print(f"You won! It took you {user_attempts} attempts!")
            input("Press any key...")
            return
        elif user_answer > random_number:
            print(f"Your guess {user_answer} is HIGHER than selected number")
            input("Press any key...")
            tries -= 1
            user_attempts += 1
        elif user_answer < random_number:
            print(f"Your guess {user_answer} is LESS than selected number")
            input("Press any key...")
            tries -= 1
            user_attempts += 1
        else:
            print("Invalid option")
            input("Press any key...")
    print(f"You have no tries left! Selected number was {random_number}")
    input("Press any key...")

def clear():
    os.system("cls")

clear()

while True:
    random_number = str(random.randint(1, 100))
    clear()
    print(high_score)
    print(f"Welcome to numbrguessr game. The game where you have to guess random selected number from 1 to 100!\nChoose option: \n1 - Easy Mode     PR: 0\n2 - Medium Mode   PR: 0\n3 - Hard Mode     PR: 0")
    user_answer = input("-> ")
    if user_answer == "1":
        clear()
        tries = 3
        print(f"You have {tries} tries")
        input("Press any key...")
        easy_mode(tries, user_attempts, game_round, random_number, high_score)
    elif user_answer == "2":
        clear()
        tries = 2
        print(f"You have {tries} tries")
        input("Press any key...")
        medium_mode(tries, user_attempts)
    elif user_answer == "3":
        clear()
        tries = 1
        print(f"You have {tries} tries")
        input("Press any key...")
        hard_mode(tries, user_attempts)
    elif user_answer == "4":
        high_score += 1
    else:
        clear()
        print("Invalid option")
        input("Press any key...")