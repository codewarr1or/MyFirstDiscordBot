from discord.ext import commands

# Import the bot instance from bot.py
from bot import bot

# Define your commands here

@bot.command(name="hello")
async def hello(ctx):
    await ctx.send("Hello, I'm your bot!")

# Add more commands here
