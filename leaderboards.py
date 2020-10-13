from discord.ext import commands

class Leaderboards(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='leaderboard', help='Shows records of fastest Extinctions, Legendary Extinctions, and Nightmares. Valid names are: exts, legendary_exts, nms. Ping Valcrist to update this list.')
    async def leaderboard(self, ctx, name):
        f = open(''.join(['fastest_', name, '.txt']), 'r')
        file_contents = f.read()
        await ctx.send(file_contents)
