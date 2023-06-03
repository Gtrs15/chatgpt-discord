from pathlib import Path
import shelve


class ChatStorageBox:

    def __init__(self, database_folder_path='data', database_file_path='data.db'):
        # Verification
        self.verify_database_folder_path(database_folder_path)
        # self.verify_database_file(database_folder_path, database_file_path)

        self.database_file_path = Path(
            f'{database_folder_path}/{database_file_path}')
        self.database_file_str = f'{database_folder_path}/{database_file_path}'

    def verify_database_folder_path(self, database_folder_path):
        # Verify that data folder exists, create one if it does not
        if Path(database_folder_path).is_dir():
            pass
        else:
            new_folder = Path(database_folder_path)
            new_folder.mkdir()

    def verify_database_file(self, database_folder_path, database_file_path):
        # Check if data file exists, create one if it does not
        if Path(f'{database_folder_path}/{database_file_path}').is_file():
            # print('File may be overwritten')
            # Add logging here later
            pass
        else:
            pass

    def write_value_to_db_list(self, value):
        # open db file and add new value
        with shelve.open(self.database_file_str) as db:
            # Get the list of values from the database
            values = db.get('values', [])
            values.append(value)
            # Write the new list of values back to the database
            db['values'] = values

    def read(self):
        with shelve.open(self.database_file_str) as db:
            # Get the list of values from the database
            values = db.get('values', [])
            return values

    def clear(self):
        with shelve.open(self.database_file_str) as db:
            # Clear the database by setting the 'values' key to an empty list
            db['values'] = []

    # The next three methods all add data to the list-
    # in the format required by OpenAI api
    def user_add(self, message):
        # Add message to current db
        self.write_value_to_db_list({'role': 'user', 'content': message})
        # TODO: Add to log after creating logging module

    def assistant_add(self, message):
        # Add assistant message to current db
        self.write_value_to_db_list({'role': 'assistant', 'content': message})
        # TODO: Add to log after creating logging module

    def system_add(self, message):
        # Add system message to current db
        self.write_value_to_db_list({'role': 'system', 'content': message})
        # TODO: Add to log after creating logging module
