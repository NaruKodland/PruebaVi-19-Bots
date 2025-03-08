import discord
from discord.ext import commands
import random
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')
@bot.command()
async def add(ctx, left: float, right: float, op: str ):
    if op == "/" and right == 0:
        await ctx.send("No puede dividir por cero")
        return
    if op == "+":
        await ctx.send(f"La suma de : {left} + {right} es: {left+right}")
    elif op == "-":
        await ctx.send(f"La resta de : {left} + {right} es: {left-right}")
    elif op == "*":
        await ctx.send(f"La multiplicación de : {left} + {right} es: {left*right}")
    elif op == "/":
        await ctx.send(f"La división de : {left} + {right} es: {left/right}")
    
    

bot.run("")
