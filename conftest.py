"""Setup minimal bot testing"""
import os
import glob
import pytest
from discord.ext import commands
import discord as dc
import discord.ext.test as dpytest


class DummyCog(commands.Cog):
    """Simple dummy cog to be added to the base discord bot"""
    @commands.command()
    async def hello(self, ctx):
        """Simple hello echo command as proof of basic working bot"""
        await ctx.send("hello world")


@pytest.fixture(autouse=True)
def bot(event_loop):
    """Bot fixture that is used by every test"""
    intents = dc.Intents.default()
    intents.members = True
    discord_bot = commands.Bot(command_prefix='?', event_loop=event_loop, intents=intents)
    discord_bot.add_cog(DummyCog(discord_bot))
    dpytest.configure(discord_bot)
    return discord_bot


def pytest_sessionfinish():
    """ Clean up attachment files"""
    files = glob.glob('./dpytest_*.dat')
    for path in files:
        try:
            os.remove(path)
        except Exception as e:
            print(f"Error while deleting file {path}: {e}")
