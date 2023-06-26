# # # # This will setup the first cog # # # #
# # # # This initializes: Ping, and Clear

from discord.ext import commands, tasks

from utils.log_manager import bot_logs
from utils.thread_manager import ThreadManager


class DB_Cleanup(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.tm = ThreadManager()

    # Logs message when bot is online
    @commands.Cog.listener()
    async def on_ready(self):
        self.deleted_thread_cleanup.start()

    # Checks all thread.db files and deletes ones from deleted threads
    # Necessary to remove old and unnecessary data.
    @tasks.loop(hours=2)
    async def deleted_thread_cleanup(self):
        thread_list = self.tm.get_list_of_thread_db_files()

        # Creates a list of threads if the thread has been deleted
        deleted_threads = [thread for thread in thread_list
                           if self.bot.get_channel(int(thread.split(".")[0])) == None]

        self.tm.remove_thread_db_files(deleted_threads)
        bot_logs.log_info(f'Deleted Threads: {", ".join(deleted_threads)}')


# # Necessary for each cog
async def setup(bot):
    await bot.add_cog(DB_Cleanup(bot))
