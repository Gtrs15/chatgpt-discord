import os
import discord
from pathlib import Path
from discord.ext import commands
from utils.log_manager import bot_logs
from config.keys import DISCORD_BOT_TOKEN as TOKEN
from config.keys import APPLICATION_ID as APP_ID
# from resources.key import GUILD_ID


class ChatBot(commands.Bot):

    def __init__(self):

        # super().__init__ uses the "init" method of the inherited class
        super().__init__(command_prefix=".",
                         intents=discord.Intents.all(),
                         application_id=APP_ID)

        self.token = TOKEN

    async def setup_hook(self):
        # # Loads from cog folder
        for filename in os.listdir(Path.cwd() / "cogs"):
            if filename.endswith(".py"):
                await self.load_extension(f"cogs.{filename[:-3]}")

        # Sync slash commands to ALL servers
        await self.tree.sync()

        # Sync slash commands to only selected servers
        # # For GPT server (One should be added for each active server)
        # If using the sync() above, all servers will be synced on restart
        # await self.tree.sync(guild=discord.Object(id=GUILD_ID))

    def start_bot(self):
        self.run(self.token,
                 reconnect=True,
                 log_handler=bot_logs.file_handler,
                 log_formatter=bot_logs.formatter)


# Start the bot
ChatBot().start_bot()
