import discord
from discord.ext import commands
from core.classes import Cog_Extension

class  React(Cog_Extension):
    @commands.command()
    async def fuck(self,ctx):
        await ctx.send('好色喔')

def setup(bot):
    bot.add_cog (React(bot))