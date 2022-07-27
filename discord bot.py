import discord
from discord.ext import commands
import json
import os
with open ( 'setting.json', 'r', encoding  = 'utf8' ) as jfile:
    jdata = json.load(jfile)

bot = commands.Bot( command_prefix = '[' )

@bot.event
async def on_ready():
    print (">>bot is online<<")

@bot.command()
async def load (ctx,extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send (f'Loaded {extension} done')
    
@bot.command()
async def unload (ctx,extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send (f'UN-Loaded {extension} done')

@bot.command()
async def reload (ctx,extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send (f'RE-Loaded {extension} done')

for Filename in os.listdir('./cmds'):
    if Filename.endswith ('.py'):
        bot.load_extension(F'cmds.{Filename[:-3]}')
    
if __name__ == "__main__":

    bot.run ( jdata[ 'TOKEN' ] )




    

