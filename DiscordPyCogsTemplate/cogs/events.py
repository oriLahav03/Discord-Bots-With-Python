from discord.ext import commands
import asyncio


class Events(commands.Cog):

    def __init__(self, bot) -> None:
        """Events cog class, here is all the events declarations."""
        self.bot = bot


async def setup(bot) -> None:
    await bot.add_cog(Events(bot))
