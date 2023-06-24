import os

from typing import Any
from open_ai.storage import ChatStorageBox


class ThreadManager:

    def __init__(self) -> None:
        pass

    def get_list_of_thread_db_files(self):
        files = os.listdir('data/chats')
        threads = [thread for thread in files if thread.endswith('.db')]
        return threads

    def remove_thread_db_files(self, thread_ids: list):

        [os.system(f'rm data/chats/{thread_id} 2> /dev/null')
         for thread_id in thread_ids]
