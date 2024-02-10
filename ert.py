import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command(description='Çünkü skoru başka bir şekilde halletmek istediğinde')
async def banasecimyapbunlarla(ctx, *choices: str):
    await ctx.send(random.choice(choices))

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

bot.run("MTIwMzI3ODk4OTUyMzgyMDU1NA.GYVRKf.NHVxm9ajwkyydWV8rtA5ftDGKZtB8x2lwwRFY0")
