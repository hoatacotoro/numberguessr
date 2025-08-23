import os
import sys
import time
import random
import threading

version = "0.0.1"

tries = 0
user_attempts = 0
game_round = 1
timer = 0
high_score = 0
current_score_easy = 0
current_score_medium = 0
current_score_hard = 0

class score:
    def __init__(self):
        self.easy_score = 0
        self.medium_score = 0
        self.hard_score = 0

    def add_score_easy(self):
        self.easy_score += 1

    def add_score_medium(self):
        self.medium_score += 1

    def add_score_hard(self):
        self.hard_score += 1

    def reset_score(self):
        self.easy_score = 0
        self.medium_score = 0
        self.hard_score = 0

game = score()

def hint():
    time.sleep(10)
    # print("\nHey are you stupid?")
    # sys.stdout.write("\033[F")
    sys.stdout.write("\nHINT: You have to enter a number from 1 to 100 that have been randomly selected by computer,"
                     "\n      if your answer is not correct i will give you a hint if it is MORE or LESS than selected number \nYour guess: ")
    # sys.stdout.write("\033[K")
    sys.stdout.flush()

def easy_mode(tries, user_attempts, game_round, random_number, high_score):
    clear()
    # print(random_number)
    print(f"Current round {game_round}")
    print("Guess the number from 1 to 100")
    threading.Thread(target=hint, args=(), daemon=True).start()
    start = time.time()
    while tries > 0:
        user_answer = input("Your guess: ")
        if user_answer == random_number: # win
            end = time.time()
            elapsed_time = round(end - start, 2)
            print(f"You won! It took you {user_attempts} attempts and {elapsed_time} seconds!\nDo you want to continue playing?\n1 - Yes\n2 - No")
            random_number = str(random.randint(1, 100))
            game_round += 1 # here
            game.add_score_easy()
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

def medium_mode(tries, user_attempts, game_round, random_number, high_score):
    clear()
    # print(random_number)
    print(f"Current round {game_round}")
    print("Guess the number from 1 to 100")
    threading.Thread(target=hint, args=(), daemon=True).start()
    start = time.time()
    while tries > 0:
        user_answer = input("Your guess: ") 
        if user_answer == random_number: # win
            end = time.time()
            elapsed_time = round(end - start, 2)
            print(f"You won! It took you {user_attempts} attempts and {elapsed_time} seconds!\nDo you want to continue playing?\n1 - Yes\n2 - No")
            random_number = str(random.randint(1, 100))
            game_round += 1 # here
            game.add_score_medium()
            user_answer = input("Choose option: ")
            if user_answer == "1":
                clear()
                print(f"You have {tries} tries")
                input("Press any key...")
                medium_mode(tries, user_attempts, game_round, random_number, high_score)
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

def hard_mode(tries, user_attempts, game_round, random_number, high_score):
    clear()
    # print(random_number)
    print(f"Current round {game_round}")
    print("Guess the number from 1 to 100")
    threading.Thread(target=hint, args=(), daemon=True).start()
    start = time.time()
    while tries > 0:
        user_answer = input("Your guess: ") 
        if user_answer == random_number: # win
            end = time.time()
            elapsed_time = round(end - start, 2)
            print(f"You won! It took you {user_attempts} attempts and {elapsed_time} seconds!\nDo you want to continue playing?\n1 - Yes\n2 - No")
            random_number = str(random.randint(1, 100))
            game_round += 1 # here
            game.add_score_hard()
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

def clear():
    os.system("cls")

clear()

while True:
    random_number = str(random.randint(1, 100))
    clear()
    if game.easy_score > current_score_easy:
        current_score_easy = game.easy_score
    if game.medium_score > current_score_medium:
        current_score_medium = game.medium_score
    if game.hard_score > current_score_hard:
        current_score_hard = game.hard_score
    # print(f"Current score: {game.easy_score}, {game.medium_score}, {game.hard_score}")
    print(
        f"Welcome to numbrguessr game. The game where you have to guess random selected number from 1 to 100!"
        f"\nChoose option: \n1 - Easy Mode     PR: {current_score_easy}\n2 - Medium Mode   PR: {current_score_medium}\n3 - Hard Mode     PR: {current_score_hard}")
    user_answer = input("-> ")
    if user_answer == "1":
        game.reset_score()
        clear()
        tries = 10
        print(f"You have {tries} tries")
        input("Press any key...")
        easy_mode(tries, user_attempts, game_round, random_number, high_score)
    elif user_answer == "2":
        game.reset_score()
        clear()
        tries = 6
        print(f"You have {tries} tries")
        input("Press any key...")
        medium_mode(tries, user_attempts, game_round, random_number, high_score)
    elif user_answer == "3":
        game.reset_score()
        clear()
        tries = 1
        print(f"You have {tries} tries")
        input("Press any key...")
        hard_mode(tries, user_attempts, game_round, random_number, high_score)
    elif user_answer == "gghh":
        game.add_score_easy()
    elif user_answer == "yuyu":
        game.add_score_medium()
    elif user_answer == "boom":
        game.add_score_hard()
    elif user_answer == "linas":
        game.reset_score()
    else:
        clear()
        print("Invalid option")
        input("Press any key...")