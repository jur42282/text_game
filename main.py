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





while (1): #Game settings
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

print("You are walking through the forest. It's getting dark.")
print("QUEST: Find some place to stay at the night")

while (1):  #Game loop 1. night
    print("You have 3 options: nearby cave, old house, or sleep in the forest")
    sleep_places = ["cave", "house", "forest"]
    sleep_place_input = input("Where do you want to sleep?")
    
    if sleep_place_input == "cave":
        print("You went to the cave...")
        if random.randint(1, x):
            print("You encountered a spider!")
            monster = "spider"
            result = fight(input("What do you do? (kick, hit, defend, random): "))
            print("You slept well in the cave.")
            break
        else:
            print("You slept well in the cave.")
            break
    elif sleep_place_input == "house":
        print("You went to the house...")
        if random.randint(1, x):
            print("You encountered a Witch!")
            monster = "witch"
            result = fight(input("What do you do? (kick, hit, defend, random): "))
            print("You slept well in the house.")
            break
        else:
            print("You slept well in the house.")
            break
    elif sleep_place_input == "forest":
        if random.randint(1, x):
            monster = random.choice(monster_list)
            print(f"You encountered a {monster}!") 
            result = fight(input("What do you do? (kick, hit, defend, random): "))
            print("You slept well in the forest.")
            break
        else:
            print("You slept well in the forest.")
            break

    else:
        print("Invalid option. Please choose from 'cave', 'house', or 'forest'.")
        continue


while (1):
    print("You woke up in the morning.")
    if sleep_place_input == "house":
        print("You decided to look around the house.")
        print("You found a book!")
        print("The book's name is The Tale of the Twilight Forest")
        print("You opened the book and started reading...")
        print("You read about the forest and its inhabitants.")
        print("You turn to the last page and read:")
        print("""In twilight's grasp, a legend thrives,
    Three bosses guard where darkness thrives.
    Defeat them all, the castle's key,
    To face the final boss, one's destiny.""")
        break
    if sleep_place_input != "house":
        print("You decided to go on your journey.")
        print("You see a house in the distance and decide to go there.")
        print("In the house you found a book!")
        print("The book's name is The Tale of the Twilight Forest")
        print("You opened the book and started reading...")
        print("You read about the forest and its inhabitants.")
        print("You turn to the last page and read:")
        print("""In twilight's grasp, a legend thrives,
    Three bosses guard where darkness thrives.
    Defeat them all, the castle's key,
    To face the final boss, one's destiny.""")
        break
