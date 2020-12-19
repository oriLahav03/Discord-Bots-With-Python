import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')  # you can change the prefix from '.' to any prefix you want


@client.event
async def on_ready():
    """
    this function Announces us when the bot is ready
    :return: None
    """
    await client.change_presence(activity=discord.Game("the message you wanna show"))
    print('Logged in as: ' + client.user.name)


@client.event
async def on_message(message):
    """
    the function handle the numbers sent and send the number plus one, not related content will be deleted.
    :param message:
    :return:
    """
    channel = message.channel
    msgs = await channel.history(limit=2).flatten()
    if not message.content.isdigit():
        await message.delete()
    elif (int(msgs[1].content) + 1) != int(message.content):
        await message.delete()
    elif message.author.bot is False:
        channel = message.channel
        await channel.send(int(message.content) + 1)


client.run('<Token>')  # enter your bot token here
