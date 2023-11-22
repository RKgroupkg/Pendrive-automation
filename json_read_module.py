import os
import json

class JSONReader:
    def __init__(self, file_name):
        self.file_name = file_name
        self.file_path = self.find_file_in_directory(file_name)
        self.data = None

    def _load_data(self):
        try:
            with open(self.file_path) as f:
                self.data = json.load(f)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"File not found: {self.file_path}") from e
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON format in file: {self.file_path}") from e

    def find_file_in_directory(self, file_name):
        for root, dirs, files in os.walk("."):
            if file_name in files:
                return os.path.join(root, file_name)
        return None

    def get_value(self, key, default=None):
        if self.data is None:
            self._load_data()

        return self.data.get(key, default)

    def get_all_keys(self):
        if self.data is None:
            self._load_data()

        return list(self.data.keys())
