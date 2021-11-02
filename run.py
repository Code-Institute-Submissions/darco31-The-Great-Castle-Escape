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
    if the player would like to play or not.
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
    P_STAT("\n You awake a little daxed and confused", 2)
    P_STAT("\n You find yourself in a dimly lit room", 2)
    P_STAT("\n You can hear the ran crashing down outside", 2)
    P_STAT("\n As you gater your senses you try to recall how you got here", 2)
    P_STAT("\n You look around the room", 2)
    P_STAT("\n Its big but cold and damp, you notice a window", 2)
    P_STAT("\n A large wooden door is in front of you", 2)
    P_STAT("\n Not a lot of choice", 2)
    P_STAT("\n So, do you have the guts to try and escape? (Escape or Stay)", 2)
    # convert the player's input to lower_case
    answer = input("> \n").lower().strip()

    if answer == "escape":
        small_window()
    elif answer == "stay":
        P_STAT("\n Shame", 1)
        P_STAT(f"\n Enjoy the solitude and loniness of the tower {P_NAME}", 2)
        play_again()
    else:
        # else return player to start()
        start()


start()