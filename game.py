from file_manager import FileManager
from node import Node
from pygame import font


class Game:
    def __init__(self, display):
        font.init()
        self.display = display
        self.json_objects = FileManager.load('objects.json')
        self.nodes = {}

        for obj in self.json_objects["objects"]:
            self.nodes.update({obj["id"]: Node(obj["id"], obj["connections"], obj["description"], self.display)})
        self.current_node = self.nodes["1"]
        self.children_indexes = []
        for index in self.current_node.connections:
            self.children_indexes.append(self.current_node.connections[index]["target_node_id"])
        self.__currently_selected_option = 1
        self.blocker = False
        self.set_menu_scene = False
        print(self.children_indexes)

    def tick(self, up, down, enter):
        if up and self.blocker:
            self.blocker = False
            if self.__currently_selected_option == 1:
                self.__currently_selected_option = len(self.children_indexes)
            else:
                self.__currently_selected_option -= 1
        elif not up and not self.blocker and not down and not enter:
            self.blocker = True

        if down and self.blocker:
            self.blocker = False
            if self.__currently_selected_option == len(self.children_indexes):
                self.__currently_selected_option = 1
            else:
                self.__currently_selected_option += 1
        elif not down and not self.blocker and not up and not enter:
            self.blocker = True

        if enter and self.blocker:
            self.current_node = self.nodes[str(self.children_indexes[self.__currently_selected_option - 1])]
            self.__currently_selected_option = 1
            self.children_indexes.clear()
            for index in self.current_node.connections:
                self.children_indexes.append(self.current_node.connections[index]["target_node_id"])
            self.blocker = False
        elif not down and not self.blocker and not up and not enter:
            self.blocker = True

    def draw(self):
        self.current_node.draw(self.__currently_selected_option)