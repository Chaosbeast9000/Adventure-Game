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
        print("\nYou leave the chapel quickly, feeling the tension in the air rise as you step back onto the path.")
        castle_entrance()
    else:
        print("\nThe figure stares at you, waiting for your decision. Time is running out!")
        chapel()  # Recurse if the user doesn't provide a valid input

def castle_entrance():
    print("\nYou walk toward the grand entrance of Castle Ravenloft. The doors creak open as if inviting you inside, but the air is thick with the scent of death.")
    print("You can feel Strahd’s eyes upon you, even from this distance.")
    print("\nThe door slams shut behind you as you enter the castle, leaving you in total darkness. A soft voice echoes from the shadows.")
    print("'I told you, fools... You will not leave this place alive.'")
    # Proceed further inside the castle or add more story as desired

# You can expand from here, adding more choices, encounters, and NPCs as your adventure progresses.
