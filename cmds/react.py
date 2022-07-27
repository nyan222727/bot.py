import discord
from discord.ext import commands
from core.classes import Cog_Extension

class  React(Cog_Extension):
    @commands.command()
    async def hi(ctx):
        await ctx.send('ABCD')

def setup(bot):
    bot.add_cog (React(bot))