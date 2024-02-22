import discord
from discord.ext import commands
import random

description = '''An example bot to showcase the discord.ext.commands extension module.
There are a number of utility commands being showcased here.'''
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return
    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


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
async def rps(ctx, choice: str):
    """Play rock-paper-scissors with the bot."""
    choices = ['rock', 'paper', 'scissors']
    bot_choice = random.choice(choices)

    if choice.lower() in choices:
        await ctx.send(f'You chose {choice}, I chose {bot_choice}.')
        if choice.lower() == bot_choice:
            await ctx.send('It\'s a tie!')
        elif (choice.lower() == 'rock' and bot_choice == 'scissors') or \
                (choice.lower() == 'paper' and bot_choice == 'rock') or \
                (choice.lower() == 'scissors' and bot_choice == 'paper'):
            await ctx.send('You win!')
        else:
            await ctx.send('I win!')
    else:
        await ctx.send('Invalid choice. You can only choose rock, paper, or scissors.')


@bot.group()
async def cool(ctx):
    """Says if a user is cool. In reality this just checks if a subcommand is being invoked."""
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')


@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')


bot.run('MTIwNTIwNzM0ODMwMjQ1NDg1NA.GUvKcE.BbmclmY5d8KR50BLcnVnZiTkjcpxwpijW_4k3k')
