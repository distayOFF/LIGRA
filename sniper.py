VERSION = "oa1.0"

import json
import requests
import re
import colorama
from colorama import Fore
import datetime
from os import system
from time import sleep
import discord
from discord.ext import commands
from win10toast import ToastNotifier

toaster = ToastNotifier()

with open('Config.json') as f:
    config = json.load(f)

onalt = config.get("on-alt")
token = config.get('discordToken')
rtoken = config.get("on-altToken")
edelay = config.get("delay-enabled")

giveaway_sniper = config.get('giveaway_sniper')
nitro_sniper = config.get('nitro_sniper')
notification = config.get('notification')

sname = ""
stag = ""

def codestart():
    global sname, stag
    if onalt:
        headers = {
            'Authorization': rtoken,
            'Content-Type': 'application/json'
        }

        res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
        res = res.json()
        sname = res['username']
        stag = res['discriminator']

    if onalt:
        onaltt: " "
    else:
        if sname != "":
            onaltt = f"{Fore.LIGHTBLACK_EX}({sname}#{stag})"
        else:
            onaltt = " "

    if edelay:
        ddelay = f"{Fore.LIGHTBLACK_EX}({delay} Seconds)"
    else:
        ddelay = " "

    if giveaway_sniper:
        giveaway = "Active"
    else:
        giveaway = "Turned off"

    if nitro_sniper:
        nitro = "Active"
    else:
        nitro = "Turned off"

    if notification:
        notify = "Active"
    else:
        notify = "Turned off"

    print(f'''{Fore.LIGHTMAGENTA_EX}
 ██▓     ██▓  ▄████  ██▀███   ▄▄▄           ██████  ███▄    █  ██▓ ██▓███  ▓█████  ██▀███
▓██▒    ▓██▒ ██▒ ▀█▒▓██ ▒ ██▒▒████▄       ▒██    ▒  ██ ▀█   █ ▓██▒▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒
▒██░    ▒██▒▒██░▄▄▄░▓██ ░▄█ ▒▒██  ▀█▄     ░ ▓██▄   ▓██  ▀█ ██▒▒██▒▓██░ ██▓▒▒███   ▓██ ░▄█ ▒
▒██░    ░██░░▓█  ██▓▒██▀▀█▄  ░██▄▄▄▄██      ▒   ██▒▓██▒  ▐▌██▒░██░▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄
░██████▒░██░░▒▓███▀▒░██▓ ▒██▒ ▓█   ▓██▒   ▒██████▒▒▒██░   ▓██░░██░▒██▒ ░  ░░▒████▒░██▓ ▒██▒
░ ▒░▓  ░░▓   ░▒   ▒ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░   ▒ ▒▓▒ ▒ ░░ ▒░   ▒ ▒ ░▓  ▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
░ ░ ▒  ░ ▒ ░  ░   ░   ░▒ ░ ▒░  ▒   ▒▒ ░   ░ ░▒  ░ ░░ ░░   ░ ▒░ ▒ ░░▒ ░      ░ ░  ░  ░▒ ░ ▒░
  ░ ░    ▒ ░░ ░   ░   ░░   ░   ░   ▒      ░  ░  ░     ░   ░ ░  ▒ ░░░          ░     ░░   ░
    ░  ░ ░        ░    ░           ░  ░         ░           ░  ░              ░  ░{Fore.LIGHTBLACK_EX}

                               Sniping User  -  {Sniper.user.name}#{Sniper.user.discriminator}
                               Nitro Sniper  -  {nitro} {onaltt}
                            Giveaway Sniper  -  {giveaway} {ddelay}
                               Notification  -  {notify}
    ''' + Fore.RESET)


colorama.init()
Sniper = commands.Bot(
    description=f'[LIGRA] Sniper | Version: {VERSION}',
    command_prefix="",
    self_bot=True
)

def Clear():
    system('cls')

Clear()

def Init():
    if onalt:
        if config.get('discordToken') == config.get('on-altToken'):
            Clear()
            system('mode 47, 24')
            print(f"""{Fore.LIGHTMAGENTA_EX}
▓█████  ██▀███   ██▀███   ▒█████   ██▀███
▓█   ▀ ▓██ ▒ ██▒▓██ ▒ ██▒▒██▒  ██▒▓██ ▒ ██▒
▒███   ▓██ ░▄█ ▒▓██ ░▄█ ▒▒██░  ██▒▓██ ░▄█ ▒
▒▓█  ▄ ▒██▀▀█▄  ▒██▀▀█▄  ▒██   ██░▒██▀▀█▄
░▒████▒░██▓ ▒██▒░██▓ ▒██▒░ ████▓▒░░██▓ ▒██▒
░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
 ░ ░  ░  ░▒ ░ ▒░  ░▒ ░ ▒░  ░ ▒ ▒░   ░▒ ░ ▒░
   ░     ░░   ░   ░░   ░ ░ ░ ░ ▒    ░░   ░
   ░  ░   ░        ░         ░ ░     ░

{Fore.LIGHTMAGENTA_EX}on-altToken{Fore.LIGHTBLACK_EX} can't be the same as {Fore.LIGHTMAGENTA_EX}discordToken{Fore.LIGHTBLACK_EX}!
""")
            sleep(5)
            exit()
        if rtoken == "":
            Clear()
            system('mode 47, 24')
            print(f"""{Fore.LIGHTMAGENTA_EX}
▓█████  ██▀███   ██▀███   ▒█████   ██▀███
▓█   ▀ ▓██ ▒ ██▒▓██ ▒ ██▒▒██▒  ██▒▓██ ▒ ██▒
▒███   ▓██ ░▄█ ▒▓██ ░▄█ ▒▒██░  ██▒▓██ ░▄█ ▒
▒▓█  ▄ ▒██▀▀█▄  ▒██▀▀█▄  ▒██   ██░▒██▀▀█▄
░▒████▒░██▓ ▒██▒░██▓ ▒██▒░ ████▓▒░░██▓ ▒██▒
░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
 ░ ░  ░  ░▒ ░ ▒░  ░▒ ░ ▒░  ░ ▒ ▒░   ░▒ ░ ▒░
   ░     ░░   ░   ░░   ░ ░ ░ ░ ▒    ░░   ░
   ░  ░   ░        ░         ░ ░     ░

{Fore.LIGHTBLACK_EX}You didn't placed your {Fore.LIGHTMAGENTA_EX}on-altToken{Fore.LIGHTBLACK_EX} in {Fore.LIGHTMAGENTA_EX}Config{Fore.LIGHTBLACK_EX}
""")
            sleep(5)
            exit()
        else:
            headers = {
                'Authorization': rtoken,
                'Content-Type': 'application/json'
            }
            r = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
            if r.status_code == 200:
                pass
            else:
                Clear()
                system('mode 47, 24')
                print(f"""{Fore.LIGHTMAGENTA_EX}
▓█████  ██▀███   ██▀███   ▒█████   ██▀███
▓█   ▀ ▓██ ▒ ██▒▓██ ▒ ██▒▒██▒  ██▒▓██ ▒ ██▒
▒███   ▓██ ░▄█ ▒▓██ ░▄█ ▒▒██░  ██▒▓██ ░▄█ ▒
▒▓█  ▄ ▒██▀▀█▄  ▒██▀▀█▄  ▒██   ██░▒██▀▀█▄
░▒████▒░██▓ ▒██▒░██▓ ▒██▒░ ████▓▒░░██▓ ▒██▒
░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
 ░ ░  ░  ░▒ ░ ▒░  ░▒ ░ ▒░  ░ ▒ ▒░   ░▒ ░ ▒░
   ░     ░░   ░   ░░   ░ ░ ░ ░ ▒    ░░   ░
   ░  ░   ░        ░         ░ ░     ░

{Fore.LIGHTBLACK_EX}Unknown {Fore.LIGHTMAGENTA_EX}on-altToken{Fore.LIGHTBLACK_EX} in {Fore.LIGHTMAGENTA_EX}Config{Fore.LIGHTBLACK_EX}
""")
                sleep(5)
                exit()

    if config.get('discordToken') == "":
        Clear()
        system('mode 47, 24')
        print(f"""{Fore.LIGHTMAGENTA_EX}
▓█████  ██▀███   ██▀███   ▒█████   ██▀███
▓█   ▀ ▓██ ▒ ██▒▓██ ▒ ██▒▒██▒  ██▒▓██ ▒ ██▒
▒███   ▓██ ░▄█ ▒▓██ ░▄█ ▒▒██░  ██▒▓██ ░▄█ ▒
▒▓█  ▄ ▒██▀▀█▄  ▒██▀▀█▄  ▒██   ██░▒██▀▀█▄
░▒████▒░██▓ ▒██▒░██▓ ▒██▒░ ████▓▒░░██▓ ▒██▒
░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
░ ░  ░  ░▒ ░ ▒░  ░▒ ░ ▒░  ░ ▒ ▒░   ░▒ ░ ▒░
░     ░░   ░   ░░   ░ ░ ░ ░ ▒    ░░   ░
░  ░   ░        ░         ░ ░     ░

{Fore.LIGHTBLACK_EX}You didn't placed your {Fore.LIGHTMAGENTA_EX}discordToken{Fore.LIGHTBLACK_EX} in {Fore.LIGHTMAGENTA_EX}Config{Fore.LIGHTBLACK_EX}
""")
        sleep(5)
        exit()
    else:
        token = config.get('discordToken')
        try:
            Sniper.run(token, bot=False, reconnect=True)
            system(f'title [LIGRA] Sniper ^| Version: {VERSION}')
        except discord.errors.LoginFailure:
            Clear()
            system('mode 47, 24')
            print(f"""{Fore.LIGHTMAGENTA_EX}
▓█████  ██▀███   ██▀███   ▒█████   ██▀███
▓█   ▀ ▓██ ▒ ██▒▓██ ▒ ██▒▒██▒  ██▒▓██ ▒ ██▒
▒███   ▓██ ░▄█ ▒▓██ ░▄█ ▒▒██░  ██▒▓██ ░▄█ ▒
▒▓█  ▄ ▒██▀▀█▄  ▒██▀▀█▄  ▒██   ██░▒██▀▀█▄
░▒████▒░██▓ ▒██▒░██▓ ▒██▒░ ████▓▒░░██▓ ▒██▒
░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
░ ░  ░  ░▒ ░ ▒░  ░▒ ░ ▒░  ░ ▒ ▒░   ░▒ ░ ▒░
░     ░░   ░   ░░   ░ ░ ░ ░ ▒    ░░   ░
░  ░   ░        ░         ░ ░     ░

{Fore.LIGHTBLACK_EX}Unknown {Fore.LIGHTMAGENTA_EX}discordToken{Fore.LIGHTBLACK_EX} has been placed (or none)
""")
            sleep(5)
            exit()

@Sniper.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, discord.errors.Forbidden):
        print(f"{Fore.RED}Error: {Fore.WHITE} Discord Error: {error}" + Fore.RESET)
    else:
        print(f"{Fore.RED}Error: {Fore.WHITE}{error_str}" + Fore.RESET)

@Sniper.event
async def on_message(message):
    global note_text

    def GiveawayInfo():
        print(
            f"{Fore.LIGHTBLACK_EX}Server: {Fore.WHITE}{message.guild}"
            f"\n{Fore.LIGHTBLACK_EX}Channel: {Fore.WHITE}{message.channel}"
            + Fore.RESET)

    def GiveawayDelayInfo():
        print(
            f"{Fore.LIGHTBLACK_EX}Server: {Fore.WHITE}{message.guild}"
            f"\n{Fore.LIGHTBLACK_EX}Channel: {Fore.WHITE}{message.channel}"
            f"\n{Fore.LIGHTBLACK_EX}Delay: {Fore.WHITE}{delay} Seconds"
            + Fore.RESET)

    def NitroInfo(elapsed, code):
        print(
           f"{Fore.LIGHTBLACK_EX}Server: {Fore.WHITE}{message.guild}"
           f"\n{Fore.LIGHTBLACK_EX}Channel: {Fore.WHITE}{message.channel}"
           f"\n{Fore.LIGHTBLACK_EX}User: {Fore.WHITE}{message.author}"
           f"\n{Fore.LIGHTBLACK_EX}User ID: {Fore.WHITE}{message.author.id}"
           f"\n{Fore.LIGHTBLACK_EX}Delay: {Fore.WHITE}{elapsed}s"
           f"\n{Fore.LIGHTBLACK_EX}Code: {Fore.WHITE}{code}"
           + Fore.RESET)

    time = datetime.datetime.now().strftime("%H:%M")
    if 'discord.gift/' in message.content:
        if nitro_sniper:
            start = datetime.datetime.now()
            code = re.search("discord.gift/(.*)", message.content).group(1)
            if onalt:
                headers = {'Authorization': rtoken}
            else:
                headers = {'Authorization': token}
            r = requests.post(
                f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem',
                headers=headers,
            ).text

            elapsed = datetime.datetime.now() - start
            elapsed = f'{elapsed.seconds}.{elapsed.microseconds}'

            if 'This Gift was already taken.' in r:
                print(""
                      f"\n{Fore.RED}{time} - Nitro has already been taken" + Fore.RESET)
                NitroInfo(elapsed, code)
            elif 'subscription_plan' in r:
                print(""
                      f"\n{Fore.GREEN}{time} - Successfully claimed Nitro" + Fore.RESET)
                NitroInfo(elapsed, code)
                if notification:
                    toaster.show_toast("LIGRA",
                                       "Nitro successfully claimed!",
                                       duration=30)
            elif 'Unknown Gift Code' in r:
                print(""
                      f"\n{Fore.YELLOW}{time} - Unknown Nitro Code" + Fore.RESET)
                NitroInfo(elapsed, code)
        else:
            return

    if 'discord.com/gifts/' in message.content:
        if nitro_sniper:
            start = datetime.datetime.now()
            code = re.search("discord.com/gifts/(.*)", message.content).group(1)
            if onalt:
                headers = {'Authorization': rtoken}
            else:
                headers = {'Authorization': token}
            r = requests.post(
                f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem',
                headers=headers,
            ).text

            elapsed = datetime.datetime.now() - start
            elapsed = f'{elapsed.seconds}.{elapsed.microseconds}'

            if 'This Gift has already been taken' in r:
                print(""
                      f"\n{Fore.GREEN}{time} - Nitro has already been taken" + Fore.RESET)
                NitroInfo(elapsed, code)
            elif 'subscription_plan' in r:
                print(""
                      f"\n{Fore.GREEN}{time} - Successfully claimed Nitro" + Fore.RESET)
                NitroInfo(elapsed, code)
                if notification:
                    toaster.show_toast("LIGRA",
                                       "Nitro successfully claimed",
                                       duration=30)
            elif 'Unknown Nitro Code' in r:
                print(f""
                      f"\n{Fore.RED}{time} - Unknown Nitro Code" + Fore.RESET)
                NitroInfo(elapsed, code)

        else:
            return

    if 'discord.com/gifts/' in message.content:
        if nitro_sniper:
            start = datetime.datetime.now()
            code = re.search("discord.com/gifts/(.*)", message.content).group(1)
            if onalt:
                headers = {'Authorization': rtoken}
            else:
                headers = {'Authorization': token}
            r = requests.post(
                f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem',
                headers=headers,
            ).text

            elapsed = datetime.datetime.now() - start
            elapsed = f'{elapsed.seconds}.{elapsed.microseconds}'

            if 'This Gift has already been taken' in r:
                print(""
                      f"\n{Fore.GREEN}{time} - Nitro has already been taken" + Fore.RESET)
                NitroInfo(elapsed, code)
            elif 'subscription_plan' in r:
                print(""
                      f"\n{Fore.GREEN}{time} - Successfully claimed Nitro" + Fore.RESET)
                NitroInfo(elapsed, code)
                if notification:
                    toaster.show_toast("LIGRA",
                                       "Nitro successfully claimed",
                                       duration=30)
            elif 'Unknown Nitro Code' in r:
                print(f""
                      f"\n{Fore.RED}{time} - Unknown Nitro Code" + Fore.RESET)
                NitroInfo(elapsed, code)

        else:
            return

    if 'GIVEAWAY' in message.content:
        if giveaway_sniper:
            if message.author.id == 294882584201003009 or message.author.id == 673918978178940951 or message.author.id == 582537632991543307 or message.author.id == 649604306596596528138:
                try:
                    if not edelay:
                        await message.add_reaction("🎉")
                except discord.errors.Forbidden:
                    print(""
                          f"\n{Fore.RED}{time} - Couldn't react to the giveaway" + Fore.RESET)
                    GiveawayInfo()
                if edelay:
                    print(""
                          f"\n{Fore.GREEN}{time} - Giveaway found" + Fore.RESET)
                    GiveawayInfo()
                if notification:
                    if edelay:
                        toaster.show_toast("LIGRA",
                                           f"Sniped a Giveaway in {delay}s",
                                           duration=30)
                    else:
                        toaster.show_toast("LIGRA",
                                          "Sniped a Giveaway",
                                          duration=30)

                try:
                    if edelay:
                        sleep(delay)
                        await message.add_creation("🎉")
                        print("")
                        print(f"{Fore.GREEN}Sniped a Giveaway in {delay} seconds")
                except discord.errors.Forbidden:
                    print(""
                          f"\n{Fore.RED}{time} - Couldn't react to the giveaway" + Fore.RESET)
                    GiveawayInfo()

        else:
            return

    if f'Congratulations <@{Sniper.user.id}>' in message.content or f'<@{Sniper.user.id}> has won' in message.content:
        if giveaway_sniper:
            if message.author.id == 294882584201003009 or message.author.id == 673918978178940951 or message.author.id == 582537632991543307 or message.author.id == 396464677032427630 or message.author.id == 649604306596596528138:
                print(""
                      f"\n{Fore.GREEN}{time} - Giveaway won" + Fore.RESET)
                GiveawayInfo()
                if notification:
                    toaster.show_toast("LIGRA",
                                       "Giveaway won",
                                       duration=30)

        else:
            return
    await Sniper.process_commands(message)

@Sniper.event
async def on_connect():
    Clear()

    codestart()
    system(f'title [LIGRA] Sniper ^| Version: {VERSION}')
