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
def combat():
    print("\nThe vampire spawn lunges toward you, fangs bared and claws outstretched!")
    print("\nPrepare for battle!")

    combat_choice = input("\nDo you fight (type 'fight') or try to flee (type 'flee')? ").lower()

    if combat_choice == "fight":
        print("\nYou draw your weapon and prepare for combat. The vampire spawn hisses and claws at you.")
        attack_roll = int(input("Attack Roll (d20 + modifiers): "))
        if attack_roll >= 15:
            print("\nYou land a solid blow! The vampire spawn staggers back, growling in pain.")
            defense_roll = int(input("Vampire spawn Defense Roll (d20 + modifiers): "))
            if defense_roll < 12:
                print("\nYour attack proves decisive, and the vampire spawn collapses in a heap, turning to dust.")
                input("Press Enter to continue...")
                chapel_victory()
            else:
                print("\nThe vampire spawn deflects your blow and lunges again. You barely dodge!")
                combat()
        else:
            print("\nYour strike misses, and the vampire spawn retaliates with a swipe of its claws!")
            combat()
    elif combat_choice == "flee":
        print("\nYou attempt to retreat from the vampire spawn, but it blocks the exit!")
        escape_roll = int(input("Escape Roll (Dexterity + roll): "))
        if escape_roll >= 14:
            print("\nYou slip past the vampire spawn and escape the chapel.")
            input("Press Enter to continue...")
            castle_entrance()
        else:
            print("\nThe vampire spawn catches you as you flee and sinks its fangs into your neck!")
            print("\nYou struggle, but the vampire spawn's grip tightens. Darkness starts to close in.")
            death()
    else:
        print("\nYou hesitate for a moment, unsure of what to do. The vampire spawn’s fangs snap inches from your face!")
        combat()

def chapel_victory():
    print("\nThe vampire spawn is vanquished, its body reduced to dust in the dim light of the chapel.")
    print("\nYou take a moment to catch your breath. The oppressive energy of the chapel begins to fade.")
    print("\nSomething on the altar catches your eye: a shimmering silver key lies beside an old, cracked tome.")
    print("\nYou approach the altar carefully and retrieve the key and the tome. The book is titled 'The Secrets of Strahd.'")
    input("\nPress Enter to continue...")

    print("\nYou leave the chapel and return to the castle entrance, the eerie atmosphere still lingering in the air.")
    castle_entrance()

def castle_entrance():
    print("\nThe entrance of Castle Ravenloft looms before you. The massive doors creak open, revealing the darkened hallways within.")
    print("\nA chill runs down your spine as you step inside, the shadows seeming to shift around you.")
    choice = input("\nDo you venture deeper into the castle (type 'enter') or search the courtyard (type 'search')? ").lower()

    if choice == "enter":
        castle_interior()
    elif choice == "search":
        print("\nYou step back into the courtyard, your eyes scanning the darkness.")
        print("\nA faint glow catches your eye from behind a fallen statue. It seems to be an old artifact, possibly a relic of the past.")
        relic = input("\nDo you investigate the glowing object (type 'investigate') or return to the castle entrance (type 'return')? ").lower()

        if relic == "investigate":
            print("\nYou approach the glowing relic and find it to be a broken piece of stained glass. Upon closer inspection, it reveals a map of the castle.")
            print("\nIt looks like there are hidden passages in the castle that could aid you in your quest!")
            input("Press Enter to continue...")
            castle_interior()
        elif relic == "return":
            print("\nYou decide not to investigate the relic. The looming darkness within the castle entrance calls to you.")
            castle_interior()
        else:
            print("\nIndecision keeps you standing still in the courtyard. The time is slipping away.")
            castle_entrance()

def castle_interior():
    print("\nYou step into the dark interior of Castle Ravenloft. The air is thick with the scent of ancient wood and decaying stone.")
    print("\nThe walls seem to close in as you move deeper, your every step echoing in the silence.")
    print("\nSuddenly, a distant sound of footsteps echoes in the hallway ahead.")
    choice = input("\nDo you investigate the sound (type 'investigate') or proceed carefully (type 'proceed')? ").lower()

    if choice == "investigate":
        print("\nYou move toward the sound, cautiously peering around the corner. There, you spot a figure cloaked in shadows, standing at the end of the hallway.")
        print("\nThe figure steps forward, revealing itself to be a vampire, its pale skin and piercing red eyes locking onto you.")
        print("\n'Ah, the adventurer who seeks to slay Strahd. I am his servant. You will never leave this place alive.'")
        combat()
    elif choice == "proceed":
        print("\nYou decide to avoid confrontation for now, moving cautiously through the hallways.")
        print("\nThe sound of footsteps grows louder as you near a door at the end of the hallway.")
        choice = input("\nDo you open the door (type 'open') or wait and listen (type 'wait')? ").lower()

        if choice == "open":
            print("\nYou open the door cautiously, revealing a lavish dining hall. But there is no one inside. The eerie silence is unsettling.")
            print("\nSuddenly, the door slams shut behind you, and a cold wind howls through the room.")
            print("\nFrom the shadows, Strahd’s voice echoes: 'You’ve come far, but now you face your doom.'")
            combat()
        elif choice == "wait":
            print("\nYou wait, holding your breath, trying to gather your courage. But nothing happens, and the silence seems to stretch forever.")
            print("\nWith a sigh, you decide to continue onward.")
            castle_interior()
        else:
            print("\nConfusion sets in as the situation grows more tense. You hesitate.")
            castle_interior()

def death():
    print("\nYour vision fades to black as the vampire spawn’s bite drains your life away.")
    print("\nYou’ve perished. The castle remains, as oppressive and unforgiving as ever.")
    print("\nWould you like to try again? (yes/no): ")
    try_again = input().lower()
    if try_again == "yes":
        start()  # Restart the game
    else:
        print("\nGame over. Thank you for playing!")
   
