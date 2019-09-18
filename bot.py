# bot.py
import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix = '$')

##ready
@client.event
async def on_ready():
    print('Bot is ready')
    
#ping
@client.command()
async def ping(ctx):
    await ctx.send(f'pong! {client.latency}')
    
#load/unload
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    
@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    
#load all cogs
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
    
client.run('AjIxNzg2NzU5MTg4OTcxNTIw.XYKOWw.GMR3vYkNhPOVawsrom8CZ0z_kbM')
