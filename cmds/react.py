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
    async def pic(self, ctx):
        await ctx.send(jdata['worship'])
        
#    @commands.command()
#    async def pop(self, ctx, x:int, y:int):
#        self.pop = []
#        self.a = self.x
#        for self.i in range(1, y+1):
#            for self.j in range(1, x+1):
#                self.pop = '||pop||'
#                if self.a == x:
#                    self.pop = ctx.send('\n')
#        await ctx.send(self.pop)
     
    @commands.command()
    async def pop(self, ctx, x:int, y:int):
        for self.i in range(0, y):
            await ctx.send('||pop||'*x)            



            

        
def setup(bot):
    bot.add_cog (React(bot))
