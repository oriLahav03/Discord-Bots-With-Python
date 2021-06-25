from __future__ import annotations
from discord.ext import commands


class Commands(commands.Cog):
    def __init__(self, bot) -> None:
        """All the fun commands are contained in this Fun cog class."""
        self.bot = bot

    @commands.command()
    async def ping(self, ctx: commands.context.Context):
        await ctx.send(f'Pong! {round(self.bot.latency * 1000)}ms')


def setup(bot) -> None:
    bot.add_cog(Commands(bot))
