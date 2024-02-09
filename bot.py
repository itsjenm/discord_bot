from dotenv import load_dotenv
import os
import discord
from discord.ext import commands
import random
import asyncio
import requests


load_dotenv()
TOKEN = os.environ.get('DISCORD_BOT_TOKEN')

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

hello_gifs = ['https://media1.tenor.com/m/OGJ56xrXzHwAAAAd/oliverbrown-hello.gif', 'https://media1.tenor.com/m/wLcMip4f4BYAAAAC/hello-kenneth.gif', 'https://media1.tenor.com/m/Fv7KKXpEe9MAAAAd/hello-chat-gojo.gif']
hello_names = ["hola","hello","hi","hey","yo","wassup","sup", "h3llo"]
greetings = ['hello', 'hi', 'hey', 'hola', 'bonjour', 'guten tag', "what's up", "yo", "wassup", "ayy", "sup", "h3llo"]


# needs to run asynchronously to handle multiple requests
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord! {bot.user.id}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

    await bot.process_commands(message)

@bot.event
async def on_member_join(member):
    await member.send(f'Hi {member.name}, welcome to the iCAN server!')
    channel = member.guild.system_channel
    if channel:
        await channel.send(f'Welcome {member.mention}!')

    embed = discord.Embed(title="Gifs", description=f"{member.author.mention} {(random.choice(hello_names))}", color=(discord.Color.random()))
    embed.set_image(url=(random.choice(hello_gifs)))

    await member.send(embed=embed)

@bot.command()
async def hello(ctx):
    embed = discord.Embed(title="Gifs", description=f"{ctx.author.mention} {(random.choice(hello_names))}", color=(discord.Color.random()))
    embed.set_image(url=(random.choice(hello_gifs)))

    await ctx.send(embed=embed)

@bot.command()
async def reminder(ctx, time, time_unit, *, reminder):
    time_units = {'s': 1, 'm': 60, 'hr': 3600, 'd': 86400}
    time_in_seconds = int(time) * time_units[time_unit]
    await ctx.send(f"{ctx.author.mention} I will remind you in {time} {time_unit}.")
    await asyncio.sleep(time_in_seconds)
    await ctx.send(f"{ctx.author.mention} {reminder}")
    
    

@bot.listen("on_message")
async def on_message(message):
    if message.author == bot.user:
        return

    for greeting in greetings:
        if message.content.lower().startswith(greeting):
            await message.add_reaction("👋")
            await message.channel.send("hey there!")
            break
    



bot.run(TOKEN)