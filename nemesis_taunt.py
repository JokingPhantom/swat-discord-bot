#!/usr/bin/python
import random

from discord.ext import commands

NEMESIS_TAUNT_LIST = [
    # Nuke taunt
    'Swwwaaaaat',
    'Doooooooom',
    'Grrrrrrrrr',
    'Paaaaiiiin',
    # Slay taunt
    'Feel the pain!',
    'Die, weakling!',
    "You're mine now!",
    'Domination!',
    # Phase taunt
    'What now, bitches?',
    'You like me now?',
    'You afraid yet?',
    # Ext EMP Blast taunt
    'No juice for you.',
    "Energy's for wimps.",
    'Suffer cell depletion.',
    # Round 2 taunt
    'Round two, fight!!',
    "Let's try again!!",
    "It's not over yet!!",
    # Flashbang taunt
    'Heh.',
    'Nah.',
    'Nope.',
    'Check it.',
]

NEMESIS_REINFORCEMENT_TAUNT_LIST = [
    'Reinforcements...',
    'Send them in...',
    'Backup coming...',
    'Need assistance...',
    'Requesting aid...',
]

class NemesisTaunt(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='nemesis_taunt', aliases=['taunt'], help='Responds with a random taunt from Nemesis')
    async def nemesis_taunt(self, ctx):
        sample = random.sample(NEMESIS_TAUNT_LIST, 1)[0]
        await ctx.send(sample)

