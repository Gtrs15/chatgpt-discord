# Base Image
FROM python:3.10.0-slim

# Copy folders
COPY cogs /app/cogs
COPY open_ai /app/open_ai
COPY utils /app/utils

# Copy files
COPY config/requirements.txt /app/config/
COPY discord_bot.py gptDiscordRestart.sh start_bot_in_docker.py /app/

WORKDIR /app/

# # Create Env Vars
ENV discord_bot_token=
ENV application_id=
ENV openai_api_key=

# Necessary for bash script that restarts bot
RUN apt-get update
RUN apt-get install -y procps

# Install packages
RUN pip install --upgrade pip
RUN pip install -r config/requirements.txt

# Allow gptDiscordRestart.sh to be executed
RUN chmod +x gptDiscordRestart.sh


# Start the bot
CMD ["sh", "-c", "python3 start_bot_in_docker.py $discord_bot_token $application_id $openai_api_key"]


# To start bot: (Run on a single line, or multiline)
# $ docker run 
# -e discord_bot_token=<INSERT_TOKEN_HERE>
# -e application_id=<INSERT_APP_ID_HERE> 
# -e openai_api_key=<INSERT_API_KEY_HERE> 
# <IMAGE ID> 

# (Optional) Add -d after "run" to start "detached" (in the background)
