# Adventure text game
# Made by Lukáš Jurák
#Version 1.0.0

# imports
import random
import time as t
import sys



#variables
monster_list = ["spider", "goblin", "troll", "zombie", "skeleton", "ghost", "witch"]
player_hp = 10
# x = chance of random encounter (1/x)
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
    if player_name.lower() == "krbec" or player_name.lower() == "jaroslav":
        print("Congratulations! You win!")
        sys.exit()
    else:
        difficulty = input("Please choose your difficulty (easy, medium, hard): ")

        if difficulty == "easy":
            x = 6
            print("Do you need diapers?")
        elif difficulty == "medium":
            print("Solid choice.")
            x = 4
        elif difficulty == "hard":
            print("*Doom music intensifies*")
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

while (1): #house loop
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

while (1): #bartender loop
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
while (1): #decisions
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
naga_hp = 50 / x
print(naga_hp)  
while (1): #Naga fight
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
                       3. Give up
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
        if action == "2":
            print("You defend against the Naga's attack!")
            random.randint(1, x)
            if random.randint == 1:
                print("The Naga attacks you!")
                player_hp = player_hp - 3
                print(f"You took 3 damage! Your HP: {player_hp}")
                break
            else:
                print("You successfully defended against the Naga's attack!")
                continue
        if action == "3":
            if input("Never back down never what? ") == "never give up" or "Never give up":
                print("NEVER GIVE UP....")
                continue
            else:
                print("You gave up!")
                print("GAME OVER")
                sys.exit()
        if naga_hp <= 0:

            break
    if naga_hp <= 0:
        print("You defeated the Naga!")
        t.sleep(2)
        print("The snake dissapears and you hear loud bang behind you.")
        t.sleep(2)
        print("You turn around and see a chest.")
        t.sleep(2)
        print("You open the chest and find a key and a throphy of with small Naga head on it.")        
        break

print("You went back to the town to get some rest.")
t.sleep(3)
print("You went to the tavern and ordered some food and drink.")
t.sleep(2)
print("You sit down at the table and the bartender comes to you.")
t.sleep(2)
print("*He notices the scars on your face*")
print("'Busy night, huh?'")
t.sleep(2)
print("'So you defeated the Naga?'")

while (1): #bartender loop 2
    bar_input = input("""What do you say?
                      1. Yes, how did you know?
                      2. What?
                      """)
    if bar_input == "1":
        print("'Well I work as a bartender in this tavern and I hear a lot of stories.'")
        t.sleep(2)
        break
    if bar_input == "2":
        print("'You're the one who defeated the Naga, right?'")
        t.sleep(2)
        print("'I've heard a few stories about it...'")
        t.sleep(2)
        break
    else:
        print("Invalid option. Please choose from '1', '2', or '3'.")
        continue

print("'Well Hydra's next, right?'")
t.sleep(2)
print("'Do you want any tips to defeat the Hydra?'")
while (1): #decisions 2
    choice = input("y/n: ")
    if choice == "y":
        print("'Well the Hydra has many heads and you have to cut them all off.'")
        t.sleep(2)
        print("'But if you cut one head, two more will grow.'")
        t.sleep(2)
        print("'So you have to cut all the heads at once.'")
        t.sleep(2)
        print("'You'll need a special sword for that.'")
        t.sleep(2)
        print("'You'll have to go to the magic lake.'")
        t.sleep(2)
        print("' There's a Siren which will grant you any wish you want.'")
        t.sleep(2)
        print("'But be careful, she's dangerous.'")
        t.sleep(2)
        print("'She'll give you 3 riddles.'")
        t.sleep(2)
        print("'If you answer them correctly, she'll grant you a wish.'")
        t.sleep(2)
        print("'But if you fail to asnwer one of them she'll take your soul.'")
        t.sleep(2)
        print("'Here's a map to the lake.'")
        t.sleep(2)
        print("'Good luck!'")
        break
    elif choice == "n":
        print("'Well good luck!'")
        t.sleep(2)
        print("'You went to fight the Hydra but with every head you cut off two more grew.'")
        t.sleep(2)
        print("'Eventually you got tired and the Hydra killed you.'")
        print("GAME OVER")
        sys.exit()
    else:
        print("Invalid option. Please choose from 'y' or 'n'.")
        continue

print("You went to the magic lake.")
t.sleep(2)
print("You were looking for the siren but you couldn't find her.")
t.sleep(2)
print("Suddenly you hear a voice singing a song behind you.")
t.sleep(2)
print("You turn around and see the siren on a rock higlighted by the moonlight.")

while (1): #siren loop
    print("*she jumps from the rock and lands infront of you*")
    t.sleep(2)
    print("'Hello there'")
    t.sleep(2)
    print("'I've heard you're looking for a special sword.'")
    t.sleep(2)
    print("'I can grant it to you... But you'll have to answer my riddles first.'")
    t.sleep(2)
    print("'Are you ready?'")
    while (1):
        choice = input("y/n: ")
        if choice == "y":
            print("'Great! Let's begin.'")
            t.sleep(2)
            break
        elif choice == "n":
            print("'Well come back when you're ready.'")
            t.sleep(2)
            print("'You went to fight the Hydra but with every head you cut off two more grew.'")
            t.sleep(2)
            print("'Eventually you got tired and the Hydra killed you.'")
            print("GAME OVER")
            sys.exit()
        else:
            print("Invalid option. Please choose from 'y' or 'n'.")
            continue
    print("'What can you catch but not throw?'")
    while (1): #riddle 1
        choice = input("Answer: ")
        if choice.lower() == "cold" or choice.lower() == "a cold":
            print("'Correct!'")
            t.sleep(2)
            break
        else:
            print("'Wrong!'")
            t.sleep(2)
            print("'You failed to answer my riddle.'")
            t.sleep(2)
            print("'Now I'll take your soul!'")
            t.sleep(2)
            print("'You died!'")
            print("GAME OVER")
            sys.exit()
    while (1): #riddle 2
        print("'What has to be broken before you can use it?'")
        choice = input("Answer: ")
        if choice.lower() == "egg" or choice.lower() == "an egg":
            print("'Correct!'")
            t.sleep(2)
            break
        else:
            print("'Wrong!'")
            t.sleep(2)
            print("'You failed to answer my riddle.'")
            t.sleep(2)
            print("'Now I'll take your soul!'")
            t.sleep(2)
            print("'You died!'")
            print("GAME OVER")
            sys.exit()
    while (1): #riddle 3
        print("'What is always in front of you but can't be seen?'")
        choice = input("Answer: ")
        if choice.lower() == "future" or choice.lower() == "the future":
            print("'Correct!'")
            t.sleep(2)
            break
        else:
            print("'Wrong!'")
            t.sleep(2)
            print("'You failed to answer my riddle.'")
            t.sleep(2)
            print("'Now I'll take your soul!'")
            t.sleep(2)
            print("'You died!'")
            print("GAME OVER")
            sys.exit()
    print("'You answered all my riddles correctly.'")
    break

print("'Now I'll grant you a wish.'")
t.sleep(2)
print("'The question is what do you want?'")
t.sleep(2)
print("'Do you want the Excalibur to defeat the Hydra?'")
t.sleep(2)
print("'Or is there anything you would like more?'")
t.sleep(2)
print("'Think carefully.'")
t.sleep(2)
wish = input("What do you wish for? ")
if wish.lower() == "excalibur" or wish.lower() == "sword":
    print("'Very well then.'")
else:
    print(f"'Your wish for {wish} and it has been granted.'")
    t.sleep(2)
    print("You forgot about the Twilight forest and lived your life.")
    sys.exit()
print("'Here you go.'")
t.sleep(2)
print("You got the Excalibur and went to fight the Hydra.")
t.sleep(2)
player_hp = 10
hydra_hp = 60 / x
while (1): #Hydra fight
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
                       3. Give up
                       """)
        if action == "1":
            print("You swing your sword at the Hydra.")
            random.randint(1, x)
            if random.randint(1, x) == 1:
                hydra_hp = hydra_hp - 3
                print("You hit the Hydra and dealt 3 damage!")
                print(f"Hydra's HP: {hydra_hp}")
                break
            else:
                print("The Hydra dodges your attack!")
                random.randint(1, x)
                if random.randint == 1:
                    print("The Hydra attacks you!")
                    player_hp = player_hp - 3
                    print(f"You took 3 damage! Your HP: {player_hp}")
                    break
                continue
        if action == "2":
            print("You defend against the Hydra's attack!")
            random.randint(1, x)
            if random.randint == 1:
                print("The Hydra attacks you!")
                player_hp = player_hp - 3
                print(f"You took 3 damage! Your HP: {player_hp}")
                break
            else:
                print("You successfully defended against the Hydra's attack!")
                continue
        if action == "3":
            if input("Never back down never what? ") == "never give up" or "Never give up":
                print("NEVER GIVE UP....")
                continue
            else:
                print("You gave up!")
                print("GAME OVER")
                sys.exit()
        if hydra_hp <= 0:

            break
    if hydra_hp <= 0:
        print("You defeated the Hydra!")
        t.sleep(2)
        print("The body dissapears and you hear loud bang behind you.")
        t.sleep(2)
        print("You turn around and see a chest.")
        t.sleep(2)
        print("You open the chest and find a second key and a throphy of with small Hydra head on it.")   
        break

print("You went back to the town to get some rest.")
t.sleep(3)
print("In the morning you encounter the bartender.")
t.sleep(2)
print("'So you defeated the Hydra?'")
t.sleep(2)
print("'Now you have to defeat the Linch.'")
t.sleep(2)
print("'You'll need a special armor for that.'")
t.sleep(2)
print("'I know someone who could help you with that.'")
t.sleep(2)
print("'He lives in the mountains.'")
t.sleep(2)
print("'Here's a map.'")
t.sleep(2)
print("'Good luck!'")
t.sleep(3)
print("You went to the mountains.")
t.sleep(2)
print("You saw a giant entrance in ine of the mountain a decide to go there.")
t.sleep(2)
print("You enter the cave and see a semi-god blacksmith.")
t.sleep(2)
print("*He notices you*")
t.sleep(2)
print("'What do you want?' *he says in a deep voice*")
t.sleep(2)
print("I was told you are the on who can make me a special armor to defeat the Linch. *You respond to him*")
t.sleep(2)
print("'I can make you the armor but you'll have to bring me some materials.'")
t.sleep(2)
print("'I need 3 pieces of iron and 1 piece of gold.'")
t.sleep(2)
print("'You can find them in the mountains.'")
t.sleep(2) 
print("'Good luck!'")
t.sleep(2)
print("You went to find the materials.")
t.sleep(2)
print("You found the iron in the mountains but you couldn't find the gold.")
t.sleep(2)
print("You decided to go back to the blacksmith.")
t.sleep(2)
print("*You give him the iron*")
t.sleep(2)
print("'Thank you. But where's the gold?'")
t.sleep(2)
print("I couldn't find it. *You respond to him*")
t.sleep(2)
print("'Well I have some gold but I can't give it to you for free.'")
t.sleep(2)
print("'After you your fight with the Linch you'll give me the Excalibur.'")
t.sleep(2)
print("'Deal?'")
t.sleep(2)
print("Do you accept his offer?")
choice = input("y/n: ")
if choice.lower() == "y":
    print("Deal! *You respond to him*")
    t.sleep(3)
    print("'Here's the armor.'")
    t.sleep(2)
    print("You got the armor and went on your way to fight the Linch.")
else:
    print("You went to fight the Linch without the armor but you couldn't defeat him.")
    t.sleep(2)
    print("You died!")
    print("GAME OVER")
    sys.exit()
print("You went on your way to fight the Linch.")
if random.randint(1, x) == 1:
    monster = random.choice(monster_list)
    print(f"you encountered a {monster}!")
    result = fight(input("What do you do? (kick, hit, defend, random): "))
t.sleep(2)
print("You see a weird castle with levitating towers.")
t.sleep(2)
print("That must be the Linch's castle. *You think to yourself*")
t.sleep(2)
print("You enter the castle and it's full of monsters!")
t.sleep(3)
print("You fight your way through the castle.")
t.sleep(2)
print("You finally reach the Linch's throne room.")
t.sleep(2)
print("You see the Linch sitting on his throne.")
t.sleep(2)
print("*He stands up and says:* How dare you enter my castle!")
t.sleep(2)
print("'You're going to regret this!'")
t.sleep(2)
print("*He reaches for his bow and starts shooting at you*")

player_hp = 10
linch_hp = 60 / x
while (1): #Linch fight
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
                       3. Give up
                       """)
        if action == "1":
            print("You swing your sword at the Linch.")
            random.randint(1, x)
            if random.randint(1, x) == 1:
                linch_hp = linch_hp - 3
                print("You hit the Linch and dealt 3 damage!")
                print(f"Linch's HP: {linch_hp}")
                break
            else:
                print("The Linch dodges your attack!")
                random.randint(1, x)
                if random.randint == 1:
                    print("The Linch attacks you!")
                    player_hp = player_hp - 3
                    print(f"You took 3 damage! Your HP: {player_hp}")
                    break
                continue
        if action == "2":
            print("You defend against the Linch's attack!")
            random.randint(1, x)
            if random.randint == 1:
                print("The Linch attacks you!")
                player_hp = player_hp - 3
                print(f"You took 3 damage! Your HP: {player_hp}")
                break
            else:
                print("You successfully defended against the Linch's attack!")
                continue
        if action == "3":
            if input("Never back down never what? ") == "never give up" or "Never give up":
                print("NEVER GIVE UP....")
                continue
            else:
                print("You gave up!")
                print("GAME OVER")
                sys.exit()
        if linch_hp <= 0:

            break
    if linch_hp <= 0:
        print("You defeated the Linch!")
        t.sleep(2)
        print("The skeleton dissapears and you hear loud bang behind you.")
        t.sleep(2)
        print("You turn around and see a chest.")
        t.sleep(2)
        print("You open the chest and find a second key and a throphy of with small Linch head on it.")   
        break

t.sleep(2)
print("You went back to the mountains to give the Excalibur to the blacksmith.")    
t.sleep(2)
print("*You give him the Excalibur*")
t.sleep(2)
print("'Thank you for keeping your promise.'")
t.sleep(2)
print("'Good luck with your journey.'")
t.sleep(2)
print("You went along with your journey.")
t.sleep(2)
print("You decide to go back to the town to get some rest.")
if random.randint(1, x) == 1:
    monster = random.choice(monster_list)
    print(f"you encountered a {monster}!")
    result = fight(input("What do you do? (kick, hit, defend, random): "))
t.sleep(2)
print("In the morning you encounter the bartender once again.")
t.sleep(2)
print("'So you defeated the Linch?'")
t.sleep(2)
print("'Now you can go to the castle.'")
t.sleep(2)
print("'Be careful, no one knows what lives there.'")
t.sleep(2)
print("'Good luck!'")
t.sleep(2)
print("You went to the castle.")
t.sleep(2)
print("After a long journey you finally reach the castle.")
t.sleep(2)
print("You see a giant castle with many towers.")
t.sleep(2)
print("As you enter the castle many monsters start attacking you.")
t.sleep(2)
print("You fight your way through the castle and find yourself in large room with throne.")
t.sleep(2)
print("As you get closer the lights starts to dim and moonlight shines through the windows onto the throne.")
t.sleep(2)
print("You look closely and realize that the throne is empty.")
t.sleep(2)
print("You notice that there a mirror lying on the throne.")
t.sleep(2)
print("You pick up the mirror and see a reflection of yourself.")
t.sleep(2)
print("Suddenly the mirror starts glowing and you see a reflection of the final boss.")
t.sleep(2)
print("It's you!")
t.sleep(2)
print("You realize that you are the final boss.")
t.sleep(2)
print("Everything that has ever happened to the Twilight forest was because of you.")
t.sleep(2)
print("You were cursed by the forest")
t.sleep(2)
print("Everything around you blacks out.")
t.sleep(2)
print("Fear fills your mind")
t.sleep(2)
print("You're lost in the darkness and start to be paranoid")
t.sleep(2)
print("You feel like everything wants to kill you")
t.sleep(2)
print("You don't even trust yourself!")
t.sleep(2)
print("Suddenly a bird flyes outside. But for you it was like a pendulum swinging above you")
t.sleep(2)
print("You take a step and there's a small dent in the floor. For you it's a deep pit")
t.sleep(2)
print("You've decided to sit on the throne as you think it's the safest place in the room")
t.sleep(5)
print("Many days have passed and you haven't moved an inch....")
t.sleep(2)
print("Eventually you've died and the whole Twilight forest has dissapeared with you....")
t.sleep(5)
print("THE END")

