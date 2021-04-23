import discord

client = discord.Client()

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('hello'):
    await message.channel.send('Hello, I am a bot')

client.run('token')