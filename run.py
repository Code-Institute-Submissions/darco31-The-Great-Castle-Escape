# Creator: Stephen Darcy
# Date:
# Project 3 - The code Institute

from functions import P_STAT
import time
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

TIME_ELAPSED = 2


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
    P_STAT("\n As you gather your senses you try to recall how you got here", 2)
    P_STAT("\n You look around the room", 2)
    P_STAT("\n Its big but cold and damp, you notice a window", 2)
    P_STAT("\n A large wooden door is in front of you", 2)
    P_STAT("\n Not a lot of choice", 2)
    P_STAT("\n So, do you have the guts to try and escape? (Escape or Stay)", 2)
    # convert the player's input to lower_case
    answer = input("=> \n").lower().strip()

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
    P_STAT("\n You peer out an can only see darkeness", 1)
    P_STAT("\n Do you try open the window? Y or N", 2)

    try_window = input("=> \n").lower().strip()
    if try_window == "y" or try_window == "yes":
        P_STAT("\n You try the wondow, nothing.", 1)
        P_STAT("\n Urggh its sealed shut", 1)
        try_door()
    else:
        P_STAT("\n You ignore the window", 1)
        P_STAT("\n and head for the door", 1)


def try_door():
    """
    The player approcahes the large door and is offered
    various choices in which way to go
    """
    P_STAT("\n Reaching the door tou try the handle", 2)
    P_STAT("\n It opens, how odd you think", 2)
    P_STAT("\n Do you take a look outside? (Y or N)", 2)

    look_outside = input("=> \n").lower().strip()

    if look_outside == "y" or look_outside == "yes":
        P_STAT("\n You open the door as silently as you can", 2)
        P_STAT("\n Looking outside you notice a door at either end", 2)
        P_STAT("\n of a long corridor", 2)
        P_STAT("\n A table just outside cathes your eye, it has a drawer inset", 2)
        P_STAT("\n Do you try the drawer in the table? (Y or N)", 2)


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