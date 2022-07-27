from multiprocessing.pool import ApplyResult
import discord
from discord.ext import commands
import os
from core.classes import Cog_Extension

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_message(self,msg):
        if msg.content == 'apple':
            await msg.channel.send('ap')

def setup(bot):
    bot.add_cog(Event(bot))