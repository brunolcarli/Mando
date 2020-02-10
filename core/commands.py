r"""
Módulo dedicado aos comandos Discord que o Mando disponibiliza
"""
from random import randint, choice
import discord
from discord.ext import commands

from core.external_requests import get_random_meme, Queries, Mutations
from core.util import get_gql_client, make_hash
from settings import API_URL

client = commands.Bot(command_prefix='--')


@client.event
async def on_ready():
    print('Ready!')


@client.command()
async def ping(discord):
    """
    Pinga o bot para teste sua execução
    """
    await discord.send('pong!')


@client.command()
async def roll(discord, sides=None):
    """
    Rola um dado e retornando o resultado.
    Por padrão o dado posusi 6 lados, fornecendo um valor Mando rolará um
    dado esta quantidade de lados.
    Exemplo
        - `--roll 20`
    """
    # Se nenhum argumento for fornecido rola um dado de 6 lados
    if not sides:
        result = randint(1, 6)
        return await discord.send(
            f'Em um dado de 6 lados {discord.author.name} rolou {result}!'
        )

    # Mensagem de erro padrão em caso de entrada de valor inválido
    invalid_value_error = 'Esta valor é inválido, por favor forneça um número!'

    # tenta realizar a conversão do argumento fornecido para um inteiro absoluto
    try:
        sides = abs(int(sides))
    except ValueError:
        # Se a conversão falhar o usuário forneceu um valor inválido
        return await discord.send(invalid_value_error)

    # Rola o dado com o valor fornecido, desde que não seja zero
    if not sides:
        return await discord.send(invalid_value_error)

    result = randint(1, sides)
    return await discord.send(
        f'Em um dado de {sides} lados {discord.author.name} rolou {result}!'
    )


@client.command(aliases=['meme'])
async def random_meme(discord):
    """
    Retorna um meme aleatório
    """
    status, data = get_random_meme()
    if status != 200:
        return discord.send(
            'Desculpe obtive um erro ao consultar os memes,'\
            ' por favor tente novamente mais tarde!'
        )

    meme_url = data.get('url')
    await discord.send(meme_url)


@client.command(aliases=['rquote', 'rq'])
async def random_quote(bot):
    """
    Retorna um quote aleatório.
    """

    server = make_hash(bot.guild.name, bot.guild.id)
    payload = Queries.get_quotes(server.decode('utf-8'))
    client = get_gql_client(API_URL)

    try:
        response = client.execute(payload)
    except Exception as err:
        print(f'Erro: {str(err)}\n\n')
        return await bot.send('Erro')

    quotes = response.get('botQuotes')
    if not quotes:
        return await bot.send('Ainda não há registros de quotes neste servidor')

    chosen_quote = choice(quotes)
    embed = discord.Embed(color=0x1E1E1E, type="rich")
    embed.add_field(name='Quote:', value=chosen_quote, inline=True)
    return await bot.send('Lembra disso:', embed=embed)


@client.command(aliases=['q', 'sq', 'save_quote'])
async def quote(bot, *args):
    """
    Retorna um quote aleatório.
    """
    message = ' '.join(word for word in args)

    if not message:
        return await bot.send(
            'Por favor insira uma mensagem.\nExemplo:\n'\
            '``` --quote my name is bond, vagabond ```'
        )

    server = make_hash(bot.guild.name, bot.guild.id)
    payload = Mutations.create_quote(message, server.decode('utf-8'))
    client = get_gql_client(API_URL)

    try:
        response = client.execute(payload)
    except Exception as err:
        print(f'Erro: {str(err)}\n\n')
        return await bot.send('Erro')

    quote = response.get('botCreateQuote')
    embed = discord.Embed(color=0x1E1E1E, type="rich")
    embed.add_field(name='Quote salvo:', value=quote.get('response'), inline=True)
    return await bot.send('Feito:', embed=embed)
