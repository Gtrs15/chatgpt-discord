#!/bin/bash

# # Checks if bot currently is running.
# # Restarts if running, starts if not running. 
# # Executing this script will ALWAYS result in the program running. 


# If executed from docker container, will use docker home dir
if [ $(pwd) = /app ]
then
    # Set your bot variable equal to the full path of the .py file
    bot="/app/discord_bot.py"

    # Set log to the full path of the log file you intend to use
    log="/app/data/logs/bot_logs.log"

    # Set your log for this script, can use the same as above 
    # Although it is reccomeded to use a different log
    shell_log="/app/data/logs/shell.log"

    # Set the "home" directory of the bot
    projects_home="/app"
else
    # Set your bot variable equal to the full path of the .py file
    bot="$HOME/projects/chatgpt_discord/discord_bot.py"

    # Set log to the full path of the log file you intend to use
    log="$HOME/projects/chatgpt_discord/data/logs/bot_logs.log"

    # Set your log for this script, can use the same as above 
    # Although it is reccomeded to use a different log
    shell_log="$HOME/projects/chatgpt_discord/data/logs/shell.log"

    # Set the "home" directory of the bot
    projects_home="$HOME/projects/chatgpt_discord"
fi

start_bot() {
    # Start process
    cd $projects_home
    # Source the virtual environment
    source $projects_home/venv/bin/activate
    # Starts process in the background
    # 'prints' to the chosen log file
    nohup python -u $bot &>> $log &
    # Start Successful
    echo "" >> $shell_log
}


# Returns true if process is running, false if process cannot return process matching name
if pgrep -f $bot > /dev/null

# This executes if the process is running
then

    # Print date, string, and bot variable to txt file
    echo $(date) "Process is running" $bot >> $shell_log

    # Set proc_id to the Process ID of running bot
    proc_id=$(pgrep -f $bot)

    # Print the Process ID var and string, to txt file
    echo $proc_id "< This is the PID of $bot" >> $shell_log

    # Kill process
    kill $proc_id

    start_bot

# This executes if the process is NOT running
else

    # Log to file 
    echo $bot "has stopped" >> $shell_log
    echo "Starting now" $(date) >> $shell_log

    start_bot
fi

