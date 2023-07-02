import discord
from multiprocessing.pool import ApplyResult
from discord.ext import commands
import os
from core.classes import Cog_Extension



class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_message(self,msg):
        keyword =['hi', 'yo', '你好']
        if msg.content in keyword and msg.author != self.bot.user:
            await msg.channel.send('ap')
            
class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_message(self,msg):
        keyword = ['sin2θ']
        if msg.content in keyword and msg.author != self.bot.user:
             await msg.channel.send('兩倍賽扣')


def setup(bot):
    bot.add_cog(Event(bot))