# # # # This will setup the Logging cog # # # #


import discord
from discord.ext import commands
from utils.log_manager import bot_logs
from pathlib import Path


class LogSetup:
    description = '''\nRequires name of log to send. \nCan be: bot, bot_persist, chat, or chat_persist.'''

    log_folder = Path.cwd() / "data" / "logs"

    bot_logs_file_path = log_folder / "bot_logs.log"
    bot_logs_file_path_persistent = log_folder / "bot_logs_persistent.log"
    chat_logs_file_path = log_folder / "chat_logs.log"
    chat_logs_file_path_persistent = log_folder / "chat_logs_persistent.log"

    log_dict = {'bot': bot_logs_file_path,
                'bot_persist': bot_logs_file_path_persistent,
                'chat': chat_logs_file_path,
                'chat_persist': chat_logs_file_path_persistent}


class Logging(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Triggers when bot goes online
    @commands.Cog.listener()
    async def on_ready(self):
        # Can add anything here if you want the bot to do something at launch
        # If task is unrelated to logging, may want to use different cog
        pass

    # Send Log File
    @commands.command(
        brief="Send log file",
        description=f"Sends the log file specified. {LogSetup.description}")
    async def log(self,
                  ctx,
                  selection=commands.parameter(
                      default=None,
                      description="Name of log")):

        # Get selected log from dict using selection arg
        selected_log = LogSetup.log_dict[selection]

        await ctx.send(file=discord.File(selected_log))


# # Necessary for each cog
async def setup(bot):
    await bot.add_cog(Logging(bot))
