import discord
from discord.ext import commands
import json, asyncio, datetime
from core.classes import Cog_Extension
with open ( 'setting.json', 'r', encoding  = 'utf8' ) as jfile:
    jdata = json.load(jfile)

class Task(Cog_Extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        async def interval():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(997312886588325961)
            while not self.bot.is_closed():
                await self.channel.send('UWU')
                await asyncio.sleep(5)
        
        self.bg_task = self.bot.loop.create_task(interval())
        
    @commands.command()
    async def set_channel(self, ctx, ch:int):
        self.channel = self.bot.get_channel(ch)
        await ctx.send (f'Set channel: {self.channel.mention}')


    
    

def setup(bot):
    bot.add_cog(Task(bot))
