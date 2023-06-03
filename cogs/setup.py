# # # # This will setup the first cog # # # #
# # # # This initializes: Ping, and Clear

from discord.ext import commands, tasks
import os
from pathlib import Path
from utils.log_manager import bot_logs
from utils.str_manipulators import extract_guild_ids
import subprocess


class SetupCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Logs message when bot is online
    @commands.Cog.listener()
    async def on_ready(self):
        bot_logs.log_info("AI Chatbot Bot Online\n")

    # PING Check
    @commands.command(
        brief="Response Time in ms",
        description="Sends a return message with current ping",
    )
    async def ping(self, ctx):
        await ctx.send(f"Ping is {round(self.bot.latency * 1000)}ms")

    # Message Delete Function
    @commands.command(
        brief="Clears messages, default - 20",
        description="Clears 20 messages, or number defined in arg",
    )
    async def clear(self, ctx, amount=20):
        # # Delete sent message
        await ctx.message.delete()
        # # Delete last 20 messages
        await ctx.channel.purge(limit=amount)


# # Necessary for each cog
async def setup(bot):
    await bot.add_cog(SetupCog(bot))
