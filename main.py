# Adventure text game
# Made by Lukáš Jurák

# imports
import random

# print("vydal jsi se na cestu")
# if random.randint(1, x) == 1:
#     monster = random.choice(monster_list)
#     print(f"you encountered a {monster}!")
#     result = fight(input("What do you do? (kick, hit, defend, random): "))

#variables
monster_list = ["spider", "goblin", "troll", "zombie", "skeleton", "ghost", "witch"]
player_hp = 10
# x = chance of random encounter (default 1-3 chance)
#
#
#
#

#random encounter fights
def fight(player_move):
    computer_move = random.randint(1, 10)
    
    if player_move == "kick":
        if computer_move <= 3:
            print(f"You kicked the {monster} and it ran away!")
        else:
            print(f"The {monster} dodged your kick!") 
    elif player_move == "hit":
        if computer_move <= 5:
            print(f"You hit the {monster} and it ran away!") 
        else:
            print(f"The {monster} blocked your hit!") 
    elif player_move == "defend":
        if computer_move <= 7:
            print(f"You successfully defended against the computer's attack!") 
        else:
            print(f"The {monster}] broke through your defense and dealt 3 damage!")
            player_hp -= 3 
    elif player_move == "random":
        moves = ["kick", "hit", "defend"]
        random_move = random.choice(moves)
        print(fight(random_move)) 
    else:
        print("Invalid move. Please choose from 'kick', 'hit', 'defend', or 'random'.")
print(f"Your HP: {player_hp}")




#start
while True:
    print("Welcome to the game!")
    player_name = input("Please enter your nickname: ")
    difficulty = input("Please choose your difficulty (easy, medium, hard): ")

    if difficulty == "easy":
        x = 6
    if difficulty == "medium":
        x = 4
    if difficulty == "hard":
        x = 2
    else:
        print("Invalid difficulty. Please choose from 'easy', 'medium', or 'hard'.")
        continue

    print(f"Name: {player_name}, difficulty: {difficulty}")
    agree = input("Are you sure? (y/n): ")
    if agree == "n":
        print("Reloading settings")
    if agree == "y":
        print("Let's go!")
        break
