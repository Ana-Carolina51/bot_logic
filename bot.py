import discord
from bot_logic import pass_gen

# A variável intents armazena as permissões do bot
intents = discord.Intents.default()
# Ativar a permissão para ler o conteúdo das mensagens
intents.message_content = True
# Criar um bot e passar as permissões
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Fizemos login como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('.oi'):
        await message.channel.send(f"oi {message.author.name}!")
        await message.channel.send(f"{message.author.display_avatar}!")

    if message.content.startswith('$hello'):
        await message.channel.send("Hello!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    else:
        await message.channel.send(message.content)
    if message.content.startswith(".senha"):
        await message.channel.send("Sua senha é" + pass_gen(10))

client.run("MTQ0MzMxODk5Nzk3MzA3Mzk1Mw.G3t_ri.H0xoZ5dcolMi_DE__lMTfsYclVrSs6lpg4b8hw")
