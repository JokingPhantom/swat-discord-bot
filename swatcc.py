#!/usr/bin/python
import os
import random

from discord.ext import commands
from dotenv import load_dotenv

from leaderboards import Leaderboards
from info import Info
from class_calls import ClassCalls
from guides import Guides
from nemesis_taunt import NemesisTaunt

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

roll_list = ['acro borg', 'sborg', 'x+k', 'solo x+k', 'x+m', 'gal', 'sal', 'tech', 'stech', 'pyro', 'hpsy', 'spsy', 'htact', 'tact', 'stact', 'gho', 'sho', 'gs', 'fcgs', 'ss', 'qmed', 'bmed', 'demo', 'sdemo', 'gwm', 'fcwm', 'swm']
slap_list = [
    '{author} slapped {target} with a large tuna! Wet.',
    '{author} slapped {target} with a tasty cookie! Yum.',
    '{author} slapped {target} with both hands!',
    '{author} slapped {target} with a taco! Messy, but tasty.',

    '{author} slapped {target}. Ouch! That must hurt!',
    '{author} slapped {target}. That should teach you a lesson!',
    '{author} slapped {target}. Take that, you fool!',
    '{author} slapped {target}. Ooooh snap!',
    '{author} slapped {target}. Get slapped, son!',
    '{author} slapped {target}. Your bloody hipster!',
    '{author} slapped {target}. Go buy us some Ice Cream!',

    '{author} slayed {target}. Feel the pain!',
    '{author} drained {target}. Energy is for wimps!',
    '{author} teleported {target} away to a dark alley... Know your name!',
    '{author} ioned {target}. Calculated?',
    '{author} shockwaved {target}. Geometry.',
    '{author} x-naded {target}. Lethal!',

    '{author} tried to slap {target} but missed. Clumsy!',
]

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='roll', help='Rolls a class, either from a provided list (separated by space), or from a pre-selected list.')
async def roll(ctx, *elements):
    list = elements or roll_list
    sample = random.sample(list, 1)[0]
    await ctx.send(str(sample))

@bot.command(name='slap', help='Slap someone with a random object')
async def roll(ctx, target):
    sample = random.sample(slap_list, 1)[0]
    await ctx.send(sample.format(author = ctx.author, target = target))

bot.add_cog(Leaderboards(bot))
bot.add_cog(Info(bot))
bot.add_cog(ClassCalls(bot))
bot.add_cog(Guides(bot))
bot.add_cog(NemesisTaunt(bot))
bot.run(TOKEN)
