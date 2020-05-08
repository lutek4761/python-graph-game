import json


class FileManager:
    @staticmethod
    def load(path):
        with open(path) as f:
            return json.load(f)

    @staticmethod
    def save():
        pass
