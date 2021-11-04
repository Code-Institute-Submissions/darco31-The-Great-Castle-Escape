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
    P_STAT(f"\n Welcome {P_NAME}, good luck, you will need it\n", 2)
    P_STAT("\n You awake a little dazed and confused", 2)
    P_STAT("\n You find yourself in a dimly lit room", 2)
    P_STAT("\n You can hear the rain crashing down outside", 2)
    P_STAT("\n Gathering your senses you try to recall how you got here", 2)
    P_STAT("\n You look around the room", 2)
    P_STAT("\n Its big but cold and damp, you notice a window", 2)
    P_STAT("\n A large wooden door is in front of you", 2)
    P_STAT("\n Not a lot of choice", 2)
    P_STAT("\n So, do you have the guts to try and escape?(Escape or Stay)", 2)
    # convert the player's input to lower_case
    answer = input("=>").lower().strip()

    if answer == "escape":
        small_window()
    elif answer == "stay":
        P_STAT("\n Shame", 1)
        P_STAT(f"\n Enjoy the solitude and loniness of the tower {P_NAME}", 2)
        play_again()
    else:
        # else return player to start()
        start()


def small_window():
    """
    Player goes to investigte small window
    and decides next course of action
    """
    P_STAT("\n You get up and walk towards the window", 1)
    P_STAT("\n You peer out an can only see darkness", 1)
    P_STAT("\n Do you try open the window? Y or N", 2)

    try_window = input("=>").lower().strip()
    if try_window == "y" or try_window == "yes":
        P_STAT("\n You try the window, nothing.", 1)
        P_STAT("\n Urggh its sealed shut", 1)
        try_door()
    else:
        P_STAT("\n You ignore the window", 1)
        P_STAT("\n and head for the door", 1)
        direction_choice()


def try_door():
    """
    The player approcahes the large door and is offered
    various choices in which way to go
    """
    P_STAT("\n Reaching the door you try the handle", 2)
    P_STAT("\n It opens, thats odd", 2)
    P_STAT("\n Do you take a look outside? (Y or N)", 2)

    look_outside = input("=>").lower().strip()

    if look_outside == "y" or look_outside == "yes":
        P_STAT("\n You open the door as silently as you can", 2)
        P_STAT("\n Looking outside you notice a door at either end", 2)
        P_STAT("\n of a long corridor", 2)
        P_STAT("\n A table outside catches your eye, it has a drawer inset", 2)
        P_STAT("\n Do you try the drawer in the table? (Y or N)", 2)

        open_drawer = input("=> \n").lower().strip()

        if open_drawer == "y" or open_drawer == "yes":
            P_STAT("\n You pull out the drawer and find a key and a knife", 2)
            take_items()
        else:
            P_STAT("\n They may notice they are taken", 2)
            P_STAT("\n Best to keep going", 2)
            direction_choice()


def take_items():
    """
    Player decide to take items from the drawer or leave them
    """
    P_STAT("\n Do you pick up the two items (Y or N)", 1)
    pickup_items = input("=> \n").lower().strip()

    if pickup_items == "y" or pickup_items == "yes":

        P_STAT("\n You reach in quickly and pick up both items", 2)
        P_STAT("\n You stuff them in your pockets and close the drawer", 2)
        P_STAT("\n You think maybe the knife will open the window", 1)
        back_to_window()

    else:
        P_STAT("\n You shut the drawer and leave the items", 1)
        direction_choice()


def back_to_window():
    """
    Brings the player back into the start room to the locked
    window
    """
    P_STAT(Fore.RED + "\n You return to the first room", 3)

    P_STAT("\n You look out the window again", 2)
    P_STAT("\n Do you try the window with the knife? (Y or N)", 1)

    open_window = input("=> \n").lower().strip()

    if open_window == "y" or open_window == "yes":
        P_STAT("\n You jam the knife into the gap of the window pane", 2)
        P_STAT("\n the timber comes loose and the window pops open", 2)
        P_STAT("\n Success, you climb up and out side", 2)
        P_STAT("\n You peer through the dark and the rain and can just", 2)
        P_STAT("\n make out the sloping roof. You jump and to your horror ", 2)
        P_STAT("\n the tile gives way and you fall to your death.", 3)

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
        P_STAT("\n Looking down into the dark bleak night", 2)
        P_STAT("\n you decide its best not to try and make your", 2)
        P_STAT("\n way back to the large door opening", 2)
        direction_choice()


def direction_choice():
    """
    Player will make a choice to go left or right
    out of the doorway.
    """
    P_STAT("\n Standing in the doorway you need to make a choice", 1)
    P_STAT("\n Do you go left or go right? (Left or Right)", 2)

    player_choice = input("=> \n").lower().strip()

    if player_choice == "left":
        go_left()
    else:
        go_right()

# Section 2 player goes left


def go_left():
    """
    The player goes left and will have to makes choices
    in the next room
    """
    P_STAT("\n You decide to turn left and head towards the door", 2)
    P_STAT("\n As you approach the door you slow down", 2)
    P_STAT("\n You push at the door and it creaks open", 2)
    P_STAT("\n As your eyes adjust you make out a single candle light", 2)
    P_STAT("\n You walk inside, at the far end there is an opening", 2)
    P_STAT("\n You approach the opening and see a staircase going down", 2)
    P_STAT("\n You look around the room", 2)
    P_STAT("\n Do you explore ,proceed down stairs or go back?", 2)

    decision = input("=> \n").lower().strip()

    if decision == "explore":
        explore_room()
    elif decision == "proceed":
        proceed_down_stairs()
    else:
        P_STAT("\n You decide it would be better to check the other door", 2)
        go_right()


def explore_room():
    """
    Player decides to explore room
    """
    P_STAT("\n As you look around the room the idea you are in a castle", 2)
    P_STAT("\n still leaves you feeling confused", 2)
    P_STAT("\n You see a bowl with fruit in it, you are starving so", 2)
    P_STAT("\n pick it up and eat while continuing to explore", 2)
    P_STAT("\n You find a belt, ", 2)
    P_STAT("\n you wrap it around you and slip the knife in", 2)
    P_STAT("\n As there is nothing else left to check ", 2)
    P_STAT("\n you decide to go down stairs", 2)

    proceed_down_stairs()


def proceed_down_stairs():
    """
    Player proceeds down the spiral stairs
    """
    P_STAT("\n You enter the doorway", 2)
    P_STAT("\n Hugging the wall you make your way down", 2)
    P_STAT("\n You reach the bottom and as you listen", 2)
    P_STAT("\n you can hear what appears to be two voices", 2)
    P_STAT("\n You take a breath and peek around the corner and see", 2)
    P_STAT("\n two large men with what looks like swords?", 2)
    P_STAT("\n Their backs are to you", 2)
    P_STAT("\n Hmmm attack or sneak? Your choice - Attack or Sneak", 2)

    attack = input("=> \n").lower().strip()

    if attack == "attack":
        P_STAT("\n You charge at the men who are surprised", 2)
        P_STAT("\n But its too little, one fouls swipe and you are....", 1)

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
        P_STAT("\n You put your back against the wall", 2)
        P_STAT("\n and sneak as quietly as you can passed them", 2)


def go_right():
    """
    Player returns to the corridor and goes to the right
    hand door from the starting room. This will also be the go right from the
    room the player initially makes.
    """
    P_STAT("\n You reach the door to the right and try open it", 2)
    P_STAT("\n You then remember the key and try it, it works", 2)
    P_STAT("\n You push the door open and enter", 2)
    P_STAT("\n Looking around this lavish room you notice what looks like", 2)
    P_STAT("\n three levers on the wall", 2)
    P_STAT("\n You decide to try the levers", 1)

    try_lever = input("=> Pick a number from '1', '2' and '3':  ").lower().strip()

    if try_lever == "1":
        P_STAT("\n You pull the first lever, you hear a groan", 1.2)
        P_STAT("\n looking around a large object comes at you ...", 2)

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
        P_STAT("\n You pull the first lever, you hear a groan", 1.2)
        P_STAT("\n looking around a large object comes at you ...", 2)

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
        P_STAT("\n You pull the third lever, you hear a groan", 1.2)
        P_STAT("\n looking around a lsecret door creaks open ...", 2)


def play_again():
    """
    Asks the player if they would like to play again
    """
    print("\n Would you like to play again? (Y or N")

    answer = input("=> \n").lower().strip()

    if answer == "y" or answer == "yes":
        start()
    elif answer == "n" or answer == "no":
        print(f"\n Sorry to see you go {P_NAME}")
        print("\n Please do comeback again")
    else:
        start()


start()