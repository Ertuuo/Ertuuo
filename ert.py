import discord
from discord.ext import commands
import time

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')


@bot.command()
async def slm(ctx):
    await ctx.send(f'Selam {bot.user}! Ben bir çevreci botum!')


@bot.command()
async def ne_yaparsin (ctx):
    await ctx.send(f"Soru şiklari; bir, ne yapababilirim. iki, video önerisi. üç, çevre koruma önlemleri. Bu şıkları lütfen yazı ile yaz  ")


@bot.command()
async def bir (ctx):
    await ctx.send(f"Senin sorularını cevaplarım bu kadar :-D")

@bot.command()
async def iki (ctx):
    await ctx.send(f"Adım 1) Google Amca'ya (ve ya teyzeye) YouTube yaz.")
    time.sleep(1)
    await ctx.send(f"Adım 2) Çıkan ilk sekmeye tıkla.")
    time.sleep(1)
    await ctx.send(f"Adım 3) Orada çıkan arama sekmesine istediğin şeyi yaz ve işlem bitti. :-P ")

@bot.command()
async def üç (ctx):
    await ctx.send(f"Çöplerini ayrıştır bu tüm dünyaya yeter.")
    time.sleep(1)
    await ctx.send(f"Eğer maddi durumun varsa elektrikli araba al.(Mesela Togg.)")
    time.sleep(1)
    await ctx.send(f"Bunun gibi pek çok örnek olabilir.")

bot.run("MTIwODM1NTk4OTgxMjk0NDkxNw.Gal2rF.f0m5a5yVPTx1fNTfes26QCiePUzjZjhC0Mrmgc")
