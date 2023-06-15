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
        self.assertIn('Response:', self.chat.usage_string)
        
        # Usage String
        if hasattr(self.chat, 'usage_string'):
            self.assertTrue(True, msg='Usage String Test: Passed')
        else:
            self.fail('Usage String Test: Failed')
            
        # Total Tokens
        if hasattr(self.chat, 'total_tokens'):
            self.assertTrue(True, msg='Total Tokens Test: Passed')
        else:
            self.fail('Total Tokens Test: Failed')
