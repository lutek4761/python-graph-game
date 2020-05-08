from file_manager import FileManager


class Game:
    def __init__(self):
        self.objects = FileManager.load('objects.json')

        for obj in self.objects["objects"]:
            print(obj)

        for obj in self.objects["objects"]:
            print(obj["connections"]["1"])

    def tick(self):
        print("Game ticking")

    def draw(self):
        print("Game drawing")
