# This example requires the 'members' and 'message_content' privileged intents to function.

import discord
from discord.ext import commands
import random
from contrazeñas import llave 

description = '''An example bot to showcase the discord.ext.commands extension
module.

Aquí se muestran varios comandos de utilidad.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='/', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Iniciado sesión como {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def sumar(ctx, left: int, right: int):
    """Suma dos números separados."""
    await ctx.send(left + right)

@bot.command()
async def contrazeña(ctx, Num: int = 5):
    """Te da una contrazeña a la que le puedes poner un largo."""
    await ctx.send(f'Esta es la contraseña:{llave(Num)}')

@bot.command()
async def roll(ctx, dice: str):
    """Lanza un dado en formato NdN."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('El formato tiene que estar en NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@bot.command(description='Para cuando quieras ajustar cuentas de otra manera')
async def elegir(ctx, *choices: str):
    """elige entre múltiples opciones."""
    await ctx.send(random.choice(choices))


@bot.command()
async def repetir(ctx, times: int, content='repitiendo...'):
    """Repite un mensaje varias veces."""
    for i in range(times):
        await ctx.send(content)


@bot.command()
async def joined(ctx, member: discord.Member):
    """Dice cuando un miembro se unió."""
    await ctx.send(f'{member.name} se unió {discord.utils.format_dt(member.joined_at)}')


@bot.group()
async def cool(ctx):
    """Dice si un usuario es genial.

    En realidad, esto sólo comprueba si se está invocando un subcomando.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} no es cool')


@cool.command(name='rokikie')
async def _bot(ctx):
    """¿rokikie es cool?"""
    await ctx.send('Sí, el bot es cool.')


bot.run('TOKEN')
