import discord
from discord.ext import commands, tasks
import datetime
import datetime
import pytz
IST = pytz.timezone("Asia/Kolkata")
import os

TOKEN = os.getenv("TOKEN")

GUILD_ID = 1418109436928458775
CATEGORY_ID = 1442032064244486204

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

vc = None

@tasks.loop(minutes=1)
async def check_time():
    global vc

    print("GUILD_ID:", GUILD_ID)

    guild = discord.utils.get(bot.guilds, id=GUILD_ID)
    category = None

    if guild:
        category = guild.get_channel(CATEGORY_ID)

    print("Guild:", guild)
    print("Category:", category)

    if guild and vc is None:
        vc = await guild.create_voice_channel("TEST VC")
        print("VC Created")
    now = datetime.datetime.now(IST).strftime("%H:%M")
    print("Current time:", now)
    guild = bot.get_guild(GUILD_ID)
    if not guild:
        return
        
    category = guild.get_channel(CATEGORY_ID)

    if now == "2356" and vc is None:
        vc = await guild.create_voice_channel("Scheduled VC")
        print("VC Created")

    if now == "0010" and vc is not None:
        await vc.delete()
        vc = None
        print("VC Deleted")
        

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    if not check_time.is_running():
        check_time.start()

bot.run(TOKEN)
