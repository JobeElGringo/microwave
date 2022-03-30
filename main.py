# bot.py
import os
import discord
from dotenv import load_dotenv
from discord import FFmpegPCMAudio

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
client = commands.Bot(command_prefix = '*')

@client.event
async def on_ready():
    print("yes")
    print("---")

@client.command(pass_context = true)
async def microwave(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('microwave.mp3')
        player = voice.play(source)
    else:
        await ctx.send('You are not in a channel!')

@client.command(pass_context = true)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
    else:
        await ctx.guild.voice_client.disconnect('I am not in a voice channel.')






client.run(OTU4NDY3MjM3MTY4MTg1MzQ2.YkNwLA.sK7d8rWU9RBStv9m62GwHwdK9yo)