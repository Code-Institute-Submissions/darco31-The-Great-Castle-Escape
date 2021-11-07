# Creator: Stephen Darcy
# Date:
# Project 3 - The code Institute

from functions import P_STAT
import time
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

TIME_ELAPSED = 2

# Start the game and gives initial choices to the player


def start():
    """
    Starts the game, gives a narrative to set the scene and asks
    if the player would like to play or not. The function also asks
    the players name
    """
    print(Fore.RED + Back.YELLOW + Style.BRIGHT + "\nThe Great Castle Escape")
    time.sleep(TIME_ELAPSED)
    print(Fore.CYAN + '''
                                     T~~
                                     |
                                     /"\\
                             T~~     |'| T~~
                         T~~ |    T~ WWWW|
                         |  /"\   |  |  |/\T~~
                         /"\ WWW  /"\ |' |WW|
                         WWWWW/\| /   \|'/\|/"\\
                         |   /__\/]WWW[\/__\WWWW
                         |"  WWWW'|I_I|'WWWW'  |
                         |   |' |/  -  \|' |'  |
                         |'  |  |LI=H=LI|' |   |
                         |   |' | |[_]| |  |'  |
                         |   |  |_|###|_|  |   |
                         '---'--'-/___\-'--'---'
                     \n
                        Can you escape the castle!\n''')
    while True:
        """
        Set P-NAME to global variable
        """
        global P_NAME
        P_NAME = input("\nPlease enter a username: \n")
        print()
        if P_NAME == "":
            print("You need to enter a username to continue...\n")
            continue
        else:
            break
    P_STAT(f"Welcome {P_NAME}, good luck, you will need it\n", 2)
    P_STAT("You awake a little dazed and confused", 2)
    P_STAT("You find yourself in a dimly lit room", 2)
    P_STAT("You can hear the rain crashing down outside", 2)
    P_STAT("Gathering your senses you try to recall how you got here", 2)
    P_STAT("You look around the room", 2)
    P_STAT("Its big but cold and damp, you notice a window", 2)
    P_STAT("A large wooden door is in front of you", 2)
    P_STAT("Not a lot to choose from", 2)
    print("\n So, do you have the guts to try and escape?(e or s)")
    # convert the player's input to lower_case
    answer = input("=> ").lower().strip()

    if answer == "escape" or answer == "e":
        small_window()
    elif answer == "stay" or answer == "s":
        P_STAT("\n Shame", 1)
        P_STAT(f"\n Enjoy the solitude and loneliness {P_NAME}", 2)
        play_again()
    else:
        P_STAT("\n Error, please enter a valid choice (e or s) ", 2)
        start()


def small_window():
    """
    Function called to let the player explore the 
    small window in the room
    """
    P_STAT("You get up and walk towards the window", 1)
    P_STAT("You peer out and can only see darkness", 1)
    print("Do you try open the window? (y or n)")

    try_window = input("=> ").lower().strip()
    if try_window == "y" or try_window == "yes":
        P_STAT("You try the window, nothing.", 1)
        P_STAT("Urggh its sealed shut", 1)
        try_door()
    else:
        P_STAT("You ignore the window", 1)
        P_STAT("and head for the door", 1)
        try_door()


def try_door():
    """
    The function offers the player the choice of
    opening the door or not.
    """
    P_STAT("Reaching the door you try the handle", 2)
    P_STAT("It opens, thats odd you think", 2)
    P_STAT("Do you take a look outside? (y or n)", 2)

    look_outside = input("=>").lower().strip()

    if look_outside == "y" or look_outside == "yes":
        P_STAT("You open the door as silently as you can", 2)
        P_STAT("Looking outside you notice a door at either end", 2)
        P_STAT("of a long corridor", 2)
        take_items()
    
    else:
        P_STAT("You are too terrified to go on, shame", 1)
        P_STAT(f"Enjoy the solitude and loneliness {P_NAME}", 2)
        play_again()


def take_items():
    """
    The function gives the player the option to check a discovered drawer
    """
    P_STAT("A table outside catches your eye, it has a drawer inset", 2)
    print("Do you try the drawer in the table? (y or n)")

    open_drawer = input("=> ").lower().strip()

    if open_drawer == "y" or open_drawer == "yes":
        P_STAT("You pull out the drawer and find a key and a knife", 2)
        P_STAT("You reach in quickly and pick up both items", 2)
        P_STAT("You stuff them in your pockets and close the drawer", 2)
        P_STAT("You think maybe the knife will open the window", 1)
        print("Do you try the window or go on? (t or g)")

    elif open_drawer == "n" or open_drawer == "no":
        P_STAT("Probably best not to disturb anything", 2)
        direction_choice_two()

    p_decision = input("=> ").lower().strip()

    if p_decision == "try" or p_decision == "t":
        back_to_window()
    elif p_decision == "go on" or p_decision == "g":
        direction_choice()
    else:
        P_STAT("Error, please enter a valid choice (t or g) ", 2)


def return_to_table():
    """
    Player returns to the table from the locked door
    """
    P_STAT("You go back to the table and pull drawer open", 2)
    P_STAT("Result, a key and a knife?", 2)
    P_STAT("You stuff them in your pockets and close the drawer", 2)
    go_right_back()


def back_to_window():
    """
    Brings the player back into the start room to the locked
    window
    """
    P_STAT(Fore.RED + "\n You return to the first room", 3)

    P_STAT("You look out the window again", 2)
    print("Do you try the window with the knife? (y or n)")

    open_window = input("=> ").lower().strip()

    if open_window == "y" or open_window == "yes":
        P_STAT("You jam the knife into the gap of the windowpane", 2)
        P_STAT("the timber comes loose and the window pops open", 2)
        P_STAT("Success, you climb up and outside", 2)
        P_STAT("You peer through the dark and the rain and can just", 2)
        P_STAT("make out the sloping roof. You jump and to your horror ", 2)
        P_STAT("the tile gives way and you fall to your death.", 3)

        P_STAT(Fore.RED + '''
          ╔╗           ╔╗
          ║║           ║║
        ╔═╝║╔══╗╔══╗ ╔═╝║
        ║╔╗║║╔╗║╚ ╗║ ║╔╗║
        ║╚╝║║║═╣║╚╝╚╗║╚╝║
        ╚══╝╚══╝╚═══╝╚══╝
            ''', 2)
        play_again()

    else:
        P_STAT("Looking down into the dark bleak night", 2)
        P_STAT("you decide its best not to try and make your", 2)
        P_STAT("way back to the large door opening", 2)
        direction_choice()


def direction_choice_two():
    """
    Second direction choice id player takes nothing from the drawer
    """
    P_STAT("You reach the door to the right and try open it", 2)
    P_STAT("Its locked, damn it, you remember the drawer, maybe?", 2)
    return_to_table()


def direction_choice():
    """
    Player will make a choice to go left or right
    out of the doorway.
    """
    P_STAT("Standing in the doorway you need to make a choice", 1)
    print("Do you go left or go right? (l or r)")

    player_choice = input("=> ").lower().strip()

    if player_choice == "l" or player_choice == "left":
        go_left()
    elif player_choice == "r" or player_choice == "right":
        go_right()

# Section 2 player goes left


def go_left():
    """
    The player goes left and will have to makes choices
    in the next room
    """
    P_STAT("You decide to turn left and head towards the door", 2)
    P_STAT("as you approach the door you slow down", 2)
    P_STAT("you push at the door and it creaks open", 2)
    P_STAT("as your eyes adjust you make out a single candle light.", 2)
    P_STAT("You walk inside, at the far end there is an opening", 2)
    P_STAT("You approach the opening and see a staircase going down", 2)
    P_STAT("You look around the room", 2)
    print("Do you explore ,proceed downstairs or go back? (e - p - g")

    decision = input("=> ").lower().strip()

    if decision == "explore" or decision == "e":
        explore_room()
    elif decision == "proceed" or decision == "p":
        proceed_down_stairs()
    else:
        P_STAT("You decide it would be better to check the other door", 2)
        go_right()


def explore_room():
    """
    Player decides to explore room
    """
    P_STAT("As you look around the room the idea you are in a castle", 2)
    P_STAT("still leaves you feeling confused", 2)
    P_STAT("You see a bowl with fruit in it, you are starving so", 2)
    P_STAT("pick it up and eat while continuing to explore", 2)
    P_STAT("You find a belt, ", 2)
    P_STAT("you wrap it around you and slip the knife in", 2)
    P_STAT("As there is nothing else left to check ", 2)
    P_STAT("you decide to go downstairs", 2)

    proceed_down_stairs()


def proceed_down_stairs():
    """
    Player proceeds down the spiral stairs
    """
    P_STAT("You enter the doorway", 2)
    P_STAT("Hugging the wall you make your way down", 2)
    P_STAT("You reach the bottom and as you listen", 2)
    P_STAT("you can hear what appears to be two voices", 2)
    P_STAT("You take a breath and peek around the corner and see", 2)
    P_STAT("two large men with what looks like swords?", 2)
    P_STAT("Their backs are to you", 2)
    P_STAT("Hmmm attack or sneak? Your choice - (a or s)", 2)

    attack = input("=> ").lower().strip()

    if attack == "attack" or attack == "a":
        P_STAT("You charge at the men who are surprised", 2)
        P_STAT("but alas, one fouls swipe and you are....", 1)

        P_STAT(Fore.RED + '''
          ╔╗           ╔╗
          ║║           ║║
        ╔═╝║╔══╗╔══╗ ╔═╝║
        ║╔╗║║╔╗║╚ ╗║ ║╔╗║
        ║╚╝║║║═╣║╚╝╚╗║╚╝║
        ╚══╝╚══╝╚═══╝╚══╝
            ''', 2)
        play_again()

    else:
        P_STAT("You put your back against the wall", 2)
        P_STAT("and sneak as quietly as you can passed them", 2)
        bottom_floor()


def go_right_back():
    """
    Return to the righthand door with the key
    """
    P_STAT("You get back to the door and use the key", 2)
    P_STAT("Looking around this lavish room you notice what looks like", 2)
    P_STAT("three levers on the wall", 2)
    P_STAT("You decide to try the levers", 1)

    try_lever = input("=> Pick a lever from '1', '2' and '3':  ").lower().strip()

    if try_lever == "1":
        P_STAT("You pull the first lever, you hear a groan", 1.2)
        P_STAT("looking around a large object comes at you ...", 2)

        P_STAT(Fore.RED + '''
          ╔╗           ╔╗
          ║║           ║║
        ╔═╝║╔══╗╔══╗ ╔═╝║
        ║╔╗║║╔╗║╚ ╗║ ║╔╗║
        ║╚╝║║║═╣║╚╝╚╗║╚╝║
        ╚══╝╚══╝╚═══╝╚══╝
            ''', 2)
        play_again()

    elif try_lever == "2":
        P_STAT("You pull the first lever, you hear a groan", 1.2)
        P_STAT("looking around a large object comes at you ...", 2)

        P_STAT(Fore.RED + '''
          ╔╗           ╔╗
          ║║           ║║
        ╔═╝║╔══╗╔══╗ ╔═╝║
        ║╔╗║║╔╗║╚ ╗║ ║╔╗║
        ║╚╝║║║═╣║╚╝╚╗║╚╝║
        ╚══╝╚══╝╚═══╝╚══╝
            ''', 2)
        play_again()

    elif try_lever == "3":

        P_STAT("You pull the third lever ", 1.2)
        P_STAT("you hear a creaking and a concealed door opens", 2)
        P_STAT("You look around the room and ", 1.2)
        P_STAT("see a candle on the side table, picking it up", 2)
        P_STAT("You crouch down and make your way into the opening", 2)
        P_STAT("Holding the candle up the passage looks long and unused", 2)

        P_STAT("You proceed forward carful as it is sloping down", 2)
        P_STAT("You eventually reach the end and reappear in a room", 2)

        P_STAT("You hear voices but they are coming from behind you", 2)
        bottom_floor()


def go_right():
    """
    Player returns to the corridor and goes to the right
    hand door from the starting room. This will also be the go right from the
    room the player initially makes.
    """
    P_STAT("You reach the door to the right and try open it", 2)
    P_STAT("You then remember the key and try it, it works", 2)
    P_STAT("You push the door open and enter", 2)
    P_STAT("Looking around this lavish room you notice what looks like", 2)
    P_STAT("three levers on the wall", 2)
    P_STAT("You decide to try the levers", 1)

    try_lever = input("=> Pick a number from '1', '2' and '3':  ").lower().strip()

    if try_lever == "1":
        P_STAT("You pull the first lever, you hear a groan", 1.2)
        P_STAT("looking around a large object comes at you ...", 2)

        P_STAT(Fore.RED + '''
          ╔╗           ╔╗
          ║║           ║║
        ╔═╝║╔══╗╔══╗ ╔═╝║
        ║╔╗║║╔╗║╚ ╗║ ║╔╗║
        ║╚╝║║║═╣║╚╝╚╗║╚╝║
        ╚══╝╚══╝╚═══╝╚══╝
            ''', 2)
        play_again()

    elif try_lever == "2":
        P_STAT("You pull the first lever, you hear a groan", 1.2)
        P_STAT("looking around a large object comes at you ...", 2)

        P_STAT(Fore.RED + '''
          ╔╗           ╔╗
          ║║           ║║
        ╔═╝║╔══╗╔══╗ ╔═╝║
        ║╔╗║║╔╗║╚ ╗║ ║╔╗║
        ║╚╝║║║═╣║╚╝╚╗║╚╝║
        ╚══╝╚══╝╚═══╝╚══╝
            ''', 2)
        play_again()

    elif try_lever == "3":

        P_STAT("You pull the third lever ", 1.2)
        P_STAT("you hear a creaking and a concealed door opens", 2)
        P_STAT("You look around the room and ", 1.2)
        P_STAT("see a candle on the side table, picking it up", 2)
        P_STAT("You crouch down and make your way into the opening", 2)
        P_STAT("Holding the candle up the passage looks long and unused", 2)

        P_STAT("You proceed forward carful as it is sloping down", 2)
        P_STAT("You eventually reach the end and reappear in a room", 2)

        P_STAT("You hear voices, but they are coming from behind you", 2)
        bottom_floor()


def bottom_floor():
    """
    The player is in the place they sneak to from
    the stairs and from the secret tunnel and has a choice of 3 paths
    """
    P_STAT("Looking ahead you can see three paths", 2)
    P_STAT("There is a straight path, left and right path", 2)
    print("Do you go s - l - r")

    path_choice = input("=> ").lower().strip()

    if path_choice == "s" or path_choice == "straight":
        P_STAT("You decide to proceed straight ahead", 2)
        P_STAT("Oh Shi.., a group of very angry men approach...", 2)

        P_STAT(Fore.RED + '''
          ╔╗           ╔╗
          ║║           ║║
        ╔═╝║╔══╗╔══╗ ╔═╝║
        ║╔╗║║╔╗║╚ ╗║ ║╔╗║
        ║╚╝║║║═╣║╚╝╚╗║╚╝║
        ╚══╝╚══╝╚═══╝╚══╝
            ''', 2)
        play_again()

    elif path_choice == "l" or path_choice == "left":
        P_STAT("You decide to take the left path ahead", 2)
        P_STAT("You are in a small room with a vent on the wall", 2)
        print("Do you open the vent? (y or n)")

        open_vent = input("=> ").lower().strip()

        if open_vent == "y" or open_vent == "yes":
            P_STAT("You pry the vent open and enter", 2)
            P_STAT("You crawl forward and can ", 2)
            P_STAT("see another vent in the distance", 2)
            P_STAT("as you reach the next vent ", 2)
            P_STAT("you can see below you a guard on his own", 2)
            print("Try kill the guard? (y or n)")

        kill_guard = input("=> ").lower().strip()

        if kill_guard == "y" or kill_guard == "yes":
            P_STAT("You pry the vent open and ready your knife", 2)
            P_STAT("You jump down surprising the guard", 2)
            P_STAT("With one stroke you cut his throat", 2)
            outside()

        elif open_vent == "n" or open_vent == "no":
            bottom_floor()
           
    elif path_choice == "r" or path_choice == "right":
        P_STAT("\n You veer right to an empty room", 2)
        P_STAT("\n more doors, two of them", 2)
        print("\n Left or Right? (l or r)", 2)

        way_forward = input("=> ").lower().strip()

        if way_forward == "left" or way_forward == "l":
            P_STAT("\n You open the lefthand door", 2)
            P_STAT("\n You walk right into a room that is full of guards", 2)

            P_STAT(Fore.RED + '''
              ╔╗           ╔╗
              ║║           ║║
            ╔═╝║╔══╗╔══╗ ╔═╝║
            ║╔╗║║╔╗║╚ ╗║ ║╔╗║
            ║╚╝║║║═╣║╚╝╚╗║╚╝║
            ╚══╝╚══╝╚═══╝╚══╝
                                ''', 2)
            play_again()

        elif way_forward == "right" or way_forward == "r":

            P_STAT("\n You open the right hand door", 2)
            P_STAT("\n Dogs? and guard dogs..", 2)

            P_STAT(Fore.RED + '''
              ╔╗           ╔╗
              ║║           ║║
            ╔═╝║╔══╗╔══╗ ╔═╝║
            ║╔╗║║╔╗║╚ ╗║ ║╔╗║
            ║╚╝║║║═╣║╚╝╚╗║╚╝║
            ╚══╝╚══╝╚═══╝╚══╝
                                ''', 2)
            play_again()
# Player choices for outside the castle


def outside():
    """
    Players choices for outside the castle
    """
    P_STAT("Quickly you search him and find keys and a sword.", 2)
    P_STAT("Looking up there is a door ahead.", 2)
    print("Proceed through door? (y or n)", 2)

    go_to_door = input("=> ").lower().strip()

    if go_to_door == "yes" or go_to_door == "y":
        P_STAT("You fumble through the keys and find the right one", 2)
        P_STAT("You open the door and find yourself outside", 2)
        P_STAT("Pitch black and raining heavily you walk forward", 2)
        P_STAT("you go to the front of the building", 2)
        P_STAT("you can make out", 2)
        P_STAT("a gate ahead , guarded by two men", 2)
        P_STAT("There are high railings all around but", 2)
        P_STAT("you think you could climb them", 2)
        print("Distract or Climb? (d or c)", 2)

    new_choice = input("=> ").lower().strip()

    if new_choice == "d":
        P_STAT("You look around for something to distract them", 2)
        P_STAT("picking up a stone you throw it towards the railing", 2)
        P_STAT("perfect shot, it makes a loud bang alerting them", 2)
        P_STAT("The two guards leave their post and go investigate", 2)
        P_STAT("This is your chance, you move as quickly", 2)
        P_STAT("and quietly as you can. You are out, you run!!!", 2)

        P_STAT(Fore.BLUE + '''
      __   __           _____                              _ 
      \ \ / /          |  ___|                            | |
       \ V /___  _   _ | |__ ___  ___ __ _ _ __   ___  __ | |
        \ // _ \| | | | |  __/ __|/ __/ _` | '_ \ / _ \/ _` |
        | | (_) | |_| | | |__\__ \ (_| (_| | |_) |  __/ (_| |
        \_/\___/ \__,_| \____/___/\___\__,_| .__/ \___|\__,_|
                                           | |               
                                           |_|               
                           ''', 2)
        play_again()

    elif new_choice == "c":
        P_STAT("You decide to climb the railings", 2)
        P_STAT("You put one foot up and pull yourself up to the", 2)
        P_STAT("top of them, you raise your other foot but", 2)
        P_STAT("to your surprise it slips, and you impale yourself", 2)
        P_STAT("You let out an anguished cry", 2)
        P_STAT("which alerts the guards", 2)
        P_STAT("AS they approach, weapons readied, one slice and ..", 2)

        P_STAT(Fore.RED + '''
          ╔╗           ╔╗
          ║║           ║║
        ╔═╝║╔══╗╔══╗ ╔═╝║
        ║╔╗║║╔╗║╚ ╗║ ║╔╗║
        ║╚╝║║║═╣║╚╝╚╗║╚╝║
        ╚══╝╚══╝╚═══╝╚══╝
                          ''', 2)
        play_again()


def play_again():
    """
    Asks the player if they would like to play again
    """
    print("Would you like to play again? (Y or N)")

    answer = input("=> \n").lower().strip()

    if answer == "y" or answer == "yes":
        start()
    elif answer == "n" or answer == "no":
        print(f"Sorry to see you go {P_NAME}")
        print("Please do comeback again")
    else:
        start()


start()
