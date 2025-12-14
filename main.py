import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

bot.run("MTQ0OTU4NjEzNzA2Nzk1MDE0MQ.GGqVQ8.d-BdOAbd08MiQ8Bq_OuGTu5g-HZXN1A3usPse8")
