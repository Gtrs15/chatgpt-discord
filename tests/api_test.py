import os
import unittest
from unittest.mock import patch
from open_ai.storage import ChatStorageBox
from open_ai.api import openai, Chat


class TestChat(unittest.TestCase):

    def setUp(self):
        # Set up the necessary objects or variables for testing
        self.chat = Chat('chat_test')

    def tearDown(self):
        # Remove the test database file
        # self.chat.storage_box.clear()
        os.remove('data/chats/chat_test.db')

    def test_api_call_to_get_response(self):
        self.chat.get_response_from_prompt('5+5')
        self.assertIn('10', self.chat.chat_output)


if __name__ == '__main__':
    unittest.main()
