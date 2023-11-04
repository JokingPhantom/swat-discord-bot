#!/usr/bin/python
from discord.ext import commands

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='hello', help='Responds with "Hello!"')
    async def hello(self, ctx):
        await ctx.send('Hello!')

    @commands.command(name='about_me', help='Returns information about the bot.')
    async def about_me(self, ctx):
        await ctx.send('Author: JokingPhantom/Valcrist77')
        await ctx.send('Current host location: Amazon Lightsail, US East')
        await ctx.send('https://github.com/JokingPhantom/swat-discord-bot')
