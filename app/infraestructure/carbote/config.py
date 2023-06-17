import os
import discord
from discord.ext import commands


class Carbote():
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True

        self.instance = commands.Bot(command_prefix='!', intents=intents)

    def start(self):
        self.instance.run(os.environ.get('BOT_TOKEN'))

carbote = Carbote()