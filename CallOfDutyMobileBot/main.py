import discord
import re
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix='!', intents=intents)  # you can change the prefix from '.' to any prefix you want

client.remove_command('help')  # remove the build in !help command

# this dir contain all the custom emojis i want to add to my reaction role message
emojis = {
    # for example: 'IsraelLegends' is the emoji name and '<:IsraelLegends:783469829872812032>' is the id
    'IsraelLegends': '<:IsraelLegends:111111111111111111>',
    'HebrewShadow': '<:HebrewShadow:222222222222222222>',
    'HebrewGods': '<:HebrewGods:333333333333333333>',
    'Israeli': '<:Israeli:444444444444444444>',
    'Israelwr': '<:Israelwr:555555555555555555>',
    'HebrewForce': '<:HebrewForce:666666666666666666>',
    'Clanless': '<:Clanless:777777777777777777>'
}

# this is for a !staff command that tag all the staff in the server
staff = """
the current staff members are: 
<@111111111111111111>
<@222222222222222222>
<@333333333333333333>
<@444444444444444444>
<@555555555555555555>
<@666666666666666666>
"""

# here I add every custom command I want to add (if i want that the command can be detach from the middle of message)
# for example: if the message will be: where is the staff the command will work.
messages = {
    'staff': staff
}


@client.event
async def on_ready():
    """
    this function Announces us when the bot is ready
    :return: None
    """
    await client.change_presence(activity=discord.Game("message to show"))
    print('Logged in as: ' + client.user.name)


@client.event
async def on_message(message):
    """
    the function handle in the commands that in the messages dir
    :param message: the message from the serever
    :return: None
    """
    if message.author != client.user:
        keys = []
        for key, value in messages.items():
            keys.append(key)
        for key in keys:
            if key in message.content.lower() and key in messages:
                channel = message.channel
                await channel.send(messages[key])


@client.command()
@commands.has_role('💻 | Programmer | 💻')
# only member with the role called '💻 | Programmer | 💻' can active this command
async def reaction(ctx):
    """
    this command send embed message and add the reaction roles to the message
    :param ctx: the command
    :return: None
    """
    await ctx.message.delete()
    description = ''
    for key, value in emojis.items():
        description += key + ' -> ' + value + '\n'
    embed_var = discord.Embed(title="The embed title",
                              description=description,
                              color=0x00ff00)
    msg = await ctx.send(embed=embed_var)
    for emoji in emojis.values():
        await msg.add_reaction(emoji)


async def dm_join(member: discord.Member = None):
    """
    the function send dm message to user
    :param member: the user to dm
    :return: None
    """
    if member:
        await member.send("this message send to the user who add reaction in direct message")


async def dm_leave(member: discord.Member = None):
    """
    the function send dm message to user
    :param member: the user to dm
    :return: None
    """
    if member:
        await member.send("this message send to the user who remove the reaction in direct message")


@client.event
async def on_raw_reaction_add(payload):
    """
    this function handle every reaction add and add role according the reaction
    :param payload: the server payload
    :return: None
    """
    message_id = payload.message_id
    if message_id == 783741092277256192:
        # to check that the message id is 783741092277256192 because we don't want
        # to add the role on every time this reaction add

        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)
        member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)

        if payload.emoji.name in emojis:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)
            await dm_join(member)

            if role is not None:
                if member is not None:
                    await member.add_roles(role)
                    print("done")
                else:
                    print("Member not found")
            else:
                print("Role not found")


@client.event
async def on_raw_reaction_remove(payload):
    """
    this function handle every reaction remove and remove role according the reaction
    :param payload: the server payload
    :return: None
    """
    message_id = payload.message_id
    if message_id == 783741092277256192:
        # to check that the message id is 783741092277256192 because we don't want
        # to remove the role on every time this reaction add

        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)
        member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)

        if payload.emoji.name in emojis:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)
            await dm_leave(member)

            if role is not None:
                if member is not None:
                    await member.remove_roles(role)
                    print("done")
                else:
                    print("Member not found")
            else:
                print("Role not found")


client.run("<Token>")  # add your bot token here
