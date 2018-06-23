import asyncio
import logging
import traceback

import discord
from discord.ext import commands

import config

description= """
A Discord bot written by a community of programmers.
"""

initial_extensions = ()

class Vixim(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=self.get_prefix_,
                         description=description)

        for extension in initial_extensions:
            try:
                self.load_extension(extension)
            except:
                print(f"Failed to load extension {extension}.")
                traceback.print_exc()

    async def get_prefix_(self, bot, message):
        # TODO: Add guild specific prefix grabbing from DB
        return commands.when_mentioned(bot, message)

    async def on_ready(self):
        print("-" * 10)
        print("Logged in as:\n"
              f"Username: {self.user}\n"
              f"ID: {self.user.id}")
        print(f"using discord.py v{discord.__version__}")
        print("-" * 10)

async def run():
    bot = Vixim()
    try:
        await bot.start(config.token)
    except KeyboardInterrupt:
        await bot.logout()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())