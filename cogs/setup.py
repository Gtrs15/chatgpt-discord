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

    # Sends message reply to unknown commands
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        bot_logs.log_info(error)
        await ctx.send(error)

    # Completes each time a command runs successfully
    @commands.Cog.listener()
    async def on_command_completion(self, ctx):
        full_command_name = ctx.command.qualified_name
        discord_user = ctx.message.author.name
        bot_logs.log_info(
            f'{discord_user} used the {full_command_name} command.')

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

    # Reload cog function
    @commands.command(
        brief="Reloads all cogs",
        description="Reloads all cogs, sends name of all reloaded cogs",
    )
    async def load(self, ctx):
        files = [
            filename
            for filename in os.listdir(Path.cwd() / "cogs")
            if filename.endswith(".py")]

        [await self.bot.reload_extension(f"cogs.{filename[:-3]}") for filename in files]

        await ctx.send(f"Reloaded Cogs:\n{', '.join(files)}")
        bot_logs.log_info(f"Reloaded Cogs: {', '.join(files)}")


# # Necessary for each cog
async def setup(bot):
    await bot.add_cog(SetupCog(bot))
