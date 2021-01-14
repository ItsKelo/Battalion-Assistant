import discord
from discord.ext import commands
import json
# This cog will contain general discord administrative commands
class Admin(commands.Cog):

    def __init__(self, client):
        self.client = client
        with open("resources/settings.json") as file:
            self.settings = json.load(file)

    # Command to check latency
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! ({round(self.client.latency * 1000)}ms)')

    @commands.command(aliases=['commands', 'cmd', 'cmds'])
    async def help(self, ctx):
        helpEmbed = discord.Embed(
            title='Commands',
            description=f'These are all the available commands. Prefix= {self.settings["prefix"]}',
            colour=discord.Colour.blue()
        )

        helpEmbed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)

        # helpEmbed.add_field(name='', value="", inline=False)

        helpEmbed.add_field(name='--------------------', value="**General Commands**", inline=False)
        helpEmbed.add_field(name='help', value="Makes this information box appear", inline=False)
        helpEmbed.add_field(name='ping', value="Pong!", inline=False)
        helpEmbed.add_field(name='--------------------', value="**Privileged Commands**", inline=False)
        helpEmbed.add_field(name='checkBL <*STEAMIDs*>', value="Checks if any of the SteamIDs are on blacklist",
                            inline=False)
        helpEmbed.add_field(name='--------------------', value="**Administrative Commands**", inline=False)
        helpEmbed.add_field(name='logout', value="Turns off the bot",
                            inline=False)
        helpEmbed.add_field(name='setLOAChannel', value="Sets the bot's LOA notifications to send in that channel", inline=False)

        helpEmbed.add_field(name='--------------------', value="**Automated Functionality**", inline=False)
        helpEmbed.add_field(name='Automated LOA system', value="Notifies Troopers and edits sheet on LOA expiration",
                            inline=False)
        # helpEmbed.add_field(name='-', value="", inline=False)
        helpEmbed.set_footer(text='Created by Kelo. Powered by the Yellow and Blue snake.',
                             icon_url='https://user-images.githubusercontent.com/32295800/104527141-f590ec80-55fb-11eb-86a0-69df012aee0e.png')
        await ctx.send(embed=helpEmbed)


def setup(client):
    client.add_cog(Admin(client))
