import discord
from discord.ext import commands
import json
with open ( 'setting.json', 'r', encoding  = 'utf8' ) as jfile:
    jdata = json.load(jfile)

client = discord.Client()

bot = commands.Bot( command_prefix = '[' )

@bot.event
async def on_ready():
    print (">>bot is online<<")
bot.run ( jdata[ 'TOKEN' ] )
