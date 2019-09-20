import os
import discord
from discord.ext import commands
from players import Players
import asyncio

class Drop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.players = Players('players.dat')
        bot.loop.create_task(self.auto_load())
        
    async def auto_load(self):
        await self.bot.wait_until_ready()
        while True:
            print('Drop updating players')
            self.players.players = self.players.load_players()
            await asyncio.sleep(60)
            
    #begin event
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def drop(self, ctx, drops:str):
        split_drops = drops.split(',')
        embed=discord.Embed(
            title = 'Drop IDs',
            color = discord.Color.from_rgb(13, 82, 92),
            description = '$bid {id} {dkp}'
        )
        embed.add_field(name='1', value=split_drops[0], inline=True)
        embed.add_field(name='Time Remaining', value='xxx', inline=True)
        for x in range(len(split_drops) - 1):
            embed.add_field(name=str(x+2), value=split_drops[x+1], inline=False)
        await ctx.send(embed=embed)
        
def setup(bot):
    bot.add_cog(Drop(bot))