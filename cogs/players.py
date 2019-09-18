import discord
from discord.ext import commands
from player import Player

class Players(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def add_player(self,id,wow_name,dkp=0):
        new_player = Player(id,wow_name,dkp)
        self.players.append(new_player)
        print('new player added {wow_name}')
        return self
        
def setup(client):
    client.add_cog(Players(client))