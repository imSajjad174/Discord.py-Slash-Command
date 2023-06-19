import discord
from discord.ext import commands
from discord_slash import SlashCommand
from dotenv import load_dotenv
import os
import asyncio

# Load environment variables from .env file
load_dotenv()

# Retrieve the bot token from environment variables
TOKEN = os.getenv('BOT_TOKEN')

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)
slash = SlashCommand(bot, sync_commands=True)

@bot.event
async def on_ready():
    print(f'Bot is connected to {bot.user.name}')
    print('Ready to accept commands and slash commands!')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@slash.slash(
    name="ping",
    description="Ping the bot"
)
async def ping_slash(ctx):
    await ctx.send('Pong!')

async def main():
    await bot.start(TOKEN)

loop = asyncio.get_event_loop()
loop.create_task(main())
loop.run_forever()
