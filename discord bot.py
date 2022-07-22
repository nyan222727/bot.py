import discord
from discord.ext import commands

bot = commands.Bot( command_prefix = '[' )

@bot.event
async def on_ready():
    print (">>bot is online<<")
bot.run ("OTk3MzE1NDA0MzM2NzI2MDY3.Gs51pt.w3PC_cItXHmCU5VdLbkRTs-9Sfuz6xUpvPm82g")
