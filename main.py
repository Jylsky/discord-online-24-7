import discord
import os
from keep_alive import keep_alive
from discord.ext import commands
import json
client = commands.Bot(command_prefix=':', self_bot=True, help_command=None)

@client.event
async def on_ready():
  activity = json.loads(os.getenv('DISCORDACTIVITY', '{}'))
  await client.change_presence(status=discord.Status[os.getenv('DISCORDSTATUS', 'online')], activity=discord.Activity(**activity))
  os.system('clear')
  print(f'Logged in as {client.user} (ID: {client.user.id})')

keep_alive()
client.run(os.getenv("TOKEN"), bot=False)