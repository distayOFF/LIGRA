VERSION = "oa1.0"

import discord, ctypes, json, webbrowser, requests, datetime, urllib, time, string, random, asyncio, aiohttp, typing, emoji, psutil, sys
from discord.ext import commands, tasks
from colorama import Fore, Back, Style
from selenium import webdriver
from itertools import cycle
from os import system, execv
from contextlib import redirect_stdout

with open("Config.json") as f:
    config = json.load(f)

TOKEN = config.get("selfbotToken")
PREFIX = config.get("selfbotPrefix")

psutil.cpu_percent(interval=1)
prefix = PREFIX

def ready():
    print(f"""{Fore.LIGHTBLACK_EX}___________________________________________________________________________________________________{Fore.LIGHTMAGENTA_EX}

 ██▓     ██▓  ▄████  ██▀███   ▄▄▄           ██████ ▓█████  ██▓      █████▒▄▄▄▄    ▒█████  ▄▄▄█████▓
▓██▒    ▓██▒ ██▒ ▀█▒▓██ ▒ ██▒▒████▄       ▒██    ▒ ▓█   ▀ ▓██▒    ▓██   ▒▓█████▄ ▒██▒  ██▒▓  ██▒ ▓▒
▒██░    ▒██▒▒██░▄▄▄░▓██ ░▄█ ▒▒██  ▀█▄     ░ ▓██▄   ▒███   ▒██░    ▒████ ░▒██▒ ▄██▒██░  ██▒▒ ▓██░ ▒░
▒██░    ░██░░▓█  ██▓▒██▀▀█▄  ░██▄▄▄▄██      ▒   ██▒▒▓█  ▄ ▒██░    ░▓█▒  ░▒██░█▀  ▒██   ██░░ ▓██▓ ░
░██████▒░██░░▒▓███▀▒░██▓ ▒██▒ ▓█   ▓██▒   ▒██████▒▒░▒████▒░██████▒░▒█░   ░▓█  ▀█▓░ ████▓▒░  ▒██▒ ░
░ ▒░▓  ░░▓   ░▒   ▒ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░   ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒░▓  ░ ▒ ░   ░▒▓███▀▒░ ▒░▒░▒░   ▒ ░░
░ ░ ▒  ░ ▒ ░  ░   ░   ░▒ ░ ▒░  ▒   ▒▒ ░   ░ ░▒  ░ ░ ░ ░  ░░ ░ ▒  ░ ░     ▒░▒   ░   ░ ▒ ▒░     ░
  ░ ░    ▒ ░░ ░   ░   ░░   ░   ░   ▒      ░  ░  ░     ░     ░ ░    ░ ░    ░    ░ ░ ░ ░ ▒    ░
    ░  ░ ░        ░    ░           ░  ░         ░     ░  ░    ░  ░        ░          ░ ░{Fore.LIGHTBLACK_EX}

                                          User  -  {LIGRA.user.name}
                                       Version  -  {VERSION}
                                        Prefix  -  {PREFIX}
___________________________________________________________________________________________________
""")

def Nitro():
    code = "".join(random.choices(string.ascii_letters + string.digits, k=16))
    return f"https://discord.gift/{code}"

def RandomColor():
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor

def RandString():
    return "".join(random.choice(string.ascii_letters + string.digits) for i in range(random.randint(4, 4)))

client = commands.Bot(
    command_prefix=PREFIX,
    self_bot=True
)
LIGRA = client
LIGRA.remove_command('help')
LIGRA.launch_time = datetime.datetime.now()

@LIGRA.event
async def on_message_edit(before, after):
    await LIGRA.process_commands(after)

@LIGRA.event
async def on_connect():
    system("mode 99, 30")
    system(f'title [LIGRA] Sniper ^| Version: {VERSION}')
    ready()

@LIGRA.command()
async def myinfo(ctx):
    print(f'{Fore.MAGENTA}[{datetime.datetime.now()} UTC]\n[INPUT] {Fore.LIGHTMAGENTA_EX}{prefix}myinfo{Fore.MAGENTA} in: {Fore.LIGHTMAGENTA_EX}#{ctx.channel}{Fore.MAGENTA}')
    await ctx.message.delete()
    await ctx.send(f'You have {len(LIGRA.user.friends)} friends and you are on {len(LIGRA.guilds)} servers!', delete_after=5)
    print(f'[OUTPUT] Answer in: {Fore.LIGHTMAGENTA_EX}#{ctx.channel}{Fore.MAGENTA}\n')

@LIGRA.command()
async def runtime(ctx):
    print(f"{Fore.MAGENTA}[{datetime.datetime.now()} UTC]\n[INPUT] {Fore.LIGHTMAGENTA_EX}{prefix}runtime{Fore.MAGENTA} in: {Fore.LIGHTMAGENTA_EX}#{ctx.channel}{Fore.MAGENTA}")
    await ctx.message.delete()
    delta_uptime = datetime.datetime.now() - LIGRA.launch_time
    hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    embed = discord.Embed(color=discord.Colour.magenta(), timestamp=ctx.message.created_at, description=f":timer: **{hours} hour(s) {minutes} minute(s), {seconds} seconds** :timer: ")
    embed.set_author(name='SELFBOT - RUNTIME')
    embed.set_footer(text=f"[LIGRA] Selfbot | Version: {VERSION}")
    await ctx.send(embed=embed, delete_after=10)
    print(f'[OUTPUT] Answer in: {Fore.LIGHTMAGENTA_EX}#{ctx.channel}{Fore.MAGENTA}\n')

@LIGRA.command()
async def ac(ctx, *, text):
    print(f"{Fore.MAGENTA}[{datetime.datetime.now()} UTC]\n[INPUT] {Fore.LIGHTMAGENTA_EX}{prefix}ac{Fore.MAGENTA} in: {Fore.LIGHTMAGENTA_EX}#{ctx.channel}{Fore.MAGENTA}")
    await ctx.message.delete()
    r = requests.get(f"http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}").text
    if len("```"+r+"```") > 2000:
        return
    await ctx.send(f"```{r}```")
    time.sleep(0.25)
    print(f'[OUTPUT] Answer in: {Fore.LIGHTMAGENTA_EX}#{ctx.channel}{Fore.MAGENTA}\n')

@LIGRA.command()
async def meme(ctx):
    print(f"{Fore.MAGENTA}[{datetime.datetime.now()} UTC]\n[INPUT] {Fore.LIGHTMAGENTA_EX}{prefix}meme{Fore.MAGENTA} in: {Fore.LIGHTMAGENTA_EX}#{ctx.channel}{Fore.MAGENTA}")
    await ctx.message.delete()
    r = requests.get("https://some-random-api.ml/meme").json()
    embed = discord.Embed(color=RandomColor(), timestamp=ctx.message.created_at)
    embed.set_image(url=str(r["image"]))
    embed.set_footer(text='LIGRA SELFBOT - bot developed by justLixra#0808 and butter#0001')
    await ctx.send(embed=embed)
    time.sleep(0.25)
    print(f'[OUTPUT] Answer in: {Fore.LIGHTMAGENTA_EX}#{ctx.channel}{Fore.MAGENTA}\n')

@LIGRA.command()
async def rdmtoken(ctx, user: discord.User = None):
    print(f"{Fore.MAGENTA}[{datetime.datetime.now()} UTC]\n[INPUT] {Fore.LIGHTMAGENTA_EX}{prefix}rdmtoken{Fore.MAGENTA} in: {Fore.LIGHTMAGENTA_EX}#{ctx.channel}{Fore.MAGENTA}")
    await ctx.message.delete()
    list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z", "_"'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o',
            'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    token = random.choices(list, k=59)
    if user is None:
        user = ctx.author
        await ctx.send(user.mention + " here you go: " + ''.join(token), delete_after=5)
    else:
        await ctx.send(user.mention + " here you go: " + "".join(token), delete_after=5)
    print(f'[OUTPUT] Answer in: {Fore.LIGHTMAGENTA_EX}#{ctx.channel}{Fore.MAGENTA}\n')

@LIGRA.command()
async def space(ctx):
    print(f"{Fore.MAGENTA}[{datetime.datetime.now()} UTC]\n[INPUT] {Fore.LIGHTMAGENTA_EX}{prefix}space{Fore.MAGENTA} in: {Fore.LIGHTMAGENTA_EX}#{ctx.channel}{Fore.MAGENTA}")
    await ctx.message.delete()
    await ctx.send("ﾠﾠ"+"\n" * 400 + "ﾠﾠ")
    time.sleep(0.25)
    print(f'[OUTPUT] Answer in: {Fore.LIGHTMAGENTA_EX}#{ctx.channel}{Fore.MAGENTA}\n')

@LIGRA.command()
async def nitro(ctx):
    print(f"{Fore.MAGENTA}[{datetime.datetime.now()} UTC]\n[INPUT] {Fore.LIGHTMAGENTA_EX}{prefix}nitro{Fore.MAGENTA} in: {Fore.LIGHTMAGENTA_EX}#{ctx.channel}{Fore.MAGENTA}")
    await ctx.message.delete()
    await ctx.send(Nitro())
    time.sleep(0.25)
    print(f'[OUTPUT] Answer in: {Fore.LIGHTMAGENTA_EX}#{ctx.channel}{Fore.MAGENTA}\n')

@LIGRA.command()
async def ip(ctx, host):
    print(f"{Fore.MAGENTA}[{datetime.datetime.now()} UTC]\n[INPUT] {Fore.LIGHTMAGENTA_EX}{prefix}ip{Fore.MAGENTA} in: {Fore.LIGHTMAGENTA_EX}#{ctx.channel}{Fore.MAGENTA}")
    await ctx.message.delete()
    start = datetime.datetime.now()
    r = requests.get(f"http://ip-api.com/json/{host}?fields=country,regionName,city,isp,mobile,proxy,query")
    geo = r.json()
    query = geo["query"]
    isp = geo["isp"]
    city = geo["city"]
    region = geo["regionName"]
    country = geo["country"]
    proxy = geo["proxy"]
    mobile = geo["mobile"]
    elapsed = datetime.datetime.now() - start
    elapsed = f"{elapsed.seconds}.{elapsed.microseconds}"
    embed = discord.Embed(description=f"**Host-IP:** {query}\n**ISP:** {isp}\n**City:** {city}\n**Region:** {region}\n**Country:** {country}\n**VPN/Proxy:** {proxy}\n**Mobile:** {mobile}", color=RandomColor())
    embed.set_author(name=f"IP-Tracker for {query}")
    embed.set_footer(text=f"[LIGRA] Selfbot | Version: {VERSION}")
    await ctx.send(embed=embed, delete_after=10)
    time.sleep(0.25)
    print(f'[OUTPUT] Answer in: {Fore.LIGHTMAGENTA_EX}#{ctx.channel}{Fore.MAGENTA}\n')

@LIGRA.command()
async def av(ctx, user: discord.Member = None):
    print(f"{Fore.MAGENTA}[{datetime.datetime.now()} UTC]\n[INPUT] {Fore.LIGHTMAGENTA_EX}{prefix}av{Fore.MAGENTA} in: {Fore.LIGHTMAGENTA_EX}#{ctx.channel}{Fore.MAGENTA}")
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    embed = discord.Embed(color=RandomColor())
    embed.set_author(name=str(user), icon_url=user.avatar_url)
    embed.set_image(url=user.avatar_url)
    embed.set_footer(text=f"[LIGRA] Selfbot | Version: {VERSION}")
    await ctx.send(embed=embed)
    print(f'[OUTPUT] Answer in: {Fore.LIGHTMAGENTA_EX}#{ctx.channel}{Fore.MAGENTA}\n')

@LIGRA.command()
async def streaming(ctx, *, message):
    print(f"{Fore.MAGENTA}[{datetime.datetime.now()} UTC]\n[INPUT] {Fore.LIGHTMAGENTA_EX}{prefix}stream{Fore.MAGENTA} in: {Fore.LIGHTMAGENTA_EX}#{ctx.channel}{Fore.MAGENTA}")
    await ctx.message.delete()
    stream = discord.Streaming(
        name=message,
        url="http://www.twitch.tv/jjustLixra"
    )
    await LIGRA.change_presence(activity=stream)
    time.sleep(0.25)
    print(f'[OUTPUT] Streamactivity changed to {Fore.LIGHTMAGENTA_EX}{message}{Fore.MAGENTA}\n')

@LIGRA.command()
async def playing(ctx, *, message):
    print(f"{Fore.MAGENTA}[{datetime.datetime.now()} UTC]\n[INPUT] {Fore.LIGHTMAGENTA_EX}{prefix}playing{Fore.MAGENTA} in: {Fore.LIGHTMAGENTA_EX}#{ctx.channel}{Fore.MAGENTA}")
    await ctx.message.delete()
    game = discord.Game(
        name=message
    )
    await LIGRA.change_presence(activity=game)
    time.sleep(0.25)
    print(f'[OUTPUT] Playingactivity changed to {Fore.LIGHTMAGENTA_EX}{message}{Fore.MAGENTA}\n')

@LIGRA.command()
async def listening(ctx, *, message):
    print(f"{Fore.MAGENTA}[{datetime.datetime.now()} UTC]\n[INPUT] {Fore.LIGHTMAGENTA_EX}{prefix}listening{Fore.MAGENTA} in: {Fore.LIGHTMAGENTA_EX}#{ctx.channel}{Fore.MAGENTA}")
    await ctx.message.delete()
    await LIGRA.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name=message,
        ))
    time.sleep(0.25)
    print(f'[OUTPUT] Listeningactivity changed to {Fore.LIGHTMAGENTA_EX}{message}{Fore.MAGENTA}\n')

@LIGRA.command()
async def watching(ctx, *, message):
    print(f"{Fore.MAGENTA}[{datetime.datetime.now()} UTC]\n[INPUT] {Fore.LIGHTMAGENTA_EX}{prefix}watching{Fore.MAGENTA} in: {Fore.LIGHTMAGENTA_EX}#{ctx.channel}{Fore.MAGENTA}")
    await ctx.message.delete()
    await LIGRA.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=message
        ))
    time.sleep(0.25)
    print(f'[OUTPUT] Watchingactivity changed to {Fore.LIGHTMAGENTA_EX}{message}{Fore.MAGENTA}\n')

@LIGRA.command()
async def ping(ctx):
    print(f"{Fore.MAGENTA}[{datetime.datetime.now()} UTC]\n[INPUT] {Fore.LIGHTMAGENTA_EX}{prefix}ping{Fore.MAGENTA} in: {Fore.LIGHTMAGENTA_EX}#{ctx.channel}{Fore.MAGENTA}")
    await ctx.message.delete()
    embed = discord.Embed(color=RandomColor(), title='Pong:', description=f"{client.latency * 1000:.4f} ms")
    await ctx.send(embed=embed, delete_after=5)
    print(f'[OUTPUT] Answer in: {Fore.LIGHTMAGENTA_EX}#{ctx.channel}{Fore.MAGENTA}\n')

@LIGRA.command()
async def tokeninfo(ctx, _token):
    print(f"{Fore.MAGENTA}[{datetime.datetime.now()} UTC]\n[INPUT] {Fore.LIGHTMAGENTA_EX}{prefix}tokeninfo{Fore.MAGENTA} in: {Fore.LIGHTMAGENTA_EX}#{ctx.channel}{Fore.MAGENTA}")
    await ctx.message.delete()
    headers = {
        'Authorization': _token,
        'Content-Type': 'application/json'
    }
    try:
        res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
        res = res.json()
        user_id = res['id']
        phone = res['phone']
        locale = res['locale']
        avatar_id = res['avatar']
        creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
    except KeyError:
        print(f"{Fore.MAGENTA}[ERROR]: {Fore.MAGENTA}Unknown Token"+Fore.RESET)

    embed = discord.Embed(color=RandomColor(),
        description=f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreationdate: `{creation_date}`\nAvatar: [**Click me**](https://cdn.discordapp.com/avatars/{user_id}/{avatar_id})")
    fields = [
        {'name': 'Mobile', 'value': res['phone']},
        {'name': 'Flags', 'value': res['flags']},
        {'name': '2FA?', 'value': res['mfa_enabled']},
        {'name': 'Verified?', 'value': res['verified']},

    ]
    print(f'[OUTPUT] Answer in: {Fore.LIGHTMAGENTA_EX}#{ctx.channel}{Fore.MAGENTA}\n')
    for field in fields:
        if field['value']:
            embed.add_field(name=field['name'], value=field['value'], inline=False)
            embed.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
            embed.set_footer(text=f"[LIGRA] Selfbot | Version: {VERSION}")
    return await ctx.send(embed=embed)

@LIGRA.command()
async def croles(ctx, amount, text):
    print(f"{Fore.MAGENTA}[{datetime.datetime.now()} UTC]\n[INPUT] {Fore.LIGHTMAGENTA_EX}{prefix}croles{Fore.MAGENTA} in: {Fore.LIGHTMAGENTA_EX}#{ctx.channel}{Fore.MAGENTA} on: {Fore.LIGHTMAGENTA_EX}{ctx.guild}{Fore.MAGENTA}")
    await ctx.message.delete()
    for _i in range(int(amount)):
        try:
            await ctx.guild.create_role(name=text, color=RandomColor())
            print(f'{Fore.LIGHTMAGENTA_EX}[STATUS] Role created...')
        except:
            print(f'[OUTPUT] You dont have enough permissions...\n')
            return
    time.sleep(0.25)
    print(f'{Fore.MAGENTA}[OUTPUT] {amount} roles created\n')

@LIGRA.command()
async def cchannel(ctx, amount, text):
    print(f"{Fore.MAGENTA}[{datetime.datetime.now()} UTC]\n[INPUT] {Fore.LIGHTMAGENTA_EX}{prefix}cchannel{Fore.MAGENTA} in: {Fore.LIGHTMAGENTA_EX}#{ctx.channel}{Fore.MAGENTA} on: {Fore.LIGHTMAGENTA_EX}{ctx.guild}{Fore.MAGENTA}")
    await ctx.message.delete()
    for _i in range(int(amount)):
        try:
            await ctx.guild.create_text_channel(name=text)
            print(f'{Fore.LIGHTMAGENTA_EX}[STATUS] Channel created...')
        except:
            print(f'[OUTPUT] You dont have enough permissions...\n')
            return
    time.sleep(0.25)
    print(f'''{Fore.MAGENTA}[OUTPUT] {amount} channel created\n''')

@LIGRA.command()
async def serverav(ctx):
    print(f"{Fore.MAGENTA}[{datetime.datetime.now()} UTC]\n[INPUT] {Fore.LIGHTMAGENTA_EX}{prefix}serverav{Fore.MAGENTA} in: {Fore.LIGHTMAGENTA_EX}#{ctx.channel}{Fore.MAGENTA}")
    await ctx.message.delete()
    embed = discord.Embed(title=f"_server av for **{ctx.guild}**_", colour=RandomColor())
    embed.set_image(url=ctx.guild.icon_url)
    embed.set_footer(text=f"[LIGRA] Selfbot | Version: {VERSION}")
    await ctx.send(embed=embed)
    print(f'[OUTPUT] Answer in: {Fore.LIGHTMAGENTA_EX}#{ctx.channel}{Fore.MAGENTA}\n')

@LIGRA.command()
async def serverinfo(ctx):
    print(f"{Fore.MAGENTA}[{datetime.datetime.now()} UTC]\n[INPUT] {Fore.LIGHTMAGENTA_EX}{prefix}serverinfo{Fore.MAGENTA} in: {Fore.LIGHTMAGENTA_EX}#{ctx.channel}{Fore.MAGENTA}")
    await ctx.message.delete()
    embed = discord.Embed(title=f"_server informations for **{ctx.guild}**_", timestamp=ctx.message.created_at, colour=RandomColor())

    embed.set_thumbnail(url=ctx.guild.icon_url)

    embed.add_field(name="ID:", value=ctx.guild.id)
    embed.add_field(name="owner:", value=ctx.guild.owner)
    embed.add_field(name="region:", value=ctx.guild.region)
    embed.add_field(name="member:", value=len(ctx.guild.members))
    embed.add_field(name="bots:", value=len(list(filter(lambda m: m.bot, ctx.guild.members))))
    embed.add_field(name="banned:", value=len(await ctx.guild.bans()),)
    embed.add_field(name="text_channels:", value=len(ctx.guild.text_channels))
    embed.add_field(name="voice_channels:", value=len(ctx.guild.voice_channels))
    embed.add_field(name="categories:", value=len(ctx.guild.categories))
    embed.add_field(name="roles:", value=len(ctx.guild.roles))
    embed.add_field(name="invites", value=len(await ctx.guild.invites()))
    embed.set_footer(text=f"[LIGRA] Selfbot | Version: {VERSION}")
    embed.set_author(name = f"[LIGRA] Selfbot | Version: {VERSION}", icon_url = client.user.avatar_url, url = "https://github.com/distayOFF/LIGRA")
    await ctx.send(embed=embed)
    time.sleep(0.25)
    print(f'[OUTPUT] Answer in: {Fore.LIGHTMAGENTA_EX}#{ctx.channel}{Fore.MAGENTA}\n')

@LIGRA.command()
async def copy(ctx):
    print(f"{Fore.MAGENTA}[{datetime.datetime.now()} UTC]\n[INPUT] {Fore.LIGHTMAGENTA_EX}{prefix}copy{Fore.MAGENTA} in: {Fore.LIGHTMAGENTA_EX}#{ctx.channel}{Fore.MAGENTA}")
    await ctx.message.delete()
    await LIGRA.create_guild(f"{ctx.guild.name} copy")
    await asyncio.sleep(4)
    for g in LIGRA.guilds:
        if f"{ctx.guild.name} copy" in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")
            for role in ctx.guild.roles:
                name = role.name
                farbe = role.colour
                rechte = role.permissions
                await g.create_role(name=name, permissions=rechte, colour=farbe)
            print(f'[OUTPUT] Servercopy created{Fore.MAGENTA}\n')

@LIGRA.command()
async def saveav(ctx, user: discord.Member):
    print(f"{Fore.MAGENTA}[{datetime.datetime.now()} UTC]\n[INPUT] {Fore.LIGHTMAGENTA_EX}{prefix}saveav{Fore.MAGENTA} in: {Fore.LIGHTMAGENTA_EX}#{ctx.channel}{Fore.MAGENTA}")
    await ctx.message.delete()
    with open(f"saved/{user}.png", "wb") as f:
        r = requests.get(user.avatar_url, stream=True)
        for block in r.iter_content(1024):
            if not block:
                break
            f.write(block)
    print(f'''[OUTPUT] {Fore.LIGHTMAGENTA_EX}{user}{Fore.MAGENTA}'s av is saved in {Fore.LIGHTMAGENTA_EX}saved{Fore.MAGENTA}\n''')

@LIGRA.command()
async def restart(ctx):
    print(f"{Fore.MAGENTA}[{datetime.datetime.now()} UTC]\n[INPUT] {Fore.LIGHTMAGENTA_EX}{prefix}restart{Fore.MAGENTA} in: {Fore.LIGHTMAGENTA_EX}#{ctx.channel}{Fore.MAGENTA}")
    await ctx.message.delete()
    print(f'''[OUTPUT] LIGRA is now restarting!\n''')
    time.sleep(2)
    execv(sys.executable, ["Discord main.py"] + sys.argv)

@LIGRA.command()
async def systeminfo(ctx):
    print(f"{Fore.MAGENTA}[{datetime.datetime.now()} UTC]\n[INPUT] {Fore.LIGHTMAGENTA_EX}{prefix}systeminfo{Fore.MAGENTA} in: {Fore.LIGHTMAGENTA_EX}#{ctx.channel}{Fore.MAGENTA}")
    start = time.perf_counter()
    message = await ctx.send("Ping...")
    end = time.perf_counter()
    duration = (end - start) * 1000
    await ctx.message.delete()
    await message.delete()
    cpuavg = psutil.cpu_percent(interval=None)
    mem = psutil.virtual_memory()[2]
    durround = round(duration, 3)
    embed = discord.Embed(
        title="System informationen", description="", color=discord.Colour.magenta()
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/702968498846171219/838335352019353620/baseline_info_black_24dp.png")
    embed.add_field(name="CPU", value=f"{cpuavg}%", inline=True)
    embed.add_field(name="Ram", value=f"{mem}%", inline=True)
    embed.add_field(name="Ping", value=f"{durround}ms", inline=True)
    embed.add_field(name="OS", value=f"{sys.platform}", inline=True)
    embed.set_footer(text=f"[LIGRA] Selfbot | Version: {VERSION}")
    await ctx.send(embed=embed)
    print(f'[OUTPUT] Answer in: {Fore.LIGHTMAGENTA_EX}#{ctx.channel}{Fore.MAGENTA}\n')

@LIGRA.command()
async def cc(ctx):
    print(f"{Fore.MAGENTA}[{datetime.datetime.now()} UTC]\n[INPUT] {Fore.LIGHTMAGENTA_EX}{prefix}cc{Fore.MAGENTA} in: {Fore.LIGHTMAGENTA_EX}#{ctx.channel}{Fore.MAGENTA}")
    await ctx.message.delete()
    await ctx.send("<ms-cxh-full://0>")
    print(f'[OUTPUT] Answer in: {Fore.LIGHTMAGENTA_EX}#{ctx.channel}{Fore.MAGENTA}\n')

@LIGRA.command()
async def reaction(ctx, messageNo: typing.Optional[int] = 1, *, text):
    print(f"{Fore.MAGENTA}[{datetime.datetime.now()} UTC]\n[INPUT] {Fore.LIGHTMAGENTA_EX}{prefix}reaction{Fore.MAGENTA} in: {Fore.LIGHTMAGENTA_EX}#{ctx.channel}{Fore.MAGENTA}")
    await ctx.message.delete()
    text = (c for c in text.lower())
    emotes = {
        "a": "🇦",
        "b": "🇧",
        "c": "🇨",
        "d": "🇩",
        "e": "🇪",
        "f": "🇫",
        "g": "🇬",
        "h": "🇭",
        "i": "🇮",
        "j": "🇯",
        "k": "🇰",
        "l": "🇱",
        "m": "🇲",
        "n": "🇳",
        "o": "🇴",
        "p": "🇵",
        "q": "🇶",
        "r": "🇷",
        "s": "🇸",
        "t": "🇹",
        "u": "🇺",
        "v": "🇻",
        "w": "🇼",
        "x": "🇽",
        "y": "🇾",
        "z": "🇿",
    }
    for i, m in enumerate(await ctx.channel.history(limit=100).flatten()):
        if messageNo == i:
            for c in text:
                await m.add_reaction(f"{emotes[c]}")
            break
    print(f'[OUTPUT] Answer in: {Fore.LIGHTMAGENTA_EX}#{ctx.channel}{Fore.MAGENTA}\n')

@LIGRA.command()
async def help(ctx):
  print(f"{Fore.MAGENTA}[{datetime.datetime.now()} UTC]\n[INPUT] {Fore.LIGHTMAGENTA_EX}{prefix}help{Fore.MAGENTA} in: {Fore.LIGHTMAGENTA_EX}#{ctx.channel}{Fore.MAGENTA}")
  await ctx.message.delete()
  embed = discord.Embed(
    color = discord.Colour.magenta(),
    timestamp=ctx.message.created_at,
    description = f"""
**__Chat Commands__**
```
{prefix}help
Shows this message

{prefix}myinfo
Shows amount of your friends and servers

{prefix}runtime
Shows runtime

{prefix}stream [title]
Set your status to streaming

{prefix}playing [title]
Set your status to playing

{prefix}listening [title]
Set your status to listening

{prefix}watching [title]
Set your status to watching

{prefix}ip [ip]
Shows the location, ISP, etc. of the IP

{prefix}tokeninfo [token]
Displays the information from the account

{prefix}rdmtoken
Creates a random token

{prefix}copy
Copy the whole server you are on

{prefix}saveav [user]
Saves the avatar of the user

{prefix}av
Shows the avatar of you / others

{prefix}ac [text]

{prefix}meme
Gives you a random meme

{prefix}ping
Shows you your ping

{prefix}space
Sends an empty text

{prefix}restart
Restarts the programm

{prefix}systeminfo
Shows your current systeminfo's

{prefix}cc
Sends crashcode (blackscreen)

{prefix}reaction [message]
Reacts to the last message
send (currently testing)

```
**__Spam Commands__**
```
{prefix}cchannel [amount] [name]
Creates a amount of channel

{prefix}croles [amount] [name]
Creates a amount of roles

```
**__Other__**
```
In case of errors etc please add
and contact distayOFF#2979

```
    """)
  embed.set_author(name = f"[LIGRA] Selfbot | Version: {VERSION}", icon_url = client.user.avatar_url, url = "https://github.com/distayOFF/LIGRA")
  embed.set_footer(text=f'[LIGRA] Selfbot | Version: {VERSION} | github.com/distayOFF/LIGRA')
  await ctx.send(embed=embed, delete_after=30)
  print(f'[OUTPUT] Answer in: {Fore.LIGHTMAGENTA_EX}#{ctx.channel}{Fore.MAGENTA}\n')

def startSelfbot():
    LIGRA.run(TOKEN, bot=False, reconnect=True)
