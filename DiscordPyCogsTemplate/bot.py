from __future__ import annotations
from discord.ext import commands
import discord
from base import Config


class Bot(commands.Bot):

    def __init__(self) -> None:
        """The Bot class, where the magic happens."""
        intents = discord.Intents.all()
        super().__init__(command_prefix='!', case_insensitive=True, intents=intents)
        self.config = Config.load()

        self.load_cogs()
        self.run()

    def load_cogs(self) -> None:
        total_cogs = len(self.config.cogs)
        for cog in self.config.cogs:
            cog_index = self.config.cogs.index(cog) + 1

            try:
                self.load_extension(cog)
                print(f'[{cog_index}/{total_cogs}] Cog "{cog}" loaded.')
            except commands.errors.ExtensionNotFound as e:
                print(f'Error occurred while cog "{cog}" was loaded.\nException: {e}\n')

    def run(self) -> None:
        try:
            super().run(self.config.token)
        except discord.errors.LoginFailure:
            print('Bad bot token was provided (Can\'t login).')
            exit(1)

    @staticmethod
    def log(text: str) -> None:
        print(f'[x] {text}')


def main() -> None:
    Bot()


if __name__ == '__main__':
    main()
