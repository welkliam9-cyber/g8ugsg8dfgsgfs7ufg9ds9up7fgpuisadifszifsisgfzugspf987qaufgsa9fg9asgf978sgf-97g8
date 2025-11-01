import discord
from discord.ext import commands


TOKEN = "You BOT TOKEN"


bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"✅ Eingeloggt als {bot.user}")

@bot.command()
async def ping(ctx):
    """Antwortet mit Pong!"""
    await ctx.send("🏓 Pong!")

@bot.command()
async def hallo(ctx):
    """Begrüßt den Nutzer."""
    await ctx.send(f"Hallo {ctx.author.name}! 👋")

@bot.command()
async def info(ctx):
    """Gibt einfache Bot-Infos aus."""
    await ctx.send("Ich bin ein einfacher Bot, geschrieben in Python 🐍")

bot.run(TOKEN)
