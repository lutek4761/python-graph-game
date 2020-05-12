import json


class FileManager:
    @staticmethod
    def load(path):
        with open(path, encoding='utf8') as f:
            return json.load(f)

    @staticmethod
    def save():
        pass
