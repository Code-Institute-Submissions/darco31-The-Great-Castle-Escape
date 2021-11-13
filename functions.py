import time

import colorama
from colorama import Fore
colorama.init(autoreset=True)


def P_STAT(text, delay):
    """
    To print a line of text and delay the next line for a set amount of time
    """
    print(text)
    time.sleep(delay)


def game_over():
    """
    When the user dies or completes the game this function
    will be called
    """
    P_STAT(Fore.GREEN + '''
    ╔═══╗                 ╔═══╗           
    ║╔═╗║                 ║╔═╗║           
    ║║ ╚╝╔══╗ ╔╗╔╗╔══╗    ║║ ║║╔╗╔╗╔══╗╔═╗
    ║║╔═╗╚ ╗║ ║╚╝║║╔╗║    ║║ ║║║╚╝║║╔╗║║╔╝
    ║╚╩═║║╚╝╚╗║║║║║║═╣    ║╚═╝║╚╗╔╝║║═╣║║ 
    ╚═══╝╚═══╝╚╩╩╝╚══╝    ╚═══╝ ╚╝ ╚══╝╚╝ 
                        ''', 2)


def player_died():
    """
    When the user dies in the game this function
    will be called
    """
    P_STAT(Fore.RED + '''
          ╔╗           ╔╗
          ║║           ║║
        ╔═╝║╔══╗╔══╗ ╔═╝║
        ║╔╗║║╔╗║╚ ╗║ ║╔╗║
        ║╚╝║║║═╣║╚╝╚╗║╚╝║
        ╚══╝╚══╝╚═══╝╚══╝
            ''', 2)


def you_escaped():
    """
    Functioned called in main file when
    the player escapes
    """
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