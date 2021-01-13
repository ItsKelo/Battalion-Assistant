import discord
import os
from discord.ext import commands
from datetime import datetime
from datetime import timedelta
import json
import re
from discord.utils import get

with open("resources/settings.json", "r") as file:
    settings = json.load(file)

#Set the prefix of the bot commands
discord_bot = commands.Bot(command_prefix=settings["prefix"], case_insensitive=True)


# Removing the old help command
discord_bot.remove_command('help')

# Permissions check for the bot's administrator. This permission will allow invididuals to shutdown the bot and have
# higher levels of control over it. Only give this permission to other individuals if completely necessary
def is_admin(ctx):
    return ctx.author.id in settings['admin_ids']


# Command to set the LOA Channel for LOA messages to appear
@discord_bot.command()
@commands.check(is_admin)
async def setLOAChannel(ctx):
    settings['loa_channel'] = ctx.channel.id
    with open("resources/settings.json","w") as outfile:
        json.dump(settings, outfile)
    await ctx.send("LOA Channel Set.")


# Developer command - Used to load command cogs, so that the bot has the commands in the cogs available for use.
@discord_bot.command()
@commands.check(is_admin)
async def load(ctx, extension):
    discord_bot.load_extension(f'cogs.{extension}')
    print("Cog Loaded")


# Developer command - Used to unload command cogs, so that the commands within the cogs aren't available for use.
@discord_bot.command()
@commands.check(is_admin)
async def unload(ctx, extension):
    discord_bot.unload_extension(f'cogs.{extension}')


# Developer command - Used to reload command cogs, so that the commands within the cogs have their code refreshed to
# the newest saved version. This command is very good for correcting small code errors in cogs without taking the bot
# offline.
@discord_bot.command()
@commands.check(is_admin)
async def reload(ctx, extension):
    await ctx.message.delete()
    discord_bot.unload_extension(f'cogs.{extension}')
    discord_bot.load_extension(f'cogs.{extension}')
    print("Cog reloaded")


# Error catching event - This event is used to tell the Developer and the user that an error has occurred.
@discord_bot.event
async def on_command_error(ctx, error):

    # This regex expression is used to make sure that all attempts at using a non-existent command are caught
    regexExp = re.compile(r'Command "(.*)" is not found')
    mo = regexExp.search(str(error))

    # This regex expression is used to make sure that all attempts at using a command that the user doesn't have
    # permissions for are caught
    regexExp2 = re.compile(r'You are missing at least one of the required roles: (.*)')
    checkFunc = regexExp2.search(str(error))

    if error == KeyError:
        await ctx.send('Not all the spreadsheet columns are filled for related data')

    elif mo is not None:
        await ctx.send(f'{mo.group()} and is not a command. Check the help command or try again')

    elif checkFunc is not None:
        await ctx.send(f'You do not have permissions to execute this command')

    else:
        print(error)
        await ctx.send(f"An unhandled error has occurred - if this error persists contact a dev")


# Logout command - Takes the bot offline
@discord_bot.command(aliases=['logout', 'down'])
@commands.check(is_admin)
async def off(ctx):
    await ctx.send('Powering down')
    print('Bot shutdown command issued')
    await discord_bot.logout()


# Change the activity of the bot
@discord_bot.event
async def on_ready():
    await discord_bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,
                                                             name="LOAs"))


def load_all():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            discord_bot.load_extension(f'cogs.{filename[:-3]}')


load_all()


# Retrieving the token from the token.txt file and using it to take the bot online
token = open("./resources/token.txt", 'r').readline()
token = token.strip()
print("Bot Online")
discord_bot.run(f'{token}')
