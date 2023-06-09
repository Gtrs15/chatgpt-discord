import os
import sys
from pathlib import Path
from utils.log_manager import bot_logs


class KeyManager:
    key_file = Path.cwd() / 'config' / 'keys.py'

    def __init__(self) -> None:
        self.check_if_key_exists()
        self.key_file_creator()
        self.start_bot()

    def check_if_key_exists(self):
        # Will not overwrite an existing key file
        if os.path.isfile(KeyManager.key_file) == True:
            bot_logs.log_info('File already exists, cannot overwrite.')
            self.key_exists = True
        else:
            self.key_exists = False

    def key_file_creator(self):

        # Will not overwrite an existing key file
        if self.key_exists == True:
            return

        args = sys.argv[1:]

        # # Create the list of keys to add to key file
        KEYS = [f'''echo "DISCORD_BOT_TOKEN = '{args[0]}'" >> {KeyManager.key_file} ''',
                f'''echo "APPLICATION_ID = '{args[1]}'" >> {KeyManager.key_file} ''',
                f'''echo "OPENAI_API_KEY = '{args[2]}'" >> {KeyManager.key_file} ''',
                ]

        # Echo each token/key to the key file
        [os.system(x) for x in KEYS]

    def start_bot(self):
        bot_logs.log_info('Starting Bot Now')
        os.system('python3 discord_bot.py')


KeyManager()
