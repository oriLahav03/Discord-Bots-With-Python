import discord
from discord.ext import commands
from discord import app_commands


class Commands(commands.Cog):
    def __init__(self, bot) -> None:
        """All the fun commands are contained in this Fun cog class."""
        self.bot = bot

    @app_commands.command()
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'Pong! {round(self.bot.latency * 1000)}ms')


async def setup(bot) -> None:
    await bot.add_cog(Commands(bot))
