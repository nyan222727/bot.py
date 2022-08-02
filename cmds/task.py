import discord
from discord.ext import commands
import json, asyncio, datetime
from core.classes import Cog_Extension
with open ( 'setting.json', 'r', encoding  = 'utf8' ) as jfile:
    jdata = json.load(jfile)

class Task(Cog_Extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        async def intreval():
            await self.wait_until_ready()
    
    
def setup(bot):
    bot.add_cog(Task(bot))
