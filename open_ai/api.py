# Note: you need to be using OpenAI Python v0.27.0 (minimum) for the code below to work
# Use 'pip list' to check that you have the correct version installed
import openai
from open_ai.storage import ChatStorageBox
from config.keys import openai_api_key


class Chat:
    # Set API ley
    openai.api_key = openai_api_key

    def __init__(self):
        self.storage_box = ChatStorageBox()

    def get_response_from_prompt(self, prompt):
        self.storage_box.user_add(prompt)

        # This will create the completion, and will return self.chat_output
        # self.chat_output will be the error code if the api call fails
        self.try_to_get_chat_completion()
        return self.chat_output

    def try_to_get_chat_completion(self):
        # Needs to be in try block in case api call fails.
        try:
            self.completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=self.storage_box.read())
            self.chat_output = self.completion.choices[0].message.content
            self.storage_box.assistant_add(self.chat_output)
            return self.chat_output
        except Exception as e:
            self.chat_output = e
            return self.chat_output
