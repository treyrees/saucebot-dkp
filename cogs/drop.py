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
            await asyncio.sleep(30)
            
    embed  = discord.Embed()
    countdown = 0
    highest_bids = []
    split_drops = []
            
    #begin event
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def drop(self, ctx, drops:str):
        global embed
        global countdown
        global highest_bids
        global split_drops
        countdown = 30
        highest_bids = []
        split_drops = []
        
        #highest initialization
        split_drops = drops[1:-1].split('][')
        for x in range(len(split_drops)):
            highest_bids.append(0)
    
        #embed creation
        embed=discord.Embed(
            color = discord.Color.green(),
            title = '\u200b'
        )
        embed.set_author(name='Time Remaining: '+str(countdown), icon_url='https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/160/facebook/105/clock-face-nine-oclock_1f558.png')
        embed.set_footer(text='$bid id dkp', icon_url='http://i.imgur.com/IPEOEew.png')
        for x in range(len(split_drops)):
            embed.add_field(name=str(x+1)+') '+split_drops[x], value='\u200b', inline=True)
            embed.add_field(name=highest_bids[x], value='\u200b', inline=True)
            if(x != len(split_drops)):
                embed.add_field(name='\u200b', value='\u200b', inline=True)
        message = await ctx.send(embed=embed)
        
        #increment countdown
        while countdown > 0:
            countdown -= 1
            embed.set_author(name='Time Remaining: '+str(countdown), icon_url='https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/160/facebook/105/clock-face-nine-oclock_1f558.png')
            await message.edit(embed=embed)
            await asyncio.sleep(1)
            
        #finish countdown
        embed.color = discord.Color.red()
        embed.set_author(name='Time\'s up!', icon_url='https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/160/facebook/105/clock-face-nine-oclock_1f558.png')
        await message.edit(embed=embed)
        grats = ''
        for x in range(len(split_drops)):
            grats += split_drops[x]+' goes to '+embed.fields[3*x+2].name+' for '+str(embed.fields[3*x+1].name)+' DKP'
            if x != len(split_drops):
                grats += '\n'
        await ctx.send(grats)
        
    @commands.command()
    async def bid(self, ctx, item_id:int, dkp:int):
        global embed
        global countdown
        global highest_bids
        global split_drops
        player = self.players.find_player(ctx.author.id)
        
        if(player.dkp < dkp):
            await ctx.send(player.id+', you do not have enough DKP for that bid.')
        elif (dkp > highest_bids[item_id-1]):
            highest_bids[item_id - 1] = dkp
            embed.set_field_at((3*item_id-2), name=str(highest_bids[item_id-1]), value='\u200b', inline=True)
            embed.set_field_at((3*item_id-1), name=ctx.author.display_name, value='\u200b', inline=True)
        elif (dkp == highest_bids[item_id-1]):
            embed.set_field_at((3*item_id-1), name=(embed.fields[3*item_id-1].name)+', '+ctx.author.display_name, value='\u200b', inline=True)
        
def setup(bot):
    bot.add_cog(Drop(bot))
