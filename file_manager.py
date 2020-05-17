import json


class FileManager:
    data = None

    @staticmethod
    def load(path):
        with open(path, encoding='utf8') as f:
            FileManager.data = json.load(f)
            return FileManager.data

    @staticmethod
    def save(path):
        with open(path, "w") as f:
            json.dump(FileManager.data, f, indent=2)

    @staticmethod
    def set_data(data):
        FileManager.data = data
