#example.py
import discord
from discord.ext import commands

class Example(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    #event
    @commands.Cog.listener()
    async def on_ready(self):
        print('Cog is online')
        
    #command
    @commands.command()
    async def pingtwo(self, ctx):
        await ctx.send('pong')
        
def setup(client):
    client.add_cog(Example(client))