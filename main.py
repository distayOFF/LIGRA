VERSION = "oa1.0"

from sniper import *
from selfbot import *

from colorama import Fore
from os import system

def mainmenu():
    system(f'title [LIGRA] Mainmenu ^| Version: {VERSION}')
    system('mode 47, 24')
    print(f'''{Fore.LIGHTMAGENTA_EX}
     ██▓     ██▓  ▄████  ██▀███   ▄▄▄
    ▓██▒    ▓██▒ ██▒ ▀█▒▓██ ▒ ██▒▒████▄
    ▒██░    ▒██▒▒██░▄▄▄░▓██ ░▄█ ▒▒██  ▀█▄
    ▒██░    ░██░░▓█  ██▓▒██▀▀█▄  ░██▄▄▄▄██
    ░██████▒░██░░▒▓███▀▒░██▓ ▒██▒ ▓█   ▓██▒
    ░ ▒░▓  ░░▓   ░▒   ▒ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░
    ░ ░ ▒  ░ ▒ ░  ░   ░   ░▒ ░ ▒░  ▒   ▒▒ ░
      ░ ░    ▒ ░░ ░   ░   ░░   ░   ░   ▒
        ░  ░ ░        ░    ░           ░  ░{Fore.LIGHTBLACK_EX}
      official LIGRA release by distayOFF{Fore.LIGHTMAGENTA_EX}
╔═════════════════════════════════════════════╗
║                                             ║
║        [1] Nitro, Giveawaysniper [1]        ║
║        [2]        Selfbot        [2]        ║
║                                             ║
╚═════════════════════════════════════════════╝
    ''' + Fore.RESET)
    choice = input(f'{Fore.LIGHTMAGENTA_EX}[>] ')
    if choice == '1':
        system('cls')
        system('mode 91, 30')
        Init()
    elif choice == '2':
        system('cls')
        startSelfbot()
    else:
        mainmenu()

if __name__ == "__main__":
    mainmenu()
