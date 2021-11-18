# Creator: Stephen Darcy
# Date: 01-11-21
# Project 3 - The code Institute

# Calls the function from clear.py to clear the terminal
# after some not all interactions
from clear import clr_terminal
from set_class import Weapon

#  Calls the functions from functions.py to give
# visual help to the player on end game scenarios
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
new_weapon = Weapon("knife", "rusty")
new_weapon_two = Weapon("sword", "razor sharp")

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
        if P_NAME == "":
            print(Fore.YELLOW + " You need to enter a username to continue...")
            continue
        else:
            break
    P_STAT(Fore.YELLOW + f" Welcome {P_NAME}, good luck, you will need it", 2)
    P_STAT(Fore.YELLOW + " You awake a little dazed and confused", 2)
    P_STAT(Fore.YELLOW + " You find yourself in a dimly lit room", 2)
    P_STAT(Fore.YELLOW + " You can hear the rain crashing down outside", 2)
    P_STAT(Fore.YELLOW + " You try to recall how you got here", 2)
    P_STAT(Fore.YELLOW + " You look around the room", 2)
    P_STAT(Fore.YELLOW + " Its big cold and damp, you notice a window", 2)
    P_STAT(Fore.YELLOW + " A large wooden door is in front of you", 2)
    P_STAT(Fore.YELLOW + " Not a lot to choose from", 2)
    print(Fore.BLUE + " So, do you have the guts to try and escape?(y or n)")
    # convert the player's input to lower_case
    answer = input("=> ").lower().strip()

    if answer == "yes" or answer == "y":
        clr_terminal()
        small_window()
    elif answer == "no" or answer == "n":
        clr_terminal()
        P_STAT(Fore.RED + " Shame", 1)
        P_STAT(Fore.RED + f" Enjoy the solitude and loneliness {P_NAME}", 2)
        play_again()
    else:
        P_STAT(Fore.RED + " Error, please enter a valid choice (e or s) ", 2)
        start()

# Player has the option to check the window or ignore it


def small_window():
    """
    Function called to let the player explore the
    small window in the room
    """
    P_STAT(Fore.BLUE + " You get up and walk towards the window", 1)
    P_STAT(Fore.BLUE + " You peer out and can only see darkness", 1)
    print(Fore.YELLOW + " Do you try open the window? (y or n)")

    try_window = input("=> ").lower().strip()

    if try_window == "y":
        clr_terminal()
        P_STAT(Fore.BLUE + " You try the window, nothing.", 1)
        P_STAT(Fore.BLUE + " Urggh its sealed shut", 1)
        try_door()

    elif try_window == "n":
        clr_terminal()
        P_STAT(Fore.BLUE + " You ignore the window", 1)
        P_STAT(Fore.BLUE + " and head for the door", 1)
        try_door()

    else:
        P_STAT(Fore.RED + " Error, please enter a valid choice (y or n)", 1)
        small_window()

# The player will have the option to try the door
# where they can choose to leave or stay


def try_door():
    """
    The function offers the player the choice of
    opening the door or not in the first room.
    """
    P_STAT(Fore.BLUE + " Reaching the door you try the handle", 2)
    P_STAT(Fore.BLUE + " It opens, thats odd you think", 2)
    print(Fore.YELLOW + " Do you take a look outside? (y or n)")

    look_outside = input("=>").lower().strip()

    if look_outside == "y" or look_outside == "yes":
        clr_terminal()
        P_STAT(Fore.BLUE + " You open the door as silently as you can", 2)
        P_STAT(Fore.BLUE + " Looking outside you see a door at either end", 2)
        P_STAT(Fore.BLUE + " of a long corridor", 2)
        take_items()

    elif look_outside == "n" or look_outside == "no":
        clr_terminal()
        P_STAT(Fore.BLUE + " You are too terrified to go on, shame", 1)
        P_STAT(Fore.BLUE + f" Enjoy the solitude and loneliness {P_NAME}", 2)
        play_again()

    else:
        P_STAT(Fore.RED + " Error, please enter a valid choice (y or n)", 1)
        try_door()

# The player can choose to search the drawer or leave it.


def take_items():
    """
    The function gives the player the option to check a discovered drawer
    """
    P_STAT(Fore.BLUE + " A table outside catches your eye,", 1)
    P_STAT(Fore.BLUE + " it has a drawer inset", 2)
    print(Fore.YELLOW + " Do you try the drawer in the table? (y or n)")

    open_drawer = input("=> ").lower().strip()

    if open_drawer == "y" or open_drawer == "yes":
        clr_terminal()
        P_STAT(Fore.BLUE + " You pull out the drawer and find a", 1)
        P_STAT(Fore.BLUE + f" key and a {new_weapon.weapon_type}", 2)
        P_STAT(Fore.BLUE + " You reach in quickly and pick up both items", 2)
        P_STAT(Fore.BLUE + " You stuff them in your pockets", 2)
        P_STAT(Fore.BLUE + " and close the drawer", 2)
        P_STAT(Fore.BLUE + f" Maybe the {new_weapon.weapon_type}", 3)
        P_STAT(Fore.BLUE + " will open the window", 2)
        back_to_window()

    elif open_drawer == "n" or open_drawer == "no":
        clr_terminal()
        P_STAT(Fore.BLUE + " Probably best not to disturb anything", 2)
        direction_choice_two()

    else:
        P_STAT(Fore.RED + " Error, please enter a valid choice (y or n)", 2)
        take_items()

# Player returns to the table form locked door to retrive items.


def return_to_table():
    """
    Player returns to the table from the locked door
    """
    P_STAT(Fore.BLUE + " You go back to the table and pull drawer open", 2)
    P_STAT(Fore.BLUE + f" Result, a key and {new_weapon.weapon_type}", 2)
    P_STAT(Fore.BLUE + " You stuff them in your pockets ", 2)
    P_STAT(Fore.BLUE + " and close the drawer", 2)
    P_STAT(Fore.BLUE + " you quickly get back to the right hand door", 2)
    go_right_back()

# Player goes back to the first room to try the window with knife.


def back_to_window():
    """
    Brings the player back into the start room to the locked
    window
    """
    P_STAT(Fore.RED + "\n You return to the first room", 2)

    P_STAT(Fore.BLUE + "You look out the window again.Do you try open the ", 2)
    print(Fore.YELLOW + f" window with the {new_weapon.weapon_type}? (y or n)")

    open_window = input("=> ").lower().strip()

    if open_window == "y" or open_window == "yes":
        clr_terminal()
        P_STAT(Fore.BLUE + f"You jam the {new_weapon.weapon_type} into the", 2)
        P_STAT(Fore.BLUE + " gap of the window, the timber comes loose ", 2)
        P_STAT(Fore.BLUE + " and the window pops open. Success, ", 2)
        P_STAT(Fore.BLUE + " you climb up and outside and as you peer", 2)
        P_STAT(Fore.BLUE + " through the dark you can just make out the", 2)
        P_STAT(Fore.BLUE + " sloping roof. You jump but to your horror", 3)
        P_STAT(Fore.BLUE + " the tile gives way and you fall to your death", 2)

        player_died()
        game_over()
        play_again()
        clr_terminal()

    elif open_window == "n" or open_window == "no":
        clr_terminal()
        P_STAT(Fore.BLUE + " Looking down into the dark bleak night", 2)
        P_STAT(Fore.BLUE + " you decide its best not to try and make your", 2)
        P_STAT(Fore.BLUE + " way back to the large door opening", 2)
        direction_choice()

    else:
        P_STAT(Fore.RED + " Error, please enter a valid choice (y or n)", 2)
        back_to_window()

# First direction choice 


def direction_choice():
    """
    Player will make a choice to go left or right
    out of the doorway and they will have the
    objects from the drawer
    """
    P_STAT(Fore.BLUE + " Standing in the doorway you need to make a choice", 1)
    print(Fore.YELLOW + " Do you go left or go right? (l or r)")

    player_choice = input("=> ").lower().strip()

    if player_choice == "l" or player_choice == "left":
        clr_terminal()
        go_left()
    elif player_choice == "r" or player_choice == "right":
        clr_terminal()
        go_right()
    else:
        print(Fore.RED + "That it not a valid option, please enter l or r")
        direction_choice()

# If player ignores the drawer ans decides to move on


def direction_choice_two():
    """
    Second direction choice if player takes nothing from the drawer
    """
    P_STAT(Fore.BLUE + " Standing in the doorway you need to make a choice", 1)
    print(Fore.YELLOW + " Do you go left or go right? (l or r)")
    player_choice_two = input("=> ").lower().strip()

    if player_choice_two == "l" or player_choice_two == "left":
        clr_terminal()
        go_left()
    elif player_choice_two == "r" or player_choice_two == "right":
        clr_terminal()
        P_STAT(Fore.BLUE + " You reach the door and try open it", 2)
        P_STAT(Fore.RED + " Its locked, you remember the drawer, maybe?", 2)
        return_to_table()
    else:
        print(Fore.RED + " That it not a valid option, please enter l or r")
        return_to_table()

# Player decides to return from left hand room 
# or goes to right hand door without key.


def direction_choice_three():
    """
    Function for the player to return to the right hand door
    if they decide to return after going left
    """
    P_STAT(Fore.BLUE + " You reach the door to the right and try open it", 2)
    P_STAT(Fore.BLUE + " Its locked, you remember the drawer, maybe?", 2)
    return_to_table()


def go_left():
    """
    The player goes left and will have to makes choices
    in the next room
    """
    P_STAT(Fore.BLUE + " You decide to turn left and head towards the door", 2)
    P_STAT(Fore.BLUE + " as you approach the door you slow down", 2)
    P_STAT(Fore.BLUE + " you push at the door and it creaks open", 2)
    P_STAT(Fore.BLUE + " as your eyes adjust you make out a candle light.", 2)
    P_STAT(Fore.BLUE + " You walk inside, at the far end there is an", 2)
    P_STAT(Fore.BLUE + " opening.You approach it and see a staircase", 2)
    P_STAT(Fore.BLUE + " going down.You look around the room", 2)
    print(Fore.YELLOW + " Do you explore,proceed or go back? (e-p-g)")

    decision = input("=> ").lower().strip()

    if decision == "explore" or decision == "e":
        clr_terminal()
        explore_room()

    elif decision == "proceed" or decision == "p":
        clr_terminal()
        proceed_down_stairs()

    elif decision == "go back" or decision == "g":
        P_STAT(Fore.BLUE + " You decide to go back to the other door", 2)
        clr_terminal()
        direction_choice_three()
    else:
        print(Fore.RED + " That it not a valid option, please enter (e-p-g)")
        go_left()

# The player can explore the right hand side room


def explore_room():
    """
    Player decides to explore room
    """
    P_STAT(Fore.BLUE + " As you look around the room, the idea you are", 2)
    P_STAT(Fore.BLUE + " in a castle still leaves you feeling confused", 2)
    P_STAT(Fore.BLUE + " You see a bowl with fruit in it, you are starving", 2)
    P_STAT(Fore.BLUE + " so you pick it up and eat while", 2)
    P_STAT(Fore.BLUE + " continuing to explore. You find a belt,", 2)
    P_STAT(Fore.BLUE + " you wrap it around you and slip the", 2)
    P_STAT(Fore.BLUE + f" {new_weapon.weapon_type} in", 2)
    P_STAT(Fore.BLUE + " As there is nothing else left to check", 2)
    P_STAT(Fore.BLUE + " you decide to go downstairs", 2)

    proceed_down_stairs()

# The player decides to ignore the room and movedown the stairs.


def proceed_down_stairs():
    """
    Player proceeds down the spiral stairs
    """
    P_STAT(Fore.BLUE + " You enter the doorway", 2)
    P_STAT(Fore.BLUE + " Hugging the wall you make your way down", 2)
    P_STAT(Fore.BLUE + " You reach the bottom and as you listen", 2)
    P_STAT(Fore.BLUE + " you can hear what appears to be two voices", 2)
    P_STAT(Fore.BLUE + " Holding your breath you peek around the corner", 2)
    P_STAT(Fore.BLUE + " and see two large men,", 2)
    P_STAT(Fore.BLUE + f" both with {new_weapon_two.weapon_type}'s?", 2)
    P_STAT(Fore.BLUE + " Their backs are to you", 2)
    P_STAT(Fore.YELLOW + " Hmmm attack or sneak? Your choice - (a or s)", 2)

    next_move = input("=> ").lower().strip()

    if next_move == "attack" or next_move == "a":
        clr_terminal()
        P_STAT(Fore.BLUE + " You charge at the men who are surprised", 2)
        P_STAT(Fore.BLUE + " but alas, one foul swipe and you are....", 1)

        player_died()
        game_over()
        play_again()

    elif next_move == "sneak" or next_move == "s":
        P_STAT(Fore.BLUE + " You put your back against the wall", 2)
        P_STAT(Fore.BLUE + " and sneak as quietly as you can passed them", 2)
        bottom_floor()

    else:
        print(Fore.RED + " That it not a valid option, please enter (e-p-g)")
        proceed_down_stairs()

# Player returns to the right hand door after searching the drawer


def go_right_back():
    """
    Return to the righthand door with the key
    """
    P_STAT(Fore.BLUE + " Using the key you push the door open and enter", 2)
    P_STAT(Fore.BLUE + " Looking around this lavish room you notice", 2)
    P_STAT(Fore.BLUE + " what looks like three levers on the wall", 2)
    P_STAT(Fore.BLUE + " You decide to try the levers", 1)

# Player will get a random choice of lever and this will decide the outcome
    try_lever = random.randint(1, 3)

    if try_lever == 1:
        clr_terminal()
        P_STAT(Fore.BLUE + " You pull the first lever, you hear a groan", 1.2)
        P_STAT(Fore.BLUE + " as you turn a large object comes at you ...", 2)

        player_died()
        game_over()
        play_again()

    elif try_lever == 2:
        clr_terminal()
        P_STAT(Fore.BLUE + " You pull the second lever, you hear a groan", 1.2)
        P_STAT(Fore.BLUE + " as you turn a large object comes at you ...", 2)

        player_died()
        game_over()
        play_again()

    elif try_lever == 3:
        clr_terminal()

        P_STAT(Fore.BLUE + " You pull the third lever ", 1.2)
        P_STAT(Fore.BLUE + " you hear a noise and a concealed door opens", 2)
        P_STAT(Fore.BLUE + " You look around the room and ", 1.2)
        P_STAT(Fore.BLUE + " see a candle on the side table, picking it up", 2)
        P_STAT(Fore.BLUE + " You crouch down and walk into the opening", 2)
        P_STAT(Fore.BLUE + " Holding the candle up the passage ", 2)
        P_STAT(Fore.BLUE + " looks long and unused. You proceed forward", 2)
        P_STAT(Fore.BLUE + " carful as it is sloping down", 2)
        P_STAT(Fore.BLUE + " You eventually reach the end and", 2)
        P_STAT(Fore.BLUE + " reappear in a room.You hear voices,", 2)
        P_STAT(Fore.BLUE + " but they are coming from behind you", 2)
        bottom_floor()

    else:
        print(Fore.RED + " That it not a valid option, please pick 1,2,3")
        go_right_back()


def go_right():
    """
    Player returns to the corridor and goes to the right
    hand door from the starting room. This will also be the go right from the
    room the player initially makes.
    """
    P_STAT(Fore.BLUE + " You reach the door to the right and try open it", 2)
    P_STAT(Fore.RED + " Locked!!", 2)
    P_STAT(Fore.BLUE + " You then remember the key and try it, it works", 2)
    P_STAT(Fore.BLUE + " You push the door open and enter", 2)
    P_STAT(Fore.BLUE + " Looking around this lavish room you notice", 2)
    P_STAT(Fore.BLUE + " three levers on the wall", 2)
    P_STAT(Fore.BLUE + " You decide to try the levers", 1)

    # Player will get a random choice of lever and this will decide the outcome
    try_lever = random.randint(1, 3)

    if try_lever == 1:
        clr_terminal()
        P_STAT(Fore.BLUE + " You pull the first lever, you hear a groan", 1.2)
        P_STAT(Fore.BLUE + " as you turn a large object comes at you ...", 2)

        player_died()
        game_over()
        play_again()

    elif try_lever == 2:
        clr_terminal()
        P_STAT(Fore.BLUE + " You pull the second lever, you hear a groan", 1.2)
        P_STAT(Fore.BLUE + " as you turn a large object comes at you ...", 2)

        player_died()
        game_over()
        play_again()

    elif try_lever == 3:
        clr_terminal()

        P_STAT(Fore.BLUE + " You pull the third lever ", 1.2)
        P_STAT(Fore.BLUE + " you hear a noise and a concealed door opens", 2)
        P_STAT(Fore.BLUE + " You look around the room and ", 1.2)
        P_STAT(Fore.BLUE + " see a candle on the side table, picking it up", 2)
        P_STAT(Fore.BLUE + " You crouch down and walk into the opening", 2)
        P_STAT(Fore.BLUE + " Holding the candle up the passage ", 2)
        P_STAT(Fore.BLUE + " looks long and unused. You proceed forward", 2)
        P_STAT(Fore.BLUE + " carful as it is sloping down", 2)
        P_STAT(Fore.BLUE + " You eventually reach the end and", 2)
        P_STAT(Fore.BLUE + " reappear in a room.You hear voices,", 2)
        P_STAT(Fore.BLUE + " but they are coming from behind you", 2)
        bottom_floor()

# The player will get a choice of three paths that lie ahead.


def bottom_floor():
    """
    The player is in the place they sneak to from
    the stairs and from the secret tunnel and has a choice of 3 paths
    """
    P_STAT(Fore.BLUE + " Looking ahead you can see three paths", 2)
    P_STAT(Fore.BLUE + " There is a straight path, left and right path", 2)
    print(Fore.YELLOW + " Do you go s - l - r")

    path_choice = input("=> ").lower().strip()

    if path_choice == "s" or path_choice == "straight":
        clr_terminal()
        P_STAT(Fore.BLUE + " You decide to proceed straight ahead", 2)
        P_STAT(Fore.BLUE + " Oh sugar..,a group of angry men approach..", 2)

        player_died()
        game_over()
        play_again()

    elif path_choice == "l" or path_choice == "left":
        clr_terminal()
        P_STAT(Fore.BLUE + " You decide to take the left path ahead", 2)
        P_STAT(Fore.BLUE + " You are in a room with a vent on the wall", 2)
        print(Fore.YELLOW + " Do you open the vent? (y or n)")

        open_vent = input("=> ").lower().strip()

        if open_vent == "y" or open_vent == "yes":
            clr_terminal()
            P_STAT(Fore.BLUE + " You pry the vent open and enter", 2)
            P_STAT(Fore.BLUE + " You crawl forward and can ", 2)
            P_STAT(Fore.BLUE + " see another vent in the distance", 2)
            P_STAT(Fore.BLUE + " as you reach the next vent ", 2)
            P_STAT(Fore.BLUE + " you can see below you a guard on his own", 2)
            print(Fore.YELLOW + " Try kill the guard? (y or n)")

        elif open_vent == "n" or open_vent == "no":
            clr_terminal()
            return_to_paths()

        else:
            print(Fore.RED + " That it not a valid option, please pick y or n")
            bottom_floor()

        kill_guard = input("=> ").lower().strip()

        if kill_guard == "y" or kill_guard == "yes":
            clr_terminal()
            P_STAT(Fore.BLUE + "You pry the vent open and ready the ", 2)
            P_STAT(Fore.BLUE + f" {new_weapon.weapon_type}", 2)
            P_STAT(Fore.BLUE + "You jump down surprising the guard.", 2)
            P_STAT(Fore.BLUE + "With one stroke you cut his throat", 2)
            outside()

        elif kill_guard == "n" or kill_guard == "no":
            clr_terminal()
            P_STAT(Fore.BLUE + " You decide to spare his life... for now.", 2)
            return_to_paths()

        else:
            print(Fore.RED + " That it not a valid option, please pick y or n")
            bottom_floor()

    elif path_choice == "r" or path_choice == "right":
        P_STAT(Fore.BLUE + " You veer right to an empty room", 2)
        P_STAT(Fore.BLUE + " more doors, two of them", 2)
        print(Fore.YELLOW + " Left or Right? (l or r)")

        way_forward = input("=> ").lower().strip()

        if way_forward == "left" or way_forward == "l":
            clr_terminal()
            P_STAT(Fore.BLUE + " You open the lefthand door", 2)
            P_STAT(Fore.BLUE + " Oh no!! A room full of guards", 2)

            player_died()
            game_over()
            play_again()

        elif way_forward == "right" or way_forward == "r":
            clr_terminal()

            P_STAT(Fore.BLUE + " You open the right hand door", 2)
            P_STAT(Fore.BLUE + " Dogs? and guard dogs..", 2)

            player_died()
            game_over()
            play_again()

    else:
        print(Fore.RED + " That it not a valid option, please pick l,r,s")
        bottom_floor()

# Player decides to return to the 3 paths


def return_to_paths():
    """
    Function returns palyers to path choices
    """
    P_STAT(Fore.BLUE + " You decide to return to the secret tunnel opening", 2)
    bottom_floor()

# Player choices for outside the castle


def outside():
    """
    Players choices for outside the castle
    """
    P_STAT(Fore.BLUE + " Quickly you search him and find keys and a", 2)
    P_STAT(Fore.BLUE + f" {new_weapon_two.weapon_type}", 2)
    P_STAT(Fore.BLUE + " Looking up there is a door ahead.", 2)
    print(Fore.YELLOW + " Proceed through door? (y or n)")

    go_to_door = input("=> ").lower().strip()

    if go_to_door == "yes" or go_to_door == "y":
        clr_terminal()
        P_STAT(Fore.BLUE + " You fumble through the keys", 2)
        P_STAT(Fore.BLUE + " and find the right one", 2)
        P_STAT(Fore.BLUE + " You open the door and find yourself outside", 2)
        P_STAT(Fore.BLUE + " Pitch black and raining heavily", 2)
        P_STAT(Fore.BLUE + " you walk forward and reach the", 2)
        P_STAT(Fore.BLUE + " front of the building you can make out", 2)
        P_STAT(Fore.BLUE + " a gate ahead , guarded by two men", 2)
        P_STAT(Fore.BLUE + " There are high railings all around but", 2)
        P_STAT(Fore.BLUE + " you think you could climb them", 2)
        print(Fore.YELLOW + " Distract or Climb? (d or c)")

    elif go_to_door == "no" or go_to_door == "n":
        P_STAT(Fore.BLUE + " You decide to go back to the pathways", 2)
        bottom_floor()
    else:
        P_STAT(Fore.RED + " That it not a valid option, please pick y or n", 1)
        outside()

    new_choice = input("=> ").lower().strip()

    if new_choice == "d":
        clr_terminal()
        P_STAT(Fore.BLUE + " You look around for something to distract", 2)
        P_STAT(Fore.BLUE + " them,picking up a stone you throw", 2)
        P_STAT(Fore.BLUE + " it at the railing,perfect shot,", 2)
        P_STAT(Fore.BLUE + " it makes a loud bang alerting them.", 2)
        P_STAT(Fore.BLUE + " The two guards leave their post", 2)
        P_STAT(Fore.BLUE + " and go investigate.This is your chance,", 2)
        P_STAT(Fore.BLUE + " you move as quickly and quietly as you can.", 2)
        P_STAT(Fore.BLUE + " You are out, you run!!!", 2)

        you_escaped()
        play_again()

    elif new_choice == "c":
        clr_terminal()
        P_STAT(Fore.BLUE + " You decide to climb the railings", 2)
        P_STAT(Fore.BLUE + " You put one foot up and pull yourself up", 2)
        P_STAT(Fore.BLUE + " to the top of them, you raise your other foot", 2)
        P_STAT(Fore.BLUE + " but to your surprise it slips, and you ", 2)
        P_STAT(Fore.BLUE + " impale yourself.You let out an anguished cry", 2)
        P_STAT(Fore.BLUE + " which alerts the guards, as they approach,", 2)
        P_STAT(Fore.BLUE + " weapons readied, one slice and ..", 2)

        player_died()
        game_over()
        play_again()

    else:
        P_STAT(Fore.RED + " That it not a valid option, please pick d or c", 1)
        outside()

# Play again function called at end of game or when player dies


def play_again():
    """
    Asks the player if they would like to play again
    """
    print(Fore.YELLOW + " Would you like to play again? (Y or N)")

    answer = input("=> \n").lower().strip()

    if answer == "y" or answer == "yes":
        clr_terminal()
        start()
    elif answer == "n" or answer == "no":
        clr_terminal()
        P_STAT(Fore.YELLOW + f" Sorry to see you go {P_NAME}", 1)
        P_STAT(Fore.YELLOW + " Please do comeback again", 1)
        game_over()
    else:
        P_STAT(Fore.RED + " That it not a valid option, please pick y or n", 1)
        start()


start()
