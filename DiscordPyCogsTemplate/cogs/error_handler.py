from discord.ext import commands
import discord


class Error_Handler(commands.Cog):

    def __init__(self, bot) -> None:
        """Events cog class, here is all the events declarations."""
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error) -> None:
        if hasattr(ctx.command, 'on_error'):  # local errors
            return

        ignored = (commands.CommandNotFound,)
        error = getattr(error, 'original', error)

        if isinstance(error, ignored):
            return

        if isinstance(error, commands.DisabledCommand):
            await ctx.send(f'{ctx.command} has been disabled.')
        elif isinstance(error, commands.NoPrivateMessage):
            try:
                await ctx.author.send(f'{ctx.command} can not be used in Private Messages.')
            except discord.HTTPException:
                pass
        elif isinstance(error, commands.BadArgument):
            if ctx.command.qualified_name == 'tag list':  # Check if the command being invoked is 'tag list'
                await ctx.send('I could not find that member. Please try again.')
        else:
            await ctx.send(embed=discord.Embed(description=f'Error occurred. {error}.'))


async def setup(bot) -> None:
    await bot.add_cog(Error_Handler(bot))
