import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
with open ( 'setting.json', 'r', encoding  = 'utf8' ) as jfile:
    jdata = json.load(jfile)

class React(Cog_Extension):
    @commands.command()
    async def abc(self,ctx):
        await ctx.send('123')

    @commands.command()
    async def 圖片(self, ctx):
        await ctx.send(jdata['worship'])
def setup(bot):
    bot.add_cog (React(bot))