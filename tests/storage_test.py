import os
import unittest
from open_ai.storage import ChatStorageBox


class TestChatStorageBox(unittest.TestCase):

    def setUp(self):
        # Set up the necessary objects or variables for testing
        self.storage_box = ChatStorageBox('tests', 'test.db')

    def tearDown(self):
        # Remove the test database file
        os.remove(f'tests/test.db')

    def test_write_value_to_db_list(self):
        # Test if the value is successfully written to the database list
        self.storage_box.write_value_to_db_list("Test Value")
        values = self.storage_box.read()
        self.assertIn("Test Value", values)

    def test_read(self):
        # Test if the read method returns the correct list of values
        values = self.storage_box.read()
        self.assertIsInstance(values, list)

    def test_clear(self):
        # Test if the clear method clears the values in the database
        self.storage_box.write_value_to_db_list("Test Value")
        self.storage_box.clear()
        values = self.storage_box.read()
        self.assertEqual(values, [])

    def test_user_add(self):
        # Test if user messages are correctly added to the database
        self.storage_box.user_add("Hello")
        values = self.storage_box.read()
        self.assertIn({'role': 'user', 'content': 'Hello'}, values)

    def test_assistant_add(self):
        # Test if assistant messages are correctly added to the database
        self.storage_box.assistant_add("Hi, how can I assist you?")
        values = self.storage_box.read()
        self.assertIn({'role': 'assistant', 'content': 'Hi, how can I assist you?'}, values)

    def test_system_add(self):
        # Test if system messages are correctly added to the database
        self.storage_box.system_add("System message")
        values = self.storage_box.read()
        self.assertIn({'role': 'system', 'content': 'System message'}, values)

