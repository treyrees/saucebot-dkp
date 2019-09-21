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
            await asyncio.sleep(300)
            
    #begin event
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def drop(self, ctx, drops:str):
        countdown = 10
    
        #embed creation
        split_drops = drops[1:-1].split('][')
        embed=discord.Embed(
            title = 'Bid now!',
            color = discord.Color.green(),
            description = 'Item IDs'
        )
        embed.add_field(name='1', value=split_drops[0], inline=True)
        embed.add_field(name='Time Remaining', value='~'+str(countdown), inline=True)
        embed.set_footer(text='Command: $bid itemId dkpValue', icon_url='http://i.imgur.com/IPEOEew.png')
        for x in range(len(split_drops) - 1):
            embed.add_field(name=str(x+2), value=split_drops[x+1], inline=False)
        message = await ctx.send(embed=embed)
        
        #increment countdown
        while countdown > 0:
            countdown -= 1
            embed.set_field_at(1, name='Time Remaining', value='~'+str(countdown), inline=True)
            await message.edit(embed=embed)
            await asyncio.sleep(1)
            
        #finish countdown
        embed.color = discord.Color.red()
        embed.title = 'Bidding closed!'
        await message.edit(embed=embed)
        await ctx.send('Bidding closed!', tts=True)
        
def setup(bot):
    bot.add_cog(Drop(bot))