import os
import discord
from discord.ext import commands
from players import Players
import asyncio

class Dkp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.players = Players('players.dat')
        bot.loop.create_task(self.auto_load())
        
    async def auto_load(self):
        await self.bot.wait_until_ready()
        while True:
            print('Updating players')
            self.players.players = self.players.load_players()
            await asyncio.sleep(300)
        
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def givedkp(self, ctx, player:str, amount:int):
        print(str(player))
        recipient = self.players.find_player(player)
        recipient.dkp += amount
        ##self.players.save_players()
        await ctx.send('<@'+str(ctx.author.id)+'> gave '+recipient.id+' '+str(amount)+' DKP')
        
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def setdkp(self, ctx, player:str, amount:int):
        print(str(player))
        recipient = self.players.find_player(player)
        recipient.dkp = amount
        ##self.players.save_players()
        await ctx.send('<@'+str(ctx.author.id)+'> set '+recipient.id+'\'s DKP to '+str(amount))
        
    @commands.command()
    async def new(self, ctx):
        new_id = '<@'+str(ctx.author.id)+'>'
        new_name = str(ctx.author)
        
        saving = True
        
        if not self.players.players:
            self.players.add_player(new_id,new_name)
            await ctx.send('<@'+str(ctx.author.id)+'> Thank you! Character created.')
        
        for player in self.players.players:
            if player.id == new_id:
                await ctx.send('<@'+str(ctx.author.id)+'> You\'re not new! Character exists.')
                saving = False
                
        if saving:
            self.players.add_player(new_id,new_name)
            await ctx.send('<@'+str(ctx.author.id)+'> Thank you! Character created.')
            
    @commands.command()
    async def list(self, ctx):
        list.players(self)
        
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def logout(self, ctx):
        await bot.logout()
        
def setup(bot):
    bot.add_cog(Dkp(bot))