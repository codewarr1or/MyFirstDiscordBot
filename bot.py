import os  # Add this line to import the os module
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get your bot token from the environment variables
TOKEN = os.getenv("DISCORD_TOKEN")

# Create intents
intents = discord.Intents.default()
intents.typing = False
intents.presences = False

# Create a bot instance with intents
bot = commands.Bot(command_prefix="!", intents=intents)

# Load your commands extension
bot.load_extension("commands")  # Replace "commands" with the actual filename without the ".py" extension

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    await bot.load_extension("commands")  # Await the load_extension coroutine

bot.run(TOKEN)
