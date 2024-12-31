# Import resources from discord
from discord_components import ComponentsBot

# Creat bot object
bot = ComponentsBot()

with open("token.txt","r") as file:
    token = file.readlines()[0]
bot.run(token)