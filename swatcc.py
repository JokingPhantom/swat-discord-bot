# bot.py
import os
import re
import discord
import tabulate
import class_call

from discord.ext import commands
from discord.ext.tasks import loop
from dotenv import load_dotenv
from class_call import ClassCall

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SWAT_SERVER_ID = os.getenv('SWAT_SERVER_ID')
SWAT_CC_CHANNEL_ID = os.getenv('SWAT_CC_CHANNEL_ID')
TEST_SERVER_ID = os.getenv('TEST_SERVER_ID')
SWAT_CC_CHANNEL = os.getenv('SWAT_CC_CHANNEL')
TEST_CC_CHANNEL = os.getenv('TEST_CC_CHANNEL')

cc_regex = '^(?P<position>[1-9])\s?[-]?\s?(?P<name>.*)$'
bot = commands.Bot(command_prefix='!')
class_call = ClassCall()

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='hello', help='Responds with "Hello!"')
async def hello(ctx):
    await ctx.send('Hello!')
    
@bot.command(name='about_me', help='Returns information about the bot.')
async def about_me(ctx):
    await ctx.send('Author: JokingPhantom/Valcrist77')
    await ctx.send('Current host location: Amazon EC2, US East')

@bot.command(name='cc', help='Responds with the current Class Call. If given a format as an argument, it will respond with the current Class Call in that format.')
async def cc(ctx, format=None):
    global class_call
    class_call.time_since_last_call = 0
    if format:
        await ctx.send(class_call.export(format))
    else:
        await ctx.send(str(class_call))

@bot.command(name='startcc', help='Starts the Class Call.')
async def start_cc(ctx):
    global class_call
    class_call = ClassCall()
    await ctx.send('Class Call started')

@bot.command(name='clearcc', help='Resets the Class Call.')
async def clear_cc(ctx):
    global class_call
    class_call = ClassCall()
    await ctx.send('Class Call restarted')

@bot.command(name='stopcc', help='Disables the Class Call')
async def stop_cc(ctx):
    global class_call
    class_call = None
    await ctx.send('Class Call stopped')
    
@bot.command(name='set_format', help='Set format the Class Call is output in. Possible formats: default, grid')
async def set_format(ctx, format):
    global class_call
    class_call.time_since_last_call = 0
    error_message = class_call.set_format(format)
    await ctx.send(error_message or 'Set format to {}'.format(format))
    
@bot.command(name='import_cc', help='Imports a Class Call. Only supports the default format. Multiple blank space characters are squashed into one.')
async def import_cc(ctx, *cc):
    global class_call
    if not class_call:
        await ctx.send('Class Call started')
        class_call = ClassCall()
    success = class_call.import_cc(' '.join(cc))
    if success:
        await ctx.send('Class Call imported')
        await ctx.send(str(class_call))
    else:
        await ctx.send('Invalid format, preserving original Class Call')

@bot.command(name='close', help='Close all slots listed by marking the call with a "-". Slots are listed by number, separated by spaces.')
async def close(ctx, *slots):
    global class_call
    for slot in slots:
        call = '{} --'.format(slot)
        print(call)
        cc_match = re.match(cc_regex, call)
        class_call.receive_call(ctx.message.author.name, cc_match)
    await ctx.send('Closed slots {}'.format(" ".join(slots)))
    await ctx.send(str(class_call))

@bot.command(name='mode', help='Set the mode. Accepts a string representing the mode declared.')
async def mode(ctx, input=None):
    global class_call
    class_call.time_since_last_call = 0
    if input:
        class_call.mode = input
        await ctx.send('Mode set to {}'.format(class_call.mode))
    else:
        await ctx.send('Mode currently set to {}'.format(class_call.mode))
    
@bot.command(name='leader', help='Set the leader. Accepts a string representing the leader declared.')
async def leader(ctx, input=None):
    global class_call
    class_call.time_since_last_call = 0
    if input:
        class_call.leader = input
        await ctx.send('Leader set to {}'.format(class_call.leader))
    else:
        await ctx.send('Leader currently set to {}'.format(class_call.leader))

@bot.command(name='lock', help='Locks the class call, so no more calls can be made.')
async def lock(ctx):
    global class_call
    class_call.time_since_last_call = 0
    class_call.lock = True
    await ctx.send('Class call locked.')

@bot.command(name='unlock', help='Unlocks the class call, so calls can be made.')
async def unlock(ctx):
    global class_call
    class_call.time_since_last_call = 0
    class_call.lock = False
    await ctx.send('Class call unlocked.')

@bot.command(name='set_lock_timer', help='Sets the inactivity period until the class call is automatically locked, in seconds.')
async def set_lock_timer(ctx, input=None):
    global class_call
    if input:
        class_call.lock_timer = int(input)
        await ctx.send('Lock timer set to {}'.format(class_call.lock_timer))
    else:
        await ctx.send('Lock timer currently set to {}'.format(class_call.lock_timer))

@bot.event
async def on_message(message):
    global class_call
    if message.author == bot.user:
        return
    if not ((message.channel.name == TEST_CC_CHANNEL and str(message.guild.id) == TEST_SERVER_ID) or 
        (message.channel.name == SWAT_CC_CHANNEL and str(message.guild.id) == SWAT_SERVER_ID)):
        return

    cc_match = re.match(cc_regex, message.content)
    if cc_match and not class_call.lock:
        if not class_call:
            await message.channel.send('Class Call started')
            class_call = ClassCall()
            class_call.lock = False
        class_call.receive_call(message.author.name, cc_match)
        await message.channel.send(str(class_call))
    await bot.process_commands(message)

@loop(seconds=1)
async def auto_lock_cc():
    await bot.wait_until_ready()
    if class_call:
        class_call.time_since_last_call += 1
        if (class_call.time_since_last_call >= class_call.lock_timer) and class_call.class_call_used and not class_call.lock:
            class_call.lock = True
            channel = bot.get_channel(int(SWAT_CC_CHANNEL_ID))
            await channel.send('Class Call locked after {} seconds of inactivity.'.format(class_call.lock_timer))

auto_lock_cc.start()
bot.run(TOKEN)

