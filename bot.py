import discord
from discord.ext import commands, tasks
import datetime
import os

TOKEN = os.getenv(TOKEN)

GUILD_ID = 1418109436928458775
CATEGORY_ID = 1442032064244486204

intents = discord.Intents.default()
bot = commands.Bot(command_prefix=!, intents=intents)

vc = None

@tasks.loop(minutes=1)
async def check_time()
    global vc
    now = datetime.datetime.now().strftime(%H%M)

    guild = bot.get_guild(GUILD_ID)
    category = guild.get_channel(CATEGORY_ID)

    if now == 1800 and vc is None
        vc = await guild.create_voice_channel(Scheduled VC, category=category)
        print(VC Created)

    if now == 2000 and vc
        await vc.delete()
        vc = None
        print(VC Deleted)

@bot.event
async def on_ready()
    print(fLogged in as {bot.user})
    check_time.start()

bot.run(TOKEN)