from dotenv import load_dotenv
import os
import discord
from discord.ext import commands
import requests


load_dotenv()
TOKEN = os.environ.get('DISCORD_BOT_TOKEN')

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

POKE_URL=""


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

@bot.command()
async def hello(ctx):
    await ctx.send('H3llo hack3r!')

@bot.listen("on_message")
async def on_message(message):
    if message.author == bot.user:
        return

    if "hello" in message.content.lower():
        await message.add_reaction("👋")


bot.run(TOKEN)