import discord
from discord.ext import commands
import random
import os
import requests

# Importar pass_gen do bot_logic.py  
from geradorsenha import pass_gen

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

def get_poke_image_url():
    poke_id = random.randint(1, 151)  # Pokémon da 1ª geração
    url = f'https://pokeapi.co/api/v2/pokemon/{poke_id}'

    res = requests.get(url)
    data = res.json()

    # pega a imagem do Pokémon
    image_url = data['sprites']['front_default']
    nome = data['name'].capitalize()

    return nome, image_url


@bot.command('poke')
async def poke(ctx):
    nome, image_url = get_poke_image_url()
    await ctx.send(f"⚡ Pokémon sorteado: **{nome}**")
    await ctx.send(image_url)


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


@bot.command()
async def meme(ctx):
    arquivos = os.listdir("memes")
    meme = random.choice(arquivos)

    with open(f"memes/{meme}", "rb") as f:
        picture = discord.File(f)

    await ctx.send(file=picture)


@bot.command()
async def dado(ctx):
    numero = random.randint(1, 6)
    await ctx.send(f"🎲 O dado caiu em **{numero}**!")


@bot.command()
async def ppt(ctx, escolha: str = None):
    if escolha is None:
        await ctx.send("❌ Use: `$ppt pedra | papel | tesoura`")
        return

    escolha = escolha.lower()
    opcoes = ["pedra", "papel", "tesoura"]

    if escolha not in opcoes:
        await ctx.send("❌ Escolha inválida. Use: pedra, papel ou tesoura.")
        return

    bot_escolha = random.choice(opcoes)

    if escolha == bot_escolha:
        resultado = "🤝 Empate!"
    elif (
        (escolha == "pedra" and bot_escolha == "tesoura") or
        (escolha == "papel" and bot_escolha == "pedra") or
        (escolha == "tesoura" and bot_escolha == "papel")
    ):
        resultado = "🎉 Você ganhou!"
    else:
        resultado = "❌ Você perdeu!"

    await ctx.send(
        f"🧠 Você escolheu **{escolha}**\n"
        f"🤖 Bot escolheu **{bot_escolha}**\n\n"
        f"{resultado}"
    )


@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, quantidade: int):
    if quantidade <= 0:
        await ctx.send("❌ Use um número maior que 0.")
        return

    # +1 para apagar a mensagem do comando também
    apagadas = await ctx.channel.purge(limit=quantidade + 1)

    msg = await ctx.send(f"🧹 {len(apagadas) - 1} mensagens apagadas com sucesso!")
    # Apaga a mensagem de confirmação depois de 5 segundos
    await msg.delete(delay=5)

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("❌ Você não tem permissão para usar esse comando.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("❌ Use: `$clear <quantidade>`")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("❌ A quantidade precisa ser um número.")


@bot.command()
async def animals(ctx):
    pasta = "memes/animals"

    arquivos = [
        f for f in os.listdir(pasta)
        if os.path.isfile(os.path.join(pasta, f))
    ]

    if not arquivos:
        await ctx.send("❌ Não encontrei memes de animais.")
        return

    meme = random.choice(arquivos)
    caminho = os.path.join(pasta, meme)

    await ctx.send(file=discord.File(caminho))


bot.run('')
