# This cog will be only for chat-related functions

import time
import datetime

import discord
from discord import app_commands
from discord.ext import commands

from open_ai.api import Chat
from utils.log_manager import bot_logs, chat_logs


class ChatBotText:
    cmd_name: str = 'chat'
    description: str = 'Talk to ChatGPT.  Uses history as context for future questions/prompts.'
    prompt: str = 'Input your question/prompt for ChatGPT.'
    date_format: str = '%a, %-m/%d | %I:%M %p'


class SlashChat(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # Ask ChatGPT with memory of previous messages
    @app_commands.command(name=ChatBotText.cmd_name,
                          description=ChatBotText.description)
    @app_commands.describe(prompt=ChatBotText.prompt)
    async def chat(self, interaction: discord.Interaction, prompt: str):
        await interaction.response.defer()
        chat_logs.clear_log()
        channel = interaction.channel

        # CREATE THREAD if channel is not thread
        if str(channel.type) == 'text':
            try:
                # Create thread with part of question as name (Limit 100 chars for thread name)
                thread = await channel.create_thread(
                    name=f"{datetime.datetime.now().strftime(ChatBotText.date_format)} - {prompt[:65]}",
                    auto_archive_duration=4320,  # 3 Days
                )
                await thread.add_user(interaction.user)

                # Sends "bot is typing" until response is ready
                await thread.typing()
                chat = Chat(str(thread.id))
                response = chat.get_response_from_prompt(prompt)

                [await thread.send(x) for x in response]
                await thread.send(f'Tokens Used: {chat.total_tokens}')
                
                # Replace the "bot is thinking" with string, then delete that message
                await interaction.followup.send('Check thread for response')
                time.sleep(4)
                await channel.last_message.delete()

            except Exception as e:
                bot_logs.log_error(e)
                await interaction.channel.send(e)

        else:
            try:
                # Already in thread
                await interaction.channel.typing()

                chat = Chat(str(channel.id))
                response = chat.get_response_from_prompt(prompt)

                [await interaction.channel.send(x) for x in response]
                await interaction.followup.send(chat.usage_string)
            except Exception as e:
                bot_logs.log_error(e)
                await interaction.channel.send(e)


async def setup(bot: commands.Bot):
    await bot.add_cog(SlashChat(bot))
