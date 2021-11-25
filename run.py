# Creator: Stephen Darcy
# Date: 01-11-21
# Project 3 - The code Institute

# Calls the function from clear.py to clear the terminal
# after some not all interactions
from clear import clr_terminal
from set_class import Weapon

# Calls the functions from functions.py to give
# visual help to the player on end game scenarios.
from functions import P_STAT, game_over, player_died, you_escaped

# Imports the time, random and colorama modules
import time
import colorama
import random
from colorama import Fore, Style
colorama.init(autoreset=True)

# Time elapsed variable and variable to center the text in the terminal
TIME_ELAPSED = 2
C = '{:^80}'.format

# Tuples containing the choices fpr the players ANSWERs

ANSWER = " "
no_list = ("N", "n", "no", "No", "NO")
yes_list = ("Y", "y", "yes", "Yes", "YES")
left_dir = ("l", "L", "LEFT", "left")
right_dir = ("r", "R", "RIGHT", "right")
straight = ("s", "S", "Straight", "STRAIGHT", "straight")
explore = ("e", "E", "Explore", "explore", "EXPLORE")
go_back = ("g", "G", "Go-back", "go-back", "GO-BACK", "Go_Back")
proceed = ("p", "P", "Proceed", "proceed", "PROCEED")
attack = ("a", "A", "ATTACK", "attack", "Attack")
sneak = ("s", "S", "SNEAK", "sneak", "Sneak")
distract = ("d", "D", "DISTRACT", "Distract", "distract")
climb = ("c", "C", "CLIMB", "Climb", "climb")

# Variable for the classes

new_weapon = Weapon("knife", "rusty", "light")
new_weapon_two = Weapon("sword", "razor sharp", "heavy")

# Start the game and gives initial choices to the player


def start():
    """
    Starts the game, gives a narrative to set the scene and asks
    if the player would like to play or not. The function also asks
    the players name
    """
    print(C(Fore.RED + Style.BRIGHT + "  The Great Castle Escape"))
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
        P_NAME = input(Fore.YELLOW + " Please enter a username: \n\n")
        print()
        if not P_NAME.isalpha():
            print(Fore.YELLOW + " Please use letters only...")
            continue
        else:
            break
    P_STAT(Fore.GREEN + f" Welcome {P_NAME}, good luck, you will need it", 2)
    P_STAT(Fore.GREEN + " You awake a little dazed and confused", 2)
    P_STAT(Fore.GREEN + " You find yourself in a dimly lit room", 2)
    P_STAT(Fore.GREEN + " You can hear the rain crashing down outside", 2)
    P_STAT(Fore.GREEN + " You try to recall how you got here", 2)
    P_STAT(Fore.GREEN + " You look around the room", 2)
    P_STAT(Fore.GREEN + " Its big cold and damp, you notice a window", 2)
    P_STAT(Fore.GREEN + " A large wooden door is in front of you", 2)
    P_STAT(Fore.GREEN + " Not a lot to choose from", 2)
    print(Fore.YELLOW + " So, do you have the guts to try and escape?(y or n)")
    # convert the player's input to lower_case

    ANSWER = input("=> ").lower().strip()

    while ANSWER not in yes_list and ANSWER not in no_list:
        P_STAT(Fore.RED + f" Please pick the correct option {P_NAME}", 2)
        ANSWER = input("=> ").lower().strip()

    if ANSWER in yes_list:
        clr_terminal()
        small_window()
    elif ANSWER in no_list:
        clr_terminal()
        P_STAT(Fore.RED + " Shame", 1)
        P_STAT(Fore.RED + f" Enjoy the solitude and loneliness {P_NAME}", 2)
        game_over()

# Player has the option to check the window or ignore it


def small_window():
    """
    Function called to let the player explore the
    small window in the room
    """
    P_STAT(Fore.GREEN + " You get up and walk towards the window", 1)
    P_STAT(Fore.GREEN + " You peer out and can only see darkness", 1)
    print(Fore.YELLOW + " Do you try open the window? (y or n)")

    ANSWER = input("=> ").lower().strip()

    while ANSWER not in yes_list and ANSWER not in no_list:
        P_STAT(Fore.RED + f" Please pick the correct option {P_NAME}", 2)
        ANSWER = input("=> ").lower().strip()

    if ANSWER in yes_list:
        clr_terminal()
        P_STAT(Fore.GREEN + " You try the window, nothing.", 1)
        P_STAT(Fore.GREEN + " Urggh its sealed shut", 1)
        try_door()

    elif ANSWER in no_list:
        clr_terminal()
        P_STAT(Fore.GREEN + " You ignore the window", 1)
        P_STAT(Fore.GREEN + " and head for the door", 1)
        try_door()

# The player will have the option to try the door
# where they can choose to leave or stay


def try_door():
    """
    The function offers the player the choice of
    opening the door or not in the first room.
    """
    P_STAT(Fore.GREEN + " Reaching the door you try the handle", 2)
    P_STAT(Fore.GREEN + " It opens, thats odd you think", 2)
    print(Fore.YELLOW + " Do you take a look outside? (y or n)")

    ANSWER = input("=>").lower().strip()

    while ANSWER not in yes_list and ANSWER not in no_list:
        P_STAT(Fore.RED + f" Please pick the correct option {P_NAME}", 2)
        ANSWER = input("=> ").lower().strip()

    if ANSWER in yes_list:
        clr_terminal()
        P_STAT(Fore.GREEN + " You open the door as silently as you can", 2)
        P_STAT(Fore.GREEN + " Looking outside you see a door at either end", 2)
        P_STAT(Fore.GREEN + " of a long corridor", 2)
        take_items()

    elif ANSWER in no_list:
        clr_terminal()
        P_STAT(Fore.GREEN + " You are too terrified to go on, shame", 1)
        P_STAT(Fore.GREEN + f" Enjoy the solitude and loneliness {P_NAME}", 2)
        game_over()

# The player can choose to search the drawer or leave it.


def take_items():
    """
    The function gives the player the option to check a discovered drawer
    """
    P_STAT(Fore.GREEN + " A table outside catches your eye,", 1)
    P_STAT(Fore.GREEN + " it has a drawer inset", 2)
    print(Fore.YELLOW + " Do you try the drawer in the table? (y or n)")

    ANSWER = input("=> ").lower().strip()

    while ANSWER not in yes_list and ANSWER not in no_list:
        P_STAT(Fore.RED + f" Please pick the correct option {P_NAME}", 2)
        ANSWER = input("=> ").lower().strip()

    if ANSWER in yes_list:
        clr_terminal()
        P_STAT(Fore.GREEN + " You pull out the drawer and find a", 1)
        P_STAT(Fore.GREEN + f" key and a {new_weapon.weapon_type}", 2)
        P_STAT(Fore.GREEN + " a belt is coiled up at the back", 2)
        P_STAT(Fore.GREEN + " You reach in quickly and pick up all items", 2)
        P_STAT(Fore.GREEN + " You stuff them in your pockets", 2)
        P_STAT(Fore.GREEN + " and wrap the belt around you", 2)
        P_STAT(Fore.GREEN + " and close the drawer", 2)
        P_STAT(Fore.GREEN + f" Maybe the {new_weapon.weapon_type}", 3)
        P_STAT(Fore.GREEN + " will open the window", 2)
        back_to_window()

    elif ANSWER in no_list:
        clr_terminal()
        P_STAT(Fore.GREEN + " Probably best not to disturb anything", 2)
        direction_choice_two()

# Player returns to the table form locked door to retrieve items.


def return_to_table():
    """
    Player returns to the table from the locked door
    """
    P_STAT(Fore.GREEN + " You go back to the table and pull drawer open", 2)
    P_STAT(Fore.GREEN + f" Result, a key and {new_weapon.weapon_type}", 2)
    P_STAT(Fore.GREEN + " You stuff them in your pockets ", 2)
    P_STAT(Fore.GREEN + " and close the drawer", 2)
    P_STAT(Fore.GREEN + " you quickly get back to the right-hand door", 2)
    go_right_back()

# Player goes back to the first room to try the window with knife.


def back_to_window():
    """
    Brings the player back into the start room to the locked
    window
    """
    P_STAT(Fore.RED + "\n You return to the first room", 2)

    P_STAT(Fore.GREEN + " You look out the window again.", 2)
    print(Fore.YELLOW + f" Open the window with the {new_weapon.weapon_type}?")
    print(Fore.YELLOW + " (y or n)")

    ANSWER = input("=> ").lower().strip()

    while ANSWER not in yes_list and ANSWER not in no_list:
        P_STAT(Fore.RED + f" Please pick the correct option {P_NAME}", 2)
        ANSWER = input("=> ").lower().strip()

    if ANSWER in yes_list:
        clr_terminal()
        P_STAT(Fore.GREEN + f" You jam the {new_weapon.weapon_type} in the", 2)
        P_STAT(Fore.GREEN + " gap of the window, the timber comes loose ", 2)
        P_STAT(Fore.GREEN + " and the window pops open. Success, ", 2)
        P_STAT(Fore.GREEN + " you climb up and outside and as you peer", 2)
        P_STAT(Fore.GREEN + " through the dark you can just make out the", 2)
        P_STAT(Fore.GREEN + " sloping roof. You jump but to your horror", 3)
        P_STAT(Fore.GREEN + " the tile snaps, and you fall to your death", 2)

        player_died()
        game_over()
        play_again()
        clr_terminal()

    elif ANSWER in no_list:
        clr_terminal()
        P_STAT(Fore.GREEN + " Looking down into the dark bleak night", 2)
        P_STAT(Fore.GREEN + " you decide its best not to try and make your", 2)
        P_STAT(Fore.GREEN + " way back to the large door opening", 2)
        direction_choice()

# First direction choice


def direction_choice():
    """
    Player will make a choice to go left or right
    out of the doorway and they will have the
    objects from the drawer
    """
    P_STAT(Fore.GREEN + " Standing in the door you need to make a choice", 1)
    print(Fore.YELLOW + " Do you go left or go right? (l or r)")

    ANSWER = input("=> ").lower().strip()

    while ANSWER not in left_dir and ANSWER not in right_dir:
        P_STAT(Fore.RED + f" Please pick the correct option {P_NAME}", 2)
        ANSWER = input("=> ").lower().strip()

    if ANSWER in left_dir:
        clr_terminal()
        go_left_with_items()
    elif ANSWER in right_dir:
        clr_terminal()
        go_right()

# If player ignores the drawer and decides to move on


def direction_choice_two():
    """
    Second direction choice if player takes nothing from the drawer
    """
    P_STAT(Fore.GREEN + " Standing in the door you need to make a choice", 1)
    print(Fore.YELLOW + " Do you go left or go right? (l or r)")

    ANSWER = input("=> ").lower().strip()

    while ANSWER not in left_dir and ANSWER not in right_dir:
        P_STAT(Fore.RED + f" Please pick the correct option {P_NAME}", 2)
        ANSWER = input("=> ").lower().strip()

    if ANSWER in left_dir:
        clr_terminal()
        go_left()
    elif ANSWER in right_dir:
        clr_terminal()
        P_STAT(Fore.GREEN + " You reach the door and try open it", 2)
        P_STAT(Fore.RED + " Its locked, you remember the drawer, maybe?", 2)
        return_to_table()

# Player decides to return from left hand room.
# or goes to right hand door without key.


def direction_choice_three():
    """
    Function for the player to return to the right hand door
    if they decide to return after going left
    """
    P_STAT(Fore.GREEN + " You reach the door to the right and try open it", 2)
    P_STAT(Fore.GREEN + " Its locked, you remember the drawer, maybe?", 2)
    return_to_table()


def go_left():
    """
    The player goes left and will have to makes choices
    in the next room
    """
    P_STAT(Fore.GREEN + " You turn left and head towards the door", 2)
    P_STAT(Fore.GREEN + " as you approach the door you slow down", 2)
    P_STAT(Fore.GREEN + " you push at the door, and it creaks open", 2)
    P_STAT(Fore.GREEN + " as your eyes adjust you make out a candlelight.", 2)
    P_STAT(Fore.GREEN + " You walk inside, at the far end there is an", 2)
    P_STAT(Fore.GREEN + " opening. You approach it and see a staircase", 2)
    P_STAT(Fore.GREEN + " going down. You look around the room", 2)
    print(Fore.YELLOW + " Do you explore,proceed or go back? (e-p-g)")

    ANSWER = input("=> ").lower().strip()

    while (
        ANSWER not in explore and
        ANSWER not in proceed and
        ANSWER not in go_back
    ):
        P_STAT(Fore.RED + f" Please pick the correct option {P_NAME}", 2)
        ANSWER = input("=> ").lower().strip()

    if ANSWER in explore:
        clr_terminal()
        explore_room()

    elif ANSWER in proceed:
        clr_terminal()
        proceed_down_stairs()

    elif ANSWER in go_back:
        P_STAT(Fore.GREEN + " You decide to go back to the other door", 2)
        clr_terminal()
        direction_choice_three()

# Player goes to the left door but has the key for the right door


def go_left_with_items():
    """
    The player goes left and will have to makes choices
    in the next room but has items from drawer
    """
    P_STAT(Fore.GREEN + " You turn left and head towards the door", 2)
    P_STAT(Fore.GREEN + " as you approach the door you slow down", 2)
    P_STAT(Fore.GREEN + " you push at the door, and it creaks open", 2)
    P_STAT(Fore.GREEN + " as your eyes adjust you make out a candlelight.", 2)
    P_STAT(Fore.GREEN + " You walk inside, at the far end there is an", 2)
    P_STAT(Fore.GREEN + " opening. You approach it and see a staircase", 2)
    P_STAT(Fore.GREEN + " going down. You look around the room", 2)
    print(Fore.YELLOW + " Do you explore,proceed or go back? (e-p-g)")

    ANSWER = input("=> ").lower().strip()

    while (
        ANSWER not in explore and
        ANSWER not in proceed and
        ANSWER not in go_back
    ):
        P_STAT(Fore.RED + f" Please pick the correct option {P_NAME}", 2)
        ANSWER = input("=> ").lower().strip()

    if ANSWER in explore:
        clr_terminal()
        explore_room_with_items()

    elif ANSWER in proceed:
        clr_terminal()
        proceed_with_items()

    elif ANSWER in go_back:
        P_STAT(Fore.GREEN + " You decide to go back to the other door", 2)
        clr_terminal()
        go_right()

# The player can explore the right hand side room after taking items


def explore_room_with_items():
    """
    Player decides to explore room but again has the items
    """
    P_STAT(Fore.GREEN + " As you look around the room, the idea you are", 2)
    P_STAT(Fore.GREEN + " in a castle still leaves you feeling confused", 2)
    P_STAT(Fore.GREEN + " You see a bowl with fruit in it, starving", 2)
    P_STAT(Fore.GREEN + " you pick it up and eat while", 2)
    P_STAT(Fore.GREEN + " continuing to explore.", 2)
    P_STAT(Fore.GREEN + " As there is nothing else left to check", 2)
    print(Fore.YELLOW + " Do you proceed or go back? (p or g)")

    ANSWER = input("=> ").lower().strip()

    while ANSWER not in proceed and ANSWER not in go_back:
        P_STAT(Fore.RED + f" Please pick the correct option {P_NAME}", 2)
        ANSWER = input("=> ").lower().strip()

    if ANSWER in proceed:
        P_STAT(Fore.GREEN + " You decide to head downstairs", 2)
        proceed_with_items()
    elif ANSWER in go_back:
        P_STAT(Fore.GREEN + " You decide to go back to the other door", 2)
        go_right()

# Go downstairs with the items from the drawer


def proceed_with_items():
    """
    Player proceeds down the spiral stairs with the items from
    the drawer
    """
    P_STAT(Fore.GREEN + " You enter the doorway", 2)
    P_STAT(Fore.GREEN + " Hugging the wall you make your way down", 2)
    P_STAT(Fore.GREEN + " You reach the bottom and as you listen", 2)
    P_STAT(Fore.GREEN + " you can hear what appears to be two voices", 2)
    P_STAT(Fore.GREEN + " Holding your breath you peek around the corner", 2)
    P_STAT(Fore.GREEN + " and see two large men,", 2)
    P_STAT(Fore.GREEN + f" both with {new_weapon_two.weapon_type}'s?", 2)
    P_STAT(Fore.GREEN + " Their backs are to you, you only have the knife", 2)
    P_STAT(Fore.YELLOW + " Hmmm attack or sneak? Your choice - (a or s)", 2)

    ANSWER = input("=> ").lower().strip()

    while ANSWER not in attack and ANSWER not in sneak:
        P_STAT(Fore.RED + f" Please pick the correct option {P_NAME}", 2)
        ANSWER = input("=> ").lower().strip()

    if ANSWER in attack:
        clr_terminal()
        P_STAT(Fore.GREEN + " You charge at the men who are surprised", 2)
        P_STAT(Fore.GREEN + f" Raising their {new_weapon_two.weapon_type}s", 2)
        P_STAT(Fore.GREEN + " the knife seems meaningless", 1)
        P_STAT(Fore.GREEN + " one foul swipe and you are....", 1)

        player_died()
        game_over()
        play_again()

    elif ANSWER in sneak:
        P_STAT(Fore.GREEN + " You put your back against the wall", 2)
        P_STAT(Fore.GREEN + " and sneak as quietly as you can passed them", 2)
        bottom_floor_with_knife()

# The player can explore the right-hand side room


def explore_room():
    """
    Player decides to explore room
    """
    P_STAT(Fore.GREEN + " As you look around the room, the idea you are", 2)
    P_STAT(Fore.GREEN + " in a castle still leaves you feeling confused", 2)
    P_STAT(Fore.GREEN + " You see a bowl with fruit in it, starving", 2)
    P_STAT(Fore.GREEN + " you pick it up and eat while", 2)
    P_STAT(Fore.GREEN + " continuing to explore.", 2)
    P_STAT(Fore.GREEN + " As there is nothing else left to check", 2)
    print(Fore.YELLOW + " Do you proceed or go back? (p or g)")

    ANSWER = input("=> ").lower().strip()

    while ANSWER not in proceed and ANSWER not in go_back:
        P_STAT(Fore.RED + f" Please pick the correct option {P_NAME}", 2)
        ANSWER = input("=> ").lower().strip()

    if ANSWER in proceed:
        P_STAT(Fore.GREEN + " You decide to head downstairs", 2)
        proceed_down_stairs()
    elif ANSWER in go_back:
        P_STAT(Fore.GREEN + " You decide to go back to the other door", 2)
        direction_choice_three()

# The player decides to ignore the room and move down the stairs.


def proceed_down_stairs():
    """
    Player proceeds down the spiral stairs
    """
    P_STAT(Fore.GREEN + " You enter the doorway", 2)
    P_STAT(Fore.GREEN + " Hugging the wall you make your way down", 2)
    P_STAT(Fore.GREEN + " You reach the bottom and as you listen", 2)
    P_STAT(Fore.GREEN + " you can hear what appears to be two voices", 2)
    P_STAT(Fore.GREEN + " Holding your breath you peek around the corner", 2)
    P_STAT(Fore.GREEN + " and see two large men,", 2)
    P_STAT(Fore.GREEN + f" both with {new_weapon_two.weapon_type}'s?", 2)
    P_STAT(Fore.GREEN + " Their backs are to you, and you are weaponless", 2)
    P_STAT(Fore.YELLOW + " Hmmm attack or sneak? Your choice - (a or s)", 2)

    ANSWER = input("=> ").lower().strip()

    while ANSWER not in attack and ANSWER not in sneak:
        P_STAT(Fore.RED + f" Please pick the correct option {P_NAME}", 2)
        ANSWER = input("=> ").lower().strip()

    if ANSWER in attack:
        clr_terminal()
        P_STAT(Fore.GREEN + " You charge at the men who are surprised", 2)
        P_STAT(Fore.GREEN + " but alas, one foul swipe and you are....", 1)

        player_died()
        game_over()
        play_again()

    if ANSWER in sneak:
        P_STAT(Fore.GREEN + " You put your back against the wall", 2)
        P_STAT(Fore.GREEN + " and sneak as quietly as you can passed them", 2)
        bottom_floor()

# Player returns to the right-hand door after searching the drawer


def go_right_back():
    """
    Return to the righthand door with the key
    """
    P_STAT(Fore.GREEN + " Using the key you push the door open and enter", 2)
    P_STAT(Fore.GREEN + " Looking around this lavish room you notice", 2)
    P_STAT(Fore.GREEN + " what looks like three levers on the wall", 2)
    P_STAT(Fore.GREEN + " You decide to try the levers", 1)

# Player will get a random choice of lever, and this will decide the outcome
    try_lever = random.randint(1, 3)

    if try_lever == 1:
        clr_terminal()
        P_STAT(Fore.GREEN + " You pull the first lever, you hear a groan", 1.2)
        P_STAT(Fore.GREEN + " as you turn a large object comes at you ...", 2)

        player_died()
        game_over()
        play_again()

    elif try_lever == 2:
        clr_terminal()
        P_STAT(Fore.GREEN + " You pull the second lever, you hear a groan", 1)
        P_STAT(Fore.GREEN + " as you turn a large object comes at you ...", 2)

        player_died()
        game_over()
        play_again()

    elif try_lever == 3:
        clr_terminal()

        P_STAT(Fore.GREEN + " You pull the third lever ", 1.2)
        P_STAT(Fore.GREEN + " you hear a noise, and a concealed door opens", 2)
        P_STAT(Fore.GREEN + " You look around the room and ", 1.2)
        P_STAT(Fore.GREEN + " see a candle on the side table, picking it", 2)
        P_STAT(Fore.GREEN + " up you crouch down and walk into the opening", 2)
        P_STAT(Fore.GREEN + " Holding the candle up, the passage ", 2)
        P_STAT(Fore.GREEN + " looks long and unused. You proceed forward", 2)
        P_STAT(Fore.GREEN + " carful as it is sloping down", 2)
        P_STAT(Fore.GREEN + " You eventually reach the end and", 2)
        P_STAT(Fore.GREEN + " reappear in a room. You hear voices,", 2)
        P_STAT(Fore.GREEN + " but they are coming from behind you", 2)
        bottom_floor_with_knife()

    else:
        print(Fore.RED + " That it not a valid option, please pick 1,2,3")
        go_right_back()


def go_right():
    """
    Player returns to the corridor and goes to the right
    hand door from the starting room. This will also be the go right from the
    room the player initially makes.
    """
    P_STAT(Fore.GREEN + " You reach the door to the right and try open it", 2)
    P_STAT(Fore.RED + " Locked!!", 2)
    P_STAT(Fore.GREEN + " You then remember the key and try it, it works", 2)
    P_STAT(Fore.GREEN + " You push the door open and enter", 2)
    P_STAT(Fore.GREEN + " Looking around this lavish room you notice", 2)
    P_STAT(Fore.GREEN + " three levers on the wall", 2)
    P_STAT(Fore.GREEN + " You decide to try the levers", 1)

    # Player will get a random choice of lever, this will decide the outcome
    try_lever = random.randint(1, 3)

    if try_lever == 1:
        clr_terminal()
        P_STAT(Fore.GREEN + " You pull the first lever, you hear a groan", 1.2)
        P_STAT(Fore.GREEN + " as you turn a large object comes at you ...", 2)

        player_died()
        game_over()
        play_again()

    elif try_lever == 2:
        clr_terminal()
        P_STAT(Fore.GREEN + " You pull the second lever, you hear a groan", 1)
        P_STAT(Fore.GREEN + " as you turn a large object comes at you ...", 2)

        player_died()
        game_over()
        play_again()

    elif try_lever == 3:
        clr_terminal()

        P_STAT(Fore.GREEN + " You pull the third lever ", 1.2)
        P_STAT(Fore.GREEN + " you hear a noise, and a concealed door opens", 2)
        P_STAT(Fore.GREEN + " You look around the room and ", 1.2)
        P_STAT(Fore.GREEN + " see a candle on the side table, picking it", 2)
        P_STAT(Fore.GREEN + " up.You crouch down and go into the opening.", 2)
        P_STAT(Fore.GREEN + " Holding the candle up, the passage ", 2)
        P_STAT(Fore.GREEN + " looks long and unused. You proceed forward", 2)
        P_STAT(Fore.GREEN + " carful as it is sloping down", 2)
        P_STAT(Fore.GREEN + " You eventually reach the end and", 2)
        P_STAT(Fore.GREEN + " reappear in a room. You hear voices,", 2)
        P_STAT(Fore.GREEN + " but they are coming from behind you", 2)
        bottom_floor_with_knife()

# Player reached the bottom floor with the items


def bottom_floor_with_knife():
    """
    The player is in the place they sneak to from
    the stairs and from the secret tunnel and have a choice of 3 paths
    but has the items
    """
    P_STAT(Fore.GREEN + " Looking ahead you can see three paths", 2)
    P_STAT(Fore.GREEN + " There is a straight path, left and right path", 2)
    print(Fore.YELLOW + " Do you go s - l - r")

    ANSWER = input("=> ").lower().strip()

    while ANSWER not in straight and ANSWER not in left_dir:
        P_STAT(Fore.RED + f" Please pick the correct option {P_NAME}", 2)
        ANSWER = input("=> ").lower().strip()

    if ANSWER in straight:
        clr_terminal()
        P_STAT(Fore.GREEN + " You decide to proceed straight ahead", 2)
        P_STAT(Fore.GREEN + " Oh sugar..,a group of angry men approach..", 2)

        player_died()
        game_over()
        play_again()

    elif ANSWER in left_dir:
        clr_terminal()
        P_STAT(Fore.GREEN + " You decide to take the left path ahead", 2)
        P_STAT(Fore.GREEN + " You are in a room with a vent on the wall", 2)
        print(Fore.YELLOW + " Do you open the vent? (y or n)")

        ANSWER = input("=> ").lower().strip()

        while ANSWER not in yes_list and ANSWER not in no_list:
            P_STAT(Fore.RED + f" Please pick the correct option {P_NAME}", 2)
            ANSWER = input("=> ").lower().strip()

        if ANSWER in yes_list:
            clr_terminal()
            P_STAT(Fore.GREEN + " You pry the vent open and enter", 2)
            P_STAT(Fore.GREEN + " You crawl forward and can ", 2)
            P_STAT(Fore.GREEN + " see another vent in the distance", 2)
            P_STAT(Fore.GREEN + " as you reach the next vent ", 2)
            P_STAT(Fore.GREEN + " you can see below you a guard on his own", 2)
            print(Fore.YELLOW + " Try kill the guard? (y or n)")

        elif ANSWER in no_list:
            clr_terminal()
            return_to_paths()

        ANSWER = input("=> ").lower().strip()

        while ANSWER not in yes_list and ANSWER not in no_list:
            P_STAT(Fore.RED + f" Please pick the correct option {P_NAME}", 2)
            ANSWER = input("=> ").lower().strip()

        if ANSWER in yes_list:
            clr_terminal()
            P_STAT(Fore.GREEN + " You pry the vent open and ready the ", 2)
            P_STAT(Fore.GREEN + f" {new_weapon.weapon_type}", 2)
            P_STAT(Fore.GREEN + f" ,it may be a bit {new_weapon.weight}", 1)
            P_STAT(Fore.GREEN + " to kill him, however", 2)
            P_STAT(Fore.GREEN + " You jump down surprising the guard.", 2)
            P_STAT(Fore.GREEN + " With one stroke you cut his throat", 2)
            outside()

        elif ANSWER in no_list:
            clr_terminal()
            P_STAT(Fore.GREEN + " You decide to spare his life... for now.", 2)
            return_to_paths()

    elif ANSWER in right_dir:
        P_STAT(Fore.GREEN + " You veer right to an empty room", 2)
        P_STAT(Fore.GREEN + " more doors, two of them", 2)
        print(Fore.YELLOW + " Left or Right? (l or r)")

        ANSWER = input("=> ").lower().strip()

        while ANSWER not in left_dir and ANSWER not in right_dir:
            P_STAT(Fore.RED + f" Please pick the correct option {P_NAME}", 2)
            ANSWER = input("=> ").lower().strip()

        if ANSWER in left_dir:
            clr_terminal()
            P_STAT(Fore.GREEN + " You open the left hand door", 2)
            P_STAT(Fore.GREEN + " Oh no!! A room full of guards", 2)

            player_died()
            game_over()
            play_again()

        elif ANSWER in right_dir:
            clr_terminal()

            P_STAT(Fore.GREEN + " You open the right-hand door", 2)
            P_STAT(Fore.GREEN + " Dogs? and guard dogs..", 2)

            player_died()
            game_over()
            play_again()

# The player will get a choice of three paths that lie ahead.


def bottom_floor():
    """
    The player is in the place they sneak to from
    the stairs and from the secret tunnel and have a choice of 3 paths
    """
    P_STAT(Fore.GREEN + " Looking ahead you can see three paths", 2)
    P_STAT(Fore.GREEN + " There is a straight path, left and right path", 2)
    print(Fore.YELLOW + " Do you go s - l - r")

    ANSWER = input("=> ").lower().strip()

    while ANSWER not in straight and ANSWER not in left_dir:
        P_STAT(Fore.RED + f" Please pick the correct option {P_NAME}", 2)
        ANSWER = input("=> ").lower().strip()

    if ANSWER in straight:
        clr_terminal()
        P_STAT(Fore.GREEN + " You decide to proceed straight ahead", 2)
        P_STAT(Fore.GREEN + " Oh sugar..,a group of angry men approach..", 2)

        player_died()
        game_over()
        play_again()

    elif ANSWER in left_dir:
        clr_terminal()
        P_STAT(Fore.GREEN + " You decide to take the left path ahead", 2)
        P_STAT(Fore.GREEN + " You are in a room with a vent on the wall", 2)
        print(Fore.YELLOW + " Do you open the vent? (y or n)")

        ANSWER = input("=> ").lower().strip()

        while ANSWER not in yes_list and ANSWER not in no_list:
            P_STAT(Fore.RED + f" Please pick the correct option {P_NAME}", 2)
            ANSWER = input("=> ").lower().strip()

        if ANSWER in yes_list:
            clr_terminal()
            P_STAT(Fore.GREEN + " You pry the vent open and enter", 2)
            P_STAT(Fore.GREEN + " You crawl forward and can ", 2)
            P_STAT(Fore.GREEN + " see another vent in the distance", 2)
            P_STAT(Fore.GREEN + " as you reach the next vent ", 2)
            P_STAT(Fore.GREEN + " you can see below you a guard on his own", 2)
            print(Fore.YELLOW + " Try kill the guard? (y or n)")

        elif ANSWER in no_list:
            clr_terminal()
            return_to_paths()

        ANSWER = input("=> ").lower().strip()

        while ANSWER not in yes_list and ANSWER not in no_list:
            P_STAT(Fore.RED + f" Please pick the correct option {P_NAME}", 2)
            ANSWER = input("=> ").lower().strip()

        if ANSWER in yes_list:
            clr_terminal()
            P_STAT(Fore.GREEN + " You pry the vent open and ready the ", 2)
            P_STAT(Fore.GREEN + " the belt you found, ", 2)
            P_STAT(Fore.GREEN + " You jump down surprising the guard.", 2)
            P_STAT(Fore.GREEN + " You quickly wrap the belt around", 2)
            P_STAT(Fore.GREEN + " his neck,gasping he falls to the ground", 2)
            outside()

        elif ANSWER in no_list:
            clr_terminal()
            P_STAT(Fore.GREEN + " You decide to spare his life... for now.", 2)
            return_to_paths()

    elif ANSWER in right_dir:
        P_STAT(Fore.GREEN + " You veer right to an empty room", 2)
        P_STAT(Fore.GREEN + " more doors, two of them", 2)
        print(Fore.YELLOW + " Left or Right? (l or r)")

        ANSWER = input("=> ").lower().strip()

        while ANSWER not in left_dir and ANSWER not in right_dir:
            P_STAT(Fore.RED + f" Please pick the correct option {P_NAME}", 2)
            ANSWER = input("=> ").lower().strip()

        if ANSWER in left_dir:
            clr_terminal()
            P_STAT(Fore.GREEN + " You open the left hand door", 2)
            P_STAT(Fore.GREEN + " Oh no!! A room full of guards", 2)

            player_died()
            game_over()
            start()

        elif ANSWER in right_dir:
            clr_terminal()

            P_STAT(Fore.GREEN + " You open the right hand door", 2)
            P_STAT(Fore.GREEN + " Dogs? and guard dogs..", 2)

            player_died()
            game_over()
            start()

# Player decides to return to the 3 paths


def return_to_paths():
    """
    Function returns palyers to path choices
    """
    P_STAT(Fore.GREEN + " You return to the secret tunnel opening", 2)
    bottom_floor()

# Player choices for outside the castle


def outside():
    """
    Players choices for outside the castle
    """
    P_STAT(Fore.GREEN + " Quickly you search him and find keys and a", 2)
    P_STAT(Fore.GREEN + f" {new_weapon_two.weapon_type}", 2)
    P_STAT(Fore.GREEN + f" You put the {new_weapon_two.weapon_type}", 2)
    P_STAT(Fore.GREEN + " in the belt, looking up there is a door ahead.", 2)
    print(Fore.YELLOW + " Proceed through door? (y or n)")

    ANSWER = input("=> ").lower().strip()

    while ANSWER not in yes_list and ANSWER not in no_list:
        P_STAT(Fore.RED + f" Please pick the correct option {P_NAME}", 2)
        ANSWER = input("=> ").lower().strip()

    if ANSWER in yes_list:
        clr_terminal()
        P_STAT(Fore.GREEN + " You fumble through the keys", 2)
        P_STAT(Fore.GREEN + " and find the right one", 2)
        P_STAT(Fore.GREEN + " You open the door and find yourself outside", 2)
        P_STAT(Fore.GREEN + " Pitch black and raining heavily", 2)
        P_STAT(Fore.GREEN + " you walk forward and reach the", 2)
        P_STAT(Fore.GREEN + " front of the building you can make out", 2)
        P_STAT(Fore.GREEN + " a gate ahead , guarded by two men", 2)
        P_STAT(Fore.GREEN + " There are high railings all around but", 2)
        P_STAT(Fore.GREEN + " you think you could climb them", 2)
        print(Fore.YELLOW + " Distract or Climb? (d or c)")

    elif ANSWER in no_list:
        P_STAT(Fore.GREEN + " You decide to go back to the pathways", 2)
        P_STAT(Fore.GREEN + " Climbing up you go back through the vent", 2)
        bottom_floor()

    ANSWER = input("=> ").lower().strip()

    while ANSWER not in distract and ANSWER not in climb:
        P_STAT(Fore.RED + f" Please pick the correct option {P_NAME}", 2)
        ANSWER = input("=> ").lower().strip()

    if ANSWER in distract:
        clr_terminal()
        P_STAT(Fore.GREEN + " You look around for something to distract", 2)
        P_STAT(Fore.GREEN + " them, picking up a stone you throw", 2)
        P_STAT(Fore.GREEN + " it at the railing, perfect shot,", 2)
        P_STAT(Fore.GREEN + " it makes a loud bang alerting them.", 2)
        P_STAT(Fore.GREEN + " The two guards leave their post", 2)
        P_STAT(Fore.GREEN + " and go investigate. This is your chance,", 2)
        P_STAT(Fore.GREEN + " you move as quickly and quietly as you can.", 2)
        P_STAT(Fore.GREEN + " You are out, you run!!!", 2)

        you_escaped()
        start()

    elif ANSWER in climb:
        clr_terminal()
        P_STAT(Fore.GREEN + " You decide to climb the railings", 2)
        P_STAT(Fore.GREEN + " You put one foot up and pull yourself up", 2)
        P_STAT(Fore.GREEN + " to the top of them, you raise your other", 2)
        P_STAT(Fore.GREEN + " foot but to your surprise it slips, and you ", 2)
        P_STAT(Fore.GREEN + " impale yourself. You let out an anguished ", 2)
        P_STAT(Fore.GREEN + " cry which alerts the guards, as they ,", 2)
        P_STAT(Fore.GREEN + " approach weapons readied, they slice at you", 2)
        P_STAT(Fore.GREEN + f" with their {new_weapon_two.weapon_type}'s", 1)
        P_STAT(Fore.GREEN + f" you raise the {new_weapon_two.weapon_type}", 1)
        P_STAT(Fore.GREEN + f" you found, it is {new_weapon_two.condition}", 1)
        P_STAT(Fore.GREEN + " , you think you have a chance", 2)
        P_STAT(Fore.GREEN + " but the pain is too much,", 2)
        P_STAT(Fore.GREEN + " and they cut you down", 2)

        player_died()
        game_over()
        start()

# Play again function called at end of game or when player dies


def play_again():
    """
    Asks the player if they would like to play again
    """
    print(Fore.YELLOW + " Would you like to play again? (Y or N)")

    ANSWER = input("=> ").lower().strip()

    while ANSWER not in yes_list and ANSWER not in no_list:
        P_STAT(Fore.RED + f" Please pick the correct option {P_NAME}", 2)
        ANSWER = input("=> ").lower().strip()

    if ANSWER in yes_list:
        clr_terminal()
        start()
    elif ANSWER in no_list:
        clr_terminal()
        P_STAT(Fore.YELLOW + f" Sorry to see you go {P_NAME}", 1)
        P_STAT(Fore.YELLOW + " Please do comeback again", 1)
        game_over()


start()
