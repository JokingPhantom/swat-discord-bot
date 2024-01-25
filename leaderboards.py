#!/usr/bin/python
from discord.ext import commands
from itertools import islice, zip_longest


class Leaderboards(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='leaderboard', aliases=['leaderboards'], help='Shows records of fastest Extinctions, Legendary Extinctions, and Nightmares. Valid names are: exts, legendary_exts, nms, solo_nms. Will limit ranks to top 10 or 2000 characters, whichever is shorter. Use start number to indicate which rank start from, defaults to 1. Post replay file and screenshot of "Official Time" in #replays or DM to Valcrist to update this list.')
    async def leaderboard(self, ctx, name, start=1):
        filename = ''.join(['leaderboards/', 'fastest_', name, '.txt'])
        result = ''

        fp = open(filename)
        for i, line in enumerate(fp):
            if start <= i:
                entry = f'{i}. {line}'
                if len(result) + len(entry) < 2000:
                    result += entry
                else:
                    break
        await ctx.send(result)
