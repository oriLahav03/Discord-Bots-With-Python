from discord.ext import commands
import asyncio


class Events(commands.Cog):

    def __init__(self, bot) -> None:
        """Events cog class, here is all the events declarations."""
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        self.bot.log(f'Logged in as: {self.bot.user}')
        self.bot.remove_command('help')
        await asyncio.sleep(3)


def setup(bot) -> None:
    bot.add_cog(Events(bot))
