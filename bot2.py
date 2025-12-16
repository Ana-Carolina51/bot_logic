import discord
from discord.ext import commands
import random
# Importar pass_gen do bot_logic.py  
from bot_logic import pass_gen

# A variável intents armazena as permissões do bot
intents = discord.Intents.default()
# Ativar a permissão para ler o conteúdo das mensagens
intents.message_content = True
# Criar um bot e passar as permissões
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Fizemos login como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")

@bot.command()
async def senha(ctx):
    await ctx.send("Sua senha é: " + pass_gen(10))

@bot.command()
async def caraoucoroa(ctx):
    random1 = random.randint(1,2)
    if random1 == 1:
        await ctx.send("A moeda saiu cara!")
    elif random1 == 2:
        await ctx.send("A moeda saiu coroa!")

@bot.command()
async def bye(ctx):
    await ctx.send("\U0001f642")

@bot.command()
async def emoji(ctx):
    await ctx.send("🎮")

@bot.command()
async def gif(ctx):
    await ctx.send("https://tenor.com/view/marceline-bubbline-adventure-time-princess-bubblegum-best-friends-gif-14213958")

@bot.command()
async def users(ctx):
    quantidade = ctx.guild.member_count
    await ctx.send(f"Há {quantidade} usuários no servidor")

@bot.command()
async def id(ctx):
    user_id = ctx.author.id
    await ctx.send(f"Seu id é {user_id}")


bot.run('')
