# Note: you need to be using OpenAI Python v0.27.0 (minimum) for the code below to work
# Use 'pip list' to check that you have the correct version installed
import openai
from open_ai.storage import ChatStorageBox
from config.keys import OPENAI_API_KEY
from utils.log_manager import chat_logs, bot_logs
from utils.str_manipulators import split_string


class Chat:
    # Set API Key
    openai.api_key = OPENAI_API_KEY
    usage_text = 'Tokens: '
    prompt = 'Prompt:'
    response = 'Response:'

    def __init__(self, database_file_path):
        self.storage_box = ChatStorageBox(
            'data/chats', str(f'{database_file_path}.db'))

    def get_response_from_prompt(self, prompt):
        self.storage_box.user_add(prompt)

        # This will create the completion, and will return self.chat_output
        # self.chat_output will be the error code if the api call fails
        self.try_to_get_chat_completion(prompt)
        return split_string(self.chat_output, 1990)

    def try_to_get_chat_completion(self, prompt):
        # Needs to be in try block in case api call fails.
        try:
            self.completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=self.storage_box.read())
            self.chat_output = self.completion.choices[0].message.content
            self.storage_box.assistant_add(self.chat_output)

            # Track Token  Usage
            usage = self.completion.usage
            chat_logs.log_info(dict(usage))
            self.total_tokens = usage['total_tokens']

            self.usage_string = "\n".join([
                f'{self.usage_text}{self.total_tokens}',
                self.prompt,
                prompt,
                self.response])

            return self.chat_output

        except Exception as e:
            # In case of invalid API key
            if str(e) == '<empty message>':
                self.chat_output = 'API Call Failed\nCheck if API key is valid'
                bot_logs.log_error(self.chat_output)
                self.usage_string = None
                self.total_tokens = None
                return self.chat_output
            
            self.chat_output = str(e)
            bot_logs.log_error(str(e))
            self.usage_string = None
            self.total_tokens = None
            return self.chat_output
