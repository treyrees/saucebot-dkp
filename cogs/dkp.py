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
            print('Dkp updating players')
            self.players.players = self.players.load_players()
            await asyncio.sleep(300)
        
    #give, set, take, kill
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def give(self, ctx, player:str, amount:int):
        recipient = self.players.find_player(player)
        recipient.dkp += amount
        self.players.save_players()
        await ctx.send('<@'+str(ctx.author.id)+'> gave '+recipient.id+' '+str(amount)+' DKP')
        
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def set(self, ctx, player:str, amount:int):
        recipient = self.players.find_player(player)
        recipient.dkp = amount
        self.players.save_players()
        await ctx.send('<@'+str(ctx.author.id)+'> set '+recipient.id+'\'s DKP to '+str(amount))
        
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def take(self, ctx, player:str, amount:int):
        recipient = self.players.find_player(player)
        recipient.dkp = amount
        self.players.save_players()
        await ctx.send('<@'+str(ctx.author.id)+'> took '+recipient.id+' '+str(amount)+' DKP')
        
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def kill(self, ctx, amount:int):
        leader_channel = ctx.message.author.voice.channel
        for player in leader_channel.members:
            user = self.players.find_player(player.id)
            user.dkp += amount
        await ctx.send('<@'+str(ctx.author.id)+'> gave everyone in '+str(leader_channel)+' '+str(amount)+' DKP')
        self.players.save_players()
        
    #prekill
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def prekill(self, ctx):
        leader_channel = ctx.message.author.voice.channel
        unadded = []
        unadded_message = ('')
        for player in leader_channel.members:
            found_player = self.players.find_player(player.id)
            if (found_player == False):
                unadded.append(player.id)
        for id in unadded:
            unadded_message = unadded_message+'<@'+str(id)+'> '
        await ctx.send(unadded_message+'You\'re not in the database! Please go to <#623720839296188445> and type `$new`.')
        
    #new player
    @commands.command()
    async def new(self, ctx):
        new_id = '<@'+str(ctx.author.id)+'>'
        new_name = str(ctx.author)
        new_nick = str(ctx.author.display_name)
        new_channel = str(ctx.author.voice.channel)
        
        saving = True
        
        if not self.players.players:
            print('char created from empty list')
            self.players.add_player(new_id,new_name,new_nick,new_channel)
            await ctx.send('<@'+str(ctx.author.id)+'> Thank you! Character created.')
        
        for player in self.players.players:
            if player.id == new_id:
                await ctx.send('<@'+str(ctx.author.id)+'> You\'re not new! Character exists.')
                saving = False
                
        if saving:
            self.players.add_player(new_id,new_name,new_nick,new_channel)
            await ctx.send('<@'+str(ctx.author.id)+'> Thank you! Character created.')
            
    #roster, balance
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def roster(self, ctx):
        embed = discord.Embed(
            title = 'Roster',
            color = discord.Color.from_rgb(13, 82, 92),
        )
        
        for player in self.players.players:
            embed.add_field(name=str(player.nick), value=str(player.dkp)+' DKP', inline=False)
        
        await ctx.send(embed = embed)
            
    @commands.command()
    async def bal(self, ctx):
        player = self.players.find_player(ctx.author.id)
        if player is not False:
            await ctx.send('<@'+str(ctx.author.id)+'> has '+str(player.dkp)+' DKP.')
        else:
            print('Error finding player')
        
def setup(bot):
    bot.add_cog(Dkp(bot))