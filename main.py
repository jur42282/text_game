# Adventure text game
# Made by Lukáš Jurák
#Version 0.0.5

# imports
import random
import time as t
import sys

# print("vydal jsi se na cestu")
# if random.randint(1, x) == 1:
#     monster = random.choice(monster_list)
#     print(f"you encountered a {monster}!")
#     result = fight(input("What do you do? (kick, hit, defend, random): "))

#variables
# WIP secret_boss= "D1dnt"
monster_list = ["spider", "goblin", "troll", "zombie", "skeleton", "ghost", "witch"]
player_hp = 10
# x = chance of random encounter (1/x)
#
#
#
#
#npcs
# bar_yes = ["yes", "y", "yeah", "sure", "ok", "okay", "yep", "yup", "yea"]
# bar_no = ["no", "n", "nope", "nah"]

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
            print(f"You successfully defended against the {monster}'s attack!") 
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
    elif difficulty == "medium":
        x = 4
    elif difficulty == "hard":
        x = 2
    else:
        print("Invalid difficulty. Please choose from 'easy', 'medium', or 'hard'.")
        t.sleep(2)
        continue

    print(f"Name: {player_name}, difficulty: {difficulty}")
    agree = input("Are you sure? (y/n): ")
    if agree == "n":
        print("Reloading settings")
        t.sleep(.5)
        print(".")
        t.sleep(.5)
        print("..")
        t.sleep(.5)
        print("...")
    if agree == "y":
        print("Let's go!")
        t.sleep(5)
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
    elif sleep_place_input == "house" or "old house":
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

t.sleep(5)

while (1):
    print("You woke up in the morning.")
    if sleep_place_input == "house" or "old house":
        print("You decided to look around the house.")
        t.sleep(2)
        print("You found a book!")
        t.sleep(2)
        print("The book's name is The Tale of the Twilight Forest")
        t.sleep(2)
        print("You opened the book and started reading...")
        t.sleep(2)
        print("You read about the forest and its inhabitants.")
        t.sleep(2)
        print("You turn to the last page and read:")
        t.sleep(2)
        print("""   In twilight's grasp, a legend thrives,
    Three bosses guard where darkness thrives.
    Defeat them all, the castle's key,
    To face the final boss, one's destiny.""")
        break
    if sleep_place_input != "house":
        print("You decided to go on your journey.")
        if random.randint(1, x) == 1:
            monster = random.choice(monster_list)
            print(f"you encountered a {monster}!")
            result = fight(input("What do you do? (kick, hit, defend, random): "))
        
        t.sleep(2)
        print("You see a house in the distance and decide to go there.")
        t.sleep(2)
        print("In the house you found a book!")
        t.sleep(2)
        print("The book's name is The Tale of the Twilight Forest")
        t.sleep(2)
        print("You opened the book and started reading...")
        t.sleep(2)
        print("You read about the forest and its inhabitants.")
        t.sleep(2)
        print("You turn to the last page and read:")
        sleep(2000)
        print("""In twilight's grasp, a legend thrives,
    Three bosses guard where darkness thrives.
    Defeat them all, the castle's key,
    To face the final boss, one's destiny.""")
        break
t.sleep(5)
print("You decided to continue in your journey.")
if random.randint(1, x) == 1:
    monster = random.choice(monster_list)
    print(f"you encountered a {monster}!")
    result = fight(input("What do you do? (kick, hit, defend, random): "))

print("You see a village in the distance and decide to go there.")
t.sleep(5)
print("You see a tavern and decide to go there.")
t.sleep(5)
print("You talk to the bartender and ask him about the book.")
t.sleep(5)

while (1):
    bar_input = input("""What do you ask the bartender?
                      1. What is the Twilight Forest?
                      2. What are the bosses?
                      3. What is the castle?
                      4. What is the final boss?
                      5. Say goodbye.
                      """)
    if bar_input == "1":
        print("""The Twilight Forest is a forest that is said to be cursed.
              But it hasn't been that way.
              It's a peaceful place where many people lived.
              But one day, a mysterious castle appeared in the middle of the forest and .""")
        t.sleep(5)
        continue
    if bar_input == "2":
        print("""The bosses are three mysterious creatures that appeared in the forest.
              The first one is Naga. Snake like creature that lives near the water in it's labyrinth.
              The second one is Hydra. A creature with many heads that lives under a hill in the forest.
              The third one is a Linch. A skeleton like creature that can do magic. It lives in weird castle wtih levitating towers.""")
        t.sleep(5)
        continue
    if bar_input == "3":
        print("""The castle is a mysterious castle that appeared in the middle of the forest.
              It is said that the final boss lives there.""")
        t.sleep(5)
        continue
    if bar_input == "4":
        print("""The final boss is a mysterious creature that lives in the castle.
              It is said that it is the one who cursed the forest.
              There are many rumors about it, but no one knows what it really is.""")
        t.sleep(5)
        continue
    if bar_input == "5":
        print("You say goodbye to the bartender and leave the tavern.")
        t.sleep(3)
        break
    else:
        print("Invalid option. Please choose from '1', '2', '3', '4', or '5'.")
        continue

print("As you leave the tavern a map suddenly appears in your pocket.")
t.sleep(2)
print("You look at the map and see the locations of the bosses.")
t.sleep(2)
while (1):
    print("Do you want to continue your journey?")
    choice = input("y/n: ")
    if choice == "n":
        print("You throw the map away and forget about all of this....")
        sys.exit()
    elif choice == "y":
        print("You decided to continue your journey.")
        break
    else:
        print("Invalid option. Please choose from 'y' or 'n'.")
        continue

print("You went to the Naga.")
t.sleep(2)
print("You see a simple labyrinth and infront of the entrance is a sword and some armor.")
t.sleep(2)
print("You put on the armor ,take the sword and go into the labyrinth.")
print("It is really simple and you find yourself in the center of it in no time.")
t.sleep(2)
print("Suddenly the ground starts shaking and you hear a loud roar.")
print("You turn around and see giant snake like creature!")

while (1):
    naga_hp = 50 / x
    print(naga_hp)    
    while (1):
        if player_hp <= 0:
            print("You died!")
            print("Do you want to try again?")
            choice = input("y/n: ")
            if choice == "y":
                print("You decided to try again.")
                break
            elif choice == "n":
                print("You decided to give up.")
                sys.exit()
            else:
                print("Invalid option. Please choose from 'y' or 'n'.")
                continue        
        action = input("""What do you do?
                       1. Swing your sword
                       2. Defend 
                       3. Dodge it's attack
                       4. Give up
                       """)
        if action == "1":
            print("You swing your sword at the Naga.")
            random.randint(1, x)
            if random.randint(1, x) == 1:
                naga_hp = naga_hp - 3
                print("You hit the Naga and dealt 3 damage!")
                print(f"Naga's HP: {naga_hp}")
                break
            else:
                print("The Naga dodges your attack!")
                random.randint(1, x)
                if random.randint == 1:
                    print("The Naga attacks you!")
                    player_hp = player_hp - 3
                    print(f"You took 3 damage! Your HP: {player_hp}")
                    break
                continue
        
