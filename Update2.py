# Variables
map_perception = 15
map_snatch = 17
gold_for_map = "gold"
persuasion_for_map = ["persuasion", " persuasion", "  persuasion"]
items = ["map"]

# Continue after user input
# input("Press Enter to continue...")

def start():
    # give some prompts
    print(
        "\nThe ornate black carriage roars along the narrow winding road leading to Castle Ravenloft."
        "\nPeering out one window, you watch rocks fall one thousand feet to the river below. "
        "\nAhead, the carriage master turns his cowled face towards you, his eyes shrouded under his tattered leather "
        "tricorn hat. "
        "\nReaching back with an arm too long for his body, he gently pushes you back into the carriage and locks the "
        "door. "
        "\nWhile your black carriage rockets through the chilly night air, wild horses speeding you through the woods "
        "toward your final destination – Castle Ravenloft. "
        "\nYou’ve been preparing for this assault for some time and still your stomach churns in knots of fear. "
        "\nA lone wolf howls in the night as you swallow back your vomit and think of the task before you. "
        "\nTo free Barovia and its people from the clutches of monster and mist, Strahd von Zarovich must "
        "die. Many have tried before you, but none have triumphed. "
        "\nThe smell of incense burns in your nose. Madam Eva, the old, hunched Vistani woman with piercing eyes and "
        "a strange smile, sits in the carriage with you. "
        "\nThe fortune-teller offered to take you in her carriage to the castle in exchange for having your fortunes "
        "read. "
        "\nAt the time it seemed a good way to avoid the wolves and other dangers of the wood, but looking into "
        "her inscrutable face, you can’t be sure. "
        "\nMadam Eva pulls a deck of tarokka cards from a box in her lap.")
    map()

def map():
    perception_check = int(input("\nPerception Check (Wisdom + roll): "))
    if perception_check >= map_perception:
        print("\nYou find a full map of Castle Ravenloft, within Madam Eva’s Box.")
        gold_persuasion = input("\nWhat do you do?: ")
        if gold_persuasion.lower() == gold_for_map:
            try:
                gold = int(input("How much do you offer?: "))
                if gold >= 500:
                    print("\nMadam Eva gives your group the map.")
                    input("Press Enter to continue...")
                    print("\nShe shuffles the cards and begins setting them on a small table in the middle of the carriage.")
                    input("Press Enter to continue...")
                    reading()
                else:
                    print("\nShe shuffles the cards and begins setting them on a small table in the middle of the carriage.")
            except ValueError:
                print("Please enter a valid number for gold.")
        elif gold_persuasion.lower() in persuasion_for_map:
            try:
                persuasion = int(input("Persuasion Check (Charisma + roll): "))
                if persuasion >= 11:
                    print("Madam Eva gives your group the map.")
                    input("Press Enter to continue...")
                    print("She shuffles the cards and begins setting them on a small table in the middle of the carriage.")
                    input("Press Enter to continue...")
                    reading()
                else:
                    print("She shuffles the cards and begins setting them on a small table in the middle of the carriage.")
                    input("Press Enter to continue...")
                    reading()
            except ValueError:
                print("Please enter a valid number for persuasion.")
        else:
            print("She shuffles the cards and begins setting them on a small table in the middle of the carriage.")
            input("Press Enter to continue...")
            reading()
    else:
        print("She shuffles the cards and begins setting them on a small table in the middle of the carriage.")
        input("Press Enter to continue...")
        reading()

def reading():
    print("You look down and see:")
    print("1. The Tome of Strahd - This card tells of history. Knowledge of the ancient will help you better understand your enemy.")
    print("2. The Holy Symbol of Ravenkind - This card tells of a powerful force for good and protection, a holy symbol of great hope.")
    print("3. The Sunsword - This is a card of power and strength. It tells of a weapon of vengeance: a sword of sunlight.")
    print("4. Strahd’s enemy - This card sheds light on one who will help you greatly in the battle against darkness.")
    print("5. Strahd’s location - Your enemy is a creature of darkness, whose powers are beyond mortality. This card will lead you to him!")

    print(
        "You are all in a carriage racing towards Castle Ravenloft. Lightning streaks through the sky and thunder "
        "rumbles all around them.")
    map_in_inventory = input("\nDoes your party have the map? (yes/no): ").lower()
    if map_in_inventory == "no":
        slight_of_hand = input("\nSlight of hand Check (Dex + roll): ")
        try:
            if int(slight_of_hand) == map_snatch:
                print("Success: You fall forward and land onto Madam Eva and take the map.")
            else:
                print("Failure: As you fall, Madam Eva’s box closes.")
        except ValueError:
            print("Please enter a valid number for your Sleight of Hand check.")
    else:
        arrive()

def arrive():
    print(
        'The carriage careens into the courtyard of Castle Ravenloft and crashes as the horses fall mysteriously dead. '
        'You are hurled from the carriage into the courtyard. As you rise, muddy and soaked through, a massive and ghostly apparition of Strahd appears before you. '
        'He cackles at your misfortune and raises an hourglass filled with blood-red sand. He looks down upon you and says: '
        '"I am the ancient. I am the land. I am Count Strahd von Zarovich. Gaze upon me and tremble, foolish hunters. '
        'The walls of Castle Ravenloft are my domain, and here, I reign supreme. You wish to hunt me down? So be it. We are but four hours from planar midnight. '
        'I grant you four cosmic hours to explore the castle, uncover its mysteries, and confront me. But when the sands of time run out, so too will your lives." '
        '"Welcome to Castle Ravenloft. Welcome to your doom!"'
    )

    print("\nThe ground beneath you shakes as the walls of Castle Ravenloft rise before you. The entrance is imposing and foreboding.")
    choice = input("\nThe castle entrance beckons, but something catches your eye to the left: a faint light flickers from the ruins of an old chapel. "
                   "\nDo you investigate the chapel (type 'chapel') or proceed to the castle entrance (type 'castle')? ").lower()

    if choice == "chapel":
        chapel()
    elif choice == "castle":
        castle_entrance()
    else:
        print("\nConfused by the options, you hesitate for a moment, but the sand in the hourglass keeps slipping away...")
        arrive()  # Recurse if the user doesn't provide a valid input

def chapel():
    print("\nYou head towards the chapel, moving past the fallen stone statues that line the path. As you approach, the faint light grows stronger.")
    print("The chapel is in ruins, but there is something unsettling about its serenity. A small window reveals a flickering candlelight within.")
    print("\nThe door creaks open, and you step inside.")
    print("\nThe interior is dimly lit by candles. The walls are adorned with faded murals of forgotten saints. In the center of the room is a figure—dressed in tattered robes—kneeling in prayer.")
    print("\nThe figure looks up and smiles. A knowing, almost predatory grin. 'I’ve been waiting for you, adventurers. Come closer, there is much to learn.'")

    # Choices inside the chapel
    choice = input("\nDo you approach the figure (type 'approach') or do you leave the chapel (type 'leave')? ").lower()

    if choice == "approach":
        print("\nYou approach cautiously, sensing something strange about the figure. As you get closer, the smile fades, and the figure stands, revealing itself to be a vampire spawn.")
        print("\nThe figure hisses, 'So... you have come to the castle to challenge Strahd. Let me give you a warning: none leave this place alive.'")
        combat()
    elif choice == "leave":
        print("\nYou step back carefully, sensing the danger. The figure's predatory grin fades as you retreat.")
        print("\nThe chapel seems to exude an oppressive energy as you leave, and the faint sound of a growl echoes behind you.")
        print("\nYou find yourself back at the castle entrance, the sand in the hourglass slipping away.")
        castle_entrance()
    else:
        print("\nIndecision freezes you momentarily. The figure's grin grows wider as the candlelight flickers ominously.")
        chapel()  # Recurse for valid input

def combat():
    print("\nThe vampire spawn lunges toward you, fangs bared and claws outstretched!")
    print("\nPrepare for battle!")

    # A basic combat sequence
    health = 20  # Player health
    vamp_health = 25  # Vampire spawn health
    while health > 0 and vamp_health > 0:
        action = input("\nDo you attack with your weapon (type 'attack') or try to retreat (type 'retreat')? ").lower()

        if action == "attack":
            damage = int(input("Roll for damage (enter a number 1-10): "))
            vamp_health -= damage
            print(f"\nYou strike the vampire for {damage} damage! Its health is now {vamp_health}.")
            if vamp_health > 0:
                vamp_damage = 7  # Fixed vampire damage
                health -= vamp_damage
                print(f"\nThe vampire claws at you, dealing {vamp_damage} damage. Your health is now {health}.")
        elif action == "retreat":
            print("\nYou stumble backward, making your way out of the chapel. The vampire spawn does not pursue but snarls as you leave.")
            print("\nYou find yourself back at the castle entrance, shaken but alive.")
            castle_entrance()
            return  # End the combat loop if retreating
        else:
            print("\nIndecision could be your downfall!")
    
    if health > 0:
        print("\nWith one final strike, you defeat the vampire spawn! Its body crumples to the floor and dissolves into ash.")
        print("\nIn the remains, you find a strange holy relic—a silver amulet etched with the sigil of the Morninglord.")
        items.append("silver amulet")
        print("\nYou take the amulet and leave the chapel, returning to the castle entrance.")
        castle_entrance()
    else:
        print("\nThe vampire spawn overpowers you. Your vision fades as darkness consumes you.")
        game_over()

def castle_entrance():
    print("\nStanding before the massive doors of Castle Ravenloft, you feel a chill run down your spine. The hourglass looms in your mind as the sands continue to fall.")
    choice = input("\nDo you push open the doors (type 'enter') or inspect the courtyard for clues (type 'inspect')? ").lower()

    if choice == "enter":
        print("\nThe ancient doors creak open, revealing the grand but foreboding entry hall of Castle Ravenloft.")
        print("\nThe sound of your footsteps echoes as you step inside.")
        castle_hall()
    elif choice == "inspect":
        print("\nYou search the courtyard, looking for anything that might help in your quest.")
        if "silver amulet" in items:
            print("\nThe silver amulet you found begins to glow faintly. A hidden engraving on the castle wall catches your attention.")
            print("\nYou discover a secret entrance leading to the lower levels of the castle.")
            secret_passage()
        else:
            print("\nYou find nothing of value. The castle entrance beckons.")
            castle_entrance()
    else:
        print("\nIndecision wastes precious time. The hourglass sands continue to fall.")
        castle_entrance()

def castle_hall():
    print("\nThe hall is vast and cold, lit by flickering torches. The air smells of decay and old stone.")
    print("\nIn the center of the room, a massive staircase leads upward, while corridors extend to the left and right.")
    choice = input("\nDo you ascend the staircase (type 'upstairs'), explore the left corridor (type 'left'), or the right corridor (type 'right')? ").lower()

    if choice == "upstairs":
        upstairs()
    elif choice == "left":
        left_corridor()
    elif choice == "right":
        right_corridor()
    else:
        print("\nThe silence is unnerving as you hesitate. You must choose!")
        castle_hall()

def secret_passage():
    print("\nYou squeeze through the narrow passage, descending a spiral staircase into the depths of the castle.")
    print("\nThe air grows colder as you enter a damp crypt. Strange symbols adorn the walls, glowing faintly in the darkness.")
    print("\nYou sense powerful magic here. This must be an important location for your quest.")
    # Add more story or gameplay interactions here as needed
    print("\nYou press onward, your resolve hardening as the hourglass sands continue to fall.")
    castle_hall()  # Return to the central hub

def upstairs():
    print("\nYou ascend the grand staircase, each step creaking loudly in the silence of the castle.")
    print("\nAt the top, you find a corridor with two doors: one to the left and one to the right.")
    choice = input("\nDo you open the left door (type 'left') or the right door (type 'right')? ").lower()

    if choice == "left":
        print("\nYou enter what appears to be a library filled with ancient tomes and dusty scrolls.")
        library_puzzle()
    elif choice == "right":
        print("\nYou enter a bedroom, ornate yet decayed, with a large canopy bed and a shattered mirror.")
        bedroom_encounter()
    else:
        print("\nThe corridor feels more oppressive as you hesitate. Time is running out.")
        upstairs()

def library_puzzle():
    print("\nThe library is eerily quiet, save for the occasional sound of rustling paper.")
    print("\nA lectern in the center holds an open book, glowing faintly with magical energy.")
    print("\nAbove it, an inscription reads: 'Solve the riddle to unlock the knowledge you seek.'")
    print("\nRiddle: 'I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?'")
    
    answer = input("\nWhat is your answer? ").lower()
    if answer == "echo":
        print("\nThe book's glow intensifies, and the pages turn by themselves.")
        print("\nYou learn the location of the Tome of Strahd, hidden deep within the catacombs.")
        print("\nA secret passage opens, leading back to the main hall.")
        castle_hall()
    else:
        print("\nThe book snaps shut, and the room grows colder.")
        print("\nYou sense danger and retreat back to the staircase.")
        upstairs()

def bedroom_encounter():
    print("\nThe bedroom feels heavy with an unseen presence.")
    print("\nAs you approach the bed, a ghostly figure appears, weeping softly.")
    print("\nThe spirit speaks: 'I am Tatyana, trapped in this cursed castle by Strahd's will. Free me, and I shall aid you.'")
    print("\nShe gestures to a small jewelry box on a vanity table.")
    choice = input("\nDo you open the jewelry box (type 'open') or leave the room (type 'leave')? ").lower()

    if choice == "open":
        print("\nInside, you find an ancient locket containing a portrait of Tatyana.")
        print("\nThe spirit smiles, fading away. You feel a surge of warmth and gain her blessing.")
        items.append("Tatyana's Blessing")
        print("\nYou return to the staircase, resolved to continue your quest.")
        upstairs()
    elif choice == "leave":
        print("\nThe spirit wails in despair as you leave, her sorrow echoing through the halls.")
        print("\nYou feel a chill as you descend the staircase.")
        castle_hall()
    else:
        print("\nThe spirit grows impatient. You must choose quickly!")
        bedroom_encounter()

def left_corridor():
    print("\nYou step into the left corridor, where the air grows colder and darker.")
    print("\nThe walls are lined with faded portraits whose eyes seem to follow you.")
    print("\nAt the end of the hall, you see a locked door with three symbols etched into it: a sun, a sword, and a raven.")
    print("\nNext to the locked door, there’s another smaller door slightly ajar, with faint glowing symbols emanating from within.")
    
    choice = input("\nDo you solve the puzzle to open the locked door (type 'solve') or enter the glowing room (type 'enter')? ").lower()

    if choice == "solve":
        puzzle_solution = input("\nThe door's inscription reads: 'Choose the symbol that brings both light and strength.' What is your choice? ").lower()
        if puzzle_solution == "sword":
            print("\nThe door creaks open, revealing a small armory. Inside, you find a gleaming silver longsword.")
            items.append("silver longsword")
            print("\nThe weapon hums with holy energy. You feel prepared for the challenges ahead.")
        else:
            print("\nThe door remains locked, and a faint laugh echoes through the corridor.")
            print("\nYou feel unwelcome and retreat to the main hall.")
        castle_hall()
    elif choice == "enter":
        puzzle_room()  # Lead into the new puzzle room
    else:
        print("\nIndecision wastes precious time. You retreat to the main hall.")
        castle_hall()

def left_corridor():
    print("\nYou step into the left corridor, where the air grows colder and darker.")
    print("\nThe walls are lined with faded portraits whose eyes seem to follow you.")
    print("\nAt the end of the hall, you see a locked door with three symbols etched into it: a sun, a sword, and a raven.")
    print("\nNext to the locked door, there’s another smaller door slightly ajar, with faint glowing symbols emanating from within.")
    
    choice = input("\nDo you solve the puzzle to open the locked door (type 'solve') or enter the glowing room (type 'enter')? ").lower()

    if choice == "solve":
        puzzle_solution = input("\nThe door's inscription reads: 'Choose the symbol that brings both light and strength.' What is your choice? ").lower()
        if puzzle_solution == "sword":
            print("\nThe door creaks open, revealing a small armory. Inside, you find a gleaming silver longsword.")
            items.append("silver longsword")
            print("\nThe weapon hums with holy energy. You feel prepared for the challenges ahead.")
        else:
            print("\nThe door remains locked, and a faint laugh echoes through the corridor.")
            print("\nYou feel unwelcome and retreat to the main hall.")
        castle_hall()
    elif choice == "enter":
        puzzle_room()  # Lead into the new puzzle room
    else:
        print("\nIndecision wastes precious time. You retreat to the main hall.")
        castle_hall()

def puzzle_room():
    print("\nYou find yourself in a circular room with walls covered in intricate carvings of ancient symbols.")
    print("In the center of the room lies a large stone pedestal with an inscription:")
    print("\n'To proceed, answer truthfully: What has roots as nobody sees, is taller than trees, up, up it goes, and yet it never grows?'")

    answer = input("\nWhat is your answer? ").lower()
    if answer == "mountain":
        print("\nThe pedestal shifts, revealing a secret passage. You sense this is the right path forward.")
        print("\nYou carefully make your way down the passage, deeper into the castle.")
        secret_passage()  # Continue deeper into the castle
    else:
        print("\nThe room begins to shake violently, and a trapdoor opens beneath you!")
        print("You fall into a dark pit, landing hard on jagged rocks.")
        print("\nYou lose 10 health.")
        # Health adjustment (if implemented)
        arrive()  # Return to the arrival stage

def right_corridor():
    print("\nThe right corridor is shrouded in an eerie silence. The flickering torches cast long, dancing shadows.")
    print("\nYou approach a pedestal with a glowing crystal orb resting on top.")
    print("\nA voice whispers: 'Gaze into the orb, and your fate will be revealed. But beware, for knowledge comes at a price.'")
    choice = input("\nDo you touch the orb (type 'touch') or leave it alone (type 'leave')? ").lower()

    if choice == "touch":
        print("\nThe orb glows brighter, and visions of the castle fill your mind.")
        print("\nYou see a hidden stairwell behind the grand staircase that leads to Strahd's private chambers.")
        print("\nHowever, the orb saps some of your strength. You lose 5 health.")
        castle_hall()
    elif choice == "leave":
        print("\nYou decide not to risk it and step back from the orb.")
        print("\nThe whispers fade as you return to the main hall.")
        castle_hall()
    else:
        print("\nIndecision grips you. The orb's glow pulses ominously.")
        right_corridor()

def game_over():
    print("\nThe mists of Barovia claim you as another victim of Strahd’s domain.")
    print("\nYour quest ends here.")
    exit()
    
    class CurseOfStrahdCampaign:
    def __init__(self):
        self.current_location = 'Vallaki'
        self.strength = 50  # Player's starting strength
        self.inventory = []
        self.allies = []
        self.quest_log = []
        self.strad_defeated = False

    def intro(self):
        print("You find yourself in the land of Barovia, ruled by the mysterious Strahd Von Zarovich.")
        print("The mist is thick, and danger lurks around every corner. Are you ready to face the horrors of this land?")
        self.add_quest('Explore Barovia')
        self.current_location = 'Vallaki'
        self.vallaki_event()

    def vallaki_event(self):
        print("You arrive at Vallaki, a town full of uneasy residents. People speak in hushed tones.")
        print("A key NPC, Ismark, approaches you and offers help. Do you want to join him?")
        choice = input("Choose: [1] Accept Ismark's help. [2] Decline and explore on your own. ")
        if choice == '1':
            print("Ismark tells you about Ireena Kolyana, a woman Strahd is obsessed with.")
            self.add_quest('Help Ismark protect Ireena')
            self.allies.append('Ismark')
        else:
            print("You decide to explore Vallaki, but the town seems eerily quiet. The people avoid you.")
            self.add_quest('Explore Vallaki')
        
        self.vallaki_decision()

    def vallaki_decision(self):
        print("While exploring Vallaki, you discover that Strahd's influence is everywhere.")
        print("You can either: [1] Confront the town's leadership or [2] Visit the church to seek shelter.")
        choice = input("Choose: ")
        if choice == '1':
            print("You challenge the town leaders. Tensions rise and a fight breaks out!")
            self.fight_boss('Vallaki Leaders')
        else:
            print("You seek refuge at the church, but the priest warns you about Strahd's curse.")
            self.add_quest('Find the Bones of St. Andral')

    def fight_boss(self, boss_name):
        print(f"You face off against the {boss_name}. Prepare for battle!")
        # Simulate a fight - use player strength and other stats to determine outcome
        if self.strength >= 60:
            print(f"You defeat the {boss_name} easily.")
        else:
            print(f"The fight is tough, but you manage to escape with minor injuries.")
            self.strength -= 10

    def add_quest(self, quest):
        self.quest_log.append(quest)
        print(f"New quest added: {quest}")
    
    def check_quests(self):
        print("Your current quests:")
        for quest in self.quest_log:
            print(f"- {quest}")

    def interact_with_npc(self, npc_name):
        print(f"You talk to {npc_name}.")
        if npc_name == "Ismark":
            print("Ismark tells you more about Strahd and how he controls the land.")
            print("He urges you to help protect Ireena Kolyana.")
        elif npc_name == "Ireena":
            print("Ireena looks worried. She feels Strahd's presence constantly.")
            print("She trusts you and believes that you can defeat Strahd.")

    def final_battle(self):
        print("You arrive at Castle Ravenloft, where Strahd awaits.")
        if 'Ireena' in self.allies:
            print("Ireena stands beside you, ready for the final confrontation.")
        else:
            print("You are alone in the final battle against Strahd.")
        self.fight_boss('Strahd Von Zarovich')
        if self.strength > 50:
            print("You have defeated Strahd! Barovia is free.")
            self.strad_defeated = True
        else:
            print("Strahd proves too powerful. You are forced to retreat.")

    def play_game(self):
        self.intro()
        while not self.strad_defeated:
            self.check_quests()
            choice = input("Choose an action: [1] Continue exploring. [2] Head to Castle Ravenloft. [3] Check quests. ")
            if choice == '1':
                self.vallaki_event()
            elif choice == '2':
                self.final_battle()
            elif choice == '3':
                self.check_quests()
            else:
                print("Invalid choice. Try again.")

import random
import time

# Function to slow down text output for better immersion
def slow_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# Game Intro
def intro():
    slow_print("You find yourself surrounded by thick fog, trapped in a land of darkness and despair.")
    slow_print("Welcome to Barovia, a cursed land ruled by the vampire lord Strahd Von Zarovich.")
    slow_print("Your adventure begins now...\n")
    input("Press Enter to continue...")

# Act 1: The Village of Barovia
def village_of_barovia():
    slow_print("You arrive in the Village of Barovia. The air is cold, and a sense of dread fills the streets.")
    slow_print("A man approaches you. 'I am Ismark Kolyanovich,' he says. 'My sister, Ireena, is in danger. Strahd has come for her.'")
    choice = input("Do you help Ismark? (yes/no): ").lower()

    if choice == "yes":
        slow_print("You agree to help Ismark and decide to escort Ireena to safety.")
        vallaki()
    else:
        slow_print("Ismark looks disappointed but understands. 'Then you must leave Barovia, for you will not survive here.'")
        slow_print("You walk away from the village, but the mists keep you trapped. You're stuck in Barovia forever.")
        game_over()

# Act 2: Vallaki
def vallaki():
    slow_print("You travel with Ismark to the town of Vallaki. It's a town filled with secrets and strange people.")
    slow_print("There, you meet Rictavio, a mysterious carnival performer who may hold knowledge about Strahd's weaknesses.")
    choice = input("Do you trust Rictavio? (yes/no): ").lower()

    if choice == "yes":
        slow_print("Rictavio reveals a hidden truth about Strahd's power and tells you to seek out the Tome of Strahd.")
        slow_print("You set out to find the Tome and weaken Strahd's influence over Barovia.")
        krezk()
    else:
        slow_print("Rictavio warns you that ignorance could lead to your downfall, but you refuse to trust him.")
        slow_print("Strahd's minions soon appear, and you are forced into a battle. You narrowly escape with your life.")
        krezk()

# Act 3: Krezk and Abbey of Saint Markovia
def krezk():
    slow_print("You arrive at Krezk, a small, isolated town. At the center is the Abbey of Saint Markovia.")
    slow_print("Father Donavich speaks of an ancient artifact that could help defeat Strahd, but he warns of dark forces.")
    choice = input("Do you investigate the Abbey? (yes/no): ").lower()

    if choice == "yes":
        slow_print("Inside the Abbey, you discover that Father Donavich's son is a vampire spawn. You must defeat him to progress.")
        slow_print("With the vampire spawn vanquished, Father Donavich gives you a key to the Abbey's secret vault.")
        slow_print("You find the **Holy Symbol of Ravenkind**, an artifact capable of weakening Strahd.")
        slow_print("Armed with new knowledge, you make your way to Castle Ravenloft for the final confrontation.")
        final_battle()
    else:
        slow_print("You decide to bypass the Abbey and search for other ways to defeat Strahd.")
        slow_print("You encounter strange creatures and wander the wilderness for days, but Strahd’s influence grows stronger.")
        final_battle()

# Final Battle: Castle Ravenloft
def final_battle():
    slow_print("After a long journey, you stand at the gates of Castle Ravenloft, the lair of Strahd Von Zarovich.")
    slow_print("Strahd appears on a balcony, laughing darkly. 'You think you can defeat me, mortal?'")
    choice = input("Do you challenge Strahd? (yes/no): ").lower()

    if choice == "yes":
        slow_print("You enter the castle and confront Strahd. The battle is fierce, but your courage and the artifacts you’ve found help you fight back.")
        slow_print("With a final strike, you defeat Strahd, breaking his curse and freeing Barovia from his grasp.")
        slow_print("You’ve won... but at what cost? The land is forever changed.")
        end_game(True)
    else:
        slow_print("You hesitate, and Strahd uses the opportunity to strike. His power is overwhelming, and you are slain.")
        game_over()

# Game Over
def game_over():
    slow_print("Game Over. The land of Barovia remains cursed, and Strahd’s rule continues.")
    end_game(False)

# End Game
def end_game(success):
    if success:
        slow_print("Congratulations, you have freed Barovia from Strahd's curse!")
    else:
        slow_print("You failed in your quest. The mists of Barovia will claim another soul.")
    choice = input("Do you want to play again? (yes/no): ").lower()
    if choice == "yes":
        main()
    else:
        slow_print("Thank you for playing. Farewell.")
        exit()

# Main function to run the game
def main():
    intro()
    village_of_barovia()

# Start the game
main()


# To play the campaign:
campaign = CurseOfStrahdCampaign()
campaign.play_game()

# Start the game
start()