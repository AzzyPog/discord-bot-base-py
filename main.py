import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
load_dotenv()


token = os.getenv("DISCORD_TOKEN")
intents = discord.Intents(messages=True, message_content=True)
client = commands.Bot(command_prefix = '/', case_insensitive = True, intents=intents)

@client.event
async def on_ready():
    print('Olá, eu estou online!')


@client.command()
async def acende(ctx):
    
    i = 0
    fogos = ['pra', 'pra pra pra pra pra', 'pra pra pra', 'pra', 'pra', 'pra', 'POOOOOW :fireworks::fireworks:'] 
    while i < 7:
        
        await ctx.send(fogos[i])
        i += 1


client.run(token)
