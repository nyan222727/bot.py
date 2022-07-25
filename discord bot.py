import discord
from discord.ext import commands
import json
with open ( 'setting.json', 'r', encoding  = 'utf8' ) as jfile:
    jdata = json.load(jfile)

bot = commands.Bot( command_prefix = '[' )

@bot.event
async def on_ready():
    print (">>bot is online<<")
    
@bot.command()
async def ping ( ctx ):
    await ctx.send ( f'{round(bot.latency*1000)}(ms)' )


bot.run ( jdata[ 'TOKEN' ] )




    

