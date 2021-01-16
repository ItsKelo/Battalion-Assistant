import discord
from discord.ext import commands, tasks
from mainSheet import *

sheet = MainSheet()

with open("resources/settings.json") as file:
    settings = json.load(file)

items = settings["privileged_roles"]

def is_privileged(ctx):
    for role in ctx.author.roles:
        if role.id in items:
            return True;


class sheetCog(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.loaChecker.start()

        with open("resources/settings.json") as file:
            self.settings = json.load(file)


    @tasks.loop(hours=24)
    async def loaChecker(self):
        print("Running LOA Checker")
        expiredNamesList = sheet.removeExpired()

        if self.settings['loa_channel'] is None:
            print(f"Please set the channel for LOA alerts by using the {self.settings['prefix']}setLOAChannel command")

        channelLOA = self.client.get_channel(self.settings['loa_channel'])

        if expiredNamesList == []:
            print("No LOAs")
            return

        for name in expiredNamesList:
            await channelLOA.send(f'**{name}** your LOA has expired')

    @loaChecker.before_loop
    async def before_loaChecker(self):
        print('Preparing LOA Checker Timer.')
        await self.client.wait_until_ready()

    @commands.command(aliases=['isBL', 'isBlacklisted', 'checkBL'])
    @commands.check(is_privileged)
    async def checkBlacklist(self, ctx, *, steamIds):
        steamId_list = steamIds.split()
        cellVals = sheet.getBL()

        onBL = []
        for steamId in steamId_list:
            if steamId in cellVals:
                onBL.append(steamId)

        colour = discord.Colour.red() if len(onBL) > 0 else discord.Colour.green()

        BL_embed = discord.Embed(
            description=f'**BlackList Checker**',
            colour=colour
        )

        if len(onBL) == 0:
            BL_embed.add_field(name='Troopers are clear for recruitment', value='All Clear')

        else:
            i = 0
            for id in onBL:
                BL_embed.add_field(name=f'{id}', value='On Blacklist')
                i = i + 1
                if (i % 24) == 0 and i > 0:
                    await ctx.send(embed=BL_embed)
                    BL_embed.clear_fields()

        await ctx.send(embed=BL_embed)

def setup(client):
    client.add_cog(sheetCog(client))
