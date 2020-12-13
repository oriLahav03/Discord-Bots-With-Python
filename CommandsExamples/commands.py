import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')  # you can change the prefix from '.' to any prefix you want


@client.event
async def on_ready():
    """
    this function Announces us when the bot is ready.
    :return: None
    """
    await client.change_presence(activity=discord.Game("Message to show"))
    print('Logged in as: ' + client.user.name)


@client.command()
@commands.has_role('Role name')
async def tag(ctx, user: discord.Member):
    """
    this function tag and spam user with a message you write befor you run the code.
    
    Example: .tag @username#1234 
    
    :param ctx: the user message in discord
    :param user: the user to tag
    :return: None
    """
    while True:
        await ctx.send(f'{user.mention} Your message')


@client.command(pass_context=True)
@commands.has_role('Role name')
async def dm(ctx, member: discord.Member = None, *, message):
    """
    this function send a direct message to user with the message given in the command.
    
    Example: .dm @username#1234 hey how are you? its me :)
    
    :param ctx: the user message in discord
    :param member: the member to dm
    :param message: the message to send
    :return: None
    """
    if not member:
        return await member.say(ctx.message.author.mention + "Specify a user to DM!")
    else:
        await member.send(message)
    await clear(ctx, 1)


@client.command(pass_context=True)
async def spam(ctx, member: discord.Member = None, *, message):
    """
    the function spam given user tag in dm with the message you want.
    
    Example: .spam @username#1234 hey how are you? its me :)
    
    :param ctx: the user message in discord
    :param member: the member to spam
    :param message: the message to send
    :return: None
    """
    await clear(ctx, 1)
    while True:
        if not member:
            return await member.say(ctx.message.author.mention + "Specify a user to DM!")
        else:
            await member.send(message)


@client.command()
async def clear(ctx, amount=1):
    """
    the function delete given amount of messages from the current channel.
    
    Example: .clear 10
    
    :param ctx: the command
    :param amount: number of messages to delete
    :return: None
    """
    await ctx.channel.purge(limit=amount)