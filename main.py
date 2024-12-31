# Import resources from discord
import discord
from discord.ext import commands
from music_cog import music_cog

# Creat bot object
intents = discord.Intents.default() # Enable required intents
bot = commands.Bot(command_prefix='!',intents=intents)

# Add music cog
bot.add_cog(music_cog(bot))

# Run music bot
with open("token.txt","r") as file:
    token = file.readlines()[0]
bot.run(token)