# bot.py
import os

import discord
#from dotenv import load_dotenv

#load_dotenv()
#token = os.getenv('DISCORD_TOKEN')

class CustomClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')
        
    async def on_member_update(before, after):
        if len(before.roles) < len(after.roles):
            new_role = next(role for role in after.roles if role not in before.roles)
            if new_role.name in ('member'):
                await client.send_message(after, "gratz")

client = CustomClient()
client.run('NjIxNzg2NzU5MTg4OTcxNTIw.XYFJEg.AdCmCMvcKpkZkWKFj0qJYUUC-ko')