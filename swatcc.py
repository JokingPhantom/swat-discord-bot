#!/usr/bin/python
import os

from discord.ext import commands
from dotenv import load_dotenv

from leaderboards import Leaderboards
from info import Info
from class_calls import ClassCalls
from guides import Guides
from nemesis_taunt import NemesisTaunt
from roll import Roll

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

bot.add_cog(Leaderboards(bot))
bot.add_cog(Info(bot))
bot.add_cog(ClassCalls(bot))
bot.add_cog(Guides(bot))
bot.add_cog(NemesisTaunt(bot))
bot.add_cog(Roll(bot))
bot.run(TOKEN)
