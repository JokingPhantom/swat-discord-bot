from discord.ext import commands

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='about_me', help='Returns information about the bot.')
    async def about_me(self, ctx):
        await ctx.send('Author: JokingPhantom/Valcrist77')
        await ctx.send('Current host location: Amazon EC2, US East')
