#!/usr/bin/python
import os
import random

from discord.ext import commands
from dotenv import load_dotenv

from leaderboards import Leaderboards
from info import Info
from class_calls import ClassCalls

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

roll_list = ['acro borg', 'sborg', 'x+k', 'solo x+k', 'x+m', 'gal', 'sal', 'tech', 'stech', 'pyro', 'hpsy', 'spsy', 'htact', 'tact', 'stact', 'gho', 'sho', 'gs', 'fcgs', 'ss', 'qmed', 'bmed', 'demo', 'sdemo', 'gwm', 'fcwm', 'swm']

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='roll', help='Rolls a class, either from a provided list (separated by space), or from a pre-selected list.')
async def roll(ctx, *elements):
    list = elements or roll_list
    sample = random.sample(list, 1)[0]
    await ctx.send(str(sample))

bot.add_cog(Leaderboards(bot))
bot.add_cog(Info(bot))
bot.add_cog(ClassCalls(bot))
bot.run(TOKEN)

