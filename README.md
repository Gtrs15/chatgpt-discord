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

# Deployment

## Key/Token Creation

For this project, the following 3 keys/tokens are required:


1. [application_id](https://discord.com/developers/applications)

    Click the link and login to create a new application. 
    Once it is created, copy the "APPLICATION ID" from the "General Information" section. 
    After that, click the "Bot" section in the sidebar. 



2. [discord_bot_token](https://discord.com/developers/applications)

    In the bot section, reset your token and copy it.  It is only available to be copied temporarily.  
    After that, scroll down to "Privileged Gateway Intents" and make sure to turn on all 3 options. (It will not work if the options are off.)


3. [openai_api_key](https://platform.openai.com/account/api-keys)

    Click the link and login to get your API keys.  If you have not created an account, you can create one for free (phone number required).


Once the 3 of these have been created and copied somewhere safe, you'll need to invite your bot to a server.  

1. Click the OAuth2 Link in the left sidebar and then click URL Generator.

2. Check the box for "bot" 

3. Scroll down and check the "View Audit Log" on the left column, and check all the boxes under "Text Permissions."

4. Scroll down and copy the link, and paste in into your browser URL bar to invite the bot to any server that the current account is in.  

5. Once the bot is in the server, proceed to the next step.  



## Using Docker:

Once your bot has been invited to the server using the link generated from the discord developer portal, you can deploy using this single command:

    docker run -d \
    -e discord_bot_token=INSERT_TOKEN_HERE \
    -e application_id=INSERT_APP_ID_HERE \
    -e openai_api_key=INSERT_API_KEY_HERE \
    gtrs15/chatgpt_discord:latest

If you would prefer to use a .env file, you can create the file to look like this:

    discord_bot_token=INSERT_TOKEN_HERE
    application_id=INSERT_APP_ID_HERE
    openai_api_key=INSERT_API_KEY_HERE

Then deploy with the command:

    docker run -d --env-file .env_file_name gtrs15/chatgpt_discord:latest


## Without Docker:


Before starting, I highly reccomend installing docker and using that method.  

That being said, here are the non-docker instructions.

First use git clone to clone the project to your desired location. 

    
    git clone https://github.com/Gtrs15/chatgpt-discord.git


Then install the requirements using the requirements.txt file.

    pip install -r config/requirements.txt


(Optional Step) 

To be able to restart the bot from within the bot, use the following command.  If you do not want to use this feature, you can skip this step. 

    chmod +x gptDiscordRestart.sh

Use this last command to start the bot. Replace the items in [brackets] with the actual value. 

    python3 start_bot_in_docker.py [discord_bot_token] [application_id] [openai_api_key]

Only the first initial startup needs the 3 arguments.

They will be saved after the first run, so next time just run the command ```python3 start_bot_in_docker.py```






---
# License

This project is licensed under the MIT License - see the LICENSE file for details.

# Acknowledgments

[OpenAI API](https://platform.openai.com/)

[Discord API](https://discord.com/developers/applications)

[Rapptz discord.py library](https://github.com/Rapptz/discord.py)

