#!/usr/bin/python
from discord.ext import commands
from itertools import islice, zip_longest
import os
class Guides(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='guide', aliases=['guides'], help='Various archived guides written by Valcrist, geared towards professional SWAT players. !list_guides to see what is available')
    async def guide(self, ctx, name, start = 0):
        filename = ''.join([name, '.txt'])
        fp = None
        files = [os.path.join(dirpath,f) for (dirpath, dirnames, filenames) in os.walk('guides') for f in filenames]
        for f in files:
            if os.path.basename(f) == filename:
                fp = open(f)
        if fp == None:
            await ctx.send('No guide found for {}'.format(name))
        else:
            result = ''
            for i, line in enumerate(fp):
                if start <= i:
                    if len(result) + len(line) < 1980:
                        result += line
                    else:
                        line_count = len(fp.readlines())
                        entry = f'{line_count - i} more lines...'
                        result += entry
                        break
            await ctx.send(result)

    @commands.command(name='list_guides', aliases=['list_guide'], help='Show all available guides that can be displayed. !guide guide_name will display the contents of the guide.')
    async def list_guides(self, ctx, start = 1):
        files = [f for (dirpath, dirnames, filenames) in os.walk('guides') for f in filenames]
        await ctx.send(', '.join(files))
