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
            await asyncio.sleep(120)
        
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def givedkp(self, ctx, user:str, amount:int):
        print(str(player))
        recipient = self.players.find_player(player)
        recipient.dkp += amount
        self.players.save_players()
        await ctx.send('<@'+str(ctx.author.id)+'> gave '+recipient.id+' '+str(amount)+' DKP')
        
    @commands.command()
    async def new(self, ctx):
        player_id = '<@'+str(ctx.author.id)+'>'
        player_name = str(ctx.author)
        
        saving = True
        updating = False
        
        for player in self.players.players:
            if player.id == player_id:
                await ctx.send('<@'+str(ctx.author.id)+'> You\'ve already signed up for DKP')
                saving = False
                updating = True

        if saving:
            self.players.add_player(player_id, player_name)
            await ctx.send('<@'+str(ctx.author.id)+'> You\'ve successfully signed up for DKP')
        
def setup(bot):
    bot.add_cog(Dkp(bot))