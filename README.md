# ChatGPT-Discord
A simple discord bot used as a front-end for the OpenAI gpt-3.5-turbo model. 

## Usage 

Use the commmand ```/chat``` to prompt the bot.  

```/chat``` from any text channel will start a new thread named after the prompt, the response is sent in the thread.

```/chat``` from inside a thread will use past prompts and responses from the current thread as context for next response. 

## Other Commands

The ```.clear``` command clears messages in current channel. (20 by default, can be customized, does not work in DM).

The ```.load``` command reloads all cogs (Used when changes are made to cog files).

Use the ```.ping``` command to check response time, or check that bot is active. 

The ```.restart``` command restarts the bot.


### For a full list of non-slash commands, use the ```.help``` command.


---

# License

This project is licensed under the MIT License - see the LICENSE file for details.

# Acknowledgments

[OpenAI API](https://platform.openai.com/)

[Discord API](https://discord.com/developers/applications)

[Rapptz discord.py library](https://github.com/Rapptz/discord.py)

