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
        self.current_node = self.nodes[self.json_objects["current_object_id"]]
        self.children_indexes = []
        for index in self.current_node.connections:
            if self.current_node.connections[index]["is_active"]:
                self.children_indexes.append(self.current_node.connections[index]["target_node_id"])
        self.__currently_selected_option = 1
        self.blocker = False
        self.set_menu_scene = False

    def tick(self, up, down, enter, esc):
        if esc:
            self.json_objects["current_object_id"] = self.current_node.id
            FileManager.set_data(self.json_objects)
            self.set_menu_scene = True
            return
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
            self.blocker = False
            self.handle_switchers()
            self.current_node = self.nodes[str(self.children_indexes[self.__currently_selected_option - 1])]
            for key in self.current_node.connections:
                if self.current_node.connections[key]["is_active"]:
                    self.__currently_selected_option = int(key)
                    break
            self.children_indexes.clear()
            for index in self.current_node.connections:
                self.children_indexes.append(self.current_node.connections[index]["target_node_id"])
        elif not down and not self.blocker and not up and not enter:
            self.blocker = True

    def draw(self):
        self.current_node.draw(self.__currently_selected_option)

    def handle_switchers(self):
        for key in self.current_node.connections:
            if len(self.current_node.connections[key]["switcher"]) > 0:
                for key2 in self.current_node.connections[key]["switcher"]:
                    value = self.current_node.connections[key]["switcher"][key2]["value"]
                    connection_id = self.current_node.connections[key]["switcher"][key2]["connection_id"]
                    node_to_set = self.nodes[self.current_node.connections[key]["switcher"][key2]["node_id"]]
                    node_to_set.connections[connection_id]["is_active"] = value
