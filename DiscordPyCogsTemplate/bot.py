import discord
from discord.ext import commands
from base import Config


class Bot(commands.Bot):
    def __init__(self) -> None:
        intents = discord.Intents.all()
        super().__init__(command_prefix='!', case_insensitive=True, intents=intents)
        self.remove_command('help')
        self.config = Config.load()

    def get_config(self):
        return self.config

    async def setup_hook(self) -> None:
        total_cogs = len(self.config.cogs)
        for cog in self.config.cogs:
            cog_index = self.config.cogs.index(cog) + 1

            try:
                await self.load_extension(cog)
                self.log(f'[{cog_index}/{total_cogs}] Cog "{cog}" loaded.')
            except commands.errors.ExtensionNotFound as e:
                self.log(f'Error occurred while cog "{cog}" was loaded.\nException: {e}\n')

        self.log(f'Logged in as: {self.user}')

    @staticmethod
    def log(text: str) -> None:
        print(f'[x] {text}')


def main() -> None:
    bot = Bot()
    bot.run(bot.config.token, log_level=0)


if __name__ == '__main__':
    main()