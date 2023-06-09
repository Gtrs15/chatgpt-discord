import logging
from pathlib import Path


class Logger:

    def __init__(self, log_level, log_folder, log_file_name, persistent_file_name):

        self.create_log_folder_if_does_not_exist(log_folder)

        self.logger = logging.getLogger(log_file_name)
        self.logger.setLevel(log_level)
        self.formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s',
                                           datefmt='%A, %B %d, %Y | %I:%M:%S %p')

        self.file_handler = logging.FileHandler(
            str(f'{log_folder}/{log_file_name}'))
        self.file_handler.setLevel(log_level)
        self.file_handler.setFormatter(self.formatter)
        self.logger.addHandler(self.file_handler)

        persistent_handler = logging.FileHandler(
            str(f'{log_folder}/{persistent_file_name}'))
        persistent_handler.setLevel(log_level)
        persistent_handler.setFormatter(self.formatter)

        self.log_file_path = str(f'{log_folder}/{log_file_name}')
        self.persistent_path = str(f'{log_folder}/{persistent_file_name}')

    @staticmethod
    def create_log_folder_if_does_not_exist(log_folder):

        a = str(log_folder).split('/')
        a.pop()
        data_folder = "/".join(a)

        def create_folder_if_none_exists(folder_name):
            # Create folder if it does not exist
            if Path(folder_name).is_dir():
                pass
            else:
                new_folder = Path(folder_name)
                new_folder.mkdir()

        create_folder_if_none_exists(data_folder)
        create_folder_if_none_exists(log_folder)

    def log_error(self, error_message):
        self.logger.error(error_message)

    def log_warning(self, warning_message):
        self.logger.warning(warning_message)

    def log_info(self, info_message):
        self.logger.info(info_message)

    def log_debug(self, debug_message):
        self.logger.debug(debug_message)

    def clear_log(self):
        self.add_to_persistent_log()
        with open(self.log_file_path, 'r+') as file:
            file.truncate(0)

    def add_to_persistent_log(self):
        # Reads log and copies log data to persistent log
        # Created so that 'log' can contain recent data
        # While the persistent log contains all historical data
        with open(self.log_file_path, 'r') as source:
            s = source.read()
            with open(self.persistent_path, 'a') as destination:
                destination.write('\n')
                destination.write(s)
                destination.write('\n')


bot_logs = Logger(
    'INFO',
    Path.cwd() / 'data' / 'logs',
    'bot_logs.log',
    'bot_logs_persistent.log')

chat_logs = Logger(
    'INFO',
    Path.cwd() / 'data' / 'logs',
    'chat_logs.log',
    'chat_logs_persistent.log')
