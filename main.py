
import discord
from discord.ext import commands
import random
import needs_more_jpeg as nmj


description = '''TI bot best bot'''
bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command(description='For when you wanna settle the score some other way')
async def choose(*choices : str):
    """Chooses between multiple choices."""
    await bot.say(random.choice(choices))


@bot.command()
async def repeat(times : int, content='repeating...'):
    """Repeats a message multiple times."""
    if times > 5:
        times = 5

    for i in range(times):
        await bot.say(content)


@bot.command()
async def joined(member : discord.Member):
    """Says when a member joined."""
    await bot.say('{0.name} joined in {0.joined_at}'.format(member))


@bot.command(pass_context=True)
async def needsmorejpeg(context, url: str):
    """Adds a bit more JPEG to the url"""
    channel = context.message.channel
    await nmj.compress_img(await nmj.url_to_img(url), 'temp.jpeg')
    await bot.send_file(channel, 'temp.jpeg')

@bot.command()
async def anthem():
    await bot.say('https://cdn.discordapp.com/attachments/357261287740145665/358184959728418816/andy_jesus.mp4')


@bot.group()
async def cool(name: str):
    name = name.lower()
    if name == 'bot':
        await bot.say('Yes, I\'m quite cool.')
    elif name == 'andy':
        await bot.say('Yes, Andy is very cool.')
    else:
        await bot.say('No, {} is not cool.'.format(name))


def get_token():
    with open('token.txt') as f:
        line = f.readline()
        f.close()
        return line


bot.run(get_token())
bot.close()
